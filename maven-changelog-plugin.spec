Name:           maven-changelog-plugin
Version:        2.2
Release:        8
Summary:        Produce SCM changelog reports

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-changelog-plugin/
#svn export http://svn.apache.org/repos/asf/maven/plugins/tags/maven-changelog-plugin-2.2/
#tar jcf maven-changelog-plugin-2.2.tar.bz2 maven-changelog-plugin-2.2/
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

BuildRequires: java-devel >= 0:1.6.0
BuildRequires: jpackage-utils
BuildRequires: maven2
BuildRequires: maven-plugin-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-shared
BuildRequires: maven-doxia
BuildRequires: maven-scm
BuildRequires: plexus-utils
BuildRequires: junit
BuildRequires: maven-plugin-testing-harness
BuildRequires: plexus-container-default
BuildRequires: netbeans-cvsclient

Requires:       maven2
Requires:       java
Requires:       jpackage-utils
Requires:       plexus-utils
Requires:       plexus-container-default

Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils

Obsoletes: maven2-plugin-changelog <= 0:2.0.8
Provides: maven2-plugin-changelog = 1:%{version}-%{release}

%description
The Maven Changelog Plugin generates reports regarding the recent changes 
in your Software Configuration Management or SCM. These reports include 
the changelog report, developer activity report and the file activity report.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils

%description javadoc
API documentation for %{name}.


%prep
%setup -q 

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mvn-jpp \
        -e \
        -Dmaven2.jpp.mode=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven.test.skip=true \
        install javadoc:javadoc

%install
rm -rf %{buildroot}

# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}-%{version}.jar

(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; \
    do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

%add_to_maven_depmap org.apache.maven.plugins %{name} %{version} JPP %{name}

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}-%{version}/
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
rm -rf target/site/api*

%post
%update_maven_depmap

%postun
%update_maven_depmap

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

