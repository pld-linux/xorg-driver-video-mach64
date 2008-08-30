Summary:	X.org video drivers for ATI VGAWonder/Mach32/Mach64 adapters
Summary(pl.UTF-8):	Sterowniki obrazu X.org do kart graficznych ATI VGAWonder/Mach32/Mach64
Name:		xorg-driver-video-mach64
Version:	6.8.0
Release:	3
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-mach64-%{version}.tar.bz2
# Source0-md5:	6081b8fa50c689d51f85c2fbaf93867e
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.1.0
%requires_xorg_xserver_videodrv
Requires:	xorg-xserver-server >= 1.1.0
Obsoletes:	XFree86-Mach32
Obsoletes:	XFree86-Mach64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for old ATI adapters; supports most of chips from:
- VGAWonder series: 18800, 18800-1, 28800-2, 28800-4, 28800-5, 28800-6
- Mach32 series: 68800-3, 68800-6, 68800AX, 68800LX
- Mach64 series: 88800GX-C, 88800GX-D, 88800GX-E, 88800GX-F, 88800CX,
  264CT, 264ET, 264VT, 264GT (3D Rage), 264VT-B, 264VT3, 264VT4,
  264GT-B (3D Rage II), 3D Rage IIc, 3D Rage Pro, 3D Rage LT, 3D Rage
  LT Pro, 3D Rage XL, 3D Rage XC, 3D Rage Mobility (including the -M
  and -P variants)

%description -l pl.UTF-8
Sterownik obrazu X.org do starych kart graficznych ATI; obsługuje
większość kart z serii:
- VGAWonder: 18800, 18800-1, 28800-2, 28800-4, 28800-5, 28800-6
- Mach32: 68800-3, 68800-6, 68800AX, 68800LX)
- Mach64: 88800GX-C, 88800GX-D, 88800GX-E, 88800GX-F, 88800CX, 264CT,
  264ET, 264VT, 264GT (3D Rage), 264VT-B, 264VT3, 264VT4, 264GT-B (3D
  Rage II), 3D Rage IIc, 3D Rage Pro, 3D Rage LT, 3D Rage LT Pro, 3D
  Rage XL, 3D Rage XC, 3D Rage Mobility (włącznie z wariantami -M i
  -P)

%prep
%setup -q -n xf86-video-mach64-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/mach64_drv.so
