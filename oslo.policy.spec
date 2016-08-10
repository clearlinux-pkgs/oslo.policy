#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oslo.policy
Version  : 1.13.0
Release  : 28
URL      : http://tarballs.openstack.org/oslo.policy/oslo.policy-1.13.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.policy/oslo.policy-1.13.0.tar.gz
Summary  : Oslo Policy library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.policy-bin
Requires: oslo.policy-python
BuildRequires : Jinja2
BuildRequires : Pygments
BuildRequires : Sphinx-python
BuildRequires : coverage-python
BuildRequires : docutils-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : flake8-python
BuildRequires : hacking
BuildRequires : iso8601-python
BuildRequires : mccabe-python
BuildRequires : msgpack-python-python
BuildRequires : netaddr
BuildRequires : netifaces-python
BuildRequires : oslo.config
BuildRequires : oslo.serialization-python
BuildRequires : oslo.utils-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pycodestyle-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mock-python
BuildRequires : python3-dev
BuildRequires : requests-mock-python
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : tox
BuildRequires : virtualenv

%description
=============
oslo.policy
=============
.. image:: https://img.shields.io/pypi/v/oslo.policy.svg
:target: https://pypi.python.org/pypi/oslo.policy/
:alt: Latest Version

%package bin
Summary: bin components for the oslo.policy package.
Group: Binaries

%description bin
bin components for the oslo.policy package.


%package python
Summary: python components for the oslo.policy package.
Group: Default
Requires: oslo.config
Requires: oslo.serialization-python
Requires: oslo.utils-python
Requires: requests-python
Requires: six-python

%description python
python components for the oslo.policy package.


%prep
%setup -q -n oslo.policy-1.13.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

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
