Name:		texlive-tex-gyre-math
Version:	41264
Release:	2
Summary:	Maths fonts to match tex-gyre text fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/tex-gyre-math
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-gyre-math.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-gyre-math.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeX-Gyre-Math is to be a collection of maths fonts to match the
text fonts of the TeX-Gyre collection. The collection will be
made available in OpenType format, only; fonts will conform to
the developing standards for OpenType maths fonts. TeX-Gyre-
Math-Pagella (to match Tex-Gyre-Pagella) and TeX-Gyre-Math-
Termes (to match Tex-Gyre-Termes) fonts are provided.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/opentype/public/tex-gyre-math
%doc %{_texmfdistdir}/doc/fonts/tex-gyre-math

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
