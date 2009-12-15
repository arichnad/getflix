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
# This pulls information about directors of the films you have rated
# from the Netflix web site. Please run getflix.pl first!
#
# Generates file called directors.txt
# Format: DirectorName~Rating


import re
from mechanize import Browser
import sys

import urllib2


idfile=open('directors.txt','w')

rat=0
id=0
tempstr=''
br=Browser()
for line in open('netflix.txt').xreadlines( ):
    arr=line.split('~')
    rat=int(arr.pop())
    id=arr.pop(0)
    tempstr="http://www.netflix.com/MovieDisplay?movieid="+id
    br.set_handle_robots(False)
    f=br.open(tempstr)
    i=0
    body=f.read()
    i=body.find('Director:')
    directorline=body[i+14:i+75]
    list=directorline.split('<')
    director=list[0].strip('. ')
    tempstr=director+"~"+str(rat)+"\n"
    idfile.write(tempstr)
    print tempstr
    idfile.flush()
#br=Browser()
#br.set_handle_robots(False)
#f=br.open(sys.argv[1])
#body=f.read()

#i=0

#i=body.find('Director')
#directorline=body[i+14:i+75]
#list=directorline.split('<')
#director=list[0].strip('. ')

#print director

