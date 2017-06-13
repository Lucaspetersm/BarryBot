'''
    Barry Bot 3.0dev0
    
    A pretty nutty Discord bot.
    
    Originally authored by Yalnix.
    Major contributions by GarethPW.
    Other contributors: unclepenguin.
    
    Licensed under Mozilla Public License Version 2.0.
'''

import platform, random, string, time
import discord, praw, youtube_dl
import config, constants, modules

ver = "3.0dev0"

user_agent = platform.system().lower() + ":pw.yalnix.barry:" + ver + " by /u/Yalnix"

discord_client = discord.Client()
praw_client = praw.Reddit(user_agent)

modules.update_clients(discord_client, praw_client)
modules.import_feature_modules()

async def on_event(wrapper_event, *args, **kwargs):
    case_match = {
        "on_message":         lambda: args[0].author,
        "on_reaction_add":    lambda: args[1],
        "on_reaction_remove": lambda: args[1],
    }.get(wrapper_event, None) == client.user
    
    if case_match:
        return
    
    actions = modules.call_event(wrapper_event, *args, **kwargs)
    
    for a in actions:
        await a() #probably won't work; let's find out

for k,v in modules.discord_events.keys():
    if v:
        client.add_listener(
            lambda *args, **kwargs: on_event(k, *args, **kwargs),
            k
        )

discord_client.run(config.discord_key)
praw_client.login(config.reddit_user, config.reddit_pass, disable_warning=True) #This really needs to be replaced with OAuth soon.
