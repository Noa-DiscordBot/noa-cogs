from .fakemod import FakeMod

async def setup(bot):
    cog = FakeMod()
    await cog.initialize()
    bot.add_cog(cog)
