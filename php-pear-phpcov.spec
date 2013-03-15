%define  upstream_name phpcov

Summary:	TextUI frontend for PHP_CodeCoverage
Name:		php-pear-%{upstream_name}
Version:	1.0.0
Release:	4
License:	BSD
Group:		Development/PHP
URL:		http://www.phpunit.de/
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
%defattr(-,root,root)
%{_bindir}/phpcov
%{_datadir}/pear/PHP/CodeCoverage/TextUI
%{_datadir}/pear/packages/phpcov.xml



%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-2mdv2012.0
+ Revision: 742321
- fix major breakage by careless packager

* Wed Nov 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1
+ Revision: 730875
- import php-pear-phpcov


* Wed Nov 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdv2010.2
- initial Mandriva package
