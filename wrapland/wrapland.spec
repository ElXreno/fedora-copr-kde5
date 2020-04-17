%global commit f0c4f67f9a9596c0179e72b4893d7d5c0f2f45bc

Name:    wrapland
Version: 0.518.0
Release: 1%{?dist}
Summary: Qt/C++ library wrapping libwayland

License: LGPLv2+
URL:     https://gitlab.com/kwinft/%{name}
Source0: %{url}/-/archive/%{name}@%{version}/%{name}-%{version}.tar.bz2

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros

BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-private-devel

BuildRequires: wayland-devel
BuildRequires: wayland-protocols-devel

BuildRequires: pkgconfig(wayland-eglstream)

%description
%{summary}.

%package     devel
Summary:     Development files for %{name}
%description devel
%{summary}.

%package     client
Summary:     Qt/C++ client library wrapping libwayland
Requires:    %{name}%{?_isa} = %{version}-%{release}
%description client
%{summary}.

%package     client-devel
Summary:     Development files for %{name}-client
Requires:    %{name}%{?_isa} = %{version}-%{release}
Requires:    %{name}-devel%{?_isa} = %{version}-%{release}
%description client-devel
%{summary}.

%package     server
Summary:     Qt/C++ server library wrapping libwayland
Requires:    %{name} = %{version}-%{release}
%description server
%{summary}.

%package     server-devel
Summary:     Development files for %{name}-server
Requires:    %{name}%{?_isa} = %{version}-%{release}
Requires:    %{name}-devel%{?_isa} = %{version}-%{release}
%description server-devel
%{summary}.


%prep
%autosetup -p1 -n %{name}-%{name}@%{version}-%{commit}


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} .. \
  -DBUILD_TESTING:BOOL=ON
popd

%make_build -C %{_target_platform}


%install
%make_install -C %{_target_platform}


%check
xvfb-run -a \
dbus-launch --exit-with-session \
make test ARGS="--output-on-failure --timeout 10" -C %{_target_platform} ||:


%files
%doc CHANGELOG.md  README.md
%license COPYING.LIB
%{_datadir}/qlogging-categories5/org_kde_wrapland.categories


%files devel
%{_includedir}/wrapland_version.h
%{_libdir}/cmake/Wrapland/Wrapland*.cmake


%files client
%{_libdir}/libWraplandClient.so.*


%files client-devel
%{_libdir}/libWraplandClient.so
%{_includedir}/Wrapland/Client/


%files server
%{_libexecdir}/org-kde-kf5-wrapland-testserver
%{_libdir}/libWraplandServer.so.*


%files server-devel
%{_libdir}/libWraplandServer.so
%{_includedir}/Wrapland/Server/


%changelog
* Fri Apr 17 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.518.0-1
- first spec


