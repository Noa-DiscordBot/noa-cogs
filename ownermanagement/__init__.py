from .ownermanagement import OwnerManagement


async def setup(bot):
    cog = OwnerManagement()
    bot.add_cog(cog)
