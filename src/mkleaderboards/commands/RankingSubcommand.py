from enum import Enum

from disnake import CommandInteraction

from src.mkleaderboards.MKLeaderboardsAPI import get_ranking


class RankingScopeChoice(str, Enum):
    World = 'world'
    Spain = 'spain'
    Americas = 'americas'
    Latam = 'latam'
    Europe = 'europe'
    Asia = 'asia'
    Oceania = 'oceania'
    USA = 'usa'
    Canada = 'canada'
    France = 'france'
    UKnIreland = 'ukie'
    Portugal = 'portugal'
    Italy = 'italy'
    GermanynAustria = 'deat'
    Benelux = 'benelux'
    Nordic = 'nordic'
    Japan = 'japan'


async def execute(ctx: CommandInteraction, country: str = 'spain'):
    ranking = get_ranking(country)
    response = f">>> **Player Ranking ({country})**\n"
    for row in ranking[:50]:
        response += f"{str(row.get('position')) + '.': <5} {row.get('player'):>10} {row.get('points'):^20}\n"
    await ctx.send(response)
