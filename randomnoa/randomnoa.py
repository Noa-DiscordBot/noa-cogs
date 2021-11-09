from redbot.core import commands
import random
import discord

class RandomNoa(commands.Cog):
    """Sends a random Noa card from the official D4DJ Groovy Mix game."""

    def __init__(self, bot):
        self.bot = bot

    link_1="https://i.ibb.co/gyLRVCf/noa1star.png"
    link_2="https://i.ibb.co/zQTQMVh/noa2star.png"
    link_3="https://i.ibb.co/B4V3hYf/noa2starfirstanniversary.png"
    link_4="https://i.ibb.co/16W96zr/noa3starinitial.png"
    link_5="https://i.ibb.co/mHZQDFR/noa3starinitial-t.png"
    link_6="https://i.ibb.co/W3SxhHh/noa3stard4fes.png"
    link_7="https://i.ibb.co/wMycFKV/noa3stard4fes-t.png"
    link_8="https://i.ibb.co/1MyW8sR/noa3starmonhun.png"
    link_9="https://i.ibb.co/47sRfZj/noa3starmonhun-t.png"
    link_10="https://i.ibb.co/Yh2NYvW/noa3starteamcevent.png"
    link_11="https://i.ibb.co/LJWHthY/noa3starteamcevent-t.png"
    link_12="https://i.ibb.co/hW91cM4/noa4starinitial.png"
    link_13="https://i.ibb.co/554b9wy/noa4starinitial-t.png"
    link_14="https://i.ibb.co/ThSRvzd/noa4starlantern.png"
    link_15="https://i.ibb.co/5195Zyt/noa4starlantern-t.png"
    link_16="https://i.ibb.co/XjRt3sC/noa4starwhiteday.png"
    link_17="https://i.ibb.co/tZdK2Sf/noa4starwhiteday-t.png"
    link_18="https://i.ibb.co/HCv4rrc/noa4stargotoubun.png"
    link_19="https://i.ibb.co/hCHGkvf/noa4stargotoubun-t.png"
    link_20="https://i.ibb.co/SRp0Sqm/noa4startanabata.png"
    link_21="https://i.ibb.co/hdsvF8S/noa4startanabata-t.png"
    link_22="https://i.ibb.co/TLwFN5G/noa4starbirthday.png"
    link_23="https://i.ibb.co/mb2QRdz/noa4starbirthday-t.png"
    link_24="https://i.ibb.co/GCFH5mp/noaSP.png"

    @commands.command()
    async def randomnoa(self, ctx):
        noachoice = random.randint(1, 2)

        if noachoice == 1:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: \n Rarity: \n Untrained or Trained: \n ", color=0x581919)
            await ctx.send(embed=embed)
        
        else:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: \n Rarity: \n Untrained or Trained: \n ", color=0x581919)
            await ctx.send(embed=embed)
