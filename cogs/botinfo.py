import discord
from discord.ext import commands

class botinfo():
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def botinfo(self, ctx, *, user: discord.Member=None):

       embed=discord.Embed(title="informações do bot", description="essas são minha informações")
       embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/409821602012856321/8247dc94c2c4527db0058c898e82780d.webp?size=1024")
       embed.add_field(name="Nome do bot", value="`-_-SkyBot-_-`", inline=True)
       embed.add_field(name="Criado em", value="`12/12/2018`", inline=True)
       embed.add_field(name="Meu id", value="`516991068521103372`", inline=True)
       embed.add_field(name="meu dono", value="<@409821602012856321>", inline=True)
       embed.add_field(name="Eu fui programado em", value="`Python 3.7.2` <:python:507486258184978443> ", inline=False)
       embed.set_footer(text="Direitos reservador")
       await ctx.send(embed=embed)

def setup(client):
    print("[Comando botinfo] Carregado")
    client.add_cog(botinfo(client))
