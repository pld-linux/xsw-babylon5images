Summary:	XShipWars sounds (Babylon5 theme)
Name:		xsw-babylon5images
Version:	1.0
Release:	1
License:	Modified GPL
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Source0:	ftp://fox.mit.edu/pub/%{name}/babylon5images%{version}.tgz
Source1:	ftp://fox.mit.edu/pub/%{name}/babylon5.ocsn.gz
URL:		http://wolfpack.tfu.net/ShipWars/XShipWars/
Provides:	xsw-images
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6

%description 
XShipWars is a highly customizable and massivly multiplayer space
gamming system designed for play entirly over the Internet.
This package contains Babylon5 graphics theme for the game.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_datadir}/xshipwars/

cd $RPM_BUILD_ROOT/%{_datadir}/xshipwars/
tar xzf %{SOURCE0}
gunzip -c %{SOURCE1} > %{_sysconfdir}/xshipwars/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/xshipwars/images/*
%{_sysconfdir}/xshipwars/*