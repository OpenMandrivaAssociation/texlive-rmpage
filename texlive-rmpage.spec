Name:		texlive-rmpage
Version:	54080
Release:	1
Summary:	A package to help change page layout parameters in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rmpage
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rmpage.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rmpage.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
