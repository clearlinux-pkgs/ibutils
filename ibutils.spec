#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ibutils
Version  : 1.5.7
Release  : 1
URL      : https://www.openfabrics.org/downloads/ibutils/ibutils-1.5.7-0.2.gbd7e502.tar.gz
Source0  : https://www.openfabrics.org/downloads/ibutils/ibutils-1.5.7-0.2.gbd7e502.tar.gz
Summary  : OpenIB Mellanox InfiniBand Diagnostic Tools
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0 GPL-3.0
Requires: ibutils-bin
Requires: ibutils-lib
Requires: ibutils-data
Requires: ibutils-doc
BuildRequires : bison
BuildRequires : flex
BuildRequires : libibumad-dev
BuildRequires : opensm-dev
BuildRequires : tcl

%description
ibutils provides IB network and path diagnostics.

%package bin
Summary: bin components for the ibutils package.
Group: Binaries
Requires: ibutils-data

%description bin
bin components for the ibutils package.


%package data
Summary: data components for the ibutils package.
Group: Data

%description data
data components for the ibutils package.


%package dev
Summary: dev components for the ibutils package.
Group: Development
Requires: ibutils-lib
Requires: ibutils-bin
Requires: ibutils-data
Provides: ibutils-devel

%description dev
dev components for the ibutils package.


%package doc
Summary: doc components for the ibutils package.
Group: Documentation

%description doc
doc components for the ibutils package.


%package lib
Summary: lib components for the ibutils package.
Group: Libraries
Requires: ibutils-data

%description lib
lib components for the ibutils package.


%prep
%setup -q -n ibutils-1.5.7

%build
%configure --disable-static --enable-ibmgtsim \
--with-tk-lib=/usr/lib/tk8.6
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/ibdiagnet1.5.7/git_version.tcl
/usr/lib64/ibdiagnet1.5.7/ibdebug.tcl
/usr/lib64/ibdiagnet1.5.7/ibdebug_if.tcl
/usr/lib64/ibdiagnet1.5.7/ibdiagnet.tcl
/usr/lib64/ibdiagnet1.5.7/pkgIndex.tcl
/usr/lib64/ibdiagpath1.5.7/git_version.tcl
/usr/lib64/ibdiagpath1.5.7/ibdebug.tcl
/usr/lib64/ibdiagpath1.5.7/ibdebug_if.tcl
/usr/lib64/ibdiagpath1.5.7/ibdiagpath.tcl
/usr/lib64/ibdiagpath1.5.7/pkgIndex.tcl
/usr/lib64/ibdiagui1.5.7/git_version.tcl
/usr/lib64/ibdiagui1.5.7/ibdebug.tcl
/usr/lib64/ibdiagui1.5.7/ibdebug_if.tcl
/usr/lib64/ibdiagui1.5.7/ibdiagui.tcl
/usr/lib64/ibdiagui1.5.7/pkgIndex.tcl
/usr/lib64/ibdm1.5.7/ibnl/Buffalo.ibnl
/usr/lib64/ibdm1.5.7/ibnl/Buffalo8.topo
/usr/lib64/ibdm1.5.7/ibnl/Cheetah.ibnl
/usr/lib64/ibdm1.5.7/ibnl/Cougar.ibnl
/usr/lib64/ibdm1.5.7/ibnl/Eagle.ibnl
/usr/lib64/ibdm1.5.7/ibnl/FullGnu.topo
/usr/lib64/ibdm1.5.7/ibnl/Gazelle.ibnl
/usr/lib64/ibdm1.5.7/ibnl/Gnu.ibnl
/usr/lib64/ibdm1.5.7/ibnl/IS4_NATIVE.ibnl
/usr/lib64/ibdm1.5.7/ibnl/IS5100.ibnl
/usr/lib64/ibdm1.5.7/ibnl/IS5200.ibnl
/usr/lib64/ibdm1.5.7/ibnl/IS5300.ibnl
/usr/lib64/ibdm1.5.7/ibnl/Lion.ibnl
/usr/lib64/ibdm1.5.7/ibnl/LionMini.ibnl
/usr/lib64/ibdm1.5.7/ibnl/MIS5600.ibnl
/usr/lib64/ibdm1.5.7/ibnl/MTS14400-48.ibnl
/usr/lib64/ibdm1.5.7/ibnl/MTS14400-DDR.ibnl
/usr/lib64/ibdm1.5.7/ibnl/MTS14400-IntraDDR.ibnl
/usr/lib64/ibdm1.5.7/ibnl/MTS14400.ibnl
/usr/lib64/ibdm1.5.7/ibnl/MTS2400-12T4.ibnl
/usr/lib64/ibdm1.5.7/ibnl/MTS2400-24.ibnl
/usr/lib64/ibdm1.5.7/ibnl/MTS3600.ibnl
/usr/lib64/ibdm1.5.7/ibnl/MTS3610.ibnl
/usr/lib64/ibdm1.5.7/ibnl/PartialGazelle.topo
/usr/lib64/ibdm1.5.7/ibnl/RhinoBased512.lst
/usr/lib64/ibdm1.5.7/ibnl/RhinoBased512.no_sp2-3.lst
/usr/lib64/ibdm1.5.7/ibnl/RhinoBased512.topo
/usr/lib64/ibdm1.5.7/ibnl/SUNBQNEM48.ibnl
/usr/lib64/ibdm1.5.7/ibnl/SUNDCS36QDR.ibnl
/usr/lib64/ibdm1.5.7/ibnl/SUNDCS648QDR.ibnl
/usr/lib64/ibdm1.5.7/ibnl/SUNDCS72QDR.ibnl
/usr/lib64/ibdm1.5.7/ibnl/SingleGazelle.topo
/usr/lib64/ibdm1.5.7/ibnl/SingleRhino.topo
/usr/lib64/ibdm1.5.7/ibnl/subnet.lst
/usr/lib64/ibdm1.5.7/pkgIndex.tcl
/usr/lib64/ibis1.5.7/pkgIndex.tcl

