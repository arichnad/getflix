
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
# This code is based on the original script by John Ressig
# of http://ejohn.org. Thanks John!
#
# To see how this module is called, look at getflix.pl

package Net::Netflix;

use Data::Dumper;
use WWW::Mechanize;

sub new {
	my $ref = shift;
	my $class = ref( $ref ) || $ref;

	my $self = bless {
		u => undef,
		p => undef,
		www => new WWW::Mechanize(),
		@_
	}, $class;

	die "Netflix requires a username and password" unless 
		( $self->{u} && $self->{p} );

	$self->{www}->get('http://www.netflix.com/Login');
#	print $self->{www}->content();
	$self->{www}->set_fields(
		email => $self->{u},
		password => $self->{p}
	);
	$self->{www}->submit();
#	print $self->{www}->content();
	return $self;
}

sub getRatings {
	my ( $self ) = @_;



	my %rat;
	my %year;
	my %id;
	my %mpaa;
	my %genre;
	my $body = '';
	my $cur = 1;
	my $genre ='';
	while ( $body !~ /next-inactive/i ) {
	open(FD, ">>netflix.txt") or die("Couldn't open netflix.txt");
		$self->{www}->get( "http://www.netflix.com/MoviesYouveSeen?st=tt&so=0&pn=$cur" );
		$body = $self->{www}->content();
		print "loading page $cur\n";
#		print $body;

# This is the main Regular Expression. If Netflix ever changes their web site, 
# this regular expression will need to change as well.
#60000165~Erin Brockovich~2000~R~Drama~5
		while ( $body =~ s/^.*?(?:movieid=(\d+)|unav).*?>.*? id="b[^"]*?".*?>\s*([^<]+?)\s*<.*?"genre">(.*?)<.*?(?:you rated this movie: (\d)|Average rating)//gsi ) {
			print FD "$1~$2~~~$3~$4\n";
		}
		++$cur;
	}
	close FD;
 
	return \%ret;
}
1;
