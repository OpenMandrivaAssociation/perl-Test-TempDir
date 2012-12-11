%define upstream_name    Test-TempDir
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A factory for creating L<Test::TempDir::Handle>
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(File::NFSLock)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Types::Path::Class)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::use::ok)
BuildRequires:	perl(namespace::clean)
BuildArch:	noarch

%description
Test::TempDir provides temporary directory creation with testing in mind.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 656829
- rebuild for updated spec-helper

* Fri Jul 30 2010 Shlomi Fish <shlomif@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 563372
- import perl-Test-TempDir


* Fri Jul 30 2010 cpan2dist 0.05-1mdv
- initial mdv release, generated with cpan2dist
