from .randomnoa import RandomNoa


def setup(bot):
    await bot.add_cog(RandomNoa(bot))
