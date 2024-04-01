import discord
from discord.ext import commands
from discord import app_commands

class Calculos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
    
    clon_value = {
        'AT': {1: 0.03, 2: 0.06, 3: 0.09, 4: 0.14, 5: 0.19, 6: 0.24, 7: 0.34, 8: 0.44, 9: 0.54, 10: 0.69, 11: 0.84, 12: 0.99, 13: 1.14, 14: 1.29, 15: 1.44},
        'CT': {1: 0.15, 2: 0.30, 3: 0.45, 4: 0.70, 5: 0.95, 6: 1.20, 7: 1.70, 8: 2.20, 9: 2.70, 10: 3.45, 11: 4.20, 12: 4.95, 13: 5.70, 14: 6.45, 15: 7.20},
        'BL': {1: 0.02, 2: 0.04, 3: 0.06, 4: 0.09, 5: 0.12, 6: 0.15, 7: 0.21, 8: 0.27, 9: 0.33, 10: 0.42, 11: 0.51, 12: 0.60, 13: 0.69, 14: 0.78, 15: 0.87},
        'EV': {1: 0.12, 2: 0.24, 3: 0.36, 4: 0.56, 5: 0.76, 6: 0.96, 7: 1.36, 8: 1.76, 9: 2.16, 10: 2.76, 11: 3.36, 12: 3.96, 13: 4.56, 14: 5.16, 15: 5.76},
        'HP': {1: 0.02, 2: 0.04, 3: 0.06, 4: 0.09, 5: 0.12, 6: 0.15, 7: 0.19, 8: 0.23, 9: 0.27, 10: 0.31, 11: 0.35, 12: 0.39, 13: 0.44, 14: 0.49, 15: 0.54}
    }

    async def calculate(self, status, clonlevel, basestatus, clonstatus):
        if status in self.clon_value and clonlevel in self.clon_value[status]:
            multi = self.clon_value[status][clonlevel]
            res = clonstatus / basestatus
            if res >= (multi - 0.01) or res == multi:
                return f"Your {status} is perfect."
            else:
                perfect = float(basestatus * multi)
                imperfect = float(basestatus * res)
                missing = perfect - imperfect
                return f"Your clon is not perfect!\nYou are missing **{missing:.2f} {status}**."                      
        else:
            return ValueError("Invalid status. Please enter a valid number/type.")

    @app_commands.command(description='Check your clon status')
    @app_commands.describe(basestatus="Put here your basestatus", clonstatus="Put here your clon status")
    @app_commands.describe(status="AT, CT, BL, EV, or HP", clonlevel="1-15")
    async def checkclon(self, interact:discord.Interaction, status:str, clonstatus:float, clonlevel:int, basestatus:float):
        try:
            res = await self.calculate(status, clonlevel, basestatus, clonstatus)
            await interact.response.send_message(res, ephemeral=True)
        except ValueError as e:
            await interact.response.send_message(e, ephemeral=True)
           
async def setup(bot):
    await bot.add_cog(Calculos(bot))