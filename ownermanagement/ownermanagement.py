from redbot.core import commands
import discord

class OwnerManagement(commands.Cog):
    """Owner management utilities."""

    __author__ = ["JeffJrShim"]
    __version__ = "1.0.0"

    def __init__(self, bot):
        self.bot = bot
        self.default_owners = self.bot.owner_ids.copy()

    def format_help_for_context(self, ctx: commands.Context) -> str:
        """Thanks Sinbad!"""
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nAuthors: {', '.join(self.__author__)}\nCog Version: {self.__version__}"

    @commands.group(invoke_without_command=True)
    @commands.is_owner()
    async def owner(self, ctx):
        """Owner management commands"""
        if ctx.invoked_subcommand is None:
            bois = ""
            for boi in list(self.bot.owner_ids):
                boi = self.bot.get_user(boi)
                bois += f"- {boi} (`{boi.id}`)"
            embed = discord.Embed(title="Current Bot Owner IDs:", description=bois, color=await ctx.embed_color())
            await ctx.send(embed=embed)

    @owner.command(invoke_without_command=True)
    @commands.is_owner()
    async def add(self, ctx, *, user: discord.User):
        """Add an owner. Be sure to note that adding the user as an owner will give that user access to everything on your bot. Use this command at your own risk."""
        user = self.bot.get_user(user.id)
        if user.id in self.bot.owner_ids:
            return await ctx.send("That user is already one of the bot owners.")
        else:
            self.bot.owner_ids.add(user.id)
            await ctx.tick()
            msg = f"{user} is now a bot owner. Do note that this user currently **has access to everything on the bot, including being able to remove your ownership from the bot.** If you've done this by mistake, please do `{ctx.prefix}owner remove {user.id}` Owners set with this command don't persist during restart. To have a more permanent option, use `redbot instancename --owner {ctx.author.id} --co-owner {user.id}`"
            await ctx.send(msg, reference=ctx.message.to_reference())

    @owner.command(invoke_without_command=True)
    @commands.is_owner()
    async def remove(self, ctx, *, user: discord.User):
        """Removes an owner from the bot."""
        user = self.bot.get_user(user.id)

        remmsg = f"{user} is no longer a bot owner."
        getoutmsg = f"{user} is a default owner, and cannot be removed."
        if user.id in self.default_owners:
            return await ctx.send(getoutmsg, reference=ctx.message.to_reference())
        else:
            if user.id not in self.bot.owner_ids:
                return await ctx.send("That user isn't one of the bot owners.")
            else:
                self.bot.owner_ids.remove(user.id)
                await ctx.tick()
                await ctx.send(remmsg, reference=ctx.message.to_reference())
