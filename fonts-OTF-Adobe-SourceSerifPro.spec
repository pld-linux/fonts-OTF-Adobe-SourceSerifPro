# NOTE: there are also TTF fonts in tarball
Summary:	Adobe Source Serif Pro - A set of OpenType fonts for coders
Summary(pl.UTF-8):	Adobe Source Serif Pro - zestaw fontów OpenType dla programistów
Name:		fonts-OTF-Adobe-SourceSerifPro
Version:	1.014
Release:	1
License:	OFL v1.1
Group:		Fonts
Source0:	https://github.com/adobe-fonts/source-serif-pro/archive/%{version}R.tar.gz
# Source0-md5:	4d803f5c10ee6b1214d5a0a32e1fe82d
Source1:	%{name}-fontconfig.conf
URL:		https://github.com/adobe-fonts/source-serif-pro
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         otffontsdir     %{_fontsdir}/OTF

%description
Source Serif Pro is a set of OpenType fonts to complement the Source
Sans Pro family.

%description -l pl.UTF-8
Source Serif Pro to zestaw fontów szeryfowych w formacie OpenType,
uzupełniających rodzinę Source Sans Pro.

%prep
%setup -q -n source-serif-pro-%{version}R

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{otffontsdir},%{_datadir}/fontconfig/conf.avail,%{_sysconfdir}/fonts/conf.d}

install -p OTF/*.otf $RPM_BUILD_ROOT%{otffontsdir}
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/%{name}.conf
ln -s %{_datadir}/fontconfig/conf.avail/%{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d/

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst OTF

%postun
fontpostinst OTF

%files
%defattr(644,root,root,755)
%doc LICENSE.txt ReadMe.html SourceSerifProReadMe.html
%{otffontsdir}/SourceSerifPro-*.otf
%{_sysconfdir}/fonts/conf.d/%{name}.conf
%{_datadir}/fontconfig/conf.avail/%{name}.conf
