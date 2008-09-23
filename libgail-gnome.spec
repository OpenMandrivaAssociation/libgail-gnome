%define lib_name %mklibname gail-gnome
%define develname %mklibname -d gail-gnome

Summary: Dynamic libraries for for libgail-gnome
Name: libgail-gnome
Version: 1.20.1
Release: %mkrel 1
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
License: LGPLv2+
Url: http://developer.gnome.org/projects/gap/
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: atk-devel >= 1.7.2
BuildRequires: at-spi-devel
Buildrequires: libgnomeui2-devel
BuildRequires: libpanel-applet-2-devel
#gw libtool dep:
BuildRequires: libxtst-devel libglade2.0-devel
Obsoletes: libgail-gnome0
Provides: libgail-gnome0

%description
Gail is the GNOME Accessibility Implementation Library

%if %_lib != lib
%package -n %{lib_name}
Summary:	%{summary}
Group:		%{group}

%description -n %{lib_name}
Gail is the GNOME Accessibility Implementation Library
%endif

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


