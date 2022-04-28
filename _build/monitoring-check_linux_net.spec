#
# spec file for package monitoring-check_linux_net
#

Name:           monitoring-check_linux_net
Version:        %{version}
Release:        %{release}
Summary:        Check Linux network IO
License:        Lunch license
Group:          System/Monitoring
Url:            https://github.com/joernott/Nag_checks
Source0:        Nag_checks-%{version}.tar.gz
BuildArch:      noarch
Provides:       check_linux_net

%description
A very extendable network monitoring tool. There are tons of arguments you can
use to have this do anything you want. It's very low resource and has performance
monitoring.

%prep
%setup -q -n Nag_checks-%{version}

%install
rm -rf "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT/usr/lib64/nagios/plugins"
cp check_linux_net "$RPM_BUILD_ROOT/usr/lib64/nagios/plugins/"

%files
%defattr(-,root,root,755)
%attr(0755,root,root) /usr/lib64/nagios/plugins/check_linux_net

%changelog
* Wed Apr 26 2022 Joern Ott <joern.ott@schufa.de>
- Initial rpm build version
