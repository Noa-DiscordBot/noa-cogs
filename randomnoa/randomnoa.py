import json
import random
from dataclasses import dataclass

import discord
from redbot.core import Config, commands
from redbot.core.data_manager import bundled_data_path


@dataclass
class Card:
    title: str
    url: str
    card_name: str
    rarity: str
    trained: str


class RandomNoa(commands.Cog):
    """Sends a random Noa card from the official D4DJ Groovy Mix game."""

    __author__ = ["JeffJrShim, Onii-Chan"]
    __version__ = "2.0.0"

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=694641)
        default_config = {"rigged": False, "card": None}
        self.config.register_global(**default_config)

    async def random_noa(self, ctx):
        with open(bundled_data_path(self) / "cards.json", "r", encoding="utf-8") as noa:
            data = json.load(noa)
            noas = data["noas"]
            rigged = await self.config.rigged()
            card_no = await self.config.card()
            if await self.bot.is_owner(ctx.author) == True and rigged == True:
                card = noas[str(card_no)]
                card_data = Card(
                    card["title"],
                    card["image_url"],
                    card["card_name"],
                    card["rarity"],
                    card["trained"],
                )
            else:
                card = noas[str(random.randint(1, len(noas)))]
                card_data = Card(
                    card["title"],
                    card["image_url"],
                    card["card_name"],
                    card["rarity"],
                    card["trained"],
                )
            return card_data

    @commands.command()
    async def randomnoa(self, ctx):
        """
        Sends a random Noa card from the official D4DJ Groovy Mix game. (JP version.)
        """

        data = await self.random_noa(ctx)
        embed = discord.Embed(
            title=data.title,
            color=await ctx.embed_colour(),
        )
        embed.set_image(url=data.url)
        embed.add_field(name="Card Name", value=data.card_name, inline=True)
        embed.add_field(name="Rarity", value=data.rarity, inline=True)
        embed.add_field(name="Trained", value=data.trained, inline=True)
        embed.set_footer(text="Powered by Lena",
                icon_url="https://bae.lena.moe/l9q3mnnat3i3.gif",
            )
        try:
            await ctx.reply(embed=embed, mention_author=False)
        except discord.HTTPException:
            await ctx.send(embed=embed)

    @commands.is_owner()
    @commands.group()
    async def randomnoaset(self, ctx):
        """Setup RandomNoa."""
        pass

    @commands.is_owner()
    @randomnoaset.command()
    async def rigged(self, ctx, rig: bool):
        """Toggle the rigged random noa."""
        await self.config.rigged.set(rig)
        await ctx.send("The new value has been set.")

    @commands.is_owner()
    @randomnoaset.command()
    async def riggedcard(self, ctx, card: int):
        """Choose the rigged card"""
        with open(bundled_data_path(self) / "cards.json", "r", encoding="utf-8") as noa:
            data = json.load(noa)
            noas = data["noas"]
        if card > len(noas) or card < 1:
            return await ctx.send(f"The value cannot be less then 1 or more then {len(noas)}")
        else:
            await self.config.card.set(card)
        await ctx.send("The new card value has been set.")

    @commands.is_owner()
    @randomnoaset.command()
    async def view(self, ctx):
        """View configuration settings, will make nicer when it actually works"""
        riggedval = await self.config.rigged()
        cardno = await self.config.card()
        await ctx.send(
            f"```ini\n[  Toggled:  ] {riggedval}\n[  Card No (if rigged):  ] {cardno} (See JSON file for more information.)```"
        )
