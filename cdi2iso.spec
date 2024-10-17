%define name	cdi2iso
%define version	0.1
%define release	10

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Convert DiskJuggler CD Images to ISO
Source:		%{name}-%{version}.tar.bz2
URL:		https://developer.berlios.de/projects/cdi2iso/
License:	GPL
Group:		Archiving/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description 
CDI2ISO is a very simple utility to convert DiscJuggler image
to the standard ISO-9660 format.

%prep
%setup -q

%build
gcc %optflags ./src/cdi2iso.c -o cdi2iso

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install cdi2iso %{buildroot}%{_bindir}/cdi2iso

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG
%{_bindir}/cdi2iso




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-9mdv2011.0
+ Revision: 616977
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.1-8mdv2010.0
+ Revision: 424753
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 0.1-7mdv2009.0
+ Revision: 240488
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Aug 19 2007 Olivier Thauvin <nanardon@mandriva.org> 0.1-5mdv2008.0
+ Revision: 66753
- rebuild


* Fri Aug 04 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/04/06 21:47:37 (53005)
- rebuild

* Fri Aug 04 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/04/06 21:43:34 (53004)
Import cdi2iso

* Mon Apr 17 2006 Olivier Thauvin <nanardon@mandriva.org> 0.1-3mdk
- rebuild

* Thu Mar 31 2005 Olivier Thauvin <nanardon@mandrake.org> 0.1-2mdk
- create a %%build stage

* Thu Mar 31 2005 Olivier Thauvin <nanardon@mandrake.org> 0.1-1mdk
- initial spec file from Michael Berger <webmaster@hmb-linux.de>

