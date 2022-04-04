from .ownermanagement import OwnerManagement


def setup(bot):
    await bot.add_cog(OwnerManagement(bot))
