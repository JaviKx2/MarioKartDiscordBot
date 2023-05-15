import datetime
import uuid
from unittest import TestCase
from unittest.mock import Mock

from src.timetrialcomp.competition.application.create_timetrial_competition import TimeTrialCompetitionCreator
from src.timetrialcomp.competition.domain.timetrial_comp_repository import TimeTrialCompetitionRepository
from src.timetrialcomp.competition.domain.timetrial_competition import CreateParams, \
    CompetitionMustStartBeforeEnding, MoreThanOneDurationSet, TimeTrialCompetition

repository = TimeTrialCompetitionRepository()
use_case = TimeTrialCompetitionCreator(repository)


class CreateParamsMother:
    @staticmethod
    def any(
            competition_id=uuid.uuid4(),
            track_code='mmm',
            starts_at=datetime.datetime(2023, 4, 11, 1, 1, 1, 1),
            duration_in_weeks=None,
            duration_in_months=1
    ):
        return CreateParams(
            id=competition_id,
            track_code=track_code,
            starts_at=starts_at,
            duration_in_weeks=duration_in_weeks,
            duration_in_months=duration_in_months
        )


class CompetitionMatcher:
    expected: TimeTrialCompetition

    def __init__(self, expected: TimeTrialCompetition):
        self.expected = expected

    def __repr__(self):
        return repr(self.expected)

    def __eq__(self, other: TimeTrialCompetition):
        return self.expected.id == other.id \
            and self.expected.track_code == other.track_code \
            and self.expected.starts_at == other.starts_at \
            and self.expected.ends_at == other.ends_at


class TestTimeTrialCompetitionCreator(TestCase):
    def test_should_create_time_trial_competition(self):
        repository.save = Mock()
        params = CreateParamsMother.any()

        response = use_case.create(params=params)

        self.assertIsNone(response)
        expected = TimeTrialCompetition(
            id=params.get('id'),
            track_code=params.get('track_code'),
            starts_at=params.get('starts_at'),
            ends_at=datetime.datetime(2023, 5, 11, 1, 1, 1, 1),
        )
        repository.save.assert_called_once_with(CompetitionMatcher(expected))

    def test_should_return_error_when_competition_starts_at_equals_ends_at(self):
        repository.save = Mock()
        params = CreateParamsMother.any(duration_in_months=0)

        response = use_case.create(params=params)

        self.assertIsInstance(response, CompetitionMustStartBeforeEnding)
        repository.save.assert_not_called()

    def test_should_return_error_when_both_durations_are_set(self):
        repository.save = Mock()
        params = CreateParamsMother.any(duration_in_months=1, duration_in_weeks=2)

        response = use_case.create(params=params)

        self.assertIsInstance(response, MoreThanOneDurationSet)
        repository.save.assert_not_called()
