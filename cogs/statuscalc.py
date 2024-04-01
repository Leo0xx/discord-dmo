import discord
from discord.ext import commands
from discord import app_commands

class Statuscalculo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @app_commands.command()
    async def status(self, ctx:commands.Context):
        my_embed = discord.Embed(title='**Status Calculator**', description='Use / with the name of the status you want to calculate according to the following list:')
        
        thumb_embed = discord.File('images/thumb.png', 'thumb.png')
        
        my_embed.set_thumbnail(url="attachment://thumb.png")
        
        my_embed.set_author(name='by LeoooX', url='https://www.youtube.com/@leo0x1409/videos', icon_url=None)
        
        my_embed.add_field(name='Max HP', value='/hp', inline=False)
        my_embed.add_field(name='Attack', value='/at', inline=False)
        my_embed.add_field(name='Critical Hit', value='/ct', inline=False)
        my_embed.add_field(name='Block', value='/bl', inline=False)
        my_embed.add_field(name='Avoid', value='/ev', inline=False)
        my_embed.add_field(name='Hit Rate', value='/ht', inline=False)
        my_embed.add_field(name='Max DS', value='/ds', inline=False)
        my_embed.add_field(name='Defense', value='/de', inline=False)
        
        my_embed.color = discord.Color.purple()
        
        await ctx.response.send_message(file=thumb_embed, embed=my_embed)

    async def deck(self, base_status, deck_buff):
        if deck_buff == 0:
            deckbuffs = base_status*1
            base_status = base_status
            return int(round(base_status))
        elif deck_buff == 1:
            deckbuffs = base_status*0.15
            base_status = base_status+deckbuffs
            return int(round(base_status))
        elif deck_buff == 2:
            deckbuffs = base_status*0.20
            base_status = base_status+deckbuffs
            return int(round(base_status))
        elif deck_buff == 3:
            deckbuffs = base_status*0.40
            base_status = base_status+deckbuffs
            return int(round(base_status))

    async def clon_level(self, clon_lvl):
        return int(round(clon_lvl))

    async def get_base_status(self, base_status):
        return float(base_status)

    async def get_clon_status_ct(self, clon_lvl, base_status):
        clon_value = {
        1: 0.15, 2: 0.30, 3: 0.45, 4: 0.70, 5: 0.95, 6: 1.20, 7: 1.70, 8: 2.20, 9: 2.70, 10: 3.45, 11: 4.20, 12: 4.95, 13: 5.70, 14: 6.45, 15: 7.20
    }
        if clon_lvl in clon_value:
            multi = clon_value[clon_lvl]
            clonStatus = base_status * multi
            return float(clonStatus)
        
    async def get_clon_status_hp(self, clon_lvl, base_status):
        clon_value = {
        1: 0.02, 2: 0.04, 3: 0.06, 4: 0.09, 5: 0.12, 6: 0.15, 7: 0.19, 8: 0.23, 9: 0.27, 10: 0.31, 11: 0.35, 12: 0.39, 13: 0.44, 14: 0.49, 15: 0.54
    }
        if clon_lvl in clon_value:
            multi = clon_value[clon_lvl]
            clonStatus = base_status * multi
            return int(round(clonStatus))
        
    async def get_clon_status_at(self, clon_lvl, base_status):
        clon_value = {
        1: 0.03, 2: 0.06, 3: 0.09, 4: 0.14, 5: 0.19, 6: 0.24, 7: 0.34, 8: 0.44, 9: 0.54, 10: 0.69, 11: 0.84, 12: 0.99, 13: 1.14, 14: 1.29, 15: 1.44
    }
        if clon_lvl in clon_value:
            multi = clon_value[clon_lvl]
            clonStatus = base_status * multi
            return int(round(clonStatus))
        
    async def get_clon_status_bl(self, clon_lvl, base_status):
        clon_value = {
        1: 0.02, 2: 0.04, 3: 0.06, 4: 0.09, 5: 0.12, 6: 0.15, 7: 0.21, 8: 0.27, 9: 0.33, 10: 0.42, 11: 0.51, 12: 0.60, 13: 0.69, 14: 0.78, 15: 0.87
    }
        if clon_lvl in clon_value:
            multi = clon_value[clon_lvl] * 100
            clonStatus = base_status + multi
            return int(round(clonStatus))
        
    async def get_clon_status_ev(self, clon_lvl, base_status):
        clon_value = {
        1: 0.12, 2: 0.24, 3: 0.36, 4: 0.56, 5: 0.76, 6: 0.96, 7: 1.36, 8: 1.76, 9: 2.16, 10: 2.76, 11: 3.36, 12: 3.96, 13: 4.56, 14: 5.16, 15: 5.76
    }
        if clon_lvl in clon_value:
            multi = clon_value[clon_lvl]
            clonStatus = base_status * multi
            return float(clonStatus)

    async def buff(self, base_status, buffs):
        if buffs == 1:
            buff = base_status * 1
            return int(round(buff))
        else:
            return 0
    
    async def buff_ht(self, buffs):
        if buffs == 1:
            buff = 500
            return int(round(buff))
        else:
            return 0
    
    async def buff_ev(self, buffs):
        if buffs == 1:
            buff = 5.0
            return float(round(buff))
        else:
            return 0

    async def seal(self, seals):
        return float(seals)

    async def equips(self, acessories):
        return float(acessories)

    async def tamerCloth(self, tamer_status):
        return int(round(tamer_status))

    async def kari(self, hikari, base_status):
        hikariBuff = 0.30
        if hikari >= 1 and hikari <= 2:
            hikariBuff = hikari*hikariBuff
            hikariBuff = base_status*hikariBuff
            return int(round(hikariBuff))
        elif hikari == 0:
            return 0
        else:
            return "Invalid insert."

    async def treelife(self, tol, base_status): 
        tolHighest = 0.65
        tolHigh = 0.60
        if tol == 0:
            return 0
        if tol == 2:
            tolHighest = base_status*tolHighest
            return int(round(tolHighest))
        elif tol == 1:
            tolHigh = base_status*tolHigh
            return int(round(tolHigh))
        else:
            return "Invalid insert."

    async def blessing(self, bless, base_status):
        if bless == 1:
            blessBuff = base_status*0.20
            return int(round(blessBuff))
        else:
            return 0
        
    async def blessing_at(self, bless, base_status):
        if bless == 1:
            blessBuff = base_status*0.10
            return int(round(blessBuff))
        else:
            return 0

    async def tamer_passive_at(self, passive, base_status):
        if passive == 1:
            passiva = base_status*0.05
            return int(round(passiva))
        else:
            return 0
        
    async def tamer_passive_hp(self, passive, base_status):
        if passive == 1:
            passiva = base_status*0.10
            return int(round(passiva))
        else:
            return 0

    async def chips(self, chipsets):
        return float(chipsets)   
    
    @app_commands.command(description='Calculate your Health Points')
    @app_commands.describe(base_status="Put here your basestatus", 
                           clon_lvl="1-15", 
                           deck_buff="No Deck (0) OX Deck (1) RKX (2) X7SM (3)", 
                           buffs="No buffs (0) Full Buff (1)", 
                           seals="Your seal status", 
                           acessories="Your total acessories given status", 
                           tamer_status="Status given from applied status", 
                           hikari="No Hikari (0) 1x Hikari (1) 2x Hikari (2)", 
                           tol="No ToL (0), ToL High (1), ToL Highest (2)", 
                           bless="No Bless (0) Bless Buff (1)", 
                           passive="No tamer passive (0), Tame Passive (1) remember: check if your tamer gives AT or HP to this digimon!", 
                           chipsets="Your chipsets status")
    async def hp(self, interact:discord.Interaction, base_status:int, clon_lvl:int, deck_buff:int, buffs:int, seals:int, acessories:int, tamer_status:int, hikari:int, tol:int, bless:int, passive:int, chipsets:int):
        try:
            total_status = 0
            base_stats = await self.get_base_status(base_status)
            clon_lv = await self.clon_level(clon_lvl)
            deck_status = await self.deck(base_status, deck_buff)
            if deck_status:
                base_status = deck_status
            total_status += int(base_status)
            clon_status = await self.get_clon_status_hp(clon_lvl, base_status)
            total_status += int(clon_status)
            buff_status = await self.buff(base_status, buffs)
            total_status += int(buff_status)
            seal_status = await self.seal(seals)
            total_status += int(seal_status)
            equip_status = await self.equips(acessories)
            total_status += int(equip_status)
            tamer_stats = await self.tamerCloth(tamer_status)
            total_status += int(tamer_stats)
            kari_status = await self.kari(hikari, base_status)
            total_status += int(kari_status)
            tol_status =  await self.treelife(tol, base_status)
            total_status += int(tol_status)
            bless_status = await self.blessing(bless, base_status)
            total_status += int(bless_status)
            passive_status = await self.tamer_passive_hp(passive, base_status)
            total_status += int(passive_status)
            chip_status = await self.chips(chipsets)
            total_status += int(chip_status)
            
            my_embed = discord.Embed(title='**Max HP**', description='')
            
            thumb_embed = discord.File('images/thumb.png', 'thumb.png')
            
            my_embed.set_thumbnail(url="attachment://thumb.png")
            
            my_embed.set_author(name='by LeoooX', url='https://www.youtube.com/@leo0x1409/videos', icon_url=None)
            
            my_embed.add_field(name='<:basestatus:1223436962338439208> Base Status', value=f'{base_status}', inline=False)
            if deck_buff == 1:
                my_embed.add_field(name='<:deck:1223436963839873025> Deck', value='OX', inline=False)
            if deck_buff == 2:
                my_embed.add_field(name='<:deck:1223436963839873025> Deck', value='RKX', inline=False)
            if deck_buff == 3:
                my_embed.add_field(name='<:deck:1223436963839873025> Deck', value='X7SM', inline=False)
            my_embed.add_field(name='<:clon:1223437023906627625> Clon Status', value=f'{clon_status}', inline=False)
            my_embed.add_field(name='<:hpbuff:1223487082211709019> Buff Status', value=f'{buff_status}', inline=False)
            my_embed.add_field(name='<:seals:1223437026100121642> Seals', value=f'{seal_status}', inline=False)
            my_embed.add_field(name='<:equip:1223437024779042859> Acessories Status', value=f'{equip_status}', inline=False)
            my_embed.add_field(name='<:tamer:1223437027639431238> Tamer Status', value=f'{tamer_stats}', inline=False)
            if hikari >= 1 and hikari <= 2:
                my_embed.add_field(name='<:hikari:1223440595037716624> Hikari buffs', value=f'{kari_status}', inline=False)
            if tol >= 1 and tol <= 2:
                my_embed.add_field(name='<:treelife:1223440567283744879> Tree Of Life', value=f'{tol_status}', inline=False)
            if bless == 1:
                my_embed.add_field(name='<:bless:1223441173604204686> Bless', value=f'{bless_status}', inline=False)
            if passive == 1:
                my_embed.add_field(name='<:passive:1223440565400633395> Passive buffs', value=f'{passive_status}', inline=False)
            my_embed.add_field(name='<:chips:1223437022258008206> Chipsets', value=f'{chip_status}', inline=False)
            my_embed.add_field(name='<:total:1223437029094854706> Total Status', value=f'{total_status}', inline=False)
            
            my_embed.color = discord.Color.purple()
            
            await interact.response.send_message(file=thumb_embed, embed=my_embed, ephemeral=True)           
        except Exception as e:
            await interact.response.send_message("Invalid insert.", ephemeral=True)
            
    @app_commands.command(description='Calculate your Attack')
    @app_commands.describe(base_status="Put here your basestatus",
                       clon_lvl="1-15",
                       buffs="No buffs (0) Full Buff (1)", 
                       seals="Your seal status", 
                       acessories="Your total acessories given status", 
                       tamer_status="Status given from applied status", 
                       bless="No Bless (0) Bless Buff (1)",
                       passive="No Passive (0) Passive Buff (1)",
                       chipsets="Your chipsets status")
    async def at(self, interact:discord.Interaction, base_status:int, clon_lvl:int, buffs:int, seals:int, acessories:int, tamer_status:int, bless:int, passive:int, chipsets:int):
        try:
            total_status = 0
            base_stats = await self.get_base_status(base_status)
            clon_lv = await self.clon_level(clon_lvl)
            total_status += int(base_status)
            clon_status = await self.get_clon_status_at(clon_lvl, base_status)
            total_status += int(clon_status)
            buff_status = await self.buff(base_status, buffs)
            total_status += int(buff_status)
            seal_status = await self.seal(seals)
            total_status += int(seal_status)
            equip_status = await self.equips(acessories)
            total_status += int(equip_status)
            tamer_stats = await self.tamerCloth(tamer_status)
            total_status += int(tamer_stats)
            bless_status = await self.blessing_at(bless, base_status)
            total_status += int(bless_status)
            passive_status = await self.tamer_passive_at(passive, base_status)
            total_status += int(passive_status)
            chip_status = await self.chips(chipsets)
            total_status += int(chip_status)

            my_embed = discord.Embed(title='**Attack**', description='')
            
            thumb_embed = discord.File('images/thumb.png', 'thumb.png')
            
            my_embed.set_thumbnail(url="attachment://thumb.png")
            
            my_embed.set_author(name='by LeoooX', url='https://www.youtube.com/@leo0x1409/videos', icon_url=None)
            
            my_embed.add_field(name='<:basestatus:1223436962338439208> Base Status', value=f'{base_status}', inline=False)
            my_embed.add_field(name='<:clon:1223437023906627625> Clon Status', value=f'{clon_status}', inline=False)
            my_embed.add_field(name='<:atbuff:1223487076599857172> Buff Status', value=f'{buff_status}', inline=False)
            my_embed.add_field(name='<:seals:1223437026100121642> Seals', value=f'{seal_status}', inline=False)
            my_embed.add_field(name='<:equip:1223437024779042859> Acessories Status', value=f'{equip_status}', inline=False)
            my_embed.add_field(name='<:tamer:1223437027639431238> Tamer Status', value=f'{tamer_stats}', inline=False)
            if bless == 1:
                my_embed.add_field(name='<:bless:1223441173604204686> Bless', value=f'{bless_status}', inline=False)
            if passive == 1:
                my_embed.add_field(name='<:passive:1223440565400633395> Passive buffs', value=f'{passive_status}', inline=False)
            my_embed.add_field(name='<:chips:1223437022258008206> Chipsets', value=f'{chip_status}', inline=False)
            my_embed.add_field(name='<:total:1223437029094854706> Total Status', value=f'{total_status}', inline=False)
            
            my_embed.color = discord.Color.purple()
            
            await interact.response.send_message(file=thumb_embed, embed=my_embed, ephemeral=True)                 
        except Exception as e:
            await interact.response.send_message(f"Invalid insert", ephemeral=True)

    @app_commands.command(description='Calculate your Critical Rate')
    @app_commands.describe(base_status="Put here your basestatus",
                       clon_lvl="1-15", 
                       seals="Your seal status", 
                       acessories="Your total acessories given status",  
                       chipsets="Your chipsets status")
    async def ct(self, interact:discord.Interaction, base_status:float, clon_lvl:int, seals:float, acessories:float, chipsets:float):
        try:
            total_status = 0
            base_stats = await self.get_base_status(base_status)
            clon_lv = await self.clon_level(clon_lvl)
            total_status += float(base_status)
            clon_status = await self.get_clon_status_ct(clon_lvl, base_status)
            total_status += float(clon_status)
            seal_status = await self.seal(seals)
            total_status += float(seal_status)
            equip_status = await self.equips(acessories)
            total_status += float(equip_status)
            chip_status = await self.chips(chipsets)
            total_status += float(chip_status)

            my_embed = discord.Embed(title='**Critical Rate**', description='')
            
            thumb_embed = discord.File('images/thumb.png', 'thumb.png')
            
            my_embed.set_thumbnail(url="attachment://thumb.png")
            
            my_embed.set_author(name='by LeoooX', url='https://www.youtube.com/@leo0x1409/videos', icon_url=None)
            
            my_embed.add_field(name='<:basestatus:1223436962338439208> Base Status', value=f'{base_status:.2f}%', inline=False)
            my_embed.add_field(name='<:clon:1223437023906627625> Clon Status', value=f'{clon_status:.2f}%', inline=False)
            my_embed.add_field(name='<:seals:1223437026100121642> Seals', value=f'{seal_status}%', inline=False)
            my_embed.add_field(name='<:equip:1223437024779042859> Acessories Status', value=f'{equip_status}%', inline=False)
            my_embed.add_field(name='<:chips:1223437022258008206> Chipsets', value=f'{chip_status}%', inline=False)
            my_embed.add_field(name='<:total:1223437029094854706> Total Status', value=f'{total_status:.2f}%', inline=False)
            
            my_embed.color = discord.Color.purple()
            
            await interact.response.send_message(file=thumb_embed, embed=my_embed, ephemeral=True)           
        except Exception as e:
            await interact.response.send_message(f"Invalid insert", ephemeral=True)
            
    @app_commands.command(description='Calculate your Evasion')
    @app_commands.describe(base_status="Put here your basestatus",
                       clon_lvl="1-15",
                       buffs="No buffs (0) Full Buff (1)", 
                       seals="Your seal status", 
                       acessories="Your total acessories given status", 
                       chipsets="Your chipsets status")
    async def ev(self, interact:discord.Interaction, base_status:float, clon_lvl:int, buffs:int, seals:float, acessories:float, chipsets:float):
        try:
            total_status = 0
            base_stats = await self.get_base_status(base_status)
            clon_lv = await self.clon_level(clon_lvl)
            total_status += float(base_status)
            clon_status = await self.get_clon_status_ev(clon_lvl, base_status)
            total_status += float(clon_status)
            buff_status = await self.buff_ev(buffs)
            total_status += float(buff_status)
            seal_status = await self.seal(seals)
            total_status += float(seal_status)
            equip_status = await self.equips(acessories)
            total_status += float(equip_status)
            chip_status = await self.chips(chipsets)
            total_status += float(chip_status)

            my_embed = discord.Embed(title='**Evasion**', description='')
            
            thumb_embed = discord.File('images/thumb.png', 'thumb.png')
            
            my_embed.set_thumbnail(url="attachment://thumb.png")
            
            my_embed.set_author(name='by LeoooX', url='https://www.youtube.com/@leo0x1409/videos', icon_url=None)
            
            my_embed.add_field(name='<:basestatus:1223436962338439208> Base Status', value=f'{base_status:2f}%', inline=False)
            my_embed.add_field(name='<:clon:1223437023906627625> Clon Status', value=f'{clon_status:.2f}%', inline=False)
            my_embed.add_field(name='<:evbuff:1223487079850311823> Buff Status', value=f'{buff_status}%', inline=False)
            my_embed.add_field(name='<:seals:1223437026100121642> Seals', value=f'{seal_status}%', inline=False)
            my_embed.add_field(name='<:equip:1223437024779042859> Acessories Status', value=f'{equip_status}%', inline=False)
            my_embed.add_field(name='<:chips:1223437022258008206> Chipsets', value=f'{chip_status}%', inline=False)
            my_embed.add_field(name='<:total:1223437029094854706> Total Status', value=f'{total_status:.2f}%', inline=False)
            
            my_embed.color = discord.Color.purple()
            
            await interact.response.send_message(file=thumb_embed, embed=my_embed, ephemeral=True)        
        except Exception as e:
            await interact.response.send_message(f"{e}", ephemeral=True)

    @app_commands.command(description='Calculate your Block')
    @app_commands.describe(base_status="Put here your basestatus",
                       clon_lvl="1-15",
                       seals="Your seal status", 
                       acessories="Your total acessories given status", 
                       chipsets="Your chipsets status")
    async def bl(self, interact:discord.Interaction, base_status:int, clon_lvl:int, seals:int, acessories:int, chipsets:int):
        try:
            total_status = 0
            base_stats = await self.get_base_status(base_status)
            clon_lv = await self.clon_level(clon_lvl)
            clon_status = await self.get_clon_status_bl(clon_lvl, base_status)
            total_status += int(clon_status)
            seal_status = await self.seal(seals)
            total_status += int(seal_status)
            equip_status = await self.equips(acessories)
            total_status += int(equip_status)
            chip_status = await self.chips(chipsets)
            total_status += int(chip_status)

            my_embed = discord.Embed(title='**Block**', description='')
            
            thumb_embed = discord.File('images/thumb.png', 'thumb.png')
            
            my_embed.set_thumbnail(url="attachment://thumb.png")
            
            my_embed.set_author(name='by LeoooX', url='https://www.youtube.com/@leo0x1409/videos', icon_url=None)
            
            my_embed.add_field(name='<:basestatus:1223436962338439208> Base Status', value=f'{base_status}%', inline=False)
            my_embed.add_field(name='<:clon:1223437023906627625> Clon Status', value=f'{clon_status}%', inline=False)
            my_embed.add_field(name='<:seals:1223437026100121642> Seals', value=f'{seal_status}%', inline=False)
            my_embed.add_field(name='<:equip:1223437024779042859> Acessories Status', value=f'{equip_status}%', inline=False)
            my_embed.add_field(name='<:chips:1223437022258008206> Chipsets', value=f'{chip_status}%', inline=False)
            my_embed.add_field(name='<:total:1223437029094854706> Total Status', value=f'{total_status}%', inline=False)
            
            my_embed.color = discord.Color.purple()
            
            await interact.response.send_message(file=thumb_embed, embed=my_embed, ephemeral=True)         
        except Exception as e:
            await interact.response.send_message(f"Invalid insert", ephemeral=True)

    @app_commands.command(description='Calculate your Hit Rate')
    @app_commands.describe(base_status="Put here your basestatus",
                       buffs="No buffs (0) Full Buff (1)", 
                       seals="Your seal status", 
                       acessories="Your total acessories given status", 
                       tamer_status="Status given from applied status", 
                       chipsets="Your chipsets status")
    async def ht(self, interact:discord.Interaction, base_status:int, buffs:int, seals:int, acessories:int, tamer_status:int, chipsets:int):
        try:
            total_status = 0
            base_stats = await self.get_base_status(base_status)
            buff_status = await self.buff_ht(base_status, buffs)
            total_status += int(buff_status)
            seal_status = await self.seal(seals)
            total_status += int(seal_status)
            equip_status = await self.equips(acessories)
            total_status += int(equip_status)
            tamer_stats = await self.tamerCloth(tamer_status)
            total_status += int(tamer_stats)
            chip_status = await self.chips(chipsets)
            total_status += int(chip_status)

            my_embed = discord.Embed(title='**Hit Rate**', description='')
            
            thumb_embed = discord.File('images/thumb.png', 'thumb.png')
            
            my_embed.set_thumbnail(url="attachment://thumb.png")
            
            my_embed.set_author(name='by LeoooX', url='https://www.youtube.com/@leo0x1409/videos', icon_url=None)
            
            my_embed.add_field(name='<:basestatus:1223436962338439208> Base Status', value=f'{base_status}', inline=False)
            my_embed.add_field(name='<:htbuff:1223487083734237184> Buff Status', value=f'{buff_status}', inline=False)
            my_embed.add_field(name='<:seals:1223437026100121642> Seals', value=f'{seal_status}', inline=False)
            my_embed.add_field(name='<:equip:1223437024779042859> Acessories Status', value=f'{equip_status}', inline=False)
            my_embed.add_field(name='<:tamer:1223437027639431238> Tamer Status', value=f'{tamer_stats}', inline=False)
            my_embed.add_field(name='<:chips:1223437022258008206> Chipsets', value=f'{chip_status}', inline=False)
            my_embed.add_field(name='<:total:1223437029094854706> Total Status', value=f'{total_status}', inline=False)
            
            my_embed.color = discord.Color.purple()
            
            await interact.response.send_message(file=thumb_embed, embed=my_embed, ephemeral=True)         
        except Exception as e:
            await interact.response.send_message(f"Invalid insert", ephemeral=True)

    @app_commands.command(description='Calculate your Defense')
    @app_commands.describe(base_status="Put here your basestatus",
                       buffs="No buffs (0) Full Buff (1)", 
                       seals="Your seal status", 
                       acessories="Your total acessories given status", 
                       tamer_status="Status given from applied status", 
                       chipsets="Your chipsets status")
    async def de(self, interact:discord.Interaction, base_status:int, buffs:int, seals:int, acessories:int, tamer_status:int, chipsets:int):
        try:
            total_status = 0
            base_stats = await self.get_base_status(base_status)
            total_status += int(base_status)
            buff_status = await self.buff(base_status, buffs)
            total_status += int(buff_status)
            seal_status = await self.seal(seals)
            total_status += int(seal_status)
            equip_status = await self.equips(acessories)
            total_status += int(equip_status)
            tamer_stats = await self.tamerCloth(tamer_status)
            total_status += int(tamer_stats)
            chip_status = await self.chips(chipsets)
            total_status += int(chip_status)

            my_embed = discord.Embed(title='**Defense**', description='')
            
            thumb_embed = discord.File('images/thumb.png', 'thumb.png')
            
            my_embed.set_thumbnail(url="attachment://thumb.png")
            
            my_embed.set_author(name='by LeoooX', url='https://www.youtube.com/@leo0x1409/videos', icon_url=None)
            
            my_embed.add_field(name='<:basestatus:1223436962338439208> Base Status', value=f'{base_status}', inline=False)
            my_embed.add_field(name='<:debuff:1223487078059475025> Buff Status', value=f'{buff_status}', inline=False)
            my_embed.add_field(name='<:seals:1223437026100121642> Seals', value=f'{seal_status}', inline=False)
            my_embed.add_field(name='<:equip:1223437024779042859> Acessories Status', value=f'{equip_status}', inline=False)
            my_embed.add_field(name='<:tamer:1223437027639431238> Tamer Status', value=f'{tamer_stats}', inline=False)
            my_embed.add_field(name='<:chips:1223437022258008206> Chipsets', value=f'{chip_status}', inline=False)
            my_embed.add_field(name='<:total:1223437029094854706> Total Status', value=f'{total_status}', inline=False)
            
            my_embed.color = discord.Color.purple()
            
            await interact.response.send_message(file=thumb_embed, embed=my_embed, ephemeral=True)        
        except Exception as e:
            await interact.response.send_message(f"Invalid insert", ephemeral=True)
            
    @app_commands.command(description='Calculate your DS')
    @app_commands.describe(base_status="Put here your basestatus",
                       buffs="No buffs (0) Full Buff (1)", 
                       seals="Your seal status", 
                       acessories="Your total acessories given status", 
                       tamer_status="Status given from applied status", 
                       chipsets="Your chipsets status")
    async def ds(self, interact:discord.Interaction, base_status:int, buffs:int, seals:int, acessories:int, tamer_status:int, bless:int, chipsets:int):
        try:
            total_status = 0
            base_stats = await self.get_base_status(base_status)
            total_status += int(base_status)
            buff_status = await self.buff(base_status, buffs)
            total_status += int(buff_status)
            seal_status = await self.seal(seals)
            total_status += int(seal_status)
            equip_status = await self.equips(acessories)
            total_status += int(equip_status)
            tamer_stats = await self.tamerCloth(tamer_status)
            total_status += int(tamer_stats)
            bless_status = await self.blessing(bless, base_status)
            total_status += int(bless_status)
            chip_status = await self.chips(chipsets)
            total_status += int(chip_status)

            my_embed = discord.Embed(title='**Max DS**', description='')
            
            thumb_embed = discord.File('images/thumb.png', 'thumb.png')
            
            my_embed.set_thumbnail(url="attachment://thumb.png")
            
            my_embed.set_author(name='by LeoooX', url='https://www.youtube.com/@leo0x1409/videos', icon_url=None)
            
            my_embed.add_field(name='<:basestatus:1223436962338439208> Base Status', value=f'{base_status}', inline=False)
            my_embed.add_field(name='<:dsbuff:1223440563915718787> Buff Status', value=f'{buff_status}', inline=False)
            my_embed.add_field(name='<:seals:1223437026100121642> Seals', value=f'{seal_status}', inline=False)
            my_embed.add_field(name='<:equip:1223437024779042859> Acessories Status', value=f'{equip_status}', inline=False)
            my_embed.add_field(name='<:tamer:1223437027639431238> Tamer Status', value=f'{tamer_stats}', inline=False)
            if bless == 1:
                my_embed.add_field(name='<:bless:1223441173604204686> Bless', value=f'{bless_status}', inline=False)
            my_embed.add_field(name='<:chips:1223437022258008206> Chipsets', value=f'{chip_status}', inline=False)
            my_embed.add_field(name='<:total:1223437029094854706> Total Status', value=f'{total_status}', inline=False)
            
            my_embed.color = discord.Color.purple()
            
            await interact.response.send_message(file=thumb_embed, embed=my_embed, ephemeral=True)               
        except Exception as e:
            await interact.response.send_message(f"Invalid insert", ephemeral=True)
            
async def setup(bot):
    await bot.add_cog(Statuscalculo(bot))