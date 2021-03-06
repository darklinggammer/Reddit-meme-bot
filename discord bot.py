import discord
from discord.ext import commands
import os
import praw
import random
client = commands.Bot(command_prefix = '!')

reddit = praw.Reddit(client_id = ('Client_id'),
                    client_secret = ('secret'),
                    username = ('username'),
                    password = ('password'),
                    user_agent = ('Agent'),
                    )



@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))



@client.command()
async def meme(ctx):
  Subreddit = reddit.subreddit('dankmemes')
  all_subs = []
  top = Subreddit.hot(limit = 100)
  for submission in top:
    all_subs.append(submission)
  random_sub = random.choice(all_subs)

  name = random_sub.title

  url = random_sub.url

  em = discord.Embed(title = name)

  em.set_image(url = url)

  await ctx.send(embed= em)


client.run('Token')
