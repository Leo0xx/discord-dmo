import discord
from discord.ext import commands
from discord import app_commands

class Equip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
    
    @app_commands.command()
    async def acc(self, ctx:commands.Context):
        my_embed = discord.Embed(title='**Accessories Guide**', description='Use the following commands to check it: ')
        
        thumb_embed = discord.File('images/thumb.png', 'thumb.png')
        
        my_embed.set_thumbnail(url="attachment://thumb.png")
        
        my_embed.set_author(name='by LeoooX', url='https://www.youtube.com/@leo0x1409/videos', icon_url=None)
        
        my_embed.add_field(name='Ring', value='/ring', inline=False)
        my_embed.add_field(name='Necklace', value='/neck', inline=False)
        my_embed.add_field(name='Earring', value='/earring', inline=False)
        my_embed.add_field(name='Bracelet', value='/bracelet', inline=False)
        
        my_embed.color = discord.Color.red()
        
        await ctx.response.send_message(file=thumb_embed, embed=my_embed)
        
    @app_commands.command()
    async def ring(self, ctx:commands.Context):
        my_embed = discord.Embed(title='**Ring Guide**', description='XX means a random status')
        
        my_embed.set_thumbnail(url="https://dmowiki.com/images/8/88/Aural_Ring_of_Sealed_Baihumon.png")
        
        my_embed.set_author(name='by LeoooX', url='https://www.youtube.com/@leo0x1409/videos', icon_url=None)
        
        my_embed.add_field(name='Damage Ring', value='AT / AT / BA / BA', inline=False)
        my_embed.add_field(name='Zero Unit Damage Ring', value='AT / AT / BA / BA / CT', inline=False)
        my_embed.add_field(name='Zero Unit New Dungeons Ring', value='AT / AT / CT / CT / BA', inline=False)
        my_embed.add_field(name='New Dungeons Ring', value='AT / AT / CT / CT', inline=False)
        my_embed.add_field(name='Support Ring', value='HP / HP / HP / XX', inline=False)
        
        my_embed.color = discord.Color.red()
        
        await ctx.response.send_message(embed=my_embed)
        
    @app_commands.command()
    async def neck(self, ctx:commands.Context):
        my_embed = discord.Embed(title='**Neck Guide**', description='XX means a random status')
        
        my_embed.set_thumbnail(url="https://dmowiki.com/images/c/c4/Baihumon_Shiny_Necklace.png")
        
        my_embed.set_author(name='by LeoooX', url='https://www.youtube.com/@leo0x1409/videos', icon_url=None)
        
        my_embed.add_field(name='Damage Neck', value='AS / CD / BA / BA', inline=False)
        my_embed.add_field(name='Zero Unit Damage Neck', value='AS / CD / BA / BA / AT', inline=False)
        my_embed.add_field(name='Zero Unit New Dungeons Neck', value='AS / CD / CT / CT / AT', inline=False)
        my_embed.add_field(name='New Dungeons Neck', value='AS / CD / CT / CT', inline=False)
        my_embed.add_field(name='Damage Neck (2nd option)', value='AS / CD / BA / AT', inline=False)
        my_embed.add_field(name='Support Neck', value='HP / HP / HP / XX', inline=False)
        
        my_embed.color = discord.Color.red()
        
        await ctx.response.send_message(embed=my_embed)
        
    @app_commands.command()
    async def earring(self, ctx:commands.Context):
        my_embed = discord.Embed(title='**Earring Guide**', description='XX means a random status (Consider only jump, colosseum, red-quadcore, miracle lv 10 earrings can get twice HT)')
        
        my_embed.set_thumbnail(url="https://dmowiki.com/images/e/ee/Baihumon_Shiny_Earring.png")
        
        my_embed.set_author(name='by LeoooX', url='https://www.youtube.com/@leo0x1409/videos', icon_url=None)
        
        my_embed.add_field(name='Damage Earring', value='CD / CD / BA / BA', inline=False)
        my_embed.add_field(name='Hit Rate Earring', value='CD / CD / HT / HT', inline=False)
        my_embed.add_field(name='Support Earring', value='HP / HP / XX / XX', inline=False)
        
        my_embed.color = discord.Color.red()
        
        await ctx.response.send_message(embed=my_embed)
        
    @app_commands.command()
    async def bracelet(self, ctx:commands.Context):
        my_embed = discord.Embed(title='**Bracelet Guide**', description='XX means a random status')
        
        my_embed.set_thumbnail(url="https://dmowiki.com/images/a/ad/Royal_-_X-Knight%27s_Bracelet.png")
        
        my_embed.set_author(name='by LeoooX', url='https://www.youtube.com/@leo0x1409/videos', icon_url=None)
        
        my_embed.add_field(name='Damage Bracelet', value='CD / CD / HT / HT / AT', inline=False)
        my_embed.add_field(name='Damage Bracelet (2nd option)', value='CD / CD / HT / HT / CT', inline=False)
        my_embed.add_field(name='New Dungeons Bracelet', value='CD / HT / HT / CT / CT', inline=False)
        my_embed.add_field(name='Support Bracelet', value='HP / HP / XX / XX / XX', inline=False)
        
        my_embed.color = discord.Color.red()
        
        await ctx.response.send_message(embed=my_embed)
    
async def setup(bot):
    await bot.add_cog(Equip(bot))