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
import time
import asyncio

plugin_base = PluginBase(package='plugins')
plugin_source = plugin_base.make_plugin_source(
    searchpath=['./plugins'])

library_base = PluginBase(package='libraries')
library_source = library_base.make_plugin_source(
    searchpath=['./libraries'])

plugins = []
libraries = []

for plugin in plugin_source.list_plugins():
    try:
        loading_plugin = plugin_source.load_plugin(plugin)
        result = loading_plugin.init(loading_plugin)
        for command in result[1]:
            result[0].on_command(command, "BOT_TEST_EVENT")
            print("Command " + command + " registed!")
        plugins.append(result)
    except Exception as e:
        print(e)
        print("Module " + plugin + " failed to load")

for library in library_source.list_plugins():
    libraries.append(library)

client = discord.Client()

@client.event
async def on_ready():
    bot_settings.startTime = int(time.time())
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if(message.content.split(" ")[0] == bot_settings.prefix + "plugins"):
        pluginlist = []
        librarylist = []
        for plugin in plugins:
            pluginlist.append(str(plugin[0].__name__).rsplit(".",1)[1])
        for library in libraries:
            librarylist.append(str(library))
        await client.send_message(message.channel, "**PLUGINS:**\n```" + ", ".join(pluginlist) + "```\n**LIBRARIES:**\n```" + ", ".join(libraries) + "```")
    elif(message.content.split(" ")[0] == bot_settings.prefix + "commands"):
        commandlist = []
        for plugin in plugins:
            for command in plugin[1]:
                commandlist.append(bot_settings.prefix + command)
        await client.send_message(message.channel, ", ".join(commandlist))
    else:
        for plugin in plugins:
            for command in plugin[1]:
                if message.content.split(" ")[0] == bot_settings.prefix + command:
                    try:
                        await client.send_typing(message.channel)
                        if(len(message.content.split(" ")) == 1):
                            result = plugin[0].on_command(message.content[1:], "")
                        else:
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
                        await client.send_message(message.channel,
                                                  "<@219683089457217536> ```NON-FATAL BOT ERROR\r\n" + str(e) + " [" + str(fname) + ":" + str(exc_tb.tb_lineno) + "]```")

client.run(open('key.txt', 'r').read().strip())