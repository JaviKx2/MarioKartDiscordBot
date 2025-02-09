import disnake
from disnake import MessageInteraction, TextInputStyle, ActionRow
from disnake.interactions.base import ClientT
from disnake.ui import Button, View

from src.timetrialcomp.competition.infrastructure.dependency_injection import current_competitions_finder
from src.timetrialcomp.presenter.find_all import present_competitions, present_competition
from src.timetrialcomp.presenter.ranking import present_ranking
from src.timetrialcomp.presenter.submit_time import present_submit_time
from src.timetrialcomp.time_submission.domain.submitted_time import SubmitTimeParams


class MainMenuButton(Button):
    def __init__(self):
        super().__init__()
        self.label = "🏠 Main menu"
        self.row = 4

    async def callback(self, interaction: MessageInteraction[ClientT], /) -> None:
        await interaction.response.defer()
        await interaction.edit_original_response("", view=TTCompView())


class RankingButton(Button):
    def __init__(self, ttcomp_id):
        super().__init__()
        self.label = "🏆 Show ranking"
        self.ttcomp_id = ttcomp_id

    async def callback(self, interaction: MessageInteraction[ClientT], /) -> None:
        await interaction.response.defer()
        await interaction.edit_original_response(
            await present_ranking(self.ttcomp_id, interaction.bot.get_or_fetch_user),
            view=RankingView(self.ttcomp_id)
        )


class SubmitTimeButton(Button):
    def __init__(self, ttcomp_id):
        super().__init__()
        self.label = "🕒 Submit time"
        self.ttcomp_id = ttcomp_id

    async def callback(self, interaction: MessageInteraction[ClientT], /) -> None:
        await interaction.response.send_modal(SubmitTimeModal(self.ttcomp_id))



class ListCompsButton(Button):
    def __init__(self):
        super().__init__()
        self.label = "📃 List current competitions"
        self.page = 0

    async def callback(self, interaction: MessageInteraction[ClientT], /) -> None:
        await interaction.response.defer()

        current_competitions = list(current_competitions_finder.find_current_competitions())

        if len(current_competitions) > 0:
            comp = current_competitions[self.page]
            await interaction.edit_original_response(present_competition(comp), view=TTCompView(comp.id))
            return

        await interaction.edit_original_response(present_competitions(current_competitions))


class SubmitTimeModal(disnake.ui.Modal):
    def __init__(self, ttcomp_id):
        components = [
            disnake.ui.TextInput(
                label="Time",
                placeholder="00:00.000",
                custom_id="time",
                style=TextInputStyle.short,
                max_length=9,
            )
        ]
        self.ttcomp_id = ttcomp_id
        super().__init__(title="Submit time", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        params = SubmitTimeParams(
            time=inter.text_values["time"],
            pic_url="",
            ctgp_url="",
            timetrial_competition_id=self.ttcomp_id,
            player_id=str(inter.user.id)
        )

        await inter.send(present_submit_time(params), view=TTCompView())


def TTCompView(ttcomp_id) -> View:
    view = View()
    view.add_item(RankingButton(ttcomp_id))
    view.add_item(SubmitTimeButton(ttcomp_id))
    return view

def RankingView(ttcomp_id) -> View:
    view = View()
    view.add_item(SubmitTimeButton(ttcomp_id))
    view.add_item(ListCompsButton())
    return view
