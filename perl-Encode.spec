%define upstream_name    Encode
%define upstream_version 2.55

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	1

Summary:    Character Encodings Handler
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/D/DA/DANKOGAI/Encode-%{upstream_version}.tar.gz

BuildRequires: perl-devel
Requires: perl-devel

%description
The "Encode" module provides the interfaces between Perl's strings and
the rest of the system.  Perl strings are sequences of characters.

The repertoire of characters that Perl can represent is at least that
defined by the Unicode Consortium. On most platforms the ordinal values
of the characters (as returned by "ord(ch)") is the "Unicode codepoint"
for the character (the exceptions are those platforms where the legacy
encoding is some variant of EBCDIC rather than a super-set of ASCII -
see perlebcdic).

Traditionally, computer data has been moved around in 8-bit chunks often
called "bytes". These chunks are also known as "octets" in networking
standards. Perl is widely used to manipulate data of many types - not
only strings of characters representing human or computer languages but
also "binary" data being the machine's representation of numbers, pixels
in an image - or just about anything.

When Perl is processing "binary data", the programmer wants Perl to
process "sequences of bytes". This is not a problem for Perl - as a byte
has 256 possible values, it easily fits in Perl's much larger "logical
character".


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
rm -rf %buildroot/%{_bindir} %buildroot%{_mandir}/man1

%clean

%files
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.430.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 2.430.0-2
+ Revision: 681695
- update file list
- fix conflicts with perl

* Sun May 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.430.0-1
+ Revision: 677326
- update to new version 2.43

* Sun Jan 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.420.0-1mdv2011.0
+ Revision: 627524
- update to new version 2.42

* Sun Dec 26 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.410.0-1mdv2011.0
+ Revision: 625270
- update to new version 2.41

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 2.400.0-2mdv2011.0
+ Revision: 597093
- rebuild

* Sat Nov 13 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.400.0-1mdv2011.0
+ Revision: 597081
- new version

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2.390.0-2mdv2011.0
+ Revision: 555252
- rebuild

* Fri Nov 27 2009 Jérôme Quelin <jquelin@mandriva.org> 2.390.0-1mdv2010.1
+ Revision: 470455
- update to 2.39

* Tue Nov 17 2009 Jérôme Quelin <jquelin@mandriva.org> 2.380.0-1mdv2010.1
+ Revision: 466747
- update to 2.38

* Mon Sep 07 2009 Jérôme Quelin <jquelin@mandriva.org> 2.370.0-1mdv2010.0
+ Revision: 432322
- update to 2.37

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 2.350.0-1mdv2010.0
+ Revision: 401666
- rebuild using %%perl_convert_version
- fixed license field

* Wed Jul 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.35-1mdv2010.0
+ Revision: 396218
- update to new version 2.35

* Thu Jul 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.34-1mdv2010.0
+ Revision: 393791
- update to new version 2.34

* Fri May 01 2009 Jérôme Quelin <jquelin@mandriva.org> 2.33-1mdv2010.0
+ Revision: 369667
- update to new version 2.33

* Sun Mar 08 2009 Jérôme Quelin <jquelin@mandriva.org> 2.32-1mdv2009.1
+ Revision: 352845
- update to new version 2.32

* Thu Feb 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.31-1mdv2009.1
+ Revision: 342933
- update to new version 2.31

* Mon Feb 16 2009 Jérôme Quelin <jquelin@mandriva.org> 2.30-1mdv2009.1
+ Revision: 340732
- update to new version 2.30

* Mon Feb 02 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.29-1mdv2009.1
+ Revision: 336360
- update to new version 2.29

* Fri Jan 23 2009 Jérôme Quelin <jquelin@mandriva.org> 2.27-1mdv2009.1
+ Revision: 332939
- v2.27
- fix upstream url

* Sun Jan 18 2009 Jérôme Quelin <jquelin@mandriva.org> 2.26-1mdv2009.1
+ Revision: 330854
- removing conflicting scripts already provided by perl-devel
- import perl-Encode


* Sat Jan 17 2009 cpan2dist 2.26-1mdv
- initial mdv release, generated with cpan2dist




