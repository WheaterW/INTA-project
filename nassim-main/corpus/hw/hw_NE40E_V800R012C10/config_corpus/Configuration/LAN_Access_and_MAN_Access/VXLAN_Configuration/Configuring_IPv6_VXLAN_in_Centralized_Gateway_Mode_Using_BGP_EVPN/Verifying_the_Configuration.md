Verifying the Configuration
===========================

After configuring IPv6 VXLAN in centralized gateway mode using BGP EVPN, verify information about the IPv6 VXLAN tunnels, VNI status, and VBDIF interfaces.

#### Prerequisites

IPv6 VXLAN in centralized gateway mode has been configured using BGP EVPN.


#### Procedure

* Run the [**display bridge-domain**](cmdqueryname=display+bridge-domain) [ **binding-info** | [ *bd-id* [ **brief** | **verbose** | **binding-info** ] ] ] command to check BD configurations.
* Run the [**display interface nve**](cmdqueryname=display+interface+nve) [ *nve-number* | **main** ] command to check NVE interface information.
* Run the [**display evpn vpn-instance**](cmdqueryname=display+evpn+vpn-instance) command to check EVPN instance information.
* Run the [**display bgp**](cmdqueryname=display+bgp) **evpn peer** [ [ *ipv6-address* ] **verbose** ] command to check information about BGP EVPN peers.
* Run the [**display vxlan peer**](cmdqueryname=display+vxlan+peer) [ **vni** *vni-id* ] command to check the ingress replication lists of all VNIs or a specified one.
* Run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) [ *tunnel-id* ] [ **verbose** ] command to check IPv6 VXLAN tunnel information.
* Run the [**display vxlan vni**](cmdqueryname=display+vxlan+vni) [ *vni-id* [ **verbose** ] ] command to check IPv6 VXLAN configurations and the VNI status.