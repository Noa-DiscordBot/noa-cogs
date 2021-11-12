from redbot.core import modlog, commands 
import discord
from datetime import datetime


class FakeMod(commands.Cog):
    """Fake moderation commands"""

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
                "default_setting": False,
                "image": "\N{BOOT}<:Ayaa:858201202017435659>",
                "case_str": "Keck",
            }
        ]
        await modlog.register_casetypes(new_types)

    @commands.command()
    @commands.guild_only()
    @commands.mod_or_permissions()
    async def bam(self, ctx, user: discord.Member, reason: str = None):
        """Bams a user! 
        """
        case = await modlog.create_case(
            ctx.bot, ctx.guild, datetime.now() , action_type="bam", user=user, moderator=ctx.author, reason=reason
        )

        await ctx.send(f"Banned {user}.")

    @commands.command()
    @commands.guild_only()
    @commands.mod_or_permissions()
    async def keck(self, ctx, user: discord.Member, reason: str = None):
        """Kecks a user! 
        """
        case = await modlog.create_case(
            ctx.bot, ctx.guild, datetime.now() , action_type="keck", user=user, moderator=ctx.author, reason=reason
        )

        await ctx.send(f"Kicked {user}.")
