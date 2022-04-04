from .breadfact import BreadFact


async def setup(bot):
    cog = BreadFact()
    bot.add_cog(cog)
