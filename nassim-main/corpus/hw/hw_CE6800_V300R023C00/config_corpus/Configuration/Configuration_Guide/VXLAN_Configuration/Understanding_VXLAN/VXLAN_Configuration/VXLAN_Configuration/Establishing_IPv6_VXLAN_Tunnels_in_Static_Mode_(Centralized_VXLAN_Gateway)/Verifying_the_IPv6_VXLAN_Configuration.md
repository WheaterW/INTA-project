Verifying the IPv6 VXLAN Configuration
======================================

Verifying the IPv6 VXLAN Configuration

#### Procedure

* Run the [**display bridge-domain**](cmdqueryname=display+bridge-domain) [ **binding-info** | *bd-id* [ **brief** | **verbose** | **binding-info** ] ] command to check BD configurations.
* Run the [**display interface nve**](cmdqueryname=display+interface+nve) [ *nve-number* | **main** ] command to check NVE interface information.
* Run the [**display vxlan peer**](cmdqueryname=display+vxlan+peer) [ **vni** *vni-id* ] command to check the ingress replication lists of all VNIs or a specified VNI.
* Run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) [ *tunnel-id* ] [ **verbose** ] command to check IPv6 VXLAN tunnel information.
* Run the [**display vxlan vni**](cmdqueryname=display+vxlan+vni) [ *vni-id* [ **verbose** ] ] command to check IPv6 VXLAN configurations and the VNI status.
* Run the [**display interface vbdif**](cmdqueryname=display+interface+vbdif) [ *bd-id* | **main** ] command to check VBDIF interface status, configurations, and statistics.