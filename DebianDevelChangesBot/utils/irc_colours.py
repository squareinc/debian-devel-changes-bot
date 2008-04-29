# -*- coding: utf-8 -*-
#
#   Debian Changes Bot
#   Copyright (C) 2008 Chris Lamb <chris@chris-lamb.co.uk>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

def colourise(s):
    tags = {
         'reset': chr(15),
         'b': chr(2),
         '/b': chr(2),
         'u': chr(31),
         '/u':  chr(31),
         'black': chr(3) + "01",
         'red': chr(3) + "04",
         'green': chr(3) + "03",
         'yellow': chr(3) + "08",
         'blue': chr(3) + "02",
         'magenta': chr(3) + "06",
         'cyan': chr(3) + "11",
         'white': chr(3) + "00",
         'nostyle': '',
    }

    # Stylesheet
    tags.update({
        'by': tags['cyan'],
        'package': tags['green'],
        'version': tags['yellow'],
        'security': tags['red'],
        'severity': tags['red'],
        'url': tags['u'],
        '/url': tags['/u'],
        'bug': tags['b'],
        '/bug': tags['/b'],
        'title': tags['nostyle'],
    })

    s = s + '[reset]'
    for k, v in tags.iteritems():
        s = s.replace('[%s]' % k, v)

    return s
