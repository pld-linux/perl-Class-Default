#
# Conditional build:
%bcond_without	tests		# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Default
Summary:	Class::Default - static calls apply to a default instantiation
Summary(pl.UTF-8):	Class::Default - domyślna instancja klasy dla wywołanych metod statycznych
Name:		perl-Class-Default
Version:	1.51
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ff10355e5ac350f14ed3e5a427592abd
URL:		http://search.cpan.org/dist/Class-Default/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::Default provides a mechanism to allow your class to take static
method calls and apply it to a default instantiation of an object.
It provides a flexibility to an API that allows it to be used more
comfortably in different situations.

%description -l pl.UTF-8
Class::Default dostarcza mechanizm pozwalający aby wywoływane
statyczne metod klasy operowały na domyślnej instancji tej klasy.
Daje to możliwość elastycznego API, które w pewnych sytuacjach
może być bardziej wygodne.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Class/Default.pm
%{_mandir}/man?/*
