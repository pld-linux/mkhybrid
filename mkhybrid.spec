Summary:	Creates an hybrid ISO9660/Joliet/HFSISO9660 filesystem image
Summary(pl):	Tworzy obraz mieszanego systemu plikow ISO9660/Joliet/HFSISO9660
Name:		mkhybrid
Version:	1.12b5.2
Release:	2
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.ge.ucl.ac.uk/pub/mkhfs/%{name}-%{version}.tar.gz
# Source0-md5:	30de5a1cec363936f66bba0ba876fc65
Patch0:		%{name}-install.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mkhybrid - create an hybrid ISO9660/JOLIET/HFS filesystem with
optional Rock Ridge attributes. Includes support for making bootable
"El Torito" CD-ROMs.

%description -l pl
mkhybrid - tworzy obraz mieszanego systemu plików ISO9660/Joliet/HFS z
opcjonalnymi atrybutami rozszerzeñ Rock Ridge. Zawiera wsparcie dla
tworzenia bootowalnych p³yt CD-ROM "El Torito".

%prep
%setup -q
%patch -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

%{__make} install DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir}/man8

rm -f README.win32

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog ChangeLog.mkhybrid README* TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
