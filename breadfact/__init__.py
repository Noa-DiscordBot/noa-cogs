from .breadfact import BreadFact


async def setup(bot):
    cog = BreadFact()
    await cog.initialize()
    bot.add_cog(cog)
