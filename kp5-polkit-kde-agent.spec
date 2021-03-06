%define		kdeplasmaver	5.22.3
%define		qtver		5.9.0
%define		kpname		polkit-kde-agent

Summary:	Daemon providing a polkit authentication UI for KDE
Name:		kp5-%{kpname}
Version:	5.22.3
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-1-%{version}.tar.xz
# Source0-md5:	ddf80106865c347a41ec68e568f2ad8c
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kcrash-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
Daemon providing a polkit authentication UI for KDE.

%prep
%setup -q -n %{kpname}-1-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/polkit-kde-authentication-agent-1
/etc/xdg/autostart/polkit-kde-authentication-agent-1.desktop
%{_datadir}/knotifications5/policykit1-kde.notifyrc
%{_desktopdir}/org.kde.polkit-kde-authentication-agent-1.desktop
%{systemduserunitdir}/plasma-polkit-agent.service
