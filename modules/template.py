def update_clients(discord_client, praw_client):
  global discord, reddit
  discord, reddit = discord_client, praw_client

# Your code here...

# e.g.
#     async def on_message(message):
#       if message.content == "foo":
#         await discord.send_message(message.channel, "bar".format(message))
