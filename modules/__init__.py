import asyncio, importlib
import config
from barry import constants

modules = []

discord_events = dict.fromkeys(constants.EVENTS, tuple())

def update_clients(discord_client, praw_client):
  global discord, reddit
  discord, reddit = discord_client, praw_client
  
  for mod in modules:
    mod.update_clients(discord, reddit)

def import_feature_modules():
  for mod_name in config.module_names:
    print("Importing {0}... ".format(mod_name), end='')
    
    mod = importlib.import_module(".{}".format(mod_name), __name__)
    mod_callable = False
    
    for event in discord_events:
      if hasattr(mod, event):
        attr = getattr(mod, event)

        if asyncio.iscoroutinefunction(attr):
          discord_events[event] += (attr,)
          mod_callable = True
    
    mod_has_update_clients = (
      hasattr(mod, "update_clients") and
      callable(mod.update_clients)
    )

    if not mod_callable:
      print("\nEvent coroutine not found in {}".format(mod_name))
    elif not mod_has_update_clients:
      print("\nCallable update_clients not found in {}".format(mod_name))
    else:
      modules.append(mod)
      print("Done!")

def call_event(wrapper_event, *args, **kwargs):
  for mod_func in discord_events[wrapper_event]:
    yield mod_func(*args, **kwargs)

# Discord events:
#
# discord.on_ready()
# discord.on_resumed()
# discord.on_error(event, *args, **kwargs)
# discord.on_message(message)
# discord.on_socket_raw_receive(msg)
# discord.on_socket_raw_send(payload)
# discord.on_message_delete(message)
# discord.on_message_edit(before, after)
# discord.on_reaction_add(reaction, user)
# discord.on_reaction_remove(reaction, user)
# discord.on_reaction_clear(message, reactions)
# discord.on_channel_delete(channel)
# discord.on_channel_create(channel)
# discord.on_channel_update(before, after)
# discord.on_member_join(member)
# discord.on_member_remove(member)
# discord.on_member_update(before, after)
# discord.on_server_join(server)
# discord.on_server_remove(server)
# discord.on_server_update(before, after)
# discord.on_server_role_create(role)
# discord.on_server_role_delete(role)
# discord.on_server_role_update(before, after)
# discord.on_server_emojis_update(before, after)
# discord.on_server_available(server)
# discord.on_server_unavailable(server)
# discord.on_voice_state_update(before, after)
# discord.on_member_ban(member)
# discord.on_member_unban(server, user)
# discord.on_typing(channel, user, when)
# discord.on_group_join(channel, user)
# discord.on_group_remove(channel, user)
