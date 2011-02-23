%define topdir %(pwd)/rpmbuild
%define _topdir %{topdir} 

Name:      glite-initscript-globus-gridftp
Version:   1.0.3
Release:   1%{?dist}
Summary:   glite-initscript-globus-gridftp

Group:     EGEE
License:   ASL 2.0
# upstream on github but they don't provide clean tar.gz downloads
Source0:   http://githubredir.debian.net/github/elwell/%{name}/0~master.tar.gz
#Source0:   %{name}.src.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-build

BuildArch: noarch
#BuildRequires:
Requires:  vdt_globus_data_server
Requires:  logrotate

%description
This package contains the init script to start globus-gridftp.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/etc/init.d/globus-gridftp
/etc/logrotate.d/globus-gridftp
%doc LICENSE

%changelog
* Wed Feb 23 2011 Andrew Elwell <Andrew.Elwell@cern.ch> 1.0.3-1
- Initial import to GIT
- Updated LICENCE to later EGEE/ASL 2.0 one
- Reworked using LSB compliant initscript

