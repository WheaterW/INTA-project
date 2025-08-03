Enabling Multicast Replication for BUM Packets
==============================================

Enabling Multicast Replication for BUM Packets

#### Prerequisites

Before enabling multicast replication for BUM packets, you have completed one of the following tasks:

* [Establishing VXLAN Tunnels in Static Mode (Centralized VXLAN Gateway)](../dc/dc_vrp_vxlan_cfg_1039.html)
* [Establishing VXLAN Tunnels in BGP EVPN Mode (Centralized VXLAN Gateway)](../dc/dc_vrp_vxlan_cfg_1072.html)
* [Establishing VXLAN Tunnels in BGP EVPN Mode (Distributed VXLAN Gateway)](../dc/dc_vrp_vxlan_cfg_1066.html)

In addition, PIM has been configured on each node of the VXLAN network (PIM-SM needs to be enabled on the directly connected physical interface on the VXLAN tunnel side).


#### Context

After multicast replication is enabled, you can still run the [**vni**](cmdqueryname=vni) *vni-id* **head-end peer-list** command to generate a remote VTEP address list for VXLAN tunnel establishment. BUM packets, however, use multicast replication instead of ingress replication.

![](../public_sys-resources/note_3.0-en-us.png) 

* Multicast replication and centralized replication cannot be configured together for BUM packets.
* Multicast replication of BUM packets is supported only on IPv4 over IPv4 and IPv6 over IPv4 networks.

Perform this task on all nodes where VTEPs reside.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the NVE interface view.
   
   
   ```
   [interface](cmdqueryname=interface) nve nve-number
   ```
3. Enable multicast replication for BUM packets and configure a multicast replication address for a specified VNI.
   
   
   ```
   [vni](cmdqueryname=vni) vni-id mcast-group ip-address
   ```
   
   By default, multicast replication is disabled.
   
   *ip-address* specifies the multicast replication address for the current VNI, that is, the address of the multicast group that all VTEPs join.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```