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


def makeBar(progress):
    return '[{0}{1}] {2}%'.format('#'*(int(round(progress/2))), ' '*(50-(int(round(progress/2)))), progress)