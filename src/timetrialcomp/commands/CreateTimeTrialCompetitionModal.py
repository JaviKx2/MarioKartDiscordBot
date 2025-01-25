import disnake
from disnake import Embed, SelectOption
from disnake import ModalInteraction, Colour
from disnake.ui import Modal, TextInput, Select


class Dropdown(disnake.ui.Select):
    def __init__(self):
        # Define the options that will be presented inside the dropdown
        options = [
            disnake.SelectOption(
                label="Red", description="Your favourite colour is red", emoji="🟥"
            ),
            disnake.SelectOption(
                label="Green", description="Your favourite colour is green", emoji="🟩"
            ),
            disnake.SelectOption(
                label="Blue", description="Your favourite colour is blue", emoji="🟦"
            ),
        ]

        # The placeholder is what will be shown when no option is chosen.
        # The min and max values indicate we can only pick one of the three options.
        # The options parameter defines the dropdown options, see above.
        super().__init__(
            placeholder="Choose your favourite colour...",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, inter: disnake.MessageInteraction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The `self` object refers to the
        # StringSelect object, and the `values` attribute gets a list of the user's
        # selected options. We only want the first one.
        await inter.response.send_message(f"Your favourite colour is {self.values[0]}")


class DropdownView(disnake.ui.View):
    def __init__(self):
        super().__init__()

        # Add the dropdown to our view object.
        self.add_item(Dropdown())
        self.add_item(Dropdown())
        self.add_item(Dropdown())
        self.add_item(Dropdown())


class CreateTimeTrialCompetitionModal(Modal):

    def __init__(self) -> None:
        title = "Create new time trial competition"
        components = [
            TextInput(
                label="Track name",
                placeholder="lc",
                min_length=2,
                max_length=2,
                required=True,
                custom_id="track_name"
            )
        ]
        super().__init__(
            title=title, components=components, custom_id="create_timetrial_competition_modal", timeout=600
        )

    async def callback(self, interaction: ModalInteraction, /) -> None:
        embed = Embed(title=interaction.data, description="hi", color=Colour.blurple())
        await interaction.response.send_message(embed=embed)
