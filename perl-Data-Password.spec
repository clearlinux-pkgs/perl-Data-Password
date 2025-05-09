#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Data-Password
Version  : 1.12
Release  : 32
URL      : https://cpan.metacpan.org/authors/id/R/RA/RAZINF/Data-Password-1.12.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RA/RAZINF/Data-Password-1.12.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libd/libdata-password-perl/libdata-password-perl_1.12-1.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Data-Password-license = %{version}-%{release}
Requires: perl-Data-Password-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Data::Password - Perl extension for assessing password quality.
SYNOPSIS
use Data::Password qw(IsBadPassword);

%package dev
Summary: dev components for the perl-Data-Password package.
Group: Development
Provides: perl-Data-Password-devel = %{version}-%{release}
Requires: perl-Data-Password = %{version}-%{release}

%description dev
dev components for the perl-Data-Password package.


%package license
Summary: license components for the perl-Data-Password package.
Group: Default

%description license
license components for the perl-Data-Password package.


%package perl
Summary: perl components for the perl-Data-Password package.
Group: Default
Requires: perl-Data-Password = %{version}-%{release}

%description perl
perl components for the perl-Data-Password package.


%prep
%setup -q -n Data-Password-1.12
cd %{_builddir}
tar xf %{_sourcedir}/libdata-password-perl_1.12-1.debian.tar.xz
cd %{_builddir}/Data-Password-1.12
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Data-Password-1.12/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Data-Password
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Data-Password/0513661cf3c127d8d092d1b0a52ac5059e3f9dcf || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Data::Password.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Data-Password/0513661cf3c127d8d092d1b0a52ac5059e3f9dcf

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
