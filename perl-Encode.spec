%define upstream_name    Encode
%define upstream_version 2.43

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:    Character Encodings Handler
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/D/DA/DANKOGAI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
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
rm -rf %buildroot
%makeinstall_std
rm -rf %buildroot/%{_bindir} %buildroot%{_mandir}/man1

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
