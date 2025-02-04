import disnake
from disnake import MessageInteraction, TextInputStyle, TextInput
from disnake.interactions.base import ClientT
from disnake.ui import Button, View

from src.shared.domain.errors import has_errors, DomainError
from src.timetrialcomp.competition.infrastructure.dependency_injection import current_competitions_finder, \
    time_submitter
from src.timetrialcomp.time_submission.domain.submitted_time import SubmitTimeParams


def render_position(index):
    positions = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

    if 0 <= index < len(positions):
        return positions[index]

    return str(index + 1)


def render_timestamp(dt):
    timestamp = str(dt.timestamp()).split(".")[0]
    return f"<t:{timestamp}>"


class MainMenuButton(Button):

    def __init__(self):
        super().__init__()
        self.label = "🏠 Main menu"
        self.row = 4

    async def callback(self, interaction: MessageInteraction[ClientT], /) -> None:
        await interaction.response.defer()
        await interaction.edit_original_response("", view=MainMenuView())


class RankingButton(Button):

    def __init__(self, ttcomp_id):
        super().__init__()
        self.label = "🏆 Show ranking"
        self.ttcomp_id = ttcomp_id

    async def callback(self, interaction: MessageInteraction[ClientT], /) -> None:
        await interaction.response.defer()

        ranking_response = time_submitter.ranking(self.ttcomp_id)

        if has_errors(ranking_response):
            error: DomainError = ranking_response
            await interaction.edit_original_response(error.message, view=MainMenuView())
            return

        if len(ranking_response) == 0:
            await interaction.edit_original_response("No times submitted yet.", view=MainMenuView())
            return

        view_rows = ""
        for i, row in enumerate(ranking_response):
            user = await interaction.bot.get_or_fetch_user(row['player_id'])
            view_rows += (
                f"{render_position(i)} "
                f"{user.display_name}\t"
                f"🕒 {row['time']}\t"
                f"🔗 CTGP: {row['ctgp_url']}\t"
                f"Approved: {'✔' if row['approved'] else '❌'}\n"
            )

        await interaction.edit_original_response(f"{view_rows}", view=MainMenuView())



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

    async def callback(self, interaction: MessageInteraction[ClientT], /) -> None:
        await interaction.response.defer()

        current_competitions = list(current_competitions_finder.find_current_competitions())

        inner_view = View()

        inner_view.add_item(MainMenuButton())

        if len(current_competitions) == 0:
            await interaction.edit_original_response(f"No competitions found.", view=inner_view)
        else:
            view_comps = ""
            for comp in current_competitions:
                view_comps += (
                    f"🆔: {comp.id}\n"
                    f"🏁 Track: {comp.track_code}\n"
                    f"🍄 Mode: {comp.mode}\n"
                    f"📅 Starts at {render_timestamp(comp.starts_at)}\n"
                    f"📅 Ends at {render_timestamp(comp.ends_at)}\n\n"
                )
                inner_view.add_item(RankingButton(comp.id))
                inner_view.add_item(SubmitTimeButton(comp.id))

            await interaction.edit_original_response(
                f"Current competitions:\n\n"
                f"{view_comps}",
                view=inner_view
            )


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

        submitted_time = time_submitter.submit_time(params)

        if has_errors(submitted_time):
            error: DomainError = submitted_time
            await inter.send(error.message, view=MainMenuView())
            return

        await inter.send("Time was submitted.", view=MainMenuView())


def MainMenuView() -> View:
    view = View()
    view.add_item(ListCompsButton())
    return view