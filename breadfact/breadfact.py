import json
import random

import discord
from redbot.core import commands
from redbot.core.data_manager import bundled_data_path


class BreadFact(commands.Cog):
    """Sends a random bread fact!"""

    __author__ = ["JeffJrShim, ＜－モカアオバ#6142"]
    __version__ = "0.1.2"

    def __init__(self, bot):
        self.bot = bot

    def format_help_for_context(self, ctx: commands.Context) -> str:
        """Thanks Sinbad!"""
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nAuthors: {', '.join(self.__author__)}\nCog Version: {self.__version__}"

    @commands.command()
    async def breadfact(self, ctx):
        facts = None
        with open(bundled_data_path(self) / "cards.json", "r", encoding="utf-8") as fact_file:
            facts = json.load(fact_file)
        bfint = random.randint(0, 49)
        try:
            await ctx.reply(facts[bfint], mention_author=False)
        except discord.HTTPException:
            await ctx.send(facts[bfint])
