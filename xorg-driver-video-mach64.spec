Summary:	X.org video drivers for ATI VGAWonder/Mach32/Mach64 adapters
Summary(pl.UTF-8):	Sterowniki obrazu X.org do kart graficznych ATI VGAWonder/Mach32/Mach64
Name:		xorg-driver-video-mach64
Version:	6.9.7
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/driver/xf86-video-mach64-%{version}.tar.xz
# Source0-md5:	ea15f55233c6e7974349f1f02d79eb87
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.2
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.12.901
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-glproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.99.1
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-proto-xf86miscproto-devel
BuildRequires:	xorg-proto-xineramaproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.4
BuildRequires:	xz
%{?requires_xorg_xserver_videodrv}
Requires:	libdrm >= 2.2
Requires:	xorg-lib-libpciaccess >= 0.12.901
Requires:	xorg-xserver-libdri >= 1.4
Requires:	xorg-xserver-libglx >= 1.4
Requires:	xorg-xserver-server >= 1.4
Provides:	xorg-driver-video
Obsoletes:	XFree86-Mach32 < 4
Obsoletes:	XFree86-Mach64 < 4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for old ATI adapters; supports most of chips from:
- VGAWonder series: 18800, 18800-1, 28800-2, 28800-4, 28800-5, 28800-6
- Mach32 series: 68800-3, 68800-6, 68800AX, 68800LX
- Mach64 series: 88800GX-C, 88800GX-D, 88800GX-E, 88800GX-F, 88800CX,
  264CT, 264ET, 264VT, 264GT (3D Rage), 264VT-B, 264VT3, 264VT4, 264GT-B
  (3D Rage II), 3D Rage IIc, 3D Rage Pro, 3D Rage LT, 3D Rage LT Pro, 3D
  Rage XL, 3D Rage XC, 3D Rage Mobility (including the -M and -P
  variants)

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
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/mach64_drv.so
