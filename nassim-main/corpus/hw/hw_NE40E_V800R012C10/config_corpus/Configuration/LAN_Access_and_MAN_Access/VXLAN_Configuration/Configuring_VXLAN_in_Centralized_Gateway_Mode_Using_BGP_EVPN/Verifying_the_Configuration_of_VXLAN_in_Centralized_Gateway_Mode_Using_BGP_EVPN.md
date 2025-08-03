Verifying the Configuration of VXLAN in Centralized Gateway Mode Using BGP EVPN
===============================================================================

After configuring VXLAN in centralized gateway mode for dynamic tunnel establishment, check VXLAN tunnel, VNI, and VBDIF interface information.

#### Prerequisites

VXLAN in centralized gateway mode has been configured for dynamic tunnel establishment.


#### Procedure

* Run the [**display bridge-domain**](cmdqueryname=display+bridge-domain) [ **binding-info** | [ *bd-id* [ **brief** | **verbose** | **binding-info** ] ] ] command to check BD configurations.
* Run the [**display interface nve**](cmdqueryname=display+interface+nve) [ *nve-number* | **main** ] command to check NVE interface information.
* Run the [**display bgp**](cmdqueryname=display+bgp) **evpn peer** [ [ *ipv4-address* ] **verbose** ] command to check BGP EVPN peer information.
* Run the [**display vxlan peer**](cmdqueryname=display+vxlan+peer) [ **vni** *vni-id* ] command to check ingress replication lists of a VNI or all VNIs.
* Run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) [ *tunnel-id* ] [ **verbose** ] command to check VXLAN tunnel information.
* Run the [**display vxlan vni**](cmdqueryname=display+vxlan+vni) [ *vni-id* [ **verbose** ] ] command to check VNI information.
* Run the [**display interface vbdif**](cmdqueryname=display+interface+vbdif) [ *bd-id* ] command to check VBDIF interface information and statistics.
* Run the [**display mac-limit bridge-domain**](cmdqueryname=display+mac-limit+bridge-domain) *bd-id* command to check MAC address limiting configurations of a BD.
* Run the [**display bgp**](cmdqueryname=display+bgp) **evpn** **all** **routing-table** command to check EVPN route information.