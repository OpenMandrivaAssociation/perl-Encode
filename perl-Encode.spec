
%define realname   Encode
%define version    2.26
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Character Encodings Handler
Source:     http://www.cpan.org/modules/by-module//%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel




%description
This module implements China-based Chinese charset encodings. Encodings
supported are as follows.

  Canonical   Alias		Description
  --------------------------------------------------------------------
  euc-cn      /\beuc.*cn$/i	EUC (Extended Unix Character)
          /\bcn.*euc$/i
              /\bGB[-_ ]?2312(?:\D.*$|$)/i (see below)
  gb2312-raw			The raw (low-bit) GB2312 character map
  gb12345-raw			Traditional chinese counterpart to 
                GB2312 (raw)
  iso-ir-165			GB2312 + GB6345 + GB8565 + additions
  MacChineseSimp                GB2312 + Apple Additions
  cp936				Code Page 936, also known as GBK 
                (Extended GuoBiao)
  hz				7-bit escaped GB2312 encoding
  --------------------------------------------------------------------

To find how to use this module in detail, see the Encode manpage.

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/enc2xs
/usr/bin/piconv
/usr/share/man/man1/enc2xs.1.lzma
/usr/share/man/man1/piconv.1.lzma

