from .breadfact import BreadFact


def setup(bot):
    cog = BreadFact()
    await cog.initialize()
    bot.add_cog(cog)
