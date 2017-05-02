#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEB6CCA1483FA74EC (infra-root@openstack.org)
#
Name     : oslo.policy
Version  : 1.22.0
Release  : 38
URL      : http://tarballs.openstack.org/oslo.policy/oslo.policy-1.22.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.policy/oslo.policy-1.22.0.tar.gz
Source99 : http://tarballs.openstack.org/oslo.policy/oslo.policy-1.22.0.tar.gz.asc
Summary  : Oslo Policy library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.policy-bin
Requires: oslo.policy-python
Requires: PyYAML
Requires: oslo.config
Requires: oslo.i18n
Requires: oslo.serialization
Requires: requests
Requires: six
Requires: stevedore
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
========================
Team and repository tags
========================
.. image:: http://governance.openstack.org/badges/oslo.policy.svg
:target: http://governance.openstack.org/reference/tags/index.html

%package bin
Summary: bin components for the oslo.policy package.
Group: Binaries

%description bin
bin components for the oslo.policy package.


%package python
Summary: python components for the oslo.policy package.
Group: Default

%description python
python components for the oslo.policy package.


%prep
%setup -q -n oslo.policy-1.22.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1490884067
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1490884067
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
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
/usr/bin/oslopolicy-sample-generator

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
