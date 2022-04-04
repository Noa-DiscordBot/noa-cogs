from .randomnoa import RandomNoa


async def setup(bot):
    cog = RandomNoa()
    # await bot.cog.initialize()
    bot.add_cog(cog)
