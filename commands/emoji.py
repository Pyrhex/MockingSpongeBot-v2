import os
from discord.ext import commands
from discord.commands import slash_command
from random                 import randint
import string
# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class Emoji(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    # Override the handle() method
    # It will be called every time the command is received
    @slash_command(name='emoji', description="Converts letters into emojis", guild_ids=[1065813802425262141])
    async def emoji(self, ctx, text):
        # 'params' is a list that contains the parameters that the command 
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object

        # try:
        #     lower_bound = int(params[0])
        #     upper_bound = int(params[1])
        # except ValueError:
        #     await client.send_message(message.channel,
        #                               "Please, provide valid numbers")
        #     return

        # if lower_bound > upper_bound:
        #     await client.send_message(message.channel,
        #                 "The lower bound can't be higher than the upper bound")
        #     return

        # rolled = randint(lower_bound, upper_bound)
        # msg = get_emoji(":game_die:") + f" You rolled {rolled}!"
        text = text.upper()
        numbers = {
        "0": ":zero: ",
        "1": ":one: ",
        "2": ":two: ",
        "3": ":three: ",
        "4": ":four: ",
        "5": ":five: ",
        "6": ":six: ",
        "7": ":seven: ",
        "8": ":eight: ",
        "9": ":nine: "
        }

        for i in text:
            if i == "?":
                text = text.replace(i, ":question: ")
            elif i == "!":
                text = text.replace(i, ":exclamation: ")
            elif i == "#":
                text = text.replace(i, ":hash: ")
            elif i == "|":
                continue
            elif i in string.punctuation:
                text = text.replace(i, "")
            elif i in string.digits:
                text = text.replace(i, numbers[i])
            elif i in string.ascii_uppercase:
                emoji = ":regional_indicator_" + i.lower() + ": "
                text = text.replace(i, emoji)

        text = text.replace("|", "||").replace(":exclamation: :exclamation:", ":bangbang:").replace(":exclamation: :question:", ":interrobang:")
        await ctx.respond(text)
    
# class Shrek(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot
        
#     @slash_command(name='shrek', description="Turns Brian's light green", guild_ids=[913881236441821324])
#     async def shrek(self, ctx):
#         url = "https://maker.ifttt.com/trigger/shrek/json/with/key/daPGUbt90Z_TJKqQ_IaQPH"
#         requests.post(url)
#         await ctx.respond("SHEEEESH, you just shrekt Brian")

def setup(bot):
    bot.add_cog(Emoji(bot))