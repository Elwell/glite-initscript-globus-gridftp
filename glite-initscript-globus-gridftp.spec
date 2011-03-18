
Name:      glite-initscript-globus-gridftp
Version:   1.0.4
Release:   1%{?dist}
Summary:   Init script for globus-gridftp

Group:     System Environment/Daemons
License:   ASL 2.0
URL:       https://github.com/Elwell/glite-initscript-globus-gridftp
# upstream on github but they don't provide clean tar.gz downloads
#Source0:   http://githubredir.debian.net/github/elwell/%{name}/0~master.tar.gz
Source0:   %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-build

BuildArch: noarch
#BuildRequires:
Requires:  globus-gridftp-server-progs
Requires:  logrotate

Requires(post): chkconfig
Requires(preun): chkconfig
# This is for /sbin/service
Requires(preun): initscripts


%description
This package contains the init script to start globus-gridftp, and a 
logrotate configuration file

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_sysconfdir}/init.d/globus-gridftp
%config(noreplace) %{_sysconfdir}/logrotate.d/globus-gridftp
%doc LICENSE

%post
# This adds the proper /etc/rc*.d links for the script
/sbin/chkconfig --add globus-gridftp

%preun
if [ $1 -eq 0 ] ; then
    /sbin/service globus-gridftp-server stop >/dev/null 2>&1
    /sbin/chkconfig --del globus-gridftp
fi

%changelog
* Fri Mar 18 2011 Andrew Elwell <Andrew.Elwell@cern.ch> 1.0.4-1
- remove references to GLOBUS_LOCATION

* Wed Feb 23 2011 Andrew Elwell <Andrew.Elwell@cern.ch> 1.0.3-1
- Initial import to GIT
- Updated LICENCE to later EGEE/ASL 2.0 one
- Reworked using LSB compliant initscript
