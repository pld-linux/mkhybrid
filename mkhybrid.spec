Summary:     Creates an hybrid ISO9660/Joliet/HFSISO9660 filesystem image
Summary(pl): Tworzy obraz mieszanego systemu plikow ISO9660/Joliet/HFSISO9660
Name:        mkhybrid
Version:     1.12a4.7
Release:     1
Copyright:   GPL
Group:       Utilities/System
Source:      ftp://ftp.ge.ucl.ac.uk/pub/mkhfs/%{name}-%{version}.tar.gz
Buildroot:   /tmp/%{name}-%{version}-root

%description 
mkhybrid  - create an hybrid ISO9660/JOLIET/HFS filesystem
with optional Rock Ridge attributes. Includes support
for making bootable "El Torito" CD-ROMs.

%description -l pl
mkhybrid  - tworzy obraz mieszanego systemu plików ISO9660/Joliet/HFS z
opcjonalnymi atrybutami rozszerzeñ Rock Ridge. Zawiera wsparcie dla tworzenia
bootowalnych p³yt CD-ROM "El Torito".

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,man/man8}

make prefix=$RPM_BUILD_ROOT/usr install
strip $RPM_BUILD_ROOT%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(644,root,root,755) %doc ChangeLog ChangeLog.mkhybrid README README.eltorito README.session README.mkhybrid TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*

%changelog
* Sun Oct  4 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.12a4.7-1]
- added fiew cleanups.

* Sat Sep 26 1998 Piotr Grochowski <pager@dione.ids.pl>
  [1.11.1]
- First relase as a PLD package.
