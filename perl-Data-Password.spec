#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-Password
Version  : 1.12
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/R/RA/RAZINF/Data-Password-1.12.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RA/RAZINF/Data-Password-1.12.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libd/libdata-password-perl/libdata-password-perl_1.12-1.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Data-Password-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Data::Password - Perl extension for assessing password quality.
SYNOPSIS
use Data::Password qw(IsBadPassword);

%package dev
Summary: dev components for the perl-Data-Password package.
Group: Development
Provides: perl-Data-Password-devel = %{version}-%{release}

%description dev
dev components for the perl-Data-Password package.


%package license
Summary: license components for the perl-Data-Password package.
Group: Default

%description license
license components for the perl-Data-Password package.


%prep
%setup -q -n Data-Password-1.12
cd ..
%setup -q -T -D -n Data-Password-1.12 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Data-Password-1.12/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Data-Password
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Data-Password/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.2/Data/Password.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Data::Password.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Data-Password/deblicense_copyright
