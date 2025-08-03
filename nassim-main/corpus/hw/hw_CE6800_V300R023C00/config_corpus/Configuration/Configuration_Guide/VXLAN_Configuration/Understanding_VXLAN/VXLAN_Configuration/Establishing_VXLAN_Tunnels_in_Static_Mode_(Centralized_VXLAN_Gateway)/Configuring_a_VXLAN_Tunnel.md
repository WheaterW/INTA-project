Configuring a VXLAN Tunnel
==========================

Configuring a VXLAN Tunnel

#### Prerequisites

Before configuring a VXLAN tunnel, you have completed the following task:

* Configure IP routes to enable Layer 3 communication between nodes on the current network.
* If the simplified mode is used for configuration, complete [Configuring a BD Profile in Simplified Mode](../vrp/dc_vrp_vxlan_cfg_bdprofile01.html).


#### Context

After you manually configure local and remote VNIs and VTEP IP addresses, a VXLAN tunnel is statically created. This configuration is simple and does not involve protocol configurations.

To ensure successful VXLAN packet forwarding, VXLAN tunnels must be configured on both Layer 2 and Layer 3 VXLAN gateways.


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
   
   If the simplified mode is used for configuration, perform this step to configure BDs in batches by binding a BD range to a BD profile. Steps 3 to 5 are then not required.
3. Enter the BD view.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id
   ```
   
   *bd-id* specified in this command must be the same as *bd-id* in the service access point configuration.
4. Create a VNI and associate the VNI with the BD.
   
   
   ```
   [vxlan vni](cmdqueryname=vxlan+vni) vni-id
   ```
   
   By default, no VNI is created.
5. (Optional) Configure the source VTEP IP address of the VXLAN tunnel.
   
   
   ```
   [vtep-src](cmdqueryname=vtep-src) ip-address
   ```
   
   By default, no source VTEP IP address is configured for a VXLAN tunnel in a BD, meaning that a VXLAN tunnel uses the source IP address configured on an NVE interface as the source VTEP IP address. Perform this step if you want to establish VXLAN tunnels over different physical paths between VTEPs to carry service data for traffic optimization. After this step is performed, services in the specified BD will use the VXLAN tunnel whose source VTEP IP address is configured in this step. Services in other BDs will continue to use the VXLAN tunnel whose source VTEP IP address is the source IP address configured on an NVE interface.
6. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. (Optional) Enable subscription to the status of the exact route to the VXLAN tunnel destination. The VXLAN tunnel can go up only when the exact route to its destination IP address is reachable.
   
   
   ```
   [vxlan tunnel-status track exact-route](cmdqueryname=vxlan+tunnel-status+track+exact-route)
   ```
   
   By default, subscription to the status of the exact route to a VXLAN tunnel destination is disabled. A VXLAN tunnel is considered up if the exact route of its source IP address and the route of the network segment where its destination IP address resides are reachable.
8. (Optional) Enable the device to use the extension mode when encapsulating the outer UDP source port number into VXLAN packets.
   
   
   ```
   [assign forward nvo3 udp src-port extend enable](cmdqueryname=assign+forward+nvo3+udp+src-port+extend+enable)
   ```
   
   By default, the device does not use the extension mode when encapsulating the outer UDP source port number into VXLAN packets.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   This command is supported only by the following: CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K.
9. Create an NVE interface and enter its view.
   
   
   ```
   [interface nve](cmdqueryname=interface+nve) nve-number
   ```
   
   By default, no NVE interface is created.
10. Configure an IP address for the source VTEP.
    
    
    ```
    [source](cmdqueryname=source) ip-address
    ```
    
    By default, no IP address is configured for a source VTEP.
    
    Either a physical interface's IP address or loopback interface address can be specified for a source VTEP. Using the loopback interface address as the source VTEP's IP address is recommended.
11. Configure an ingress replication list.
    
    
    ```
    [vni](cmdqueryname=vni) vni-id head-end peer-list ip-address &<1-10>
    ```
    
    By default, no ingress replication list is configured.
    
    After receiving a BUM packet, the ingress of a VXLAN tunnel replicates the packet and sends a copy to each VTEP in the ingress replication list. The ingress replication list is a collection of remote VTEP IP addresses to which the ingress of a VXLAN tunnel should send replicated BUM packets.
12. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```