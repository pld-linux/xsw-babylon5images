Summary:	XShipWars graphics (Babylon5 theme)
Summary(pl):	Grafika do XShipWars (motyw Babylon5)
Name:		xsw-babylon5images
Version:	1.0
Release:	1
License:	Modified GPL
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Source0:	ftp://gd.tuwien.ac.at/games/wolfpack/babylon5images%{version}.tar.bz2
Source1:	ftp://gd.tuwien.ac.at/games/wolfpack/babylon5.ocsn.gz
URL:		http://wolfpack.twu.net/ShipWars/XShipWars/
Provides:	xsw-images
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6

%description 
XShipWars is a highly customizable and massivly multiplayer space
gamming system designed for play entirly over the Internet.
This package contains Babylon5 graphics theme for the game.

%description -l pl
XShipWars to wysoko konfigurowalny system gry w przestrzeni kosmicznej
dla wielu graczy, zaprojektowany do grania przez Internet. Ten pakiet
zawiera motyw graficzny Babylon5 dla tej gry.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir},%{_sysconfdir}/xshipwars

cd $RPM_BUILD_ROOT%{_datadir}/xshipwars
tar xzf %{SOURCE0}
gunzip -c %{SOURCE1} > $RPM_BUILD_ROOT%{_sysconfdir}/xshipwars/babylon5.ocsn

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/xshipwars/images/*
%{_sysconfdir}/xshipwars/*
