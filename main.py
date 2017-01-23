#
#===================================================
#
#SydBot is Copyright (c) Sydney 2017
#
#This is free and unencumbered software released into the public domain.
#
#Anyone is free to copy, modify, publish, use, compile, sell, or
#distribute this software, either in source code form or as a compiled
#binary, for any purpose, commercial or non-commercial, and by any
#means.
#
#===================================================
#

from pluginbase import PluginBase
import discord
import asyncio

plugin_base = PluginBase(package='plugins')
plugin_source = plugin_base.make_plugin_source(
    searchpath=['./plugins'])

plugins = []

for plugin in plugin_source.list_plugins():
    loading_plugin = plugin_source.load_plugin(plugin)
    result = loading_plugin.init(loading_plugin)
    for command in result[1]:
        print("Command " + command + " registed!")
    plugins.append(result)

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    for plugin in plugins:
        for command in plugin[1]:
            if message.content == command:
                plugin[0].on_command(message.content)

client.run(open('key.txt', 'r').read().strip())