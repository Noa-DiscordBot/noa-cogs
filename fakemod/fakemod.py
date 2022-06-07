from datetime import datetime

import discord
from redbot.core import commands, modlog


class FakeMod(commands.Cog):
    """Fake moderation commands"""

    __author__ = ["JeffJrShim", "Guacaplushy"]
    __version__ = "1.0.1"

    def format_help_for_context(self, ctx: commands.Context) -> str:
        """Thanks Sinbad!"""
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nAuthors: {', '.join(self.__author__)}\nCog Version: {self.__version__}"

    async def initialize(self):
        await self.register_casetypes()

    @staticmethod
    async def register_casetypes():
        new_types = [
            {
                "name": "bam",
                "default_setting": True,
                "image": "\N{HAMMER}<:Ayaa:858201202017435659>",
                "case_str": "Bam",
            },
            {
                "name": "keck",
                "default_setting": True,
                "image": "\N{WOMANS BOOTS}<:Ayaa:858201202017435659>",
                "case_str": "Keck",
            },
            {
                "name": "moot",
                "default_setting": True,
                "image": "\N{FACE WITH FINGER COVERING CLOSED LIPS}<:Ayaa:858201202017435659>",
                "case_str": "Moot",
            },
            {
                "name": "warm",
                "default_setting": True,
                "image": "\N{WARNING SIGN}<:Ayaa:858201202017435659>",
                "case_str": "Warm",
            },
        ]
        await modlog.register_casetypes(new_types)

    @commands.command()
    @commands.guild_only()
    @commands.mod_or_permissions()
    async def bam(self, ctx, user: discord.Member, *, reason: str = None):
        """Bams a user!"""
        await modlog.create_case(
            ctx.bot,
            ctx.guild,
            datetime.now(),
            action_type="bam",
            user=user,
            moderator=ctx.author,
            reason=reason,
        )

        await ctx.send(f"Bammed {user}.")

    @commands.command()
    @commands.guild_only()
    @commands.mod_or_permissions()
    async def keck(self, ctx, user: discord.Member, *, reason: str = None):
        """Kecks a user!"""
        await modlog.create_case(
            ctx.bot,
            ctx.guild,
            datetime.now(),
            action_type="keck",
            user=user,
            moderator=ctx.author,
            reason=reason,
        )

        await ctx.send(f"Kecked {user}.")

    @commands.command()
    @commands.guild_only()
    @commands.mod_or_permissions()
    async def moot(self, ctx, user: discord.Member, *, reason: str = None):
        """Moots a user!"""
        await modlog.create_case(
            ctx.bot,
            ctx.guild,
            datetime.now(),
            action_type="moot",
            user=user,
            moderator=ctx.author,
            reason=reason,
        )

        await ctx.send(f"Mooted {user}.")

    @commands.command()
    @commands.guild_only()
    @commands.mod_or_permissions()
    async def warm(self, ctx, user: discord.Member, *, reason: str = None):
        """Warms a user!"""
        await modlog.create_case(
            ctx.bot,
            ctx.guild,
            datetime.now(),
            action_type="warm",
            user=user,
            moderator=ctx.author,
            reason=reason,
        )

        await ctx.send(f"Warmed {user}.")
