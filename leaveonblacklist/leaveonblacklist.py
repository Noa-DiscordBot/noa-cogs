from redbot.core.commands import *

class LeaveOnBlacklist(Cog):
    
  __author__ = ["JeffJrShim", "Guacaplushy"]
  __version__ = "1.0.0"

  def __init__(self, bot):
    self.bot = bot

  def format_help_for_context(self, ctx: commands.Context) -> str:
    """Thanks Sinbad!"""
    pre_processed = super().format_help_for_context(ctx)
    return f"{pre_processed}\n\nAuthors: {', '.join(self.__author__)}\nCog Version: {self.__version__}"
  
  @Cog.listener()
  async def on_guild_join(self, guild):
    is_blacklisted = not await self.bot.allowed_by_whitelist_blacklist(who_id=guild.owner_id)
    if is_blacklisted:
      await guild.leave()
