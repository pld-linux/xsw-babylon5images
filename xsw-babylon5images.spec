Summary:	XShipWars graphics (Babylon5 theme)
Summary(pl.UTF-8):   Grafika do XShipWars (motyw Babylon5)
Name:		xsw-babylon5images
Version:	1.1
Release:	1
License:	GPL-like
Group:		Applications/Games
Source0:	ftp://gd.tuwien.ac.at/games/wolfpack/babylon5images%{version}.tar.bz2
# Source0-md5:	2e656293db1d9d3a519d24074653e19d
Source1:	ftp://gd.tuwien.ac.at/games/wolfpack/babylon5.ocsn.gz
# Source1-md5:	311289c319d87b1d2afa4df7c6c609d2
URL:		http://wolfpack.twu.net/ShipWars/XShipWars/
Provides:	xsw-images
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
XShipWars is a highly customizable and massivly multiplayer space
gamming system designed for play entirly over the Internet. This
package contains Babylon5 graphics theme for the game.

%description -l pl.UTF-8
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
