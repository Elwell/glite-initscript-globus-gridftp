%define topdir %(pwd)/rpmbuild
%define _topdir %{topdir} 
Summary: glite-initscript-globus-gridftp
Name: glite-initscript-globus-gridftp
Version: 1.0.2
Vendor: EGEE
Release: 1
License: EGEE
Group: EGEE
Source: %{name}.src.tgz
BuildArch: noarch
Prefix: /
Requires: vdt_globus_data_server 
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Packager: EGEE

%description
This package contains the init script to start globus-gridftp.

%prep

%setup -c

%build
make install prefix=%{buildroot}%{prefix}

%files
%defattr(-,root,root)
%{prefix}/etc/init.d/globus-gridftp
%{prefix}/etc/logrotate.d/globus-gridftp
%doc LICENSE

%clean
rm -rf %{buildroot}



