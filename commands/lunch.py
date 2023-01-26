import os
from discord.ext import commands
from discord.commands import slash_command
import string
import pandas as pd
from random import randint
# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class Lunch(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    # Override the handle() method
    # It will be called every time the command is received
    @slash_command(name='lunch', description="Chooses a place to eat lunch", guild_ids=[1065813802425262141])
    async def lunch(self, ctx):

        sheet_id = "1eQA366OF97O_rdDun4ukkvfnhioYFP-LuI4njNgzR6g"    
        sheet_name = "Sheet1"
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

        df = pd.read_csv(url)
        # df = pd.read_table("/app/data/Restaurants.tsv")
         

        lower_bound = 1
        upper_bound = df.shape[0]
        
        num = randint(lower_bound, upper_bound)

        selected = df.iloc[[num]][['Restaurant']]

        final = selected.iloc[0]['Restaurant']

        text = "You should have lunch at *" + str(final) + "* :fork_knife_plate:"
        await ctx.respond(text)
def setup(bot):
    bot.add_cog(Lunch(bot))