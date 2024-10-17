%define  upstream_name phpcov
%define __noautoreq /usr/bin/php

Summary:	TextUI frontend for PHP_CodeCoverage

Name:		php-pear-%{upstream_name}
Version:	1.0.0
Release:	5
License:	BSD
Group:		Development/PHP
URL:		https://www.phpunit.de/
Source0:	http://pear.phpunit.de/get/phpcov-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-cli >= 3:5.2.1
Requires:	php-pear >= 1:1.9.4
Requires:	php-channel-phpunit
BuildArch:	noarch
BuildRequires:	php-pear
BuildRequires:	php-channel-phpunit
Suggests:	php-pear-PHPUnit >= 3.6.3
Suggests:	php-pear-PHP_CodeCoverage >= 1.1.0

%description
PHPUnit is a regression testing framework used by the developer who implements
unit tests in PHP.

This package provides TextUI frontend for PHP_CodeCoverage for PHPUnit.

%prep

%setup -q -c 
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%build

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%{_bindir}/phpcov
%{_datadir}/pear/PHP/CodeCoverage/TextUI
%{_datadir}/pear/packages/phpcov.xml



