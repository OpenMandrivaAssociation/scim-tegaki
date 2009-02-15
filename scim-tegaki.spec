Summary: 	Chinese and Japanese Handwriting Recognition - scim integration
Name: 		scim-tegaki
Version: 	0.1
Release: 	%mkrel 1
License: 	GPLv2+
Group: 		System/Internationalization
Source: 	http://downloads.sourceforge.net/tegaki/%name-%version.tar.gz
URL: 		http://tegaki.sourceforge.net/
Buildroot: 	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch
%py_requires -d
Requires:	tegaki
Requires:	scim-python

%description
Tegaki is an ongoing project which aims to develop a free and open-source
modern implementation of handwriting recognition software, that is suitable for
both the desktop and mobile devices, and that is designed from the ground up to
work well with Chinese and Japanese.

This package contains tegaki module towards scim engine.

%prep
%setup -qn %name-%version

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%{py_puresitedir}/*
%{_datadir}/scim-python/helper/tegaki
