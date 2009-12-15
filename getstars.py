#!/usr/bin/python

##########################################################
#This script has been created by
#Copyright 2006 Devanshu Mehta
#  of http://www.scienceaddiction.com
#It is released under the GNU General Public License v2
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
# This script gets the rating information by actor or actress in the film.
# Please run getflix.pl first!



import re
from mechanize import Browser
import sys

import urllib2

br=Browser()
br.set_handle_robots(False)
f=br.open(sys.argv[1])
body=f.read()

i=0

i=body.find('Starring')
starline=body[i+14:i+100]
stars=starline.split('<')
starlist=stars[0].split(',')
i=0
while i<len(starlist):
    starlist[i]=starlist[i].strip('. ')
    i=i+1

print starlist

