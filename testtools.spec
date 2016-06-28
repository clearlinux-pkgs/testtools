#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : testtools
Version  : 2.1.0
Release  : 22
URL      : https://pypi.python.org/packages/source/t/testtools/testtools-2.1.0.tar.gz
Source0  : https://pypi.python.org/packages/source/t/testtools/testtools-2.1.0.tar.gz
Summary  : Extensions to the Python standard library unit testing framework
Group    : Development/Tools
License  : MIT
Requires: testtools-python
BuildRequires : extras
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pyrsistent-python
BuildRequires : python-dev
BuildRequires : python-mimeparse
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : testtools
BuildRequires : unittest2

%description
These are scripts to help with building, maintaining and releasing testtools.
There is little here for anyone except a testtools contributor.

%package python
Summary: python components for the testtools package.
Group: Default

%description python
python components for the testtools package.


%prep
cd ..
%setup -q -n testtools-2.1.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python -m subunit.run testtools.tests.test_suite | subunit2pyunit
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
