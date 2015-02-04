Summary: Alice Token Authorization Acc plugin
Name: xrootd-alicetokenacc
Version: 1.3.0
Release: 1.dpmmgr
License: none
Group: CERN IT-DSS-TD

Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

AutoReqProv: no
Requires: xrootd-server >= 4.1.0
BuildRequires: xrootd-private-devel >= 4.1.0
BuildRequires: xrootd-devel >= 4.1.0
BuildRequires: xrootd-server-devel >= 4.1.0

#Requires: tokenauthz >= 1.1.8


%description
An authorization plugin for xrootd using the Alice Token authorization envelope.

%prep
%setup -q

%build
./configure --prefix=/usr --libdir=/usr/lib64 --includedir=/usr/include
make 
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/grid-security/xrootd/
cp -av .authz/xrootd/* $RPM_BUILD_ROOT/etc/grid-security/xrootd
cp -av /usr/lib64/libTokenAuthz.so.1 $RPM_BUILD_ROOT/usr/lib64/
cp -av /usr/lib64/libTokenAuthz.so.1.0.0 $RPM_BUILD_ROOT/usr/lib64/

find $RPM_BUILD_ROOT \( -type f -o -type l \) -print \
    | sed "s#^$RPM_BUILD_ROOT/*#/#" > RPM-FILE-LIST

%clean
rm -rf $RPM_BUILD_ROOT


%files -f RPM-FILE-LIST
%defattr(-,root,root,-)
%attr(644, dpmmgr, dpmmgr) /etc/grid-security/xrootd/TkAuthz.Authorization
%attr(400, dpmmgr, dpmmgr) /etc/grid-security/xrootd/privkey.pem
%attr(400, dpmmgr, dpmmgr) /etc/grid-security/xrootd/pubkey.pem
%doc


%changelog
* Fri Aug 22 2008 root <root@pcitsmd01.cern.ch> - alicetokenacc-1
- Initial build.

