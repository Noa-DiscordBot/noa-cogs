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
        bfint = random.randint(0,57)
        if ctx.author.id == 750325757024141392 or ctx.author.id == 818631385392218112:
            await ctx.send(facts[bfint])
        elif bfint == 8 or bfint == 15 or bfint == 27 or bfint == 36 or bfint == 48 or bfint == 57:
            await ctx.send(facts[bfint+1])

