# https://github.com/square/go-jose
%global goipath         gopkg.in/square/go-jose.v2
%global forgeurl        https://github.com/square/go-jose
Version:                2.1.9

%gometa

%global common_description %{expand:
Package jose aims to provide an implementation of the Javascript Object
Signing and Encryption set of standards. This includes support for JSON Web
Encryption, JSON Web Signature, and JSON Web Token standards.}

%global golicenses    LICENSE
%global godocs        *.md

%global godevelheader %{expand:
# The devel package will usually benefit from corresponding project binaries.
Requires:  %{name} = %{version}-%{release}
}

Name:           %{goname}
Release:        1%{?dist}
Summary:        An implementation of JOSE standards (JWE, JWS, JWT) in Go
# Detected licences
# - *No copyright* Apache License (v2.0) at 'LICENSE'
# json/ is BSD
License:        ASL 2.0 and BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(golang.org/x/crypto/ed25519)
BuildRequires: golang(golang.org/x/crypto/pbkdf2)
BuildRequires: golang(github.com/stretchr/testify/assert)
BuildRequires: golang(gopkg.in/alecthomas/kingpin.v2)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in jose-util jwk-keygen; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%check
%gocheck

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/*

%gopkgfiles

%changelog
* Thu Mar 21 21:59:10 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.1.9-1
- First package for Fedora
