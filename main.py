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
import bot_settings
import sys
import os
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
            if message.content.split(" ")[0] == bot_settings.prefix + command:
                try:
                    message_content = message.content.split(" ", 1)
                    result = plugin[0].on_command(message_content[0][1:], message_content[1])
                    if (result[0] != ""):
                        print("Uploading files to Discord is not supported at this moment.")
                        if (result[1] != ""):
                            await client.send_message(message.channel, result[1])
                    elif (result[1] != ""):
                        await client.send_message(message.channel, result[1])
                    else:
                        await client.send_message(message.channel, "The command did not return and output.")
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    await client.send_message(message.channel, "<@219683089457217536> ```NON-FATAL BOT CRASH ERROR\r\n" + str(e) + " [" + str(fname) + ":" + str(exc_tb.tb_lineno) + "]```")

client.run(open('key.txt', 'r').read().strip())