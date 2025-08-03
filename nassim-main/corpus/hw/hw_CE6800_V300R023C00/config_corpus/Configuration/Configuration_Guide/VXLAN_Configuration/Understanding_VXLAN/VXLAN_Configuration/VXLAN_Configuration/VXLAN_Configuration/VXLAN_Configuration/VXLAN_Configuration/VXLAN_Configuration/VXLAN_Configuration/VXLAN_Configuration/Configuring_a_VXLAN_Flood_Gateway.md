Configuring a VXLAN Flood Gateway
=================================

Configuring a VXLAN Flood Gateway

#### Prerequisites

Before configuring a VXLAN flood gateway, you have completed the following tasks:

* [Establishing VXLAN Tunnels in Static Mode (Centralized VXLAN Gateway)](dc_vrp_vxlan_cfg_1039.html)
* [Establishing VXLAN Tunnels in BGP EVPN Mode (Centralized VXLAN Gateway)](dc_vrp_vxlan_cfg_1072.html)
* [Establishing VXLAN Tunnels in BGP EVPN Mode (Distributed VXLAN Gateway)](dc_vrp_vxlan_cfg_1066.html)

#### Context

On a VXLAN network, if a source VTEP corresponds to multiple remote VTEPs, the [**vni head-end peer-list**](cmdqueryname=vni+head-end+peer-list) command needs to be run to specify the remote VTEPs. When the source VTEP sends a BUM packet in ingress replication mode, it needs to send a copy to each remote VTEP. This causes the packet to be flooded and increases the network load. You can configure a flood gateway to prevent this issue. After a flood proxy IP address is configured on a VXLAN gateway, the gateway functions as the centralized replicator. When the source VTEP receives a BUM packet, it only needs to send one copy to the centralized replicator, which then sends the packet to each remote VTEP, reducing flooded traffic on the network.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the NVE interface view.
   
   
   ```
   [interface](cmdqueryname=interface) nve nve-number
   ```
3. Configure centralized replication.
   
   
   ```
   [vni](cmdqueryname=vni) vni-id flood-vtep { ip-address } &<1-10>
   ```
   
   By default, centralized replication is disabled. The IP address specified in this command should be the flood proxy IP address of the centralized replicator.
   
   Centralized replication takes precedence over ingress replication. If both replication modes are configured (using the [**vni flood-vtep**](cmdqueryname=vni+flood-vtep) and [**vni head-end peer-list**](cmdqueryname=vni+head-end+peer-list) commands) on a device, a VXLAN tunnel works in centralized replication mode.
4. Configure a flood proxy IP address.
   
   
   ```
   [flood proxy](cmdqueryname=flood+proxy) ip-address
   ```
   
   By default, no flood proxy IP address is configured. The flood proxy IP address must be the same as the address specified when you enable the centralized replication function.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   Generally, the loopback interface IP address is configured as the flood proxy IP address, and it is different from the source IP address of the NVE interface of the VTEP.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display vxlan flood-vtep**](cmdqueryname=display+vxlan+flood-vtep) [ **vni** *vni-id* ] command to check the VXLAN centralized replication list.