%define		status		stable
%define		pearname	fDOMDocument
%define		php_min_version 5.3.3
Summary:	An Extension to PHP standard DOM
Name:		php-theseer-fDOMDocument
Version:	1.6.1
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.netpirates.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	9ab93fc04551f4f461e38ce5582e8d0c
URL:		https://github.com/theseer/fDOMDocument
BuildRequires:	php-channel(pear.netpirates.net)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(dom)
Requires:	php(xml)
Requires:	php-channel(pear.netpirates.net)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An Extension to PHP's standard DOM to add various convenience methods
and exceptions by default.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc docs/fDOMDocument/*
%{php_pear_dir}/.registry/.channel.*/*.reg
%dir %{php_pear_dir}/TheSeer
%{php_pear_dir}/TheSeer/fDOMDocument
