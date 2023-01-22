import json
import os.path
from discord.ext import commands
from discord.commands import slash_command

# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class Gro(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    # Override the handle() method
    # It will be called every time the command is received
    @slash_command(name='gro', description="Manages grocery lists", guild_ids=[1065813802425262141])
    async def gro(self, ctx, subcommand, listname="", item=""):

        savefile = "/Users/brian/Documents/MockingSpongeBot-v2/files/groceries.json"
        params = []
        params.append(subcommand)
        params.append(listname)
        params.append(item)
        print(params)
        if len(params) > 0: 
            subcommand = params[0].lower()
            if len(params) >= 2:
                # keep a dict of regex matches and proper name of lists?
                # use value to fetch key???
                # print(list(mydict.keys())[list(mydict.values()).index("ikea")]

                if subcommand == "new":
                    if os.path.exists(savefile) == True:
                        with open(savefile, "r") as f:
                            groceries = json.load(f)
                    sublist = params[1]
                    groceries[sublist] = []

                    jsonfile = json.dumps(groceries, indent = 4)
                    with open(savefile, "w") as f:
                        f.write(jsonfile)
                    await ctx.respond(f"Created new list: **{sublist}**")
                    return
                else:
                    sublist = params[1].title()
                    if sublist != sublist.upper() and sublist != "all":
                        sublist = sublist.capitalize()
                    if sublist == "Ikea":
                        sublist = "IKEA"
                    if sublist == "T&t" or sublist == "Tnt" or sublist == "TNT":
                        sublist = "T&T"
                    if sublist == "Ct" or sublist == "CT":
                        sublist = "Canadian Tire"
                    if sublist == "Ld" or sublist == "LD":
                        sublist = "London Drugs"
                            
            else:
                sublist = ""

            # will this be allowed for the bot if i specify 3 argument?
            # how do quotes work in discord bot input?
            # what is default type for params?
            if len(params) >= 3:
                if params[1].replace("“","").replace("”", "").startswith('"'): 
                    temp = " ".join(params)
                    item = " ".join([x.strip() for x in temp.replace("“","").replace("”", "").split('"')[2:]]).lower()
                else:
                    item = " ".join(params[2:]).lower()# .capitalize()
            else:
                item = ""
            if os.path.exists(savefile) == True:
                with open(savefile, "r") as f:
                    groceries = json.load(f)
            else:
                groceries = {}

 


 # will be called groceries
            if subcommand not in ["add", "remove", "clear", "list", "delete", "edit", "append"]:
                await ctx.respond(f"Unrecognized subcommand: *{subcommand}*")
                return
            else:
                # CHECKBOX = u'\u2751'

                # check if the listname exists
                if sublist not in ["all"] + list(groceries.keys()):
                    # create the list
                    if sublist == "" and subcommand != "list":
                        await ctx.respond(f"Missing list argument.")
                        return
                    if subcommand == "add":
                        groceries[sublist] = []
                if subcommand == "add":
                    if item != "":
                        bulk = item.replace(", ", ",").split(",")
                        for i in bulk:
                            groceries[sublist].append(i)
                        await ctx.respond(f"Added *{item}* to **{sublist}**.")

                        msg = [ f":shopping_cart: **{sublist}**" ]
                        items = []
                        for index, i in enumerate(groceries[sublist]):
                            idx = index+1
                            items.append(f"\t{idx : >2}. {i.capitalize()}")
                        msg.extend(items)
                        text = '\n'.join(msg)
                        await ctx.respond(":warning: This message will self-destruct in 5 seconds :warning:\n\n" + text, delete_after = 5) 

                        jsonfile = json.dumps(groceries, indent = 4)
                        with open(savefile, "w") as f:
                            f.write(jsonfile)
                    else:
                        await ctx.respond(f"Missing item to be added.")
                elif subcommand in ["edit", "append"]:
                    if sublist not in list(groceries.keys()):
                        if sublist == "":
                            await ctx.respond(f"Unrecognized list: **{sublist}**")
                        else:
                            await ctx.respond("Missing list argument.")
                    else:
                        if item != "":
                            string = item.split()
                            try:
                                # SPLIT BACK TO individual
                                index = int(string[0])
                                if index not in range(1, len(groceries[sublist])+1):
                                    await ctx.respond("Unrecognized index: *{index}*")
                                else:
                                    if subcommand == "edit":
                                        new_item = " ".join(string[1:])
                                        old_item = groceries[sublist][index-1] 
                                        groceries[sublist][index-1] = new_item
                                        await ctx.respond(f"Edited *{old_item}* to *{new_item}* in **{sublist}**.")


                                        msg = [ f":shopping_cart: **{sublist}**" ]
                                        items = []
                                        for index, i in enumerate(groceries[sublist]):
                                            idx = index+1
                                            items.append(f"\t{idx : >2}. {i.capitalize()}")
                                        msg.extend(items)
                                        text = '\n'.join(msg)
                                        await ctx.respond(":warning: This message will self-destruct in 5 seconds :warning:\n\n" + text, delete_after = 5) 

                                        jsonfile = json.dumps(groceries, indent = 4)
                                        with open(savefile, "w") as f:
                                            f.write(jsonfile)
                                    elif subcommand == "append":
                                        old_item = groceries[sublist][index-1] 
                                        new_item = " ".join(string[1:])
                                        groceries[sublist][index-1] = old_item + " " + new_item
                                        await ctx.respond(f"Appended *{new_item}* to *{old_item}* in **{sublist}**.")
                                        msg = [ f":shopping_cart: **{sublist}**" ]
                                        items = []
                                        for index, i in enumerate(groceries[sublist]):
                                            idx = index+1
                                            items.append(f"\t{idx : >2}. {i.capitalize()}")
                                        msg.extend(items)
                                        text = '\n'.join(msg)
                                        await ctx.respond(":warning: This message will self-destruct in 5 seconds :warning:\n\n" + text, delete_after = 5) 
                                        jsonfile = json.dumps(groceries, indent = 4)
                                        with open(savefile, "w") as f:
                                            f.write(jsonfile)
                            except ValueError as ve:
                                await ctx.respond(f"First item must be an index: {string[0]}")
                        else:
                            await ctx.respond(f"Missing item to {subcommand}.")
                elif subcommand == "remove":
                    # if the sublist is not in the grocery keys, check if that arg is a number after splitting by commas
                    if sublist not in list(groceries.keys()):
                        indices = sublist.replace(", ", ",").split(",")
                        try:
                            # if the first item can be converted into an int, means that it was intended as the indices number and the list is missing
                            x = int(indices[0])
                            await ctx.respond(f"Missing list argument.")
                        except ValueError as ve:
                            # if indices cannot be converted into int and is empty string, then the list arg is missing entirely
                            if indices[0] == "":
                                await ctx.respond(f"Missing list argument.")
                            # if indices is still a string, then it means the list given unrecognized
                            else:
                                await ctx.respond(f"Unrecognized list: **{sublist}**")
                    else:
                        # the list is valid, and the item is slot is not empty
                        if item != "":
                            # assume that multiple indices are given
                            indices = item.replace(", ", ",").split(",")
                            # create a copy of the grocery list to retain the indices
                            copy = groceries[sublist].copy()
                            removed = []
                            # for each indices
                            for i in indices:
                                try:
                                    # if indices is an int
                                    index = int(i)
                                    # then check if its in range of the available indices (+1 since python iz zero based) 
                                    if index not in range(1, len(copy)+1):
                                        await ctx.respond("Unrecognized index: *{index}*")
                                    else:
                                        item = copy[index-1] # get item from original list
                                        idx = groceries[sublist].index(item) # get new index from new list using original item
                                        temp = groceries[sublist].pop(idx) # use the new index to pop 
                                        removed.append(item)
                                        # await ctx.respond(f"Removed *{item}* from **{sublist}**.")
                                except ValueError as ve:
                                    # if the indices is actually an item itself
                                    if i not in groceries[sublist]:
                                        await ctx.respond(f"Unrecognized item: *{i}*")
                                    else:
                                        # remove using name
                                        groceries[sublist].remove(i)
                                        removed.append(i)
                                        # await ctx.respond(f"Removed *{item}* from **{sublist}**.")
                            text = ", ".join(removed)
                            await ctx.respond(f"Removed *{text}* from **{sublist}**.")
                            msg = [ f":shopping_cart: **{sublist}**" ]
                            items = []
                            for index, i in enumerate(groceries[sublist]):
                                idx = index+1
                                items.append(f"\t{idx : >2}. {i.capitalize()}")
                            msg.extend(items)
                            text = '\n'.join(msg)
                            await ctx.respond(":warning: This message will self-destruct in 5 seconds :warning:\n\n" + text, delete_after = 5) 
                            jsonfile = json.dumps(groceries, indent = 4)
                            with open(savefile, "w") as f:
                                f.write(jsonfile)
                        else:
                            await ctx.respond(f"Missing item to be removed.")
                elif subcommand == "delete":
                    if sublist == "all":
                        groceries = {}
                        await ctx.respond("Deleted all grocery lists.")
                        jsonfile = json.dumps(groceries, indent = 4)
                        with open(savefile, "w") as f:
                            f.write(jsonfile)
                    else:
                        if sublist not in list(groceries.keys()):
                            if sublist != "":
                                await ctx.respond(f"Unrecognized list: **{sublist}**")
                            else:
                                await ctx.respond(f"Missing list argument.")
                        else:
                            groceries.pop(sublist)
                            await ctx.respond(f"Deleted **{sublist}**.")
                            jsonfile = json.dumps(groceries, indent = 4)
                            with open(savefile, "w") as f:
                                f.write(jsonfile)
                elif subcommand == "clear":
                    if sublist == "all":
                        for i in list(groceries.keys()):
                            groceries[i] = []
                        jsonfile = json.dumps(groceries, indent = 4)
                        with open(savefile, "w") as f:
                            f.write(jsonfile)
                    elif sublist not in list(groceries.keys()):
                        if sublist != "":
                            await ctx.respond(f"Unrecognized list: **{sublist}**")
                        else:
                            await ctx.respond(f"Missing list argument.")
                    else:
                        groceries[sublist] = []
                        await ctx.respond(f"Cleared **{sublist}**.")
                        jsonfile = json.dumps(groceries, indent = 4)
                        with open(savefile, "w") as f:
                            f.write(jsonfile)
                elif subcommand == "list":
                    if sublist == "all" or sublist == "":
                        if len(groceries) > 0:
                            msg = []
                            for i in list(groceries.keys()):
                                items = []
                                if len(groceries[i]) > 0:
                                    for index, j in enumerate(groceries[i]):
                                        idx = index+1
                                        items.append(f"\t{idx : >2}. {j.capitalize()}")
                                    temp = [ f":shopping_cart: **{i}**" ] + items
                                    chunk = '\n'.join(temp)
                                    msg.append(chunk)
                                else:
                                    chunk = f":shopping_cart: **{i}**\n\t*No groceries.*"
                                    msg.append(chunk)
                            text = '\n\n'.join(msg)

                            # change this to edit the last 'list' command made
                            # shop_ch = client.get_channel(1032804856135688302)
                            # msg_id = 1062250044360765499
                            # pinned_msg = await shop_ch.fetch_message(msg_id)
                            # await pinned_msg.edit(content=text) # why does the edit not show up until the next time !gro list is enacted?
                            await ctx.respond(text)
                        else:
                            await ctx.respond("You have no grocery lists.")
                    elif sublist not in list(groceries.keys()):
                        if sublist != "":
                            await ctx.respond(f"Unrecognized list: **{sublist}**")
                        else:
                            await ctx.respond(f"Missing list argument.")
                    else:
                        msg = [ f":shopping_cart: **{sublist}**" ]
                        items = []
                        for index, i in enumerate(groceries[sublist]):
                            idx = index+1
                            items.append(f"\t{idx : >2}. {i.capitalize()}")
                        msg.extend(items)
                        text = '\n'.join(msg)
                        # shop_ch = client.get_channel(1032804856135688302)
                        # msg_id = 1062250044360765499
                        # pinned_msg = await shop_ch.fetch_message(msg_id)
                        # await pinned_msg.edit(content=text)
                        await ctx.respond(text) 
        else:
            if os.path.exists(savefile) == True:
                with open(savefile, "r") as f:
                    groceries = json.load(f)
                if len(groceries) > 0:
                    msg = []
                    for i in list(groceries.keys()):
                        items = []
                        if len(groceries[i]) > 0:
                            for index, j in enumerate(groceries[i]):
                                idx = index+1
                                items.append(f"\t{idx : >2}. {j.capitalize()}")
                            temp = [ f":shopping_cart: **{i}**" ] + items
                            chunk = '\n'.join(temp)
                            msg.append(chunk)
                        else:
                            chunk = f":shopping_cart: **{i}**\n\t*No groceries.*"
                            msg.append(chunk)
                    text = '\n\n'.join(msg)
                    await ctx.respond(text)
            else:
                await ctx.respond("You have no grocery lists.")


def setup(bot):
    bot.add_cog(Gro(bot))