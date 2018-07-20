'''
  Barry Bot 3.0dev0
  
  A pretty nutty Discord bot.
  
  Originally authored by Yalnix.
  Major contributions by GarethPW.
  
  Licensed under Mozilla Public License Version 2.0.
'''

import asyncio, platform, random, string, time
import discord, praw
from . import config, constants, modules

ver = "3.0dev0"

user_agent = (
  platform.system().lower() +
  ":pw.yalnix.barry:" +
  ver +
  " by /u/Yalnix"
)

discord_client = discord.Client()
praw_client = praw.Reddit(user_agent=user_agent,
                          client_id=config.reddit_client_id,
                          client_secret=config.reddit_client_secret,
                          username=config.reddit_user,
                          password=config.reddit_pass)

modules.import_feature_modules()
modules.update_clients(discord_client, praw_client)

async def on_event(wrapper_event, *args, **kwargs):
  case_match = {
    "on_message": (lambda: args[0].author, lambda: kwargs["message"].author),
    "on_reaction_add": (lambda: args[1], lambda: kwargs["user"]),
    "on_reaction_remove": (lambda: args[1], lambda: kwargs["user"]),
  }.get(wrapper_event, None)
  
  if case_match:
    for f in case_match: # check subject of event is not Barry
      try:
        assert f() == discord_client.user
      except (IndexError, KeyError): # incorrect arg type
        pass
      except AssertionError: # user is not Barry
        break
      else: # user is Barry
        return
  
  actions = modules.call_event(wrapper_event, *args, **kwargs)
  
  for a in actions:
    await a

for k,v in modules.discord_events.items():
  if v: # if there are any event responses to call
    discord_client.add_listener(
      asyncio.coroutine(
        lambda *args, **kwargs: on_event(k, *args, **kwargs)
      ), k
    )

discord_client.run(config.discord_key)
