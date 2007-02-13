%define		module		wtp
%define		_ver_major	1.5
%define		_ver_minor	1
%define		_buildid	200609230508
Summary:	Web Tools Platform
Summary(pl.UTF-8):	Web Tools Platform - platforma narzędzi WWW
Name:		eclipse-%{module}
Version:	%{_ver_major}.%{_ver_minor}
Release:	0.2
License:	EPL v1.0
Group:		Development/Tools
Source0:	http://download.eclipse.org/webtools/downloads/drops/R%{_ver_major}/R-%{version}-%{_buildid}/%{module}-R-%{version}-%{_buildid}.zip
# Source0-md5:	ef6ee106fae286499a268b32c73cbb56
#URL:		
BuildRequires:	unzip
Requires:	eclipse >= 3.2
Requires:	eclipse-emf-sdo >= 2.2.1
Requires:	eclipse-gef >= 3.2.1
Requires:	eclipse-jem >= 1.2.1
Requires:	eclipse-xsd >= 2.2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_eclipsedir	%{_libdir}/eclipse

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
