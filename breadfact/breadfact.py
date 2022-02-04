from redbot.core import commands, cog_manager
import random, discord, json


class BreadFact(commands.Cog):
    """Sends a random bread fact!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def breadfact(self, ctx):
        cm = cog_manager.CogManager()
        ipath = str(await cm.install_path())
        facts = json.load(open(ipath + "/breadfact/facts.json", "r", encoding="utf-8"))
        bfint = random.randint(0, 49)
        try:
            await ctx.reply(facts[bfint], mention_author=False)
        except discord.HTTPException:
            await ctx.send(facts[bfint])
