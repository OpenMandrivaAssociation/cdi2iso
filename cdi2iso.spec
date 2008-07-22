%define name	cdi2iso
%define version	0.1
%define release	%mkrel 7

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Convert DiskJuggler CD Images to ISO
Source:		%{name}-%{version}.tar.bz2
URL:		http://developer.berlios.de/projects/cdi2iso/
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


