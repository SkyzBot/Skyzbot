import discord
from discord.ext import commands

class pic():
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def pic(self, ctx, *, user: discord.Member=None):
     if user is None:
        usuario = ctx.author.avatar_url
        texto = f"Olá {ctx.author.name}, esta é o seu avatar"
     else:
         usuario = user.avatar_url
         texto = f"Olá {ctx.author.name}, esta é o avatar o {user.name}"

     embed = discord.Embed(title=texto, color=0xF4CBD1)
     embed.set_image(url=usuario)
     embed.set_footer(text=self.client.user.name+"meus direitos!")
     await ctx.send(embed=embed)


def setup(client):
    print("[Comando pic] Carregado")
    client.add_cog(pic(client))
