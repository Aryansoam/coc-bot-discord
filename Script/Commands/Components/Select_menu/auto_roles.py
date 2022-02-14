# Add/remove the roles to the member
import discord

from Data.Constants.useful import Useful
from Script.import_emojis import Emojis


async def auto_roles__th(ctx):
    if "auto_roles th" in ctx.origin_message.embeds[0].footer.text:
        await ctx.defer(edit_origin=False, hidden=True)
        roles_list = []
        for th_level in range(1, Useful["max_th_lvl"] + 1):
            roles_list += [f"Town Hall {th_level}"]
        roles_to_remove = [role_name for role_name in roles_list if role_name.split(" ")[1] not in ctx.selected_options]
        removed_roles = []
        for role_name in roles_to_remove:
            if role_name in [r.name for r in ctx.author.roles]:
                removed_roles += [role_name]
                role = discord.utils.get(ctx.guild.roles, name=role_name)
                await ctx.author.remove_roles(role)
        roles_to_add = [f"Town Hall {th_level}" for th_level in ctx.selected_options]
        added_roles = []
        for role_name in roles_to_add:
            if role_name not in [r.name for r in ctx.author.roles]:
                added_roles += [role_name]
                role = discord.utils.get(ctx.guild.roles, name=role_name)
                await ctx.author.add_roles(role)
        removed_roles.sort(key=lambda x: int(x.split(" ")[2]))
        removed_roles_str = ', '.join(removed_roles)
        added_roles.sort(key=lambda x: int(x.split(" ")[2]))
        added_roles_str = ', '.join(added_roles)
        await ctx.send(f"Roles removed : {removed_roles_str}\nRoles added : {added_roles_str}")
    return


async def auto_roles__bh(ctx):
    if "auto_roles bh" in ctx.origin_message.embeds[0].footer.text:
        await ctx.defer(edit_origin=False, hidden=True)
        roles_list = []
        for bh_level in range(1, Useful["max_bh_lvl"] + 1):
            roles_list += [f"Builder Hall {bh_level}"]
        roles_to_remove = [role_name for role_name in roles_list if role_name.split(" ")[1] not in ctx.selected_options]
        removed_roles = []
        for role_name in roles_to_remove:
            if role_name in [r.name for r in ctx.author.roles]:
                removed_roles += [role_name]
                role = discord.utils.get(ctx.guild.roles, name=role_name)
                await ctx.author.remove_roles(role)
        roles_to_add = [f"Builder Hall {bh_level}" for bh_level in ctx.selected_options]
        added_roles = []
        for role_name in roles_to_add:
            if role_name not in [r.name for r in ctx.author.roles]:
                added_roles += [role_name]
                role = discord.utils.get(ctx.guild.roles, name=role_name)
                await ctx.author.add_roles(role)
        removed_roles.sort(key=lambda x: int(x.split(" ")[2]))
        removed_roles_str = ', '.join(removed_roles)
        added_roles.sort(key=lambda x: int(x.split(" ")[2]))
        added_roles_str = ', '.join(added_roles)
        await ctx.send(f"Roles removed : {removed_roles_str}\nRoles added : {added_roles_str}")
    return


async def auto_roles__league(ctx):
    if "auto_roles league" in ctx.origin_message.embeds[0].footer.text:
        await ctx.defer(edit_origin=False, hidden=True)
        roles_list = []
        for league in Useful["league_trophies"].keys():
            roles_list += [league]
        roles_to_remove = [role_name for role_name in roles_list if role_name not in ctx.selected_options]
        removed_roles = []
        for role_name in roles_to_remove:
            if role_name in [r.name for r in ctx.author.roles]:
                removed_roles += [role_name]
                role = discord.utils.get(ctx.guild.roles, name=role_name)
                await ctx.author.remove_roles(role)
        roles_to_add = [league for league in ctx.selected_options]
        added_roles = []
        for role_name in roles_to_add:
            if role_name not in [r.name for r in ctx.author.roles]:
                added_roles += [role_name]
                role = discord.utils.get(ctx.guild.roles, name=role_name)
                await ctx.author.add_roles(role)
        removed_roles.sort(key=lambda x: list(Emojis["League_emojis"].keys()).index(x))
        removed_roles_str = ', '.join(removed_roles)
        added_roles.sort(key=lambda x: list(Emojis["League_emojis"].keys()).index(x))
        added_roles_str = ', '.join(added_roles)
        await ctx.send(f"Roles removed : {removed_roles_str}\nRoles added : {added_roles_str}")
    return
