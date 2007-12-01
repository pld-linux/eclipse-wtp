# TODO
# - build noarch
%define		module		wtp
%define		ver_major	2.0
%define		ver_minor	%{nil}
%define		buildid	200706260303
Summary:	Web Tools Platform
Summary(pl.UTF-8):	Web Tools Platform - platforma narzędzi WWW
Name:		eclipse-%{module}
Version:	%{ver_major}
Release:	0.2
License:	EPL v1.0
Group:		Development/Tools
Source0:	http://archive.eclipse.org/webtools/downloads/drops/R%{ver_major}/R-%{version}-%{buildid}/%{module}-sdk-R-%{version}-%{buildid}.zip
# Source0-md5:	c968db511655b0c55e02b4faab0efb55
URL:		http://www.eclipse.org/webtools/
BuildRequires:	unzip
Requires:	eclipse >= 3.2
Requires:	eclipse-emf-sdo >= 2.2.1
Requires:	eclipse-gef >= 3.2.1
Requires:	eclipse-jem >= 1.2.1
Requires:	eclipse-xsd >= 2.2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipsedir	%{_libdir}/eclipse

%description
Web Tools Platform.

%description -l pl.UTF-8
Web Tools Platform - platforma narzędzi WWW.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/{features,plugins}
cp -rf eclipse/features/* $RPM_BUILD_ROOT%{_eclipsedir}/features
cp -rf eclipse/plugins/* $RPM_BUILD_ROOT%{_eclipsedir}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_eclipsedir}/features/*
%{_eclipsedir}/plugins/*
