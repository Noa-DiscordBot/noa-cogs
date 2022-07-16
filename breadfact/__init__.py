from .breadfact import BreadFact


async def setup(bot):
    cog = BreadFact(bot)
    await bot.add_cog(cog)
