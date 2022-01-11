from redbot.core import commands

class MyCog(commands.Cog):
    """Bread facts!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def breadfact(self, ctx):
        """Gets bread facts randomly :-)"""
        # Your code will go here
        await ctx.send()
