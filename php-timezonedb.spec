#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-timezonedb
Version  : 2022.7
Release  : 40
URL      : https://pecl.php.net/get/timezonedb-2022.7.tgz
Source0  : https://pecl.php.net/get/timezonedb-2022.7.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.01
Requires: php-timezonedb-lib = %{version}-%{release}
Requires: php-timezonedb-license = %{version}-%{release}
BuildRequires : buildreq-php

%description
No detailed description available

%package lib
Summary: lib components for the php-timezonedb package.
Group: Libraries
Requires: php-timezonedb-license = %{version}-%{release}

%description lib
lib components for the php-timezonedb package.


%package license
Summary: license components for the php-timezonedb package.
Group: Default

%description license
license components for the php-timezonedb package.


%prep
%setup -q -n timezonedb-2022.7
cd %{_builddir}/timezonedb-2022.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-timezonedb
cp %{_builddir}/timezonedb-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-timezonedb/a0de8178be391188a8cd696998a75de204d5798d
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20220829/timezonedb.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-timezonedb/a0de8178be391188a8cd696998a75de204d5798d
