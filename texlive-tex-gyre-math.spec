# revision 26838
# category Package
# catalog-ctan /fonts/tex-gyre-math
# catalog-date 2012-06-05 00:19:44 +0200
# catalog-license lppl
# catalog-version 1.008
Name:		texlive-tex-gyre-math
Version:	1.008
Release:	1
Summary:	Maths fonts to match tex-gyre text fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/tex-gyre-math
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-gyre-math.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-gyre-math.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeX-Gyre-Math is to be a collection of maths fonts to match the
text fonts of the TeX-Gyre collection. The collection will be
made available in OpenType format, only; fonts will conform to
the developing standards for OpenType maths fonts. At present,
only TeX-Gyre-Math-Pagella is available.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/opentype/public/tex-gyre-math/texgyrepagella-math.otf
%doc %{_texmfdistdir}/doc/fonts/tex-gyre-math/GUST-FONT-LICENSE.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre-math/MANIFEST-TeX-Gyre-Pagella-Math.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre-math/README-TeX-Gyre-Pagella-Math.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre-math/math-test.tex
%doc %{_texmfdistdir}/doc/fonts/tex-gyre-math/presentation-tg_pagella_math.pdf
%doc %{_texmfdistdir}/doc/fonts/tex-gyre-math/test-lualatex-tg_pagella_math.pdf
%doc %{_texmfdistdir}/doc/fonts/tex-gyre-math/test-lualatex-tg_pagella_math.tex
%doc %{_texmfdistdir}/doc/fonts/tex-gyre-math/test-word-tg_pagella_math.docx
%doc %{_texmfdistdir}/doc/fonts/tex-gyre-math/test-word-tg_pagella_math.pdf
%doc %{_texmfdistdir}/doc/fonts/tex-gyre-math/test-xelatex-tg_pagella_math.pdf
%doc %{_texmfdistdir}/doc/fonts/tex-gyre-math/test-xelatex-tg_pagella_math.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
