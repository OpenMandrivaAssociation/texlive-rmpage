# revision 20002
# category Package
# catalog-ctan /macros/latex/contrib/rmpage
# catalog-date 2010-10-04 11:12:53 +0200
# catalog-license gpl
# catalog-version 0.92
Name:		texlive-rmpage
Version:	0.92
Release:	2
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

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.92-2
+ Revision: 755707
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.92-1
+ Revision: 719456
- texlive-rmpage
- texlive-rmpage
- texlive-rmpage
- texlive-rmpage

