%undefine __cmake_in_source_build
%global unstable 0

Name:           kpmcore
Version:        4.2.0
Release:        1%{?dist}
Summary:        Library for managing partitions by KDE programs
License:        GPLv3+
URL:            https://github.com/KDE/kpmcore
%if 0%{?unstable}
Source0:        http://download.kde.org/unstable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
%else
Source0:        http://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
%endif

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kauth-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  qca-qt5-devel

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(libatasmart)
BuildRequires:  pkgconfig(libparted)

BuildRequires:  cmake(PolkitQt5-1)

Requires:       parted
Requires:       e2fsprogs
Requires:       kf5-filesystem

Recommends:     f2fs-tools
Recommends:     hfsutils
Recommends:     hfsplus-tools
Recommends:     jfsutils
Recommends:     nilfs-utils
Recommends:     reiserfs-utils
Recommends:     udftools

%description
KPMcore contains common code for managing partitions by KDE Partition Manager 
and other KDE projects


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}


%prep
%setup -q

%build
sed -i 's|set(BLKID_MIN_VERSION "2.33.2")|set(BLKID_MIN_VERSION "2.32.1")|' CMakeLists.txt

mkdir -p %{_target_platform}
%{cmake_kf5}

%cmake_build


%install
%cmake_install
%find_lang %{name} --with-kde



%files -f %{name}.lang
%license LICENSES/*.txt
%{_kf5_libdir}/libkpmcore.so.*
%{_kf5_qtplugindir}/libpm*.so
%{_kf5_datadir}/polkit-1/actions/*.policy
%{_kf5_datadir}/dbus-1/system-services/*.service
%{_kf5_datadir}/dbus-1/system.d/org.kde.kpmcore.*.conf
%{_libexecdir}/kpmcore_externalcommand


%files devel
%{_includedir}/%{name}/
%{_kf5_libdir}/cmake/KPMcore
%{_kf5_libdir}/libkpmcore.so



%changelog
* Fri Nov  6 14:46:54 MSK 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 4.2.0-1
- 4.2.0

* Fri Mar 06 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 4.1.0-1
- 4.1.0

* Thu May 02 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 4.0.0-1
- 4.0.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Mattia Verga <mattia.verga@yandex.com> - 3.3.0-3
- Remove ldconfig scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 26 2017 Mattia Verga <mattia.verga@tiscali.it> - 3.3.0-1
- Update to stable release 3.3.0
- Soname bump to libkpmcore.so.7

* Wed Nov 01 2017 Mattia Verga <mattia.verga@email.it> - 3.2.1-1
- Update to stable release 3.2.1

* Sun Oct 01 2017 Mattia Verga <mattia.verga@tiscali.it> - 3.2.0-1
- Update to stable release 3.2.0
- Soname bump to libkpmcore.so.6
- Remove kf5-kio-devel dependency
- Add udftools as recommended package

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 06 2017 Mattia Verga <mattia.verga@tiscali.it> - 3.1.2-1
- Update to stable release 3.1.2

* Sun Jun 04 2017 Mattia Verga <mattia.verga@tiscali.it> - 3.1.0-1
- Update to stable release 3.1.0
- Soname bump to libkpmcore.so.5

* Thu Feb 09 2017 Mattia Verga <mattia.verga@tiscali.it> - 3.0.3-1
- Update to stable release 3.0.3

* Sun Jan 15 2017 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.0.2-1
- Update to stable release 3.0.2 (additional bug fixes for Calamares)

* Sun Jan 01 2017 Mattia Verga <mattia.verga@tiscali.it> - 3.0.1-1
- Update to stable release 3.0.1 to fix possible data loss

* Wed Dec 21 2016 Mattia Verga <mattia.verga@tiscali.it> - 3.0.0-1
- Update to stable release 3.0.0

* Fri Nov 25 2016 Mattia Verga <mattia.verga@tiscali.it> - 2.9.90-2
- Backport patch from upstream to fix Calamares bug CAL-416

* Wed Nov 9 2016 Mattia Verga <mattia.verga@tiscali.it> - 2.9.90-1
- Update to unstable 2.9.90
- Soname bump to libkpmcore.so.4
- Add LVM support

* Sun Jul 10 2016 Mattia Verga <mattia.verga@tiscali.it> - 2.2.1-1
- Update to stable 2.2.1
- Switch to hfsplus-tools

* Sun Jun 12 2016 Mattia Verga <mattia.verga@tiscali.it> - 2.2.0-2
- Add weak dependencies to less used filesystem tools

* Sat Jun 11 2016 Mattia Verga <mattia.verga@tiscali.it> - 2.2.0-1
- Update to stable 2.2.0
- Soname bump to libkpmcore.so.3

* Sun May 15 2016 Mattia Verga <mattia.verga@tiscali.it> - 2.1.1-1
- Update to stable 2.1.1

* Sun Mar 13 2016 Mattia Verga <mattia.verga@tiscali.it> - 2.1.0-1
- Update to stable 2.1.0
- Use pkgconfig for libparted

* Sun Feb 28 2016 Mattia Verga <mattia.verga@tiscali.it> - 2.0.1-1
- Update to stable 2.0.1
- Use pkgconfig for libraries
- Alphabetically ordered BR
- Fix Provides and Obsoletes also for -devel package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Mattia Verga <mattia.verga@tiscali.it> - 2.0.0-2
- Rename from KPMcore to kpmcore

* Thu Jan 14 2016 Mattia Verga <mattia.verga@tiscali.it> - 2.0.0-1
- Update to stable 2.0.0

* Sun Nov 29 2015 Mattia Verga <mattia.verga@tiscali.it> - 1.9.50-5
- Fix package naming

* Sun Nov 29 2015 Mattia Verga <mattia.verga@tiscali.it> - 1.9.50-4
- Replace Obsoletes with Conflicts

* Wed Nov 25 2015 Mattia Verga <mattia.verga@tiscali.it> - 1.9.50-3
- Patch to fix soname versioning

* Mon Nov 23 2015 Mattia Verga <mattia.verga@tiscali.it> - 1.9.50-2
- Make a devel subpackage

* Sun Nov 22 2015 Mattia Verga <mattia.verga@tiscali.it> - 1.9.50-1
- Initial release
