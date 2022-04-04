from .ownermanagement import OwnerManagement


async def setup(bot):
    cog = OwnerManagement()
    await cog.initialize()
    bot.add_cog(cog)
