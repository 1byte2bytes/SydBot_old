#Original code from https://github.com/corpnewt/CorpBot.py/tree/a3f0f419192dbae17f537a02dc377a41acf90757 is under the following license
#
#MIT License
#
#Copyright (c) 2016-2017 CorpNewt
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
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

import asyncio
import os
import psutil
import platform
import time
import sys
import libraries.readabletime
import libraries.progressbar
import bot_settings

def init(plugin):
    return [plugin, ["hostinfo"]]

def on_command(command, text):
    if(command == "hostinfo"):
        try:
            # cpuCores    = psutil.cpu_count(logical=False)
            # cpuThred    = psutil.cpu_count()
            cpuThred = os.cpu_count()
            cpuUsage = psutil.cpu_percent(interval=1)
            memStats = psutil.virtual_memory()
            memPerc = memStats.percent
            memUsed = memStats.used
            memTotal = memStats.total
            memTotalGB = "{0:.1f}".format(((memTotal / 1024) / 1024) / 1024)
            memUsedGB = "{0:.1f}".format(((memUsed / 1024) / 1024) / 1024)
            currentOS = platform.platform()
            system = platform.system()
            release = platform.release()
            version = platform.version()
            processor = platform.processor()
            # botMember = DisplayName.memberForID(self.bot.user.id, ctx.message.server)
            # botName = DisplayName.name(botMember)
            currentTime = int(time.time())
            timeString = libraries.readabletime.getReadableTimeBetween(bot_settings.startTime, currentTime)
            pythonMajor = sys.version_info.major
            pythonMinor = sys.version_info.minor
            pythonMicro = sys.version_info.micro
            pythonRelease = sys.version_info.releaselevel

            msg = '***Dipper Bot\'s*** **Home:**\n'
            msg += '```{}\n'.format(currentOS)
            msg += 'Python {}.{}.{} {}\n\n'.format(pythonMajor, pythonMinor, pythonMicro, pythonRelease)
            msg += '   CPU: {}% of {} ({} thread[s]) {}\n'.format(cpuUsage, processor, cpuThred, libraries.progressbar.makeBar(int(round(cpuUsage))))
            #msg += libraries.progressbar.makeBar(int(round(cpuUsage))) + "\n"
            msg += '   RAM: {} ({}%) of {}GB used   {}\n'.format(memUsedGB, memPerc, memTotalGB, libraries.progressbar.makeBar(int(round(memPerc))))
            #msg += libraries.progressbar.makeBar(int(round(memPerc))) + "\n"
            msg += '  TIME: {} ({})\n'.format(time.strftime("%H:%M:%S", time.gmtime()), time.tzname[time.daylight])
            msg += 'UPTIME: {}```'.format(timeString)

            return "", msg
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            return "", "<@219683089457217536> ```NON-FATAL BOT CRASH ERROR\r\n" + str(e) + " [" + str(
                                    fname) + ":" + str(exc_tb.tb_lineno) + "]```"
