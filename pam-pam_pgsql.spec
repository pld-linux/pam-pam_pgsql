# $Revision: 1.1 $Date: 2003-11-25 13:40:21 $
Summary:	PostgreSQL PAM Module
Summary(pl):	Modu³ PAM PostgreSQL
Name:		pam-pam_pgsql
Version:	0.9.3
Release:	1
License:	GPL
Group:		Base
Source0:	http://dl.sourceforge.net/sysauth-pgsql/pam-pgsql-%{version}.tar.gz
# Source0-md5:	6d91662f167c87bf64dd24753181e9e3
URL:		http://sysauth-pgsql.sourceforge.net/
BuildRequires:	sed
BuildRequires:	pam-devel
BuildRequires:	postgresql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/lib/security

%description
PAM PgSQL is a PAM module that uses PostgreSQL database.

%description -l pl
PAM PgSQL jest modu³em PAM u¿ywaj±cym bazy PostgreSQL.

%prep
%setup -q -n pam-pgsql-%{version}
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
