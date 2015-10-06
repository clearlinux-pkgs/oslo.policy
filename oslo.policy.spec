#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oslo.policy
Version  : 0.11.0
Release  : 12
URL      : http://tarballs.openstack.org/oslo.policy/oslo.policy-0.11.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.policy/oslo.policy-0.11.0.tar.gz
Summary  : Oslo Policy library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.policy-python
BuildRequires : Babel
BuildRequires : Jinja2
BuildRequires : MarkupSafe
BuildRequires : Pygments
BuildRequires : Sphinx
BuildRequires : debtcollector-python
BuildRequires : discover
BuildRequires : docutils
BuildRequires : extras
BuildRequires : fixtures
BuildRequires : flake8
BuildRequires : funcsigs
BuildRequires : hacking
BuildRequires : iso8601
BuildRequires : linecache2
BuildRequires : mccabe
BuildRequires : mock-python
BuildRequires : monotonic-python
BuildRequires : mox3
BuildRequires : msgpack-python
BuildRequires : netaddr
BuildRequires : netifaces
BuildRequires : oslo.config
BuildRequires : oslo.i18n
BuildRequires : oslo.serialization
BuildRequires : oslo.utils
BuildRequires : oslosphinx
BuildRequires : oslotest
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyflakes
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mimeparse
BuildRequires : python-subunit
BuildRequires : python3-dev
BuildRequires : pytz
BuildRequires : requests
BuildRequires : setuptools
BuildRequires : six
BuildRequires : stevedore
BuildRequires : testrepository
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : tox
BuildRequires : traceback2
BuildRequires : unittest2
BuildRequires : virtualenv
BuildRequires : wrapt-python

%description
=============
oslo.policy
=============
The Oslo Policy library provides support for RBAC policy enforcement across
all OpenStack services.

%package python
Summary: python components for the oslo.policy package.
Group: Default

%description python
python components for the oslo.policy package.


%prep
%setup -q -n oslo.policy-0.11.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
