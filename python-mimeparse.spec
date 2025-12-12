%define pypi_name python-mimeparse
%define pypi_oname python-mimeparse

Name:           %{pypi_name}
Version:        1.6.0
Release:        3
Group:          Development/Python
Summary:        Python module for parsing mime-type names
License:        MIT
URL:            https://pypi.python.org/pypi/python-mimeparse
Source0:        http://pypi.python.org/packages/source/p/%{pypi_oname}/%{pypi_oname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
Provides:       python3-python-mimeparse = %{version}-%{release}

%description
A module provides basic functions for parsing mime-type names and
matching them against a list of media-ranges.

%prep
%setup -q -n %{pypi_oname}-%{version}

# drop bundled egg-info
rm -rf python_mimeparse.egg-info/

%build
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/*
