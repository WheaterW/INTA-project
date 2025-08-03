Verifying the Configuration of Multicast Replication for BUM Packets
====================================================================

Verifying the Configuration of Multicast Replication for BUM Packets

#### Procedure

* Run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) command to check VXLAN tunnel information, including the VXLAN tunnel whose destination address is the multicast replication address.
* Run the [**display vxlan vni**](cmdqueryname=display+vxlan+vni) *vni* **verbose** command to check the detailed VXLAN configuration of a specified VNI. In the command output, **BUM Mode** is **multicast replication**.