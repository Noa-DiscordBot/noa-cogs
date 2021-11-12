from redbot.core import commands, cog_manager
import random, discord, json

class RandomNoa(commands.Cog):
    """Sends a random Noa card from the official D4DJ Groovy Mix game."""

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def randomnoa(self, ctx):
        cm = cog_manager.CogManager()
        ipath = str(await cm.install_path())
        cards = json.load(open(ipath + "/randomnoa/cards.json", "r"))
        noachoice = random.randint(1, 25)

        if noachoice == 1:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: Uniform \n Rarity: 1⭐ \n Untrained or Trained: None \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.reply(embed=embed, mention_author=False)

        elif noachoice == 2:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: DJ-LIVE! \n Rarity: 2⭐\n Untrained or Trained: None \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.reply(embed=embed, mention_author=False)

        elif noachoice == 3:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: DJ-MIX! \n Rarity: 2⭐\n Untrained or Trained: None \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.reply(embed=embed, mention_author=False)

        elif noachoice == 4:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: CuteBringer \n Rarity: 3⭐\n Untrained or Trained: Untrained \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.reply(embed=embed, mention_author=False)
        
        elif noachoice == 5:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: CuteBringer \n Rarity: 3⭐\n Untrained or Trained: Trained \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.reply(embed=embed, mention_author=False)

        elif noachoice == 6:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: Melty Smile \n Rarity: 3⭐\n Untrained or Trained: Untrained \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.reply(embed=embed, mention_author=False)

        elif noachoice == 7:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: Melty Smile \n Rarity: 3⭐\n Untrained or Trained: Trained \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.reply(embed=embed, mention_author=False)

        elif noachoice == 8:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: EXウルムーα\n Rarity: 3⭐\n Untrained or Trained: Untrained \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.reply(embed=embed, mention_author=False)

        elif noachoice == 9:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: EXウルムーα \n Rarity: 3⭐\n Untrained or Trained: Trained \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.reply(embed=embed, mention_author=False)

        elif noachoice == 10:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: Enchanted Lamp \n Rarity: 3⭐\n Untrained or Trained: Untrained \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.reply(embed=embed, mention_author=False)

        elif noachoice == 11:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: Enchanted Lamp \n Rarity: 3⭐\n Untrained or Trained: Trained  \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.reply(embed=embed, mention_author=False)

        elif noachoice == 12:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: Skydrifter \n Rarity: 4⭐\n Untrained or Trained: Untrained  \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])        
            await ctx.reply(embed=embed, mention_author=False)

        elif noachoice == 13:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: Skydrifter \n Rarity: 4⭐\n Untrained or Trained: Trained  \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.reply(embed=embed, mention_author=False)

        elif noachoice == 14:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: Fantastic Lantern \n Rarity: 4⭐\n Untrained or Trained: Untrained  \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.reply(embed=embed, mention_author=False)

        elif noachoice == 15:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: Fantastic Lantern \n Rarity: 4⭐\n Untrained or Trained: Trained  \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.reply(embed=embed, mention_author=False)

        elif noachoice == 16:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: Sweet Cookie \n Rarity: 4⭐\n Untrained or Trained: Untrained  \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.reply(embed=embed, mention_author=False)

        elif noachoice == 17:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: Sweet Cookie \n Rarity: 4⭐\n Untrained or Trained: Trained  \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.reply(embed=embed, mention_author=False)

        elif noachoice == 18:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: \n - English name: Brilliant Hydrangea\n - Japanese name: 燦爛たるあじさい \n Rarity: 4⭐\n Untrained or Trained: Untrained  \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])  
            await ctx.reply(embed=embed, mention_author=False)
        
        elif noachoice == 19:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: \n - English name: Brilliant Hydrangea\n - Japanese name: 燦爛たるあじさい \n Rarity: 4⭐\n Untrained or Trained: Trained \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.reply(embed=embed, mention_author=False)

        elif noachoice == 20:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: Lemonade Flash \n Rarity: 4⭐\n Untrained or Trained: Untrained \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.reply(embed=embed, mention_author=False)

        elif noachoice == 21:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: Lemonade Flash \n Rarity: 4⭐\n Untrained or Trained: Trained \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.reply(embed=embed, mention_author=False)

        elif noachoice == 22:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: Birthday Noa (1st Set) \n Rarity: 4⭐\n Untrained or Trained: Untrained \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.reply(embed=embed, mention_author=False)

        elif noachoice == 23:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: Birthday Noa (1st Set) \n Rarity: 4⭐\n Untrained or Trained: Trained \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.reply(embed=embed, mention_author=False)

        elif noachoice == 24:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: 1st Anniversary \n Rarity: 4⭐\n Untrained or Trained: Trained \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.reply(embed=embed, mention_author=False)

        else:
            embed=discord.Embed(title="Is that.... a prank?", description="Card Name: Pingu Hitting Those Moves \n Rarity: 20:star: \n Untrained or Trained: Trained (obviously?) \n ", color=await ctx.embed_color())
            embed.set_image(url=" https://c.tenor.com/wuyEcsxrvQwAAAAC/club-penguin-ghosthy.gif ")
            await ctx.reply(embed=embed, mention_author=False)

 #    @commands.command()
 #   async def aboutnoa(self,ctx):
 #       embed=discord.Embed(title="About Noa", description="Card Name: Pingu Hitting Those Moves \n Rarity: 20:star: \n Untrained or Trained: Trained (obviously?) \n ", color=await ctx.embed_color())
 #       embed.set_image(url=" https://c.tenor.com/wuyEcsxrvQwAAAAC/club-penguin-ghosthy.gif ")
#        await ctx.reply(embed=embed, mention_author=False)