from redbot.core import commands, cog_manager
import random
import discord
import json


class RandomNoa(commands.Cog):
    """Sends a random Noa card from the official D4DJ Groovy Mix game."""

    def __init__(self, bot):
        self.bot = bot
        
    async def random_noa(self):
        cm = cog_manager.CogManager()
        ipath = str(await cm.install_path())
        # cards = json.load(open(ipath + "/randomnoa/cards.json", "r"))
        with open(ipath + "/randomnoa/cards.json", "r",  encoding="utf-8") as noa:
            data = json.load(noa)
            noas = data["noas"]
            random_index = str(random.randint(0, len(noas)-1))
            return_data = {
                "title": noas[random_index]["title"],
                "url": noas[random_index]["image_url"],
                "desc": noas[random_index]["desc"]
            }
            return return_data

    @commands.command()
    async def randomnoa(self, ctx):
        """Sends a random Noa card from the official D4DJ Groovy Mix game. (JP version.)"""
        # cm = cog_manager.CogManager()
        # ipath = str(await cm.install_path())
        # cards = json.load(open(ipath + "/randomnoa/cards.json", "r"))
        # noachoice = random.randint(1, 29)

        data =  await self.random_noa()
        embed = discord.Embed(
            title=data["title"],
            description=data["desc"],
            color=await ctx.embed_colour()
        )
        embed.set_image(url=data["url"])
        try:
            await ctx.reply(embed=embed, mention_author=False)
        except discord.HTTPException:
            await ctx.send(embed=embed)
