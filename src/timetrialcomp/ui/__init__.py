from disnake import MessageInteraction
from disnake.interactions.base import ClientT
from disnake.ui import Button, View

from src.timetrialcomp.competition.infrastructure.dependency_injection import current_competitions_finder

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

            await interaction.edit_original_response(
                f"Current competitions:\n\n"
                f"{view_comps}",
                view=inner_view
            )


def MainMenuView() -> View:
    view = View()
    view.add_item(ListCompsButton())
    return view