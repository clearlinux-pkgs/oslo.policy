#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : oslo.policy
Version  : 2.1.0
Release  : 54
URL      : http://tarballs.openstack.org/oslo.policy/oslo.policy-2.1.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.policy/oslo.policy-2.1.0.tar.gz
Source99 : http://tarballs.openstack.org/oslo.policy/oslo.policy-2.1.0.tar.gz.asc
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
BuildRequires : buildreq-distutils3
BuildRequires : pbr

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
%setup -q -n oslo.policy-2.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548943147
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
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
