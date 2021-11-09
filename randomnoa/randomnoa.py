from redbot.core import commands
import random, discord, json

class RandomNoa(commands.Cog):
    """Sends a random Noa card from the official D4DJ Groovy Mix game."""

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def randomnoa(self, ctx):
        cards = json.load(open("cards.json", "r"))
        noachoice = random.randint(1, 2)

        if noachoice == 1:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: Uniform \n Rarity: 1 ⭐ \n Untrained or Trained: None \n ", color=0x581919)
            embed.set_image(cards[noachoice])
            await ctx.send(embed=embed)
        
        else:
            e=discord.Embed(title="Random Noa generated!", description="Card Name: DJ- LIVE! \n Rarity: 2 ⭐\n Untrained or Trained: None \n ", color=0x581919)
            e.set_image(cards[noachoice])
            await ctx.send(embed=e)
