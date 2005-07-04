#
# gaim_major_ver and gaim_minor_ver should be defined to match the minimum
# Gaim API version _required_ to build Guifications
# Due to the way Gaim checks plugin versions, we need to also ensure that
# the correct minimum version of Gaim is Require:'d based on what version of
# the Gaim headers we actually build with.
#
%define gaim_major_ver 1
%define gaim_minor_ver 0
%define gaim_next_major_ver %(echo $((%{gaim_major_ver}+1)))
%define gaim_build_minor_ver %(pkg-config --modversion gaim 2>/dev/null | awk -F. '{ print $2 }')
#
Summary:	Guifications Plugin for Gaim
Summary(pl):	Wtyczka Guifications dla Gaima
Name:		gaim-plugin-guifications
Version:	2.10
Release:	0.2
Epoch:		0
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/guifications/guifications-%{version}.tar.bz2
# Source0-md5:	df22e7f44722ecd9cf12876c83032d60
URL:		http://guifications.sf.net/Guifications/
BuildRequires:	gaim-devel >= 1:%{gaim_major_ver}.%{gaim_minor_ver}
BuildRequires:	gaim-devel < 1:%{gaim_next_major_ver}
BuildRequires:	gettext
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	gaim >= 1:%{gaim_major_ver}.%{gaim_build_minor_ver}
Requires:	gaim < 1:%{gaim_next_major_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Guifications is a Gaim plugin that adds notification windows styled
after those found in MSN, deadaim, and newer versions of AIM, Yahoo
instant messenger, and a lot of other applications.

%description -l pl
Guifications to wtyczka dla Gaima dodaj±ca okienka powiadomieñ
stylizowane na takie, jakie mo¿na napotkaæ w MSN, deadaimie i nowszych
wersjach AIM-a, Yahoo Instant Messengerze oraz wielu innych
aplikacjach.

%prep
%setup -q -n guifications-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang guifications

rm -f $RPM_BUILD_ROOT%{_libdir}/gaim/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f guifications.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README doc/flow.png doc/flow.dia doc/QUOTES
%attr(755,root,root) %{_libdir}/gaim/*.so
%{_datadir}/pixmaps/gaim/guifications
