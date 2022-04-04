from .ownermanagement import OwnerManagement


async def setup(bot):
    cog = OwnerManagement(bot)
    bot.add_cog(cog)
