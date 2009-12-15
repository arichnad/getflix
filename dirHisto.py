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
# This script calculates a histogram of the ratings of films by director.
# Please run getflix.pl and getdirectors.py first!
#
# Generates file directors2.txt for directors with ratings averaging 5
# Format: DirectorName~#ofFilms~AverageRating

import sys


#idfile=open('directors.txt','r')


rat=0
director=''
tempstr=''
directorh={}
directorhr={}
directordiv={}

idfile=open('directors2.txt','w')

for line in open('directors.txt').xreadlines( ):
    arr=line.split('~')
    director=arr.pop(0)
    directorhr[director]=0.0
    directorh[director]=0.0
    directordiv[director]=0

for line in open('directors.txt').xreadlines( ):
    arr=line.split('~')
    rat=int(arr.pop())
    director=arr.pop()
    directorh[director]=directorh[director]+1
    directorhr[director]=directorhr[director]+rat
#    print str(directorh[director])+"~"+str(directorhr[director])
    if directorhr[director]>=5:
	directordiv[director]=directorhr[director]/directorh[director]
	tempstr=director+"~"+str(directorh[director])+"~"+str(directordiv[director])+"\n"
	idfile.write(tempstr)


print directordiv
