%global debug_package %{nil}

Name:       rust-analyzer
Version:    2022.08.22
Release:    1%{?dist}
Summary:    A Rust compiler front-end for IDEs
License:    MIT
URL:        https://github.com/rust-lang/rust-analyzer
Source0:    %{url}/releases/download/2022-08-22/%{name}-x86_64-unknown-linux-gnu.gz

%description
rust-analyzer is a modular compiler frontend for the Rust language. It is a part of a larger rls-2.0 effort to create excellent IDE support for Rust.

%prep
%setup -T -c -n rust-analyzer
gunzip -c %{SOURCE0} > rust-analyzer

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 rust-analyzer %{buildroot}%{_bindir}

%files
%{_bindir}/rust-analyzer
