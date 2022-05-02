from .russianroulette import RussianRoulette


async def setup(bot):
    cog = RussianRoulette(bot)
    await bot.add_cog(cog)