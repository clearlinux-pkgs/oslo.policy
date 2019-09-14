#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xFC43F0EE211DFED8 (infra-root@openstack.org)
#
Name     : oslo.policy
Version  : 2.3.2
Release  : 62
URL      : http://tarballs.openstack.org/oslo.policy/oslo.policy-2.3.2.tar.gz
Source0  : http://tarballs.openstack.org/oslo.policy/oslo.policy-2.3.2.tar.gz
Source1 : http://tarballs.openstack.org/oslo.policy/oslo.policy-2.3.2.tar.gz.asc
Summary  : Oslo Policy library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.policy-bin = %{version}-%{release}
Requires: oslo.policy-license = %{version}-%{release}
Requires: oslo.policy-python = %{version}-%{release}
Requires: oslo.policy-python3 = %{version}-%{release}
Requires: PyYAML
Requires: oslo.config
Requires: oslo.context
Requires: oslo.i18n
Requires: oslo.serialization
Requires: requests
Requires: six
Requires: stevedore
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : oslo.config
BuildRequires : oslo.context
BuildRequires : oslo.i18n
BuildRequires : oslo.serialization
BuildRequires : pbr
BuildRequires : requests
BuildRequires : six
BuildRequires : stevedore

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/oslo.policy.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

%package bin
Summary: bin components for the oslo.policy package.
Group: Binaries
Requires: oslo.policy-license = %{version}-%{release}

%description bin
bin components for the oslo.policy package.


%package license
Summary: license components for the oslo.policy package.
Group: Default

%description license
license components for the oslo.policy package.


%package python
Summary: python components for the oslo.policy package.
Group: Default
Requires: oslo.policy-python3 = %{version}-%{release}

%description python
python components for the oslo.policy package.


%package python3
Summary: python3 components for the oslo.policy package.
Group: Default
Requires: python3-core

%description python3
python3 components for the oslo.policy package.


%prep
%setup -q -n oslo.policy-2.3.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568320427
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oslo.policy
cp LICENSE %{buildroot}/usr/share/package-licenses/oslo.policy/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/oslopolicy-checker
/usr/bin/oslopolicy-list-redundant
/usr/bin/oslopolicy-policy-generator
/usr/bin/oslopolicy-policy-upgrade
/usr/bin/oslopolicy-sample-generator

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oslo.policy/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
