%global framework libgravatar

Name:    kf5-%{framework}
Version: 18.12.2
Release: 1%{?dist}
Summary: Gravatar support library

License: GPLv2
URL:     http://cgit.kde.org/%{framework}.git

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/applications/%{version}/src/%{framework}-%{version}.tar.xz

# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)

%global kf5_ver 5.23.0
BuildRequires:  extra-cmake-modules >= %{kf5_ver}
BuildRequires:  kf5-rpm-macros >= %{kf5_ver}
BuildRequires:  kf5-ki18n-devel >= %{kf5_ver}
BuildRequires:  kf5-kconfig-devel >= %{kf5_ver}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{kf5_ver}
BuildRequires:  kf5-ktextwidgets-devel >= %{kf5_ver}

#global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global majmin_ver %{version}
BuildRequires:  kf5-akonadi-contacts-devel >= %{majmin_ver}
BuildRequires:  kf5-kcalendarcore-devel >= %{majmin_ver}
BuildRequires:  kf5-pimcommon-devel >= %{majmin_ver}

Obsoletes:      kdepim-libs < 7:16.04.0
Conflicts:      kdepim-libs < 7:16.04.0

Requires:       kf5-filesystem

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.


%prep
%autosetup -n %{framework}-%{version}


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang %{name} --all-name --with-html


%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING*
%{_kf5_sysconfdir}/xdg/libgravatar.*
%{_kf5_libdir}/libKF5Gravatar.so.5*

%files devel
%{_kf5_libdir}/libKF5Gravatar.so
%{_kf5_libdir}/cmake/KF5Gravatar/
%{_kf5_includedir}/Gravatar/
%{_kf5_includedir}/gravatar/
%{_kf5_includedir}/gravatar_version.h
%{_kf5_archdatadir}/mkspecs/modules/qt_Gravatar.pri


%changelog
* Tue Feb 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.2-1
- 18.12.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.1-1
- 18.12.1

* Fri Dec 14 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.12.0-1
- 18.12.0

* Tue Nov 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.3-1
- 18.08.3

* Wed Oct 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.2-1
- 18.08.2

* Mon Oct 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.1-1
- 18.08.1

* Fri Jul 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.3-1
- 18.04.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.2-1
- 18.04.2

* Wed May 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.1-1
- 18.04.1

* Fri Apr 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.0-1
- 18.04.0

* Tue Mar 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.3-1
- 17.12.3

* Tue Feb 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.2-1
- 17.12.2

* Thu Jan 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.1-1
- 17.12.1

* Tue Dec 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.12.0-1
- 17.12.0

* Wed Dec 06 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.11.90-1
- 17.11.90

* Wed Nov 22 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.11.80-1
- 17.11.80

* Wed Nov 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.3-1
- 17.08.3

* Mon Sep 25 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.1-1
- 17.08.1

* Fri Jul 28 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.3-1
- 17.04.3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.2-1
- 17.04.2

* Sun May 14 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.1-1
- 17.04.1

* Thu Mar 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.3-1
- 16.12.3

* Thu Feb 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.2-1
- 16.12.2

* Mon Jan 16 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.1-1
- 16.12.1

* Mon Dec 05 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.3-1
- 16.08.3

* Fri Oct 28 2016 Than Ngo <than@redhat.com> - 16.08.2-2
- don't build on ppc64/s390x as qtwebengine is not supported yet

* Thu Oct 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.2-1
- 16.08.2

* Thu Sep 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.1-1
- 16.08.1

* Sun Sep 04 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.0-1
- 16.08.0

* Sun Jul 10 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.3-1
- 16.04.3

* Sun Jun 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.2-1
- 16.04.2

* Wed May 25 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.1-2
- BR: kf5-ktextwidgets-devel

* Wed May 25 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.1-1
- First try

* Tue May 03 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 16.04.0-1
- Initial version