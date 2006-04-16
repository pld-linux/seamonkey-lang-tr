Summary:	Turkish resources for SeaMonkey
Summary(pl):	Tureckie pliki jêzykowe dla SeaMonkeya
Name:		seamonkey-lang-tr
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/contrib-localized/seamonkey-%{version}.tr-TR.langpack.xpi
# Source0-md5:	ea0a0175ab0f6d39a11f14102787cd92
Source1:	gen-installed-chrome.sh
URL:		http://www.mozilla.org/projects/seamonkey/
BuildRequires:	unzip
Requires(post,postun):	seamonkey >= %{version}
Requires(post,postun):	textutils
Requires:	seamonkey >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_chromedir	%{_datadir}/seamonkey/chrome

%description
Turkish resources for SeaMonkey.

%description -l pl
Tureckie pliki jêzykowe dla SeaMonkeya.

%prep
%setup -q -c -T
unzip %{SOURCE0}
install %{SOURCE1} .
./gen-installed-chrome.sh locale chrome/{TR,tr-TR,tr-unix}.jar > lang-tr-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install chrome/{TR,tr-TR,tr-unix}.jar $RPM_BUILD_ROOT%{_chromedir}
install lang-tr-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}
cp -r defaults $RPM_BUILD_ROOT%{_datadir}/seamonkey

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/tr-TR.jar
%{_chromedir}/tr-unix.jar
%{_chromedir}/TR.jar
%{_chromedir}/lang-tr-installed-chrome.txt
%{_datadir}/seamonkey/defaults/messenger/TR
%{_datadir}/seamonkey/defaults/profile/TR
