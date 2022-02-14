## https://github.com/square/go-jose
%global with_debug 0
%global debug_package %{nil}
%global goipath         github.com/operator-framework/operator-sdk
Version:        1.17.0

%gometa

%global common_description %{expand:
Package jose aims to provide an implementation of the Javascript Object
Signing and Encryption set of standards. This includes support for JSON Web
Encryption, JSON Web Signature, and JSON Web Token standards.}

%global golicenses    LICENSE
%global godocs        *.md

%global godevelheader %{expand:
# The devel package will usually benefit from corresponding project binaries.
# Requires:  %{name} = %{version}-%{release}
}

Name:           %{goname}
Release:        1%{?dist}
Summary:        INSERT SDK SUMMARY HERE
# Detected licences
# - *No copyright* Apache License (v2.0) at 'LICENSE'
# json/ is BSD
License:        ASL 2.0 and BSD
URL:            %{gourl}
Source0:        %{gosource}
Patch0:         00-fix-build.patch

# BuildRequires: golang(golang.org/x/crypto/ed25519)
# BuildRequires: golang(golang.org/x/crypto/pbkdf2)
# BuildRequires: golang(github.com/stretchr/testify/assert)
# BuildRequires: golang(gopkg.in/alecthomas/kingpin.v2)

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

%build
make build/operator-sdk

%install
%gopkginstall
# install -m 0755 -vd                     %{buildroot}%{_bindir}
# install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%check
##% gocheck

%files
# % license % {golicenses}
# % doc % {godocs}
# % {_bindir}/*

%gopkgfiles

%changelog
* Mon Feb 14 2022 jesus m. rodriguez <jesusr@redhat.com> - 1.17.0-1
- First package for Fedora
