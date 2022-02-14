# Sends a message with the maximum level of each main base building for the given TH level

from Data.Constants.clash_of_clans import MainBuildings
from Data.components import Components
from Data.Constants.useful import Useful
from Script.import_functions import create_embed


async def buildings_th_embed(ctx, lvl):
    level_th = MainBuildings[lvl]
    text_th = ""
    for category, buildings in level_th.items():
        text_th += f"\n__{category} :__\n"
        for building_name, building_max_level in buildings.items():
            text_th += f"{building_name} level max : {building_max_level}\n"
    embed = create_embed(f"__**TH {lvl} :\n**__", text_th, ctx.guild.me.color, f"buildings_th|{ctx.author.id}", ctx.guild.me.avatar_url)
    return embed


async def buildings_th(ctx, lvl):
    if lvl > Useful["max_th_lvl"] or lvl < 0:
        await ctx.send(f"Town Hall not found\nPlease give a valid TH level : there is no level `{lvl}` TH.", hidden=True)
        return

    elif lvl == 0:
        embed = create_embed("What is your TH level ?", "", ctx.guild.me.color, f"buildings_th|{ctx.author.id}", ctx.guild.me.avatar_url)
        await ctx.send(embed=embed, components=Components["buildings_th"])

    elif 0 < lvl <= Useful["max_th_lvl"]:
        embed = await buildings_th_embed(ctx, lvl)
        await ctx.send(embed=embed, components=Components["buildings_th"])
    return
