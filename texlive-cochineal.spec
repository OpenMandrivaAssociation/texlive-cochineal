%global tl_name cochineal
%global tl_revision 77682
%global tl_version 1.085

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Cochineal fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cochineal
License:	ofl lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cochineal.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cochineal.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Cochineal is a fork from the Crimson fonts (Roman, Italic, Bold,
BoldItalic only) released under the OFL by Sebastian Kosch. These
remarkable fonts are inspired by the famous oldstyle fonts in the
garalde family (Garamond, Bembo) but, in the end, look more similar to
Minion, though with smaller xheight and less plain in detail. The
Crimson fonts on which these were based had roughly 4200 glyphs in the
four styles mentioned above. Cochineal adds more than 1500 glyphs in
those styles so that it is possible to make a TeX support collection
that contains essentially all glyphs in all styles. Bringing the
Semibold styles up the same level would have required adding about 2000
additional glyphs, which I could not even contemplate. The fonts are
provided in OpenType and PostScript formats.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from cochineal:
Map Cochineal.map
TL_DROPIN_EOF
