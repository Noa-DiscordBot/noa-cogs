from .ownermanagement import OwnerManagement


async def setup(bot):
    cog = OwnerManagement(bot)
    await bot.add_cog(cog)
