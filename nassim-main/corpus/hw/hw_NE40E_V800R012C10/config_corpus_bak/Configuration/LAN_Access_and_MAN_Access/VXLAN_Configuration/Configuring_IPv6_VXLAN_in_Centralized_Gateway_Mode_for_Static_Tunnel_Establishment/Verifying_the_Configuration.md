Verifying the Configuration
===========================

After configuring IPv6 VXLAN in centralized gateway mode for static tunnel establishment, check IPv6 VXLAN tunnel, VNI, and VBDIF interface information.

#### Prerequisites

IPv6 VXLAN in centralized gateway mode has been configured for static tunnel establishment.


#### Procedure

* Run the [**display bridge-domain**](cmdqueryname=display+bridge-domain) [ **binding-info** | [ *bd-id* [ **brief** | **verbose** | **binding-info** ] ] ] command to check BD configurations.
* Run the [**display interface nve**](cmdqueryname=display+interface+nve) [ *nve-number* | **main** ] command to check NVE interface information.
* Run the [**display vxlan peer**](cmdqueryname=display+vxlan+peer) [ **vni** *vni-id* ] command to check IPv6 ingress replication lists of a VNI or all VNIs.
* Run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) [ *tunnel-id* ] [ **verbose** ] command to check IPv6 VXLAN tunnel information.
* Run the [**display vxlan vni**](cmdqueryname=display+vxlan+vni) [ *vni-id* [ **verbose** ] ] command to check IPv6 VXLAN configurations and the VNI status.