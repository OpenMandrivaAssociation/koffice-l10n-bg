Name: koffice-l10n-bg
Version: 1.9.98.5
Release: %mkrel 2
Summary: Language files for KOffice Bulgarian
Group: System/Internationalization
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPLv2+
URL: http://www.koffice.org
BuildArch: noarch
Source: ftp://ftp.kde.org/pub/kde/unstable/koffice-%version/src/koffice-l10n/%name-%version.tar.bz2
BuildRequires: gettext >= 0.15
BuildRequires: kdelibs4-devel
Requires: locales-bg
Requires: koffice-core
Provides: koffice-l10n

%description 
Provides Bulgarian translations for KOffice.

%files 
%defattr(-,root,root,-)
%{_kde_datadir}/*/*/*

#------------------------------------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%clean
rm -rf %buildroot


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9.98.5-2mdv2011.0
+ Revision: 612616
- the mass rebuild of 2010.1 packages

* Sat Jan 17 2009 Funda Wang <fwang@mandriva.org> 1.9.98.5-1mdv2009.1
+ Revision: 330472
- new version 1.9.98.5

* Thu Dec 11 2008 Funda Wang <fwang@mandriva.org> 1.9.98.3-1mdv2009.1
+ Revision: 312658
- new version 1.9.98.3

* Thu Nov 20 2008 Funda Wang <fwang@mandriva.org> 1.9.98.2-1mdv2009.1
+ Revision: 305024
- add source and spec
- rename wrong dir
- Created package directory for koffice-l10n-bg.


* Sat Jul 15 2006 Laurent MONTEL <lmontel@mandriva.com> 1.5.2-1
- 1.5.2

* Tue Jul 11 2006 Laurent MONTEL <lmontel@mandriva.com> 1.5.1-3
- Requires koffice-apps

* Sat May 27 2006 Laurent MONTEL <lmontel@mandriva.com> 1.5.1-2
- Use %%mkrel

* Wed May 24 2006 Laurent MONTEL <lmontel@mandriva.com> 1.5.1-1mdk
- 1.5.1

* Wed Apr 12 2006 Laurent MONTEL <lmontel@mandriva.com> 1.5.0-1mdk
- 1.5.0

* Thu Mar 30 2006 Laurent MONTEL <lmontel@mandriva.com> 1.5-0.rc1.1mdk
- 1.5.0-rc1

* Thu Mar 30 2006 Laurent MONTEL <lmontel@mandriva.com> 1.5-0.rc1.1mdk
- 1.5.0-rc1

* Mon Oct 17 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4.2-1mdk
- 1.4.2

* Mon Oct 17 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4.2-1mdk
- 1.4.2

* Fri Aug 12 2005 Laurent MONTEL <lmontel@mandriva.com> 20mdk
- Remove conflict with kde-i18n

* Thu Jul 28 2005 Laurent MONTEL <lmontel@mandriva.com> 10mdk
- Fix provides koffice-l10n

* Mon Jul 25 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4.1-1mdk
- 1.4.1

* Fri Jun 17 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4.0-1mdk
- 1.4.0

* Tue Apr 19 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3.91-1mdk
- 1.3.91

* Wed Nov 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3.5-1mdk
- 1.3.5

* Wed Oct 13 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3.4-1mdk
- 1.3.4

* Tue Sep 21 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3.3-1mdk
- 1.3.3

* Mon Jul 05 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3.2-1mdk
- 1.3.2

* Tue May 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3.1-1mdk
- 1.3.1

* Tue Jan 27 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3-1mdk
- 1.3

* Fri Dec 19 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3-0.rc2.1mdk
- rc2

* Fri Nov 28 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3-0.rc1.2mdk
- Fix buildrequires

* Wed Oct 29 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3-0.rc1.1mdk
- 1.3

* Wed Oct 29 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3-0.rc1.1mdk
- 1.3

* Sat Sep 27 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3-0.beta4.1mdk
- 1.3

* Sat Aug 16 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3-0.beta3.1mdk
- 1.3

* Wed Jul 16 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.3-0.beta2.2mdk
- buildrequires

