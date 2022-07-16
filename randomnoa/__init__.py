from .randomnoa import RandomNoa


async def setup(bot):
    cog = RandomNoa(bot)
    await bot.add_cog(cog)
