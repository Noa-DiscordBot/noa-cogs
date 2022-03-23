from redbot.core import commands, cog_manager, Config
import random
import discord
import json


class RandomNoa(commands.Cog):
    """Sends a random Noa card from the official D4DJ Groovy Mix game."""

    __author__ = ["JeffJrShim"]
    __version__ = "1.0.1"

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=694641)
        default_guild = {"rigged": False, "cards": ""}
        self.config.register_guild(**default_guild)

    async def random_noa(self):
        cm = cog_manager.CogManager()
        ipath = str(await cm.install_path())
        with open(ipath + "/randomnoa/cards.json", "r", encoding="utf-8") as noa:
            data = json.load(noa)
            noas = data["noas"]
            rig_val = await self.config.guild(ctx.guild).rigged()
            card_no = await self.config.guild(ctx.guild).cards()
            if await bot.is_owner(ctx.author) == True and rig_val == True:
                index = str(card_no)
                return_data = {
                    "title": noas[index]["title"],
                    "url": noas[index]["image_url"],
                    "desc": noas[index]["desc"],
                }
            else:
                random_index = str(random.randint(1, len(noas)))
                return_data = {
                    "title": noas[random_index]["title"],
                    "url": noas[random_index]["image_url"],
                    "desc": noas[random_index]["desc"],
                }
            return return_data

    @commands.command()
    async def randomnoa(self, ctx):
        """
        Sends a random Noa card from the official D4DJ Groovy Mix game. (JP version.)
        """

        data = await self.random_noa()
        embed = discord.Embed(
            title=data["title"],
            description=data["desc"],
            color=await ctx.embed_colour(),
        )
        embed.set_image(url=data["url"])
        try:
            await ctx.reply(embed=embed, mention_author=False)
        except discord.HTTPException:
            await ctx.send(embed=embed)

    @commands.is_owner()
    @commands.group()
    async def randomnoaset(self, ctx):
        """Setup RandomNoa."""
        pass
    
    @randomnoaset.command()
    async def rigged(self, ctx, rig: bool):
        """Toggle the rigged random noa."""
        await self.config.guild(ctx.guild).rigged.set(rig)
        await ctx.send("The new value has been set.")
    
    @randomnoaset.command()
    async def riggedcard(self, ctx, card: str):
        """Choose the rigged card"""
        await self.config.guild(ctx.guild).cards(card)
        await ctx.send("The new card value has been set.")

    @randomnoaset.command()
    async def view(self, ctx):
        """View configuration settings, will make nicer when it actually works"""
        riggedval = await self.config.guild(ctx.guild).chances()
        cardno = await self.config.guild(ctx.guild).cards()
        await ctx.send(f"```Rigged?: {riggedval}\n\n Card No: {cardno}```")