%{?nodejs_find_provides_and_requires}

Name:           nodejs-mock-fs
Version:        4.12.0
Release:        1
Summary:        A configurable mock file system

License:        MIT
URL:            https://www.npmjs.com/package/mock-fs
Source0:        https://github.com/tschaub/mock-fs/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(chai)
BuildRequires:  npm(semver)


%description
The mock-fs module allows Node's built-in fs module to be backed
temporarily by an in-memory, mock file system. This lets you run
tests against a set of mock files and directories instead of lugging
around a bunch of test fixtures.


%prep
%autosetup -p 1 -n mock-fs-%{version}
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/mock-fs
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/mock-fs
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha --recursive test


%files
%doc readme.md changelog.md
%license license.md
%{nodejs_sitelib}/mock-fs


%changelog
* Thu Dec 31 2020 Ge Wang <wangge20@huawei.com> - 4.12.0-1
- Update to 4.12.0

* Thu Aug 20 2020 Ge Wang <wangge20@huawei.com> - 4.8.0-1
- Package init
