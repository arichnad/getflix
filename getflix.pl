#!/usr/bin/perl

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
# Remember to modify the email address and password below!
#
# This code is based on the original script by John Ressig
# of http://ejohn.org. Thanks John!
#
# It generates an output file called nflicks.txt with ratings information.
# Format: 60000161~Wonder Boys~2000~R~Drama~3
#         NflixID~Film Title~Year~MPAA~Genre~Rating


use Netflix;
use Data::Dumper;


my $netflix = new Net::Netflix( u => 'email@address.com', p => 'password' );

print Dumper( $netflix->getRatings() );
