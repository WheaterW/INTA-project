Clearing VXLAN Packet Statistics
================================

This section describes how to clear VXLAN packet statistics in a BD, VXLAN packet statistics collected per VNI, or per VNI and VXLAN tunnel.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Packet statistics cannot be restored after they are cleared. Exercise caution when running the reset commands.



#### Procedure

* Run the [**reset bridge-domain**](cmdqueryname=reset+bridge-domain) *bd-id* **statistics** command in the user view to delete packet statistics in a specified BD.
* Run the [**reset vxlan statistics**](cmdqueryname=reset+vxlan+statistics) **vni** *vni-id* command in the user view to delete VXLAN packet statistics collected per VNI.
* Run the [**reset vxlan statistics**](cmdqueryname=reset+vxlan+statistics) **source** *source-ip* **peer** *peer-ip* **vni** *vni-id* command in the user view to delete packet statistics collected per VNI and VXLAN tunnel.
* Run the [**reset vxlan statistics**](cmdqueryname=reset+vxlan+statistics) **source** *source-ipv6* **peer** *peer-ipv6* **vni** *vni-val* command in the user view to delete VNI- and IPv6 VXLAN tunnel-based packet statistics.
* Run the [**reset vxlan statistics**](cmdqueryname=reset+vxlan+statistics) **source** *source-ip* **peer** *peer-ip* **local-vni** *local-vni-id* command in the user view to delete uplink VXLAN packet statistics collected based on the local VNI ID.
* Run the [**reset vxlan statistics**](cmdqueryname=reset+vxlan+statistics) **source** *source-ipv6* **peer** *peer-ipv6* **local-vni** *vni-val* command in the user view to delete uplink IPv6 VXLAN packet statistics collected based on the local VNI ID.
* Run the [**reset vxlan statistics**](cmdqueryname=reset+vxlan+statistics) **source** *source-ip* **peer** *peer-ip* **remote-vni** *remote-vni-id* command in the user view to delete downstream VXLAN packet statistics collected based on the remote VNI ID.
* Run the [**reset vxlan statistics**](cmdqueryname=reset+vxlan+statistics) **source** *source-ipv6* **peer** *peer-ipv6* **remote-vni** *vni-val* command in the user view to delete downlink IPv6 VXLAN packet statistics collected based on the peer VNI ID.
* Run the [**reset vxlan statistics l3-mode**](cmdqueryname=reset+vxlan+statistics+l3-mode) **source** *source-ip* **peer** *peer-ip* **local-vni** *vni-id* command in the user view to delete Layer 3 upstream packet statistics collected per VNI and VXLAN tunnel.
* Run the [**reset vxlan statistics l3-mode**](cmdqueryname=reset+vxlan+statistics+l3-mode) **source** *source-ipv6* **peer** *peer-ipv6* **local-vni** *vni-val* command in the user view to delete VNI- and IPv6 VXLAN tunnel-based Layer 3 uplink traffic statistics.
* Run the [**reset vxlan statistics l3-mode**](cmdqueryname=reset+vxlan+statistics+l3-mode) **source** *source-ip* **peer** *peer-ip* **remote-vni** *vni-id* command in the user view to delete Layer 3 downstream packet statistics collected per VNI and VXLAN tunnel.
* Run the [**reset vxlan statistics l3-mode**](cmdqueryname=reset+vxlan+statistics+l3-mode) **source** *source-ipv6* **peer** *peer-ipv6* **remote-vni** *vni-val* command in the user view to delete VNI- and IPv6 VXLAN tunnel-based Layer 3 downlink traffic statistics.