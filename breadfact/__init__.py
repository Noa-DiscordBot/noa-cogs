from .breadfact import BreadFact


def setup(bot):
    cog = BreaFact()
    await cog.initialize()
    bot.add_cog(cog)
