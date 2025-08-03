Configuring an IPv6 VXLAN Tunnel
================================

Configuring an IPv6 VXLAN Tunnel

#### Prerequisites

Before configuring an IPv6 VXLAN tunnel, you have completed the following task:

* Configure IPv6 routes to enable Layer 3 communication between nodes on the current network.
* If the simplified mode is used for configuration, complete [Configuring a BD Profile in Simplified Mode](../vrp/dc_vrp_vxlan_cfg_bdprofile01.html).


#### Context

After you manually configure local and remote VNIs and VTEP IPv6 addresses, an IPv6 VXLAN tunnel is statically created. This configuration is simple and does not involve protocol configurations.

To ensure the proper forwarding of IPv6 VXLAN packets, IPv6 VXLAN tunnels must be configured on both Layer 2 and Layer 3 gateways.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Configure BDs in batches.
   
   
   ```
   [bridge-domain range](cmdqueryname=bridge-domain+range) { bdIdBgn [ to bdIdEnd ] } &<1-10>
   [binding bridge-domain profile](cmdqueryname=binding+bridge-domain+profile) profileId
   ```
   
   If the simplified mode is used for configuration, perform this step to configure BDs in batches by binding a BD range to a BD profile. Steps 3 and 4 are then not required.
3. Enter the BD view.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id
   ```
   
   *bd-id* specified in this command must be the same as *bd-id* specified in Step 2 in the service access point configuration.
4. Create a VNI and associate the VNI with the BD.
   
   
   ```
   [vxlan vni](cmdqueryname=vxlan+vni) vni-id
   ```
   
   By default, no VNI is created.
5. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. (Optional) Enable subscription to the status of the exact route to the IPv6 VXLAN tunnel destination. The VXLAN tunnel can go up only when the exact route to its destination IPv6 address is reachable.
   
   
   ```
   [vxlan tunnel-status track exact-route](cmdqueryname=vxlan+tunnel-status+track+exact-route)
   ```
   
   By default, subscription to the status of the exact route to an IPv6 VXLAN tunnel destination is disabled. An IPv6 VXLAN tunnel is considered up if the exact route of its source IPv6 address and the route of the network segment where its destination IPv6 address resides are reachable.
7. (Optional) Enable the device to use the extension mode when encapsulating the outer UDP source port number into VXLAN packets.
   
   
   ```
   [assign forward nvo3 udp src-port extend enable](cmdqueryname=assign+forward+nvo3+udp+src-port+extend+enable)
   ```
   
   By default, the device does not use the extension mode when encapsulating the outer UDP source port number into VXLAN packets.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   Only the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, and CE6881H-K support this command.
8. Create an NVE interface and enter its view.
   
   
   ```
   [interface nve](cmdqueryname=interface+nve) nve-number
   ```
   
   By default, no NVE interface is created.
9. Configure an IPv6 address for the source VTEP.
   
   
   ```
   [source](cmdqueryname=source) ipv6-address
   ```
   
   By default, no IPv6 address is configured for a source VTEP.
   
   Either a physical or loopback interface's address can be specified as a source VTEP's IPv6 address. Using the loopback interface's address is recommended.
10. Configure an ingress replication list.
    
    
    ```
    [vni](cmdqueryname=vni) vni-id head-end peer-list ipv6-address &<1-10>
    ```
    
    By default, no ingress replication list is configured.
    
    After receiving a BUM packet, the ingress of a VXLAN tunnel replicates the packet and sends a copy to each VTEP in the ingress replication list. The ingress replication list is a collection of remote VTEP IPv6 addresses to which the ingress of a VXLAN tunnel should send replicated BUM packets.
11. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```