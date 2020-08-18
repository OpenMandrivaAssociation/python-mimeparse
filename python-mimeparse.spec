%define pypi_name python-mimeparse
%define pypi_oname python-mimeparse

Name:           %{pypi_name}
Version:        1.6.0
Release:        %mkrel 9
Group:          Development/Python
Summary:        Python module for parsing mime-type names
License:        MIT
URL:            http://pypi.python.org/pypi/python-mimeparse
Source0:        http://pypi.python.org/packages/source/p/%{pypi_oname}/%{pypi_oname}-%{version}.tar.gz
BuildArch:      noarch

%description
A module provides basic functions for parsing mime-type names and
matching them against a list of media-ranges.

%package -n python3-mimeparse
Summary:        Python 3 module for parsing mime-type names
Group:          Development/Python

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
Provides:       python3-python-mimeparse = %{version}-%{release}
Obsoletes:      python3-python-mimeparse < %{version}-%{release}

%description -n python3-mimeparse
A module provides basic functions for parsing mime-type names
and matching them against a list of media-ranges.

%prep
%setup -q -n %{pypi_oname}-%{version}

# drop bundled egg-info
rm -rf python_mimeparse.egg-info/

%build
%py3_build

%install
%py3_install

%files -n python3-mimeparse
%license LICENSE
%doc README.rst
%{python3_sitelib}/*
