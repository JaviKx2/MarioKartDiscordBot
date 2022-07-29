import os
import uuid

from discord import File, Embed
from discord.ext.commands import command, Context
from html2image import Html2Image
from jinja2 import Environment, FileSystemLoader, select_autoescape

from src.MKLeaderboards import get_course


@command(
    aliases=["l", "lb"],
    help="Leaderboards"
)
async def leaderboards(ctx: Context, *args):
    course_data = get_course(args[0])
    track = dict(
        name=course_data.get('track_name'),
        image_url=f"https://www.mkleaderboards.com/images/mkw/{course_data.get('track_abbrev')}.png",
        top=[
            dict(
                rank=player.get('rank'),
                name=player.get('name'),
                score_formatted=player.get('score_formatted')
            ) for player in course_data.get('data')]
    )
    file = generate_top10_image_file(track)
    response = Embed(title=track.get("name"), description="Top 10")
    response.set_image(url="attachment://{}".format(file.filename))
    await ctx.send(file=file, embed=response)
    os.remove(file.filename)


@leaderboards.after_invoke
async def after_invoke(ctx: Context):
    await ctx.send(f"<@{ctx.author.id}>, results are ready!", reference=ctx.message)


def generate_top10_image_file(track) -> File:
    filename = 'top10_{}.png'.format(uuid.uuid4())
    hti = Html2Image()
    screenshot = hti.screenshot(html_str=render(track), css_file='templates/top10/top10.css', size=(700, 1000),
                                save_as=filename)
    return File(screenshot[0], filename)


def render(track):
    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape()
    )
    template = env.get_template("top10/top10.html")
    return template.render(track=track)
