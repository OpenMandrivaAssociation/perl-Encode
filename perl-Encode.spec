
%define realname   Encode
%define version    2.30
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Character Encodings Handler
Source:     http://search.cpan.org/CPAN/authors/id/D/DA/DANKOGAI/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std
rm -rf %buildroot/usr/bin

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/share/man/man1/enc2xs.1.lzma
/usr/share/man/man1/piconv.1.lzma

