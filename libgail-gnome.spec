%define lib_name %mklibname gail-gnome
%define develname %mklibname -d gail-gnome

Summary: Dynamic libraries for for libgail-gnome
Name: libgail-gnome
Version: 1.20.4
Release: 4
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0: libgail-gnome-1.20.4-compile.patch
License: LGPLv2+
Url: http://developer.gnome.org/projects/gap/
Group: System/Libraries
BuildRequires: pkgconfig(atk)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(libbonobo-2.0)
BuildRequires: pkgconfig(libbonoboui-2.0)
BuildRequires: pkgconfig(libgnomeui-2.0)
BuildRequires: pkgconfig(libpanelapplet-4.0)
BuildRequires: pkgconfig(libspi-1.0)
BuildRequires: pkgconfig(cspi-1.0)
#gw libtool dep:
BuildRequires: libxtst-devel libglade2.0-devel
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
%apply_patches
libtoolize --force
aclocal
automake -a
autoconf

%build

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std

#remove unpackaged files
rm -f %{buildroot}%{_libdir}/gtk-2.0/modules/*.la

%clean
rm -rf %{buildroot}

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/gtk-2.0/modules/*.so

%files -n %develname
%defattr(-,root,root)
%{_libdir}/pkgconfig/*

%files common
%defattr(-,root,root)
%{_sysconfdir}/gconf/schemas/*.schemas
