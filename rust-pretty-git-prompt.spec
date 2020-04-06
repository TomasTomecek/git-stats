# Generated by rust2rpm
%bcond_without check

%global crate pretty-git-prompt

Name:           rust-%{crate}
Version:        0.2.1
Release:        1%{?dist}
Summary:        Your current git repository information inside a beautiful shell prompt

License:        MIT
URL:            https://crates.io/crates/pretty-git-prompt
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
# [dependencies]
BuildRequires:  (crate(clap) >= 2.19.0 with crate(clap) < 3.0.0)
BuildRequires:  (crate(git2) >= 0.7.0 with crate(git2) < 0.8.0)
BuildRequires:  (crate(yaml-rust) >= 0.3.4 with crate(yaml-rust) < 0.4.0)

%description
%{summary}.

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate}
%{summary}.

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
# https://github.com/tomastomecek/pretty-git-prompt/issues/35
%cargo_test || :
%endif

%files       -n %{crate}
%license LICENSE
%doc README.md
%doc files
%{_bindir}/pretty-git-prompt

%changelog
* Mon Apr 06 2020 Tomas Tomecek <ttomecek@redhat.com> - 0.2.1-1
- new upstream release: 0.2.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 10 2018 Josh Stone <jistone@redhat.com> - 0.2.0-6
- Rebuild with fixed rust-libgit2-sys-0.7.7

* Fri Aug 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-5
- Rebuild for libgit2 0.27.x

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-3
- Bump git2 to 0.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-1
- Initial package
