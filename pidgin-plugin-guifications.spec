# TODO:
# - requirements of pidgin needed (libs)
%define pidgin_ver %(pkg-config --modversion pidgin 2>/dev/null || echo ERROR)
Summary:	Guifications Plugin for Pidgin
Summary(pl.UTF-8):	Wtyczka Guifications dla Pidginaa
Name:		pidgin-plugin-guifications
Version:	2.14
Release:	4
Epoch:		1
License:	GPL
Group:		Applications/Communications
#Source0:	http://dl.sourceforge.net/guifications/pidgin-guifications-%{version}.tar.bz2
Source0:	http://downloads.guifications.org/plugins/Guifications2/pidgin-guifications-%{version}.tar.bz2
# Source0-md5:	3c7b126d255d0c768a4af699c4454481
URL:		http://guifications.sf.net/Guifications/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	libtool
BuildRequires:	pidgin-devel >= 2.2
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	pidgin >= %{pidgin_ver}
Obsoletes:	gaim-plugin-guifications
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Guifications is a Pidgin plugin that adds notification windows styled
after those found in MSN, deadaim, and newer versions of AIM, Yahoo
instant messenger, and a lot of other applications.

%description -l pl.UTF-8
Guifications to wtyczka dla Pidgina dodająca okienka powiadomień
stylizowane na takie, jakie można napotkać w MSN, deadaimie i nowszych
wersjach AIM-a, Yahoo Instant Messengerze oraz wielu innych
aplikacjach.

%prep
%setup -q -n pidgin-guifications-%{version}
mv po/{no,nb}.po
sed -i -e '/ALL_LINGUAS/s,no,nb,' configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang guifications

rm -f $RPM_BUILD_ROOT%{_libdir}/pidgin/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f guifications.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README doc/flow.png doc/flow.dia doc/QUOTES
%attr(755,root,root) %{_libdir}/pidgin/*.so
%{_pixmapsdir}/pidgin/guifications
