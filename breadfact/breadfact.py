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
        facts = json.load(open(ipath + "/breadfact/facts.json", "r"))
        bfint = random.randint(0,57)
        await ctx.send(facts[bfint])

