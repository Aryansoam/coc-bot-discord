# Sends emoji info

import discord

from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def emoji_info(ctx, emoji):
    if emoji.count(":") == 2 and emoji.split(":")[1] in (e.name for e in list(ctx.guild.emojis)):
        emoji = discord.utils.get(ctx.guild.emojis, name=emoji.split(":")[1])
        embed = create_embed(emoji.name, f"{Emojis['Name']} Name : `{emoji.name}`\n{Emojis['Id']} ID : `{emoji.id}`\nAnimated : {emoji.animated}\nTry it : {emoji}", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        embed.set_thumbnail(url=emoji.url)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"Error\nPlease send the emoji with the emoji argument = `:emoji_name:` instead of `{emoji}`\n*Only emojis from this guild are available*", hidden=True)
    return
