%global base_name    plasma-thunderbolt

Name:    plasma-thunderbolt
Summary: Plasma integration for controlling Thunderbolt devices
Version: 5.17.0
Release: 1%{?dist}

License: GPLv2+
URL:     https://cgit.kde.org/%{base_name}.git

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{base_name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Notifications)

Requires:       kf5-filesystem
Requires:       bolt%{?_isa}

%description
%{summary}.


%prep
%autosetup -n %{base_name}-%{version} -p1


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang %{name} --all-name


%files -f %{name}.lang
%license COPYING
%{_kf5_libdir}/libkbolt.so
%{_kf5_qtplugindir}/kcms/kcm_bolt.so
%{_kf5_plugindir}/kded/kded_bolt.so
%{_kf5_datadir}/knotifications5/kded_bolt.notifyrc
%{_kf5_datadir}/kpackage/kcms/kcm_bolt/contents/ui/*.{qml,js}
%{_kf5_datadir}/kpackage/kcms/kcm_bolt/metadata.{desktop,json}
%{_kf5_datadir}/kservices5/kcm_bolt.desktop


%changelog
* Tue Oct 15 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.17.0-1
- 5.17.0
