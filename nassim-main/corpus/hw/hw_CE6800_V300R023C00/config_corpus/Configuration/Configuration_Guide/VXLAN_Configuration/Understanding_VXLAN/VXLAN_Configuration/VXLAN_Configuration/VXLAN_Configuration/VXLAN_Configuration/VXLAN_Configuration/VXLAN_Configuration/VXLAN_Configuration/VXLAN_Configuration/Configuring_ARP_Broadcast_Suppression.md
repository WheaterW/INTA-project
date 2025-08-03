Configuring ARP Broadcast Suppression
=====================================

Configuring ARP Broadcast Suppression

#### Prerequisites

Before configuring ARP broadcast suppression, you have completed one of the following tasks:

* [Establishing VXLAN Tunnels in BGP EVPN Mode (Centralized VXLAN Gateway)](dc_vrp_vxlan_cfg_1072.html)
* [Establishing VXLAN Tunnels in BGP EVPN Mode (Distributed VXLAN Gateway)](dc_vrp_vxlan_cfg_1066.html)


#### Context

When two end tenants communicate with one another for the first time, the initiator sends an ARP request, which is broadcast on the Layer 2 network. If a large number of ARP requests are broadcast, a broadcast storm may occur. To prevent this problem, you can enable ARP broadcast suppression on Layer 2 VXLAN gateways. ![](../public_sys-resources/note_3.0-en-us.png) 

ARP broadcast suppression is supported by IPv4 overlay networks only.



**Figure 1** ARP broadcast suppression networking  
![](figure/en-us_image_0000001176744013.png)

On the network shown in [Figure 1](#EN-US_TASK_0000001176664061__fig_dc_fd_vxlan_001201), the Layer 3 VXLAN gateway dynamically learns the ARP entries of tenants and generates host information (including host IP addresses, MAC addresses, VTEP addresses, and VNIs) based on these ARP entries. The Layer 3 VXLAN gateway then uses BGP EVPN to advertise the host information to BGP peers. Layer 2 VXLAN gateways functioning as BGP peers use the learned host information for ARP broadcast suppression.

When Server1 accesses Server2 for the first time, Server1 broadcasts an ARP request message for Server2's MAC address. The process is as follows:

1. Server1 broadcasts an ARP request for Server2's MAC address.
2. Device1, a Layer 2 VXLAN gateway, receives the ARP request and queries host information.
   * If the host information on Device1 contains Server2 information, Device1 replaces the broadcast destination MAC address and target MAC address in the ARP request with Server2's MAC address, performs VXLAN encapsulation, and forwards the VXLAN packet.
   * If the host information on Device1 does not contain Server2 information, Device1 retains the broadcast destination MAC address in the broadcast ARP request, performs VXLAN encapsulation, and forwards the VXLAN packet.
3. After Device2 (a Layer 2 VXLAN gateway) receives the VXLAN packet, it performs VXLAN decapsulation and obtains the ARP request. Device2 then determines whether the destination MAC address in the ARP request message is a broadcast MAC address.
   * If the destination MAC address is a broadcast MAC address, Device2 broadcasts the ARP request to the non-VXLAN network side in the Layer 2 BD.
   * If the destination MAC address is not a broadcast MAC address, Device2 forwards the ARP request to the destination host.
4. Server2 receives the ARP request and responds with an ARP reply.
5. Server1 receives the ARP reply and generates an ARP entry in the ARP cache. At this point, Server1 can communicate with Server2.

#### Procedure

1. Configure BGP EVPN on Layer 2 and Layer 3 VXLAN gateways to advertise host information.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enter the BGP view or BGP multi-instance view.
      
      
      ```
      [bgp](cmdqueryname=bgp) as-number [ instance instance-name ]
      ```
   3. Enter the BGP-EVPN address family view or BGP multi-instance EVPN address family view.
      
      
      ```
      [l2vpn-family evpn](cmdqueryname=l2vpn-family+evpn)
      ```
   4. Configure ARP route advertisement.
      
      
      ```
      [peer](cmdqueryname=peer) { ipv4-address | group-name } advertise arp
      ```
      
      By default, a device does not advertise ARP routes to its BGP EVPN peers.
2. Enable BGP EVPN on a Layer 3 VXLAN gateway to collect host information.
   1. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   2. Enter the VBDIF interface view.
      
      
      ```
      [interface vbdif](cmdqueryname=interface+vbdif) bd-id
      ```
   3. Enable EVPN BGP to collect host information.
      
      
      ```
      [arp collect host enable](cmdqueryname=arp+collect+host+enable)
      ```
      
      By default, BGP EVPN is disabled from collecting host information.
3. Enable ARP broadcast suppression on a Layer 2 VXLAN gateway.
   1. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   2. Enter the BD view.
      
      
      ```
      [bridge-domain](cmdqueryname=bridge-domain) bd-id
      ```
   3. Enable ARP broadcast suppression.
      
      
      ```
      [arp broadcast-suppress](cmdqueryname=arp+broadcast-suppress) [ mismatch-discard ] enable
      ```
      
      By default, ARP broadcast suppression is disabled.
      
      If **mismatch-discard** is not specified, the device still broadcasts the broadcast packets that do not match any entries in the ARP broadcast suppression table. If **mismatch-discard** is specified, the device discards such broadcast packets.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display arp broadcast-suppress user bridge-domain**](cmdqueryname=display+arp+broadcast-suppress+user+bridge-domain) *bd-id* command to check the ARP broadcast suppression table in a BD.