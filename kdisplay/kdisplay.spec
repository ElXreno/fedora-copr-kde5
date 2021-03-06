%undefine __cmake_in_source_build
%global min_qt_version     5.14.0
%global min_kf_version     5.66.0
%global min_disman_version 0.520.0

Name:    kdisplay
Version: 5.20.0
Release: 1%{?dist}
Summary: App and daemon for display managing

%global  real_version %(echo %{version} |sed 's/~/-/')
License: GPLv2
URL:     https://gitlab.com/kwinft/%{name}
Source0: %{url}/-/archive/%{name}@%{real_version}/%{name}-%{name}@%{real_version}.tar.bz2

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  desktop-file-utils

BuildRequires:  qt5-qtbase-devel  >= %{min_qt_version}
BuildRequires:  cmake(Qt5Test)    >= %{min_qt_version}
BuildRequires:  cmake(Qt5Sensors) >= %{min_qt_version}

BuildRequires:  cmake(KF5Config)      >= %{min_kf_version}
BuildRequires:  cmake(KF5DBusAddons)  >= %{min_kf_version}
BuildRequires:  cmake(KF5Declarative) >= %{min_kf_version}
BuildRequires:  cmake(KF5GlobalAccel) >= %{min_kf_version}
BuildRequires:  cmake(KF5I18n)        >= %{min_kf_version}
BuildRequires:  cmake(KF5IconThemes)  >= %{min_kf_version}
BuildRequires:  cmake(KF5KCMUtils)    >= %{min_kf_version}
BuildRequires:  cmake(KF5Plasma)      >= %{min_kf_version}
BuildRequires:  cmake(KF5XmlGui)      >= %{min_kf_version}
BuildRequires:  cmake(KF5Kirigami2)   >= %{min_kf_version}

BuildRequires:  cmake(Disman) >= %{min_disman_version}


%description
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{name}@%{real_version}


%build
%{cmake_kf5}
%cmake_build


%install
%cmake_install


%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kwinft.%{name}.desktop


%files
%doc README.md
%license COPYING COPYING.LGPL
%{_bindir}/kdisplay
%{_kf5_datadir}/kded_kdisplay/qml/*.qml
%{_kf5_datadir}/kpackage/kcms/kcm_kdisplay/
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_datadir}/plasma/plasmoids/org.kwinft.kdisplay/
%{_kf5_datadir}/qlogging-categories5/kdisplay.categories
%{_kf5_metainfodir}/org.kwinft.kdisplay.appdata.xml
%{_kf5_qtplugindir}/kcms/kcm_kdisplay.so
%{_kf5_qtplugindir}/plasma/applets/plasma_applet_kdisplay.so
%{_kf5_plugindir}/kded/kdisplayd.so
%{_kf5_datadir}/applications/org.kwinft.%{name}.desktop


%changelog
* Wed Oct 14 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.20.0-1
- version 5.20.0

* Tue Jun 16 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.19.0-1
- first spec for version 5.19.0

