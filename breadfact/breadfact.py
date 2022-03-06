from redbot.core import commands, cog_manager
import random, discord, json


class BreadFact(commands.Cog):
    """Sends a random bread fact!"""
    __author__ = "JeffJrShim#2396, ＜－モカアオバ#6142"
    __version__ = "0.1.2"

    def __init__(self, bot):
        self.bot = bot
    
    def format_help_for_context(self, ctx: commands.Context) -> str:
        """Thanks Sinbad!"""
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nAuthors: {', '.join(self.__author__)}\nCog Version: {self.__version__}"

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
