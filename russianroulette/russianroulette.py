import asyncio
import random

import discord
from redbot.core import Config, commands


class RussianRoulette(commands.Cog):
    """russian roulette tbh"""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=723841)
        default_guild = {
            "chances": 6,
            "dead_msg": "BANG! You're dead!",
            "safe_msg": "Click! You're safe!",
        }
        self.config.register_guild(**default_guild)

    @commands.command()
    @commands.max_concurrency(1, commands.BucketType.channel)
    async def russianroulette(self, ctx):
        """try your luck"""
        chances_val = await self.config.guild(ctx.guild).chances()
        killmsg = await self.config.guild(ctx.guild).dead_msg()
        safemsg = await self.config.guild(ctx.guild).safe_msg()
        russianroulettegenerator = random.randint(1, chances_val)
        embed = discord.Embed(
            description="You pulled the trigger and...", color=await ctx.embed_color()
        )
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(3)
        if russianroulettegenerator == 1:
            embed2 = discord.Embed(
                description=f"You pulled the trigger and...\n\n{killmsg}",
                color=await ctx.embed_color(),
            )
            await msg.edit(embed=embed2)
        else:
            embed3 = discord.Embed(
                description=f"You pulled the trigger and...\n\n{safemsg}",
                color=await ctx.embed_color(),
            )
            await msg.edit(embed=embed3)

    @commands.mod()
    @commands.group()
    async def russianrouletteset(self, ctx):
        """Set defaults for the russian roulette"""
        pass

    @commands.mod()
    @russianrouletteset.command(alias=["chances"])
    async def chamber(self, ctx, new_value: int):
        """Sets the chamber value for the Russian Roulette."""
        if new_value < 2:
            return await ctx.send("The chamber value cannot be less than 2.")
        elif new_value > 50:
            return await ctx.send("The chamber value cannot be more than 50.")
        else:
            await self.config.guild(ctx.guild).chances.set(new_value)
            await ctx.send("The new value has been set.")

    @commands.mod()
    @russianrouletteset.command(alias=["survivemsg"])
    async def safemsg(self, ctx, new_value: str = "Click! You're safe!"):
        """Set default message when you're safe."""
        await self.config.guild(ctx.guild).safe_msg.set(new_value)
        await ctx.send("The new value has been set.")

    @commands.mod()
    @russianrouletteset.command(alias=["deadmsg"])
    async def killmsg(self, ctx, new_value: str = "BANG! You're dead!"):
        """Set default message when you're killed."""
        await self.config.guild(ctx.guild).dead_msg.set(new_value)
        await ctx.send("The new value has been set.")

    @russianrouletteset.command()
    async def view(self, ctx):
        """Shows the configuration of the cog."""
        chancesvalue = await self.config.guild(ctx.guild).chances()
        killmsgvalue = await self.config.guild(ctx.guild).dead_msg()
        safemsgvalue = await self.config.guild(ctx.guild).safe_msg()
        embed = discord.Embed(
            title=f"{ctx.guild}'s Russian Roulette Configuration", color=await ctx.embed_color()
        )
        embed.add_field(name="Chances", value=chancesvalue, inline=False)
        embed.add_field(name="Death Message", value=killmsgvalue, inline=False)
        embed.add_field(name="Safe Message", value=safemsgvalue, inline=False)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(
            text=f"To edit these values, use {ctx.prefix}help russianrouletteset to see the commands."
        )
        await ctx.send(embed=embed)
