from .LeaveOnBlacklist import LeaveOnBlacklist
      

def setup(bot):
  bot.add_cog(LeaveOnBlacklist(bot))
