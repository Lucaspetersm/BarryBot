'''
  Barry Bot 3.0dev1.1

  A pretty nutty Discord bot.

  Originally authored by Yalnix.
  Major contributions by GarethPW.

  Licensed under Mozilla Public License Version 2.0.
'''

import asyncio, platform, random, string, time
import discord, praw
import config, modules
from . import constants

ver = "3.0dev1.1"

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


class EventLink:

  def __init__(self, event):
    self.__name__, self.event = event, event

  @asyncio.coroutine # decorator differs slightly from builtin async
  def __call__(self, *args, **kwargs):
    yield from on_event(self.event, *args, **kwargs)

  _is_coroutine = __call__._is_coroutine # (reason for decorator)


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

  async for a in actions:
    await a

for event,f in modules.discord_events.items():
  if f: # if there are any event responses to call
    discord_client.event(EventLink(event))

discord_client.run(config.discord_key)
