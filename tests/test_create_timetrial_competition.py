import datetime
import uuid
from unittest import TestCase
from unittest.mock import Mock

from src.shared.domain.errors import DomainError
from src.timetrialcomp.competition.application.create_timetrial_competition import TimeTrialCompetitionCreator
from src.timetrialcomp.competition.domain.timetrial_comp_repository import TimeTrialCompetitionRepository
from src.timetrialcomp.competition.domain.timetrial_competition import CreateTimeTrialCompetitionParams, \
    CompetitionMustStartBeforeEnding, MoreThanOneDurationSet, TimeTrialCompetition

repository = TimeTrialCompetitionRepository()
use_case = TimeTrialCompetitionCreator(repository)


def any(
        id=uuid.uuid4(),
        track_code='mmm',
        starts_at=datetime.datetime(2023, 4, 11, 1, 1, 1, 1),
        duration_in_weeks=None,
        duration_in_months=1
):
    return CreateTimeTrialCompetitionParams(
        id=id,
        track_code=track_code,
        starts_at=starts_at,
        duration_in_weeks=duration_in_weeks,
        duration_in_months=duration_in_months
    )


class TestTimeTrialCompetitionCreator(TestCase):
    def test_should_create_time_trial_competition(self):
        repository.save = Mock()
        params = any()

        response = use_case.create(params=params)

        self.assertIsNone(response)
        repository.save.assert_called_once()
        ttcomp = TimeTrialCompetition(
            id=str(params.get('id')),
            track_code=params.get('track_code'),
            starts_at=params.get('starts_at'),
            ends_at=datetime.datetime(2023, 5, 11, 1, 1, 1, 1),
        )
        repository.save.assert_called_once_with(ttcomp)

    def test_should_return_error_when_competition_starts_at_equals_ends_at(self):
        repository.save = Mock()
        params = any(duration_in_months=0)

        response = use_case.create(params=params)

        self.assertIsInstance(response, CompetitionMustStartBeforeEnding)
        repository.save.assert_not_called()

    def test_should_return_error_when_both_durations_are_set(self):
        repository.save = Mock()
        params = any(duration_in_months=1, duration_in_weeks=2)

        response = use_case.create(params=params)

        self.assertIsInstance(response, MoreThanOneDurationSet)
        repository.save.assert_not_called()