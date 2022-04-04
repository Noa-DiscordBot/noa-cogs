from .randomnoa import RandomNoa


async def setup(bot):
    cog = RandomNoa(bot)
    bot.add_cog(cog)
