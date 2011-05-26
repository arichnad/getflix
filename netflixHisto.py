#!/usr/bin/python

##########################################################
# This script has been created by
# Copyright 2006 Devanshu Mehta
#  of http://www.scienceaddiction.com
# It is released under the GNU General Public License v2
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
# This file will generate a histogram of the netflix data generated by
# the getflix.pl script. Please run getflix.pl first!


rating=[0,0,0,0,0]
i=0
yearh= {1900:0, 1901:0}
yearhr={1900:0.0}
yearhr5={1900:0.0}

mpaah={'PG':0, 'R':0, 'PG-13':0, 'UR':0, 'G':0, 'NC-17':0, 'NR':0}
mpaahr={'PG':0.0, 'R':0.0, 'PG-13':0.0, 'UR':0.0, 'G':0.0, 'NC-17':0.0, 'NR':0.0}
mpaahr5={'PG':0.0, 'R':0.0, 'PG-13':0.0, 'UR':0.0, 'G':0.0, 'NC-17':0.0, 'NR':0.0}

genreh={'Foreign':0, 'Drama':0, 'Independent':0, 'Classics':0, 'Television':0, 'Children & Family':0, 'Sci-Fi & Fantasy':0, 'Comedy':0, 'Romance':0, 'Action & Adventure':0, 'Horror':0, 'Documentary':0, 'Thrillers':0, 'Music & Musicals':0, 'Anime & Animation':0, 'Gay & Lesbian':0, 'Special Interest':0}
genrehr={'Foreign':0.0, 'Drama':0.0, 'Independent':0.0, 'Classics':0.0, 'Television':0.0, 'Children & Family':0.0, 'Sci-Fi & Fantasy':0.0, 'Comedy':0.0, 'Romance':0.0, 'Action & Adventure':0.0, 'Horror':0.0, 'Documentary':0.0, 'Thrillers':0.0, 'Music & Musicals':0.0, 'Anime & Animation':0.0, 'Gay & Lesbian':0.0, 'Special Interest':0.0}
genrehr5={'Foreign':0.0, 'Drama':0.0, 'Independent':0.0, 'Classics':0.0, 'Television':0.0, 'Children & Family':0.0, 'Sci-Fi & Fantasy':0.0, 'Comedy':0.0, 'Romance':0.0, 'Action & Adventure':0.0, 'Horror':0.0, 'Documentary':0.0, 'Thrillers':0.0, 'Music & Musicals':0.0, 'Anime & Animation':0.0, 'Gay & Lesbian':0.0, 'Special Interest':0.0}


decadehr={'1':0}
decadeh={'1':0}
decadehr5={'1':0}

for i in range (0,10):
    decadehr[str(i)]=0.0
    decadeh[str(i)]=0
    decadehr5[str(i)]=0.0
i=0

idfile=open('idfile.txt','w')

for i in range(1900,2080):
    yearh[str(i)]=0
    yearhr[str(i)]=0.0
    yearhr5[str(i)]=0.0

for line in open('netflix.txt').xreadlines( ):
    arr=line.split('~')
    rat=arr.pop()
    if rat == '\n':
	rat = 1
    rat=int(rat)
    genre=arr.pop()
    mpaa=arr.pop()
    year=arr.pop()
    name=arr.pop()
    id=arr.pop()
    rating[rat-1]=rating[rat-1]+1
    if genre != '' :
        genreh[genre]=genreh[genre]+1
    if genre != 'Television' :
	if len(year) == 4 :
	    decadeh[year[2]]=decadeh[year[2]]+1
	    decadehr[year[2]]=decadehr[year[2]]+rat
	    yearh[year]=yearh[year]+1
	    yearhr[year]=yearhr[year]+rat
	if mpaa != '' :
	    mpaah[mpaa]=mpaah[mpaa]+1
	    mpaahr[mpaa]=mpaahr[mpaa]+rat
	if genre != '' :
	    genrehr[genre]=genrehr[genre]+rat
	if rat==5 :
	    if len(year) == 4 :
	        decadehr5[year[2]]=decadehr5[year[2]]+1
	        yearhr5[year]=yearhr5[year]+1
	    if mpaa != '' :
		mpaahr5[mpaa]=mpaahr5[mpaa]+1
	    if genre != '' :
	        genrehr5[genre]=genrehr5[genre]+1
	tempstr=id+"~"+str(rat)+"\n"
	idfile.write(tempstr)

print
print "Number of Films per Ratings from 1-5"
for x in range(0,5):
    print "Star-Rating "+str(x+1)+".0: "+str(rating[x])

mpaas=['G','PG','PG-13','R','NC-17','UR','NR']
print
print "MPAA  #films  %5star  Avg Rating"
for m in mpaas:
    if mpaah[m] != 0:
	print '%-6s%6d%8.0f%12.1f' % (m, mpaah[m],mpaahr5[m]*100.0/mpaah[m],mpaahr[m]/mpaah[m])

genres=['Drama', 'Comedy', 'Independent', 'Classics', 'Romance', 'Thrillers', 'Sci-Fi & Fantasy', 'Action & Adventure', 'Foreign', 'Documentary', 'Horror', 'Children & Family']

print
print "Genre               #films  %5star  Avg Rating"
for g in genres:
    if genreh[g] != 0:
	print '%-20s%6d%8.0f%12.1f' % (g,genreh[g],genrehr5[g]*100.0/genreh[g],genrehr[g]/genreh[g])

print
print "Decade  #films  %5star  Avg Rating"
for x in range(0,10):
    if decadeh[str(x)] != 0 :
	print '%d0s   %8d%8.0f%12.1f' % (x,decadeh[str(x)],decadehr5[str(x)]*100.0/decadeh[str(x)],decadehr[str(x)]/decadeh[str(x)])


print
print "Year  #films  %5star  Avg Rating"
for x in range(1990,2080):
    if yearh[str(x)] != 0 :
	print '%d%8d%8.0f%12.1f' % (x,yearh[str(x)],yearhr5[str(x)]*100.0/yearh[str(x)],yearhr[str(x)]/yearh[str(x)])

