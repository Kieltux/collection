#
# spec file for package raidar
#

Name:           raidar
Version:        6.0.0
Release:        0
Summary:        NETGEAR Storage device discover tool
License:        NonFree
Group:          Productivity/Networking
Url:            https://www.readynas.com
Source:         https://www.readynas.com/contributed/mdgm/%{name}/%{name}_%{version}_amd64.deb
Patch1:         fix_opensuse_raidar.desktop.diff
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
ExclusiveArch:  x86_64

%description
RAIDar is used to discover NETGEAR Storage devices on your local network.

%prep
ar -x %{SOURCE0}
tar -xf data.tar.xz
rm -f data.tar.xz

# fix desktop file
%patch1

mv -f .%{_datadir}/doc/%{name}/copyright COPYING
gzip -d .%{_datadir}/doc/%{name}/changelog.gz
mv -f .%{_datadir}/doc/%{name}/changelog ChangeLog

%build
# Nothing to build.

%install
install -Dm 0644 .%{_datadir}/applications/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
cp -a .%{_datadir}/icons/ \
  %{buildroot}%{_datadir}/

install -Dm 0755 .%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm 0755 .%{_bindir}/%{name}-cli %{buildroot}%{_bindir}/%{name}-cli
install -Dm 0644 .%{_mandir}/man1/%{name}.1%{ext_man} %{buildroot}%{_mandir}/man1/%{name}.1%{ext_man}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc ChangeLog COPYING
%defattr(-,root,root)
%{_bindir}/%{name}
%{_bindir}/%{name}-cli
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
* Wed Jan 06 2016 - kieltux@gmail.com
- Update to 6.0.0:
  * Interface has been updated to NETGEAR's latest branding.
     Admin Page appears instead of Setup when the device is already setup
     You can still setup RAIDiator 4.1, 4.2, and 5.3 boxes with 
     RAIDar 6.0.
   * Diagnostic Functions
     With RAIDar 6.0, you can now restart the device without accessing 
     the web interface.
     You can download the logs in the event that the admin page is 
     inaccessible.
     If your ReadyNAS is having a problem, you can run Diagnostics 
     from RAIDar to find out what the device is doing.
   * No more duplicate devices for each network interface.
     Previously in RAIDar 4.3.8, RAIDar showed one entry per network 
     adapter. In RAIDar 6.0, we've combined the network interfaces into 
     a single instance.
