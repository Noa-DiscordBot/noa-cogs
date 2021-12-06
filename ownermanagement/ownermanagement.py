from discord.ext import commands
from redbot.core import commands 
from typing import Union
import humanize
from redbot.core.utils.chat_formatting import box, humanize_list
import discord
import random

class OwnerManagement(commands.Cog):
    """Owner management utilities."""

    def __init__(self, bot):
        self.bot = bot
        self.default_owners = self.bot.owner_ids.copy()
    
    @commands.group(invoke_without_command="True")
    @commands.is_owner()
    async def owner(self,ctx):
        """Owner management commands"""
        if ctx.invoked_subcommand is None:
            bois=next(iter(self.bot.owner_ids))
            await ctx.send(f"Current Bot Owner IDs:\n{bois}")

    @owner.command(invoke_without_command="True")
    @commands.is_owner()
    async def add(self, ctx, *, user: discord.User):
        """Add an owner. Be sure to note that adding the user as an owner will give that user access to everything on your bot. Use this command at your own risk."""
        user=self.bot.get_user(user.id)
        self.bot.owner_ids.add(user.id)
        await ctx.tick()
        msg=f"{user} is now a bot owner. Do note that this user currently **has access to everything on the bot, including being able to remove your ownership from the bot.** If you've done this by mistake, please do `{ctx.prefix}owner remove {user.id}` Owners set with this command don't persist during restart. To have a more permanent option, use `redbot instancename --owner {ctx.author.id} --co-owner {user.id}`"
        await ctx.send(msg)

    @owner.command(invoke_without_command="True")
    @commands.is_owner()
    async def remove(self, ctx, *, user: discord.User):
        """Removes an owner from the bot."""
        user=self.bot.get_user(user.id)
        
        remmsg=f"{user} is no longer a bot owner."
        getoutmsg=f"{user} is a default owner, and cannot be removed."
        if user.id in self.default_owners:
            await ctx.send(getoutmsg)
        else:
            self.bot.owner_ids.remove(user.id)
            await ctx.tick()
            await ctx.send(remmsg)
        
