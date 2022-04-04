from .randomnoa import RandomNoa


async def setup(bot):
    cog = RandomNoa()
    await cog.initialize()
    bot.add_cog(cog)
