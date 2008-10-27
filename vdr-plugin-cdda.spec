
%define plugin	cdda
%define name	vdr-plugin-%plugin
%define version	0.1.0
%define rel	16

Summary:	VDR plugin: music cd player
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.wahnadium.org
Source:		ftp://ftp.wahnadium.org/pub/vdr-cdda/vdr-%plugin-%version.tar.bz2
Patch0:		cdda-0.1.0-i18n-1.6.patch
# From e-tobi repository:
Patch1:		02_fix-cdda_menu.h.dpatch
Patch2:		90_cdda-1.3.38.dpatch
Patch3:		03_cdbremse.dpatch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
BuildRequires:	libcdio-devel
BuildRequires:	libmad-devel
Requires:	vdr-abi = %vdr_abi

%description
The "cdda" plugin is an audio cd player with cd-text and cddb support. You can
play your favorite music cd's as like as you do it with your standalone cd
player.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%patch1 -p1 -b .menu
%patch2 -p1 -b .1338
%patch3 -p1
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# set the cdrom device
var=CDROM_DEVICE
param=--device=CDROM_DEVICE
# set the base directory to the cddb cache (no default
# argument). When no directory is set, then the local cache
# is automatically disabled.
var=CDDB_CACHEDIR
param=--cddbDir=CDDB_CACHEDIR
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


