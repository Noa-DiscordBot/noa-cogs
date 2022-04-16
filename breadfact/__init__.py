from .breadfact import BreadFact


def setup(bot):
    bot.add_cog(BreadFact(bot))
