# $Revision: 1.7 $Date: 2004-07-29 20:47:35 $
%define 	modulename pam_pgsql
Summary:	PostgreSQL PAM Module
Summary(pl):	Modu³ PAM PostgreSQL
Name:		pam-%{modulename}
Version:	0.9.3
Release:	2.1
Epoch:		0
License:	GPL
Group:		Base
Source0:	http://dl.sourceforge.net/sysauth-pgsql/pam-pgsql-%{version}.tar.gz
# Source0-md5:	6d91662f167c87bf64dd24753181e9e3
Patch0:		%{name}-include.patch
URL:		http://sysauth-pgsql.sourceforge.net/
BuildRequires:	pam-devel
BuildRequires:	postgresql-devel
BuildRequires:	postgresql-ecpg-devel
Obsoletes:	pam_pgsql
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/%{_lib}/security

%description
PAM PgSQL is a PAM module that uses PostgreSQL database.

%description -l pl
PAM PgSQL jest modu³em PAM u¿ywaj±cym bazy PostgreSQL.

%prep
%setup -q -n pam-pgsql-%{version}
%patch0 -p1
sed -e 's@#include <postgresql/libpq-fe.h>@#include <libpq-fe.h>@' \
	src/pam_pgsql.h > pam_pgsql.h.tmp
mv -f pam_pgsql.h.tmp src/pam_pgsql.h

%build
%configure \
	%{!?debug:--disable-debug}

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
