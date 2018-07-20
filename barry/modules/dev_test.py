def update_clients(discord_client, praw_client):
  global discord, reddit
  discord, reddit = discord_client, praw_client

async def on_message(message):
    
  if (message.channel.name == "barrys-babes" and
      message.content.lower() == "ifunny is okay sometimes"):
    await discord.send_message(
      message.channel,
      "REEEEEEEEEEEEEEEEEEEEEEEEEEEEevaluate your life".format(message)
    )
