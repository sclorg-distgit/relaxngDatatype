%global pkg_name relaxngDatatype
%{?scl:%scl_package %{pkg_name}}
%{?java_common_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.0
Release:        11.11%{?dist}
Summary:        RELAX NG Datatype API
License:        BSD
URL:            https://sourceforge.net/projects/relaxng
# wget http://netcologne.dl.sourceforge.net/project/relaxng/datatype%20%28java%29/Ver.%{version}/%{pkg_name}-%{version}.zip
Source0:        http://netcologne.dl.sourceforge.net/project/relaxng/datatype%20%28java%29/Ver.%{version}/%{pkg_name}-%{version}.zip
Source1:        http://repo1.maven.org/maven2/%{pkg_name}/%{pkg_name}/20020414/%{pkg_name}-20020414.pom
Patch0:         %{pkg_name}-compressjar.patch

BuildArch:      noarch
BuildRequires:  %{?scl_prefix}javapackages-tools
BuildRequires:  %{?scl_prefix}ant >= 0:1.6

%description
RELAX NG is a public space for test cases and other ancillary software
related to the construction of the RELAX NG language and its
implementations.

%package        javadoc
Summary:        API documentation for %{pkg_name}

%description    javadoc
This package provides %{pkg_name}.

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%patch0 -p0
sed -i s/// copying.txt doc/stylesheet.css
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
set -e -x
ant -Dbuild.sysclasspath=only
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
set -e -x
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 644 %{pkg_name}.jar $RPM_BUILD_ROOT%{_javadir}/

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{pkg_name}.pom
%add_maven_depmap

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}
%{?scl:EOF}

%files -f .mfiles
%doc copying.txt

%files javadoc
%doc copying.txt
%doc %{_javadocdir}/%{name}

%changelog
* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.0-11.11
- Mass rebuild 2015-01-13

* Fri Jan 09 2015 Michal Srb <msrb@redhat.com> - 1.0-11.10
- Mass rebuild 2015-01-09

* Tue Dec 16 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-11.9
- Migrate requires and build-requires to rh-java-common

* Mon Dec 15 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-11.8
- Mass rebuild 2014-12-15

* Mon Dec 15 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-11.7
- Rebuild for rh-java-common collection

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-11.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-11.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-11.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-11.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-11.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-11.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0-11
- Mass rebuild 2013-12-27

* Fri Jul 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-10.7
- Remove workaround for rpm bug #646523

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-10.6
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Fri Jun 21 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-10.5
- Install license file with javadoc package
- Convert versioned javadoc to versionless
- Update to current packaging guidelines
- Remove msv provides and obsoletes

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 12 2012 Michal Srb <msrb@redhat.com> - 1.0-9.4
- Source0 is now URL (Resolves: #875884)

* Fri Nov  2 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-8.4
- Add maven POM

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Mar  8 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.0-5.3
- Added missing Requires: jpackage-utils (%%{_javadir} and %%{_javadocdir})

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0-3.2
- drop repotag

* Mon Feb 12 2007 Andrew Overholt <overholt@redhat.com> 1.0-3jpp.1
- Fixed issues for Fedora-ization
- Add patch to compress the main jar

* Tue Apr 11 2006 Ralph Apel <r.apel@r-apel.de>- 0:1.0-3jpp
- First JPP-1.7 release

* Wed Aug 25 2004 Fernando Nasser <fnasser@redhat.com>- 0:1.0-2jpp
- Require Ant > 1.6
- Rebuild with Ant 1.6.2

* Tue Jul 06 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.0-1jpp
- First JPackage build from sources

