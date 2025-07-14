%define 	modulename pam_pgsql
Summary:	PostgreSQL PAM Module
Summary(pl.UTF-8):	Moduł PAM PostgreSQL
Name:		pam-%{modulename}
Version:	0.9.3
Release:	4
Epoch:		0
License:	GPL
Group:		Base
Source0:	http://dl.sourceforge.net/sysauth-pgsql/pam-pgsql-%{version}.tar.gz
# Source0-md5:	6d91662f167c87bf64dd24753181e9e3
Patch0:		%{name}-include.patch
URL:		http://sysauth-pgsql.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pam-devel
BuildRequires:	postgresql-devel
BuildRequires:	postgresql-ecpg-devel
Obsoletes:	pam_pgsql
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/%{_lib}/security

%description
PAM PgSQL is a PAM module that uses PostgreSQL database.

%description -l pl.UTF-8
PAM PgSQL jest modułem PAM używającym bazy PostgreSQL.

%prep
%setup -q -n pam-pgsql-%{version}
%patch -P0 -p1
rm -f src/acct.c src/auth.c src/chauth.c src/cred.c src/pam_pgsql.c

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%configure \
	%{!?debug:--disable-debug} 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# useless
rm -f $RPM_BUILD_ROOT%{_libdir}/pam_pgsql.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_libdir}/pam_pgsql.so
