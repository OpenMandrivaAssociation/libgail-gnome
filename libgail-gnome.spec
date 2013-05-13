%define lib_name %mklibname gail-gnome
%define develname %mklibname -d gail-gnome

Summary: Dynamic libraries for for libgail-gnome
Name: libgail-gnome
Version: 1.20.4
Release: 5
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
License: LGPLv2+
Url: http://developer.gnome.org/projects/gap/
Group: System/Libraries
BuildRequires: atk-devel >= 1.7.2
BuildRequires: at-spi-devel
Buildrequires: libgnomeui2-devel
BuildRequires: libpanel-applet-2-devel
#gw libtool dep:
BuildRequires: pkgconfig(xtst) libglade2.0-devel
Obsoletes: libgail-gnome0
Provides: libgail-gnome0
Requires:	%{name}-common >= %{version}

%description
Gail is the GNOME Accessibility Implementation Library

%if %_lib != lib
%package -n %{lib_name}
Summary:	%{summary}
Group:		%{group}
Requires:	%{name}-common >= %{version}

%description -n %{lib_name}
Gail is the GNOME Accessibility Implementation Library
%endif

%package common
Summary:	%{summary}
Group:		%{group}

%description common
Gail is the GNOME Accessibility Implementation Library.
This package contains files used by libgail-gnome.

%package -n %develname
Summary:	Static libraries, include files for libgail-gnome
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{lib_name} = %{version}
Obsoletes:  libgail-gnome0-devel
Provides:   libgail-gnome0-devel

%description -n %develname
Gail is the GNOME Accessibility Implementation Library


%prep
%setup -q

%build

%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

#remove unpackaged files
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/modules/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/gtk-2.0/modules/*.so

%files -n %develname
%defattr(-,root,root)
%{_libdir}/pkgconfig/*

%files common
%defattr(-,root,root)
%{_sysconfdir}/gconf/schemas/*.schemas


%changelog
* Sun May 22 2011 Funda Wang <fwang@mandriva.org> 1.20.4-3mdv2011.0
+ Revision: 677082
- rebuild to add gconf2 as req

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.20.4-2
+ Revision: 662367
- mass rebuild

* Thu Feb 24 2011 Götz Waschk <waschk@mandriva.org> 1.20.4-1
+ Revision: 639594
- update to new version 1.20.4

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 1.20.3-2mdv2011.0
+ Revision: 602545
- rebuild

* Mon Jun 21 2010 Frederic Crozat <fcrozat@mandriva.com> 1.20.3-1mdv2010.1
+ Revision: 548381
- Release 1.20.3
- create common subpackage for gconf schemas

* Tue Mar 30 2010 Götz Waschk <waschk@mandriva.org> 1.20.2-1mdv2010.1
+ Revision: 529806
- update to new version 1.20.2

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.20.1-4mdv2010.1
+ Revision: 520781
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.20.1-3mdv2010.0
+ Revision: 425544
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.20.1-2mdv2009.1
+ Revision: 351400
- rebuild

* Tue Sep 23 2008 Götz Waschk <waschk@mandriva.org> 1.20.1-1mdv2009.0
+ Revision: 287509
- update build deps
- new version
- update license

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Mar 23 2008 Emmanuel Andry <eandry@mandriva.org> 1.20.0-3mdv2008.1
+ Revision: 189625
- Fix lib group

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.20.0-2mdv2008.1
+ Revision: 150562
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Sep 17 2007 Götz Waschk <waschk@mandriva.org> 1.20.0-1mdv2008.0
+ Revision: 88993
- new version
- spec fix

* Tue Jul 10 2007 Götz Waschk <waschk@mandriva.org> 1.19.5-1mdv2008.0
+ Revision: 50885
- new version


* Mon Mar 12 2007 Götz Waschk <waschk@mandriva.org> 1.18.0-1mdv2007.1
+ Revision: 141742
- new version

* Fri Dec 29 2006 Frederic Crozat <fcrozat@mandriva.com> 1.1.3-2mdv2007.1
+ Revision: 102455
- Fix biarch
- Import libgail-gnome

* Tue Jan 31 2006 Götz Waschk <waschk@mandriva.org> 1.1.3-1mdk
- New release 1.1.3
- use mkrel

* Fri Nov 18 2005 Götz Waschk <waschk@mandriva.org> 1.1.2-1mdk
- New release 1.1.2

* Tue Jun 28 2005 G�tz Waschk <waschk@mandriva.org> 1.1.1-1mdk
- New release 1.1.1

* Wed Nov 10 2004 G�tz Waschk <waschk@linux-mandrake.com> 1.1.0-1mdk
- New release 1.1.0

* Wed Jul 28 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.6-1mdk
- Release 1.0.6
- Enable libtoolize

* Thu Apr 22 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.4-2mdk
- Fix BuildRequires

* Wed Apr 21 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.4-1mdk
- New release 1.0.4

