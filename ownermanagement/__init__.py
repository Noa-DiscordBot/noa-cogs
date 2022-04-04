from .ownermanagement import OwnerManagement


def setup(bot):
    cog = OwnerManagement()
    await cog.initialize()
    bot.add_cog(cog)
