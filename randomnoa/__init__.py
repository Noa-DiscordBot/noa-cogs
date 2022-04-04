from .randomnoa import RandomNoa


def setup(bot):
    cog = RandomNoa()
    await cog.initialize()
    bot.add_cog(cog)
