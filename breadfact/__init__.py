from .breadfact import BreadFact


def setup(bot):
    await bot.add_cog(BreadFact(bot))
