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

def getReadableTimeBetween(first, last):
    # A helper function to make a readable string between two times
    timeBetween = int(last - first)
    weeks = int(timeBetween / 604800)
    days = int((timeBetween - (weeks * 604800)) / 86400)
    hours = int((timeBetween - (days * 86400 + weeks * 604800)) / 3600)
    minutes = int((timeBetween - (hours * 3600 + days * 86400 + weeks * 604800)) / 60)
    seconds = int(timeBetween - (minutes * 60 + hours * 3600 + days * 86400 + weeks * 604800))
    msg = ""

    if weeks > 0:
        if weeks == 1:
            msg = '{}{} week, '.format(msg, str(weeks))
        else:
            msg = '{}{} weeks, '.format(msg, str(weeks))
    if days > 0:
        if days == 1:
            msg = '{}{} day, '.format(msg, str(days))
        else:
            msg = '{}{} days, '.format(msg, str(days))
    if hours > 0:
        if hours == 1:
            msg = '{}{} hour, '.format(msg, str(hours))
        else:
            msg = '{}{} hours, '.format(msg, str(hours))
    if minutes > 0:
        if minutes == 1:
            msg = '{}{} minute, '.format(msg, str(minutes))
        else:
            msg = '{}{} minutes, '.format(msg, str(minutes))
    if seconds > 0:
        if seconds == 1:
            msg = '{}{} second, '.format(msg, str(seconds))
        else:
            msg = '{}{} seconds, '.format(msg, str(seconds))

    if not msg:
        return "0 seconds"
    else:
        return msg[:-2]