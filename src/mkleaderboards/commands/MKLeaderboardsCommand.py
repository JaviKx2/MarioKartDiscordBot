from typing import Dict, Any, Callable

from disnake import CommandInteraction, ApplicationCommandInteraction
from disnake.ext.commands import slash_command, InvokableSlashCommand, SubCommand
from disnake.ext.commands.base_core import CommandCallback
from disnake.i18n import LocalizedOptional

from src.mkleaderboards.commands.CoursesSubcommand import execute as courses_execute
from src.mkleaderboards.commands.RankingSubcommand import execute as ranking_execute, RankingScopeChoice


@slash_command()
async def leaderboards(ctx: CommandInteraction):
    pass


@leaderboards.sub_command()
async def courses(ctx: CommandInteraction, track_abbrev: str):
    await courses_execute(ctx, track_abbrev)


@leaderboards.sub_command()
async def ranking(ctx: CommandInteraction, scope: RankingScopeChoice):
    await ranking_execute(ctx, scope)



class test(InvokableSlashCommand):

    def sub_command(self, name: LocalizedOptional = None, description: LocalizedOptional = None, options: list = None,
                    connectors: dict = None, extras: Dict[str, Any] = None, **kwargs) -> Callable[
        [CommandCallback], SubCommand]:
        return super().sub_command(name, description, options, connectors, extras, **kwargs)

    async def invoke(self, inter: ApplicationCommandInteraction):
        return await super().invoke(inter)