%files bin
%defattr(-,root,root,-)
/usr/bin/IBMgtSim
/usr/bin/RunSimTest
/usr/bin/dump2psl.pl
/usr/bin/dump2slvl.pl
/usr/bin/git_version.tcl
/usr/bin/ibdiagnet
/usr/bin/ibdiagpath
/usr/bin/ibdiagui
/usr/bin/ibdmchk
/usr/bin/ibdmsh
/usr/bin/ibdmtr
/usr/bin/ibis
/usr/bin/ibmsquit
/usr/bin/ibmssh
/usr/bin/ibnlparse
/usr/bin/ibtopodiff
/usr/bin/mkSimNodeDir

%files data
%defattr(-,root,root,-)
/usr/share/ibmgtsim/12-ary-2-tree.topo
/usr/share/ibmgtsim/12-node-spaced.topo
/usr/share/ibmgtsim/2-ary-4-tree.topo
/usr/share/ibmgtsim/32nodes-3lvl-is1-cbb2-2st.topo
/usr/share/ibmgtsim/32nodes-3lvl-is1-cbb2.topo
/usr/share/ibmgtsim/32nodes-3lvl-is1.topo
/usr/share/ibmgtsim/4-ary-2-tree-diff-num-pgroups.topo
/usr/share/ibmgtsim/4-ary-2-tree-links-at-same-rank-1.topo
/usr/share/ibmgtsim/4-ary-2-tree-links-at-same-rank-2.topo
/usr/share/ibmgtsim/4-ary-2-tree-missing-sw-link.topo
/usr/share/ibmgtsim/4-ary-2-tree.topo
/usr/share/ibmgtsim/4-ary-3-tree.topo
/usr/share/ibmgtsim/4-ary-4-tree.topo
/usr/share/ibmgtsim/FatTree.check.tcl
/usr/share/ibmgtsim/FatTree.sim.tcl
/usr/share/ibmgtsim/FatTreeFails.check.tcl
/usr/share/ibmgtsim/FullGnu.topo
/usr/share/ibmgtsim/IS1-16.topo
/usr/share/ibmgtsim/IS3-128.topo
/usr/share/ibmgtsim/IS3-loop.topo
/usr/share/ibmgtsim/OsmTest.check.tcl
/usr/share/ibmgtsim/OsmTest.sim.tcl
/usr/share/ibmgtsim/RhinoBased10K.topo
/usr/share/ibmgtsim/RhinoBased512Nodes.topo
/usr/share/ibmgtsim/RhinoDDR.topo
/usr/share/ibmgtsim/RhinoReindeer1100.topo
/usr/share/ibmgtsim/blend-4-ary-2-tree.topo
/usr/share/ibmgtsim/discover.check.tcl
/usr/share/ibmgtsim/discover.sim.tcl
/usr/share/ibmgtsim/duplicateGuid.sim.tcl
/usr/share/ibmgtsim/gnu-stallion-64.topo
/usr/share/ibmgtsim/half-4-ary-3-tree.topo
/usr/share/ibmgtsim/ibdiag-drops.sim.tcl
/usr/share/ibmgtsim/ibdiag-dup-both-guids.sim.tcl
/usr/share/ibmgtsim/ibdiag-dup-node-guid.sim.tcl
/usr/share/ibmgtsim/ibdiag-dup-port-guid.sim.tcl
/usr/share/ibmgtsim/ibdiag-lid.sim.tcl
/usr/share/ibmgtsim/ibdiag-mcast.sim.tcl
/usr/share/ibmgtsim/ibdiag-ucast.sim.tcl
/usr/share/ibmgtsim/ibdiagnet.check.tcl
/usr/share/ibmgtsim/merge-2-ary-4-tree.topo
/usr/share/ibmgtsim/merge-root-12-ary-2-tree.topo
/usr/share/ibmgtsim/merge-root-4-ary-3-tree.topo
/usr/share/ibmgtsim/merge-roots-4-ary-2-tree.topo
/usr/share/ibmgtsim/merge-roots-reorder-4-ary-2-tree.topo
/usr/share/ibmgtsim/osm-dup-local-port-guid.sim.tcl
/usr/share/ibmgtsim/osm-join-leave.check.tcl
/usr/share/ibmgtsim/osm-join-leave.sim.tcl
/usr/share/ibmgtsim/osmLidAssignment.check.tcl
/usr/share/ibmgtsim/osmLidAssignment.sim.tcl
/usr/share/ibmgtsim/osmMulticast.sim.tcl
/usr/share/ibmgtsim/osmMulticastRoutingTest.check.tcl
/usr/share/ibmgtsim/osmMulticastRoutingTest.sim.tcl
/usr/share/ibmgtsim/osmStability.check.tcl
/usr/share/ibmgtsim/osmStability.sim.tcl
/usr/share/ibmgtsim/osmStress.check.tcl
/usr/share/ibmgtsim/osmStress.sim.tcl
/usr/share/ibmgtsim/osm_no_quit.check.tcl
/usr/share/ibmgtsim/osm_no_quit.sim.tcl
/usr/share/ibmgtsim/part-4-ary-3-tree.topo
/usr/share/ibmgtsim/pkey.check.tcl
/usr/share/ibmgtsim/pkey.sim.tcl

