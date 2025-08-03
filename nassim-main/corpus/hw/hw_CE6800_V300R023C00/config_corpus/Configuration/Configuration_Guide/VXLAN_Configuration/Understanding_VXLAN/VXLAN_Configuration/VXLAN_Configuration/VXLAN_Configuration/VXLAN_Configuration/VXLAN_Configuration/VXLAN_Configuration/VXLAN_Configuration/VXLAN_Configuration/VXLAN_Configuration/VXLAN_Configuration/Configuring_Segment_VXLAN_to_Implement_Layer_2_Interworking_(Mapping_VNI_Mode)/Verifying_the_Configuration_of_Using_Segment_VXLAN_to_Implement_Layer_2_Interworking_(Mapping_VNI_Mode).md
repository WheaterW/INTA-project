Verifying the Configuration of Using Segment VXLAN to Implement Layer 2 Interworking (Mapping VNI Mode)
=======================================================================================================

Verifying the Configuration of Using Segment VXLAN to Implement Layer 2 Interworking (Mapping VNI Mode)

#### Procedure

* Run the [**display bgp evpn peer**](cmdqueryname=display+bgp+evpn+peer) command to check BGP EVPN peer information.
* Run the [**display vxlan peer**](cmdqueryname=display+vxlan+peer) [ **vni** *vni-id* ] command to check the ingress replication lists of all VNIs or a specified VNI.
* Run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) [ *tunnel-id* ] [ **verbose** ] command to check VXLAN tunnel information.
* Run the [**display vxlan vni**](cmdqueryname=display+vxlan+vni) [ *vni-id* [ **verbose** ] ] command to check VXLAN configuration and VNI state information.