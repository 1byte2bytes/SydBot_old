#Original code from https://github.com/corpnewt/CorpBot.py is under the following license
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

import urllib
import requests
import bot_settings


def init(plugin):
    return [plugin, [bot_settings.prefix + "ascii"]]

def on_command(text):
    if(text.startswith(bot_settings.prefix + "ascii ")):
        """Beautify some text (font list at http://artii.herokuapp.com/fonts_list)."""

        if text == None:
            return 'Usage: `{}ascii [font (optional)] [text]`\n(font list at http://artii.herokuapp.com/fonts_list)'.format(
                bot_settings.prefix)
            return

        # Get list of fonts
        fonturl = "http://artii.herokuapp.com/fonts_list"
        response = response = requests.get(fonturl)
        fonts = response.text.split()

        font = None
        # Split text by space - and see if the first word is a font
        parts = text.split()
        if len(parts) > 1:
            # We have enough entries for a font
            if parts[0] in fonts:
                # We got a font!
                font = parts[0]
                text = ' '.join(parts[1:])

        url = "http://artii.herokuapp.com/make?{}".format(urllib.parse.urlencode({'text': text}))
        if font:
            url += '&font={}'.format(font)
        response = requests.get(url)
        return "", "```Markup\n{}```".format(response.text)