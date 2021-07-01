#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : testtools
Version  : 2.4.0
Release  : 70
URL      : https://files.pythonhosted.org/packages/11/9a/26b2f192024c4abcf702750ce7f4eb4cad305d8aad9482d9b5f3760118c7/testtools-2.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/11/9a/26b2f192024c4abcf702750ce7f4eb4cad305d8aad9482d9b5f3760118c7/testtools-2.4.0.tar.gz
Summary  : Extensions to the Python standard library unit testing framework
Group    : Development/Tools
License  : MIT
Requires: testtools-license = %{version}-%{release}
Requires: testtools-python = %{version}-%{release}
Requires: testtools-python3 = %{version}-%{release}
Requires: extras
Requires: fixtures
Requires: pbr
Requires: python-mimeparse
Requires: six
Requires: traceback2
Requires: unittest2
BuildRequires : buildreq-distutils3
BuildRequires : extras
BuildRequires : fixtures
BuildRequires : pbr
BuildRequires : python-mimeparse
BuildRequires : six
BuildRequires : testtools
BuildRequires : traceback2
BuildRequires : unittest2

%description
These are scripts to help with building, maintaining and releasing testtools.
There is little here for anyone except a testtools contributor.

%package license
Summary: license components for the testtools package.
Group: Default

%description license
license components for the testtools package.


%package python
Summary: python components for the testtools package.
Group: Default
Requires: testtools-python3 = %{version}-%{release}

%description python
python components for the testtools package.


%package python3
Summary: python3 components for the testtools package.
Group: Default
Requires: python3-core
Provides: pypi(testtools)
Requires: pypi(extras)
Requires: pypi(fixtures)
Requires: pypi(pbr)
Requires: pypi(python_mimeparse)
Requires: pypi(six)
Requires: pypi(traceback2)
Requires: pypi(unittest2)

%description python3
python3 components for the testtools package.


%prep
%setup -q -n testtools-2.4.0
cd %{_builddir}/testtools-2.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1625012400
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/testtools
cp %{_builddir}/testtools-2.4.0/LICENSE %{buildroot}/usr/share/package-licenses/testtools/6830df2fe805c26be8f114e4b8635505d6c7d766
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/testtools/6830df2fe805c26be8f114e4b8635505d6c7d766

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