%files dev
%defattr(-,root,root,-)
/usr/include/ibdm/Bipartite.h
/usr/include/ibdm/Congestion.h
/usr/include/ibdm/CredLoops.h
/usr/include/ibdm/Fabric.h
/usr/include/ibdm/Regexp.h
/usr/include/ibdm/RouteSys.h
/usr/include/ibdm/SubnMgt.h
/usr/include/ibdm/SysDef.h
/usr/include/ibdm/TopoMatch.h
/usr/include/ibdm/TraceRoute.h
/usr/include/ibdm/git_version.h
/usr/include/ibdm/ibdm.i
/usr/include/ibdm/ibnl_parser.h
/usr/include/ibdm/ibsysapi.h
/usr/include/ibmgtsim/dispatcher.h
/usr/include/ibmgtsim/git_version.h
/usr/include/ibmgtsim/helper.h
/usr/include/ibmgtsim/ib_types_extend.h
/usr/include/ibmgtsim/ibms_client_api.h
/usr/include/ibmgtsim/msgmgr.h
/usr/include/ibmgtsim/node.h
/usr/include/ibmgtsim/pma.h
/usr/include/ibmgtsim/randmgr.h
/usr/include/ibmgtsim/server.h
/usr/include/ibmgtsim/sim.h
/usr/include/ibmgtsim/simmsg.h
/usr/include/ibmgtsim/sma.h
/usr/include/ibmgtsim/tcpcomm.h
/usr/include/ibmgtsim/vsa.h
/usr/lib64/*.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
/usr/lib64/ibdm1.5.7/libibdm.so.1.5.7
/usr/lib64/ibis1.5.7/libibis.so.1.5.7
