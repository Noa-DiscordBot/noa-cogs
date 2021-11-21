from redbot.core.commands import *

class LeaveOnBlacklist(Cog):

  def __init__(self, bot):
    self.bot = bot
  
  @Cog.listener()
  async def on_guild_join(self, guild):
    is_blacklisted = not await self.bot.allowed_by_whitelist_blacklist(who_id=guild.owner_id)
    if is_blacklisted:
      await guild.leave()
