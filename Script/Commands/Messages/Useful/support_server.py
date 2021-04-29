import discord
from Script.import_functions import create_embed_img


async def support_server(ctx):
    url = "attachment://support_server.png"
    file = discord.File("Pictures/Support_Server.png", filename="support_server.png")
    embed = create_embed_img("Our support server :", "Join our support server if you have questions or suggestions. https://discord.gg/KQmstPw", ctx.guild.me.color, "", ctx.guild.me.avatar_url, url)
    await ctx.send(embed=embed, file=file)
    return
