#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x20CAA0E7EA885677 (freee@debian.org)
#
Name     : testtools
Version  : 2.3.0
Release  : 55
URL      : http://pypi.debian.net/testtools/testtools-2.3.0.tar.gz
Source0  : http://pypi.debian.net/testtools/testtools-2.3.0.tar.gz
Source99 : http://pypi.debian.net/testtools/testtools-2.3.0.tar.gz.asc
Summary  : Extensions to the Python standard library unit testing framework
Group    : Development/Tools
License  : MIT
Requires: testtools-python3
Requires: testtools-python
Requires: extras
Requires: fixtures
Requires: pbr
Requires: python-mimeparse
Requires: six
Requires: testresources
Requires: testscenarios
Requires: traceback2
Requires: unittest2
BuildRequires : extras
BuildRequires : pbr
BuildRequires : pip

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
Requires: testtools-python3

%description python
python components for the testtools package.


%package python3
Summary: python3 components for the testtools package.
Group: Default
Requires: python3-core

%description python3
python3 components for the testtools package.


%prep
%setup -q -n testtools-2.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523308950
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
