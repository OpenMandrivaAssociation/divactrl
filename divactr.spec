Summary:	A user utility for supported active ISDN cards from Eicon Networks
Name:		divactrl
Version:	2.1
Release:	%mkrel 1
Group:		System/Kernel and hardware
License:	GPL
URL:		http://isdn4linux.org/~armin/divas/
Source0:	http://isdn4linux.org/~armin/divas/%{name}_%{version}.tar.bz2
Patch0:		divactrl_2.1-dialog.diff
Requires:	cdialog
BuildRequires:	dos2unix

%description
The divactrl user utility for supported active ISDN cards
from Eicon Networks.

%prep

%setup -q -n %{name}_%{version}
%patch0 -p1

# clean up CVS stuff
for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -r $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v "\.gif" | grep -v "\.png" | grep -v "\.jpg" | xargs dos2unix -U

%build

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/* CHANGES README README.firmware
%attr(0755,root,root) /sbin/divactrl
%{_datadir}/eicon


