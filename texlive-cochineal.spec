Name:		texlive-cochineal
Version:	62063
Release:	1
Summary:	Cochineal fonts with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cochineal
License:	ofl lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cochineal.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cochineal.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Cochineal is a fork from the Crimson fonts (Roman, Italic,
Bold, BoldItalic only) released under the OFL by Sebastian
Kosch. These remarkable fonts are inspired by the famous
oldstyle fonts in the garalde family (Garamond, Bembo) but, in
the end, look more similar to Minion, though with smaller
xheight and less plain in detail. The Crimson fonts on which
these were based had roughly 4200 glyphs in the four styles
mentioned above. Cochineal adds more than 1500 glyphs in those
styles so that it is possible to make a TeX support collection
that contains essentially all glyphs in all styles. Bringing
the Semibold styles up the same level would have required
adding about 2000 additional glyphs, which I could not even
contemplate. The fonts are provided in OpenType and PostScript
formats.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/cochineal
%{_texmfdistdir}/fonts/vf/public/cochineal
%{_texmfdistdir}/fonts/type1/public/cochineal
%{_texmfdistdir}/fonts/tfm/public/cochineal
%{_texmfdistdir}/fonts/opentype/public/cochineal
%{_texmfdistdir}/fonts/map/dvips/cochineal
%{_texmfdistdir}/fonts/enc/dvips/cochineal
%{_texmfdistdir}/fonts/afm/public/cochineal
%doc %{_texmfdistdir}/doc/fonts/cochineal

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
