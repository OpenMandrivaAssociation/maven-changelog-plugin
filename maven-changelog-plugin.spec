%{?_javapackages_macros:%_javapackages_macros}
Name:           maven-changelog-plugin
Version:        2.2
Release:        18.1
Summary:        Produce SCM changelog reports
Group:		Development/Java

License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-changelog-plugin/
#svn export http://svn.apache.org/repos/asf/maven/plugins/tags/maven-changelog-plugin-2.2/
#tar jcf maven-changelog-plugin-2.2.tar.bz2 maven-changelog-plugin-2.2/
Source0:        %{name}-%{version}.tar.bz2
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Patch0:         pom.patch
Patch1:         ChangeLog.java.patch

BuildArch: noarch

BuildRequires: java-devel >= 1:1.6.0
BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: maven-plugin-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-site-plugin
BuildRequires: maven-doxia-sink-api
BuildRequires: maven-scm
BuildRequires: plexus-utils
BuildRequires: junit
BuildRequires: maven-plugin-testing-harness
BuildRequires: plexus-containers-container-default

Requires:       maven
Requires:       java
Requires:       jpackage-utils
Requires:       plexus-utils
Requires:       plexus-containers-container-default

Obsoletes: maven2-plugin-changelog <= 0:2.0.8
Provides: maven2-plugin-changelog = 1:%{version}-%{release}

%description
The Maven Changelog Plugin generates reports regarding the recent changes 
in your Software Configuration Management or SCM. These reports include 
the changelog report, developer activity report and the file activity report.

%package javadoc

Summary:        Javadoc for %{name}
Requires:       jpackage-utils

%description javadoc
API documentation for %{name}.


%prep
%setup -q 
%patch0 -p0
%patch1 -p2
cp -p %{SOURCE1} .

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt
%{_javadir}/*

%files javadoc
%doc LICENSE-2.0.txt
%{_javadocdir}/%{name}

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-16
- Drop dependency on plexus-container-default
- Resolves: rhbz#878552

* Wed Mar 20 2013 Michal Srb <msrb@redhat.com> - 2.2-15
- Migrate from maven-doxia to doxia subpackages (Resolves: #909226)

* Mon Feb 18 2013 Tomas Radej <tradej@redhat.com> - 2.2-14
- Removed BR on maven-shared (unnecessary + blocking maven-shared retirement)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.2-12
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Dec 11 2012 Michal Srb <msrb@redhat.com> - 2.2-11
- Migrated to plexus-containers-container-default (Resolves: #878552)
- Added license
- Use add_maven_depmap instead of add_to_maven_depmap

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild


* Tue Feb 21 2012 Jiri Vanek <jvanek@redhat.com> 2.2-9
- Added patch0 pom.patch to remove unused and from-fedora-removed maven cvsjava plugin
  and patch1 ChangeLog.java.patch which is fixing invalid character uncompileable by JDK7
- Added build requires maven-site-plugin to fix one maven warning

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Alexander Kurtakov <akurtako@redhat.com> 2.2-7
- Build with maven 3.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 09 2010 Hui Wang <huwang@redhat.com> - 2.2-5
- Add missing BR netbeans-cvsclient

* Tue Jul 13 2010 Hui Wang <huwang@redhat.com> - 2.2-4
- Add missing requires

* Wed Jun 02 2010 Hui Wang <huwang@redhat.com> - 2.2-3
- Added epoch 1 to provides

* Tue Jun 01 2010 Hui Wang <huwang@redhat.com> - 2.2-2
- Change BR maven2-plugin-plugin to maven2-plugin-plugin
- Fix incoherent version in changelog
- Fix summary and description
- Add provides/obsoletes
- Add missing requires

* Mon May 31 2010 Hui Wang <huwang@redhat.com> - 2.2-1
- Initial version of the package
