import discord
from discord.ext import commands
from discord import app_commands

class Ajuda(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
    
    @commands.command()
    async def help(self, ctx:commands.Context):
        my_embed = discord.Embed(title='Hello! I am DigiHelper', description='This is my commands:')
        
        thumb_embed = discord.File('images/thumb.png', 'thumb.png')
        
        my_embed.set_thumbnail(url="attachment://thumb.png")
        
        my_embed.set_author(name='by LeoooX', url='https://www.youtube.com/@leo0x1409/videos', icon_url=None)
        
        my_embed.add_field(name='Clon Calculator', value='/cloncheck', inline=False)
        my_embed.add_field(name='Status Calculator', value='/status', inline=False)
        my_embed.add_field(name='Accessories Guide', value='/acc', inline=False)
        
        my_embed.color = discord.Color.blue()
        
        await ctx.reply(file=thumb_embed, embed=my_embed)
    
async def setup(bot):
    await bot.add_cog(Ajuda(bot))