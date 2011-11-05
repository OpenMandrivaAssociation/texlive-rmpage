# revision 20002
# category Package
# catalog-ctan /macros/latex/contrib/rmpage
# catalog-date 2010-10-04 11:12:53 +0200
# catalog-license gpl
# catalog-version 0.92
Name:		texlive-rmpage
Version:	0.92
Release:	1
Summary:	A package to help change page layout parameters in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rmpage
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rmpage.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rmpage.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package lets you change page layout parameters in small
steps over a range of values using options. It can set
\textwidth appropriately for the main fount, and ensure that
the text fits inside the printable area of a printer. An
rmpage-formatted document can be typeset identically without
rmpage after a single cut and paste operation. Local
configuration can set defaults: for all documents; and by
class, by printer, and by paper size. The geometry package is
better if you want to set page layout parameters to particular
measurements.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/rmpage/rmpage.sty
%{_texmfdistdir}/tex/latex/rmpage/rmpgen.cfg
%doc %{_texmfdistdir}/doc/latex/rmpage/readme
%doc %{_texmfdistdir}/doc/latex/rmpage/rmpage-doc.pdf
%doc %{_texmfdistdir}/doc/latex/rmpage/rmpage-doc.tex
%doc %{_texmfdistdir}/doc/latex/rmpage/rmpage.tex
%doc %{_texmfdistdir}/doc/latex/rmpage/rmplocal.gfc
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
