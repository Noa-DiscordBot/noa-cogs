from redbot.core import commands, cog_manager
import random, discord, json

class BreadFact(commands.Cog):
    """Sends a random bread fact!"""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def breadfact(self, ctx):
        await ctx.send("owo")