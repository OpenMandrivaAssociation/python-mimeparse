%define module python_mimeparse
%bcond tests 1

Name:		python-mimeparse
Version:	2.0.0
Release:	1
Group:		Development/Python
Summary:	Python module for parsing mime-type names
License:	MIT
URL:		https://pypi.org/project/python-mimeparse
# Upstream is this repo:	https://github.com/falconry/python-mimeparse
# See for more info: https://github.com/falconry/python-mimeparse/issues/20
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:  pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
%endif

%description
A module provides basic functions for parsing mime-type names and
matching them against a list of media-ranges.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info/

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
pytest
%endif

%files
%doc README.rst
%{python_sitelib}/__pycache__
%{python_sitelib}/mimeparse.py
%{python_sitelib}/%{module}-%{version}.dist-info

