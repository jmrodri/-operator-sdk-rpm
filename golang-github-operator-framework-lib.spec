# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/operator-framework/operator-lib
%global goipath         github.com/operator-framework/operator-lib
Version:                0.10.0

%gometa

%global common_description %{expand:
This is a library to help Operator developers.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        This is a library to help Operator developers

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Thu Feb 17 2022 Venkat Ramaraju - 0.10.0-1
- Initial package
