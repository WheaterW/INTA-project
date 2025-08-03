Configuring Three-Segment VXLAN to Implement Layer 3 Interworking
=================================================================

The three-segment VXLAN can be configured to enable communications between inter-subnet VMs in DCs that belong to different ASs.

#### Context

As shown in [Figure 1](#EN-US_TASK_0172363812__fig_dc_vrp_vxlan_cfg_108601), BGP EVPN must be configured to create VXLAN tunnels between distributed gateways in each DC and to create VXLAN tunnels between leaf nodes so that the inter-subnet VMs in DC A and DC B can communicate with each other.

When DC A and DC B belong to the same BGP AS, Leaf2 or Leaf3 does not forward EVPN routes received from an IBGP EVPN peer to other IBGP EVPN peers. Therefore, it is necessary to configure Leaf2 and Leaf3 as route reflectors (RRs).

**Figure 1** Network diagram of configuring the three-segment VXLAN tunnels  
![](images/fig_dc_vrp_vxlan_cfg_108601.png)

#### Procedure

1. Configure EVPN within DC A and DC B to establish VXLAN tunnels. For detailed configurations, see [Configuring VXLAN in Distributed Gateway Mode Using BGP EVPN](dc_vrp_vxlan_cfg_1216.html).
2. Configure BGP EVPN on Leaf2 and Leaf3 to establish a VXLAN tunnel between them. For detailed configurations, see [Configuring VXLAN in Distributed Gateway Mode Using BGP EVPN](dc_vrp_vxlan_cfg_1216.html).
3. (Optional) Configure Leaf2 and Leaf3 as RRs. For detailed configurations, see [Configuring a BGP Route Reflector](dc_vrp_bgp_cfg_3034.html).
4. Configure Leaf2 and Leaf3 to advertise routes that are re-originated by the EVPN address family to BGP EVPN peers.
   1. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   2. Run the [**l2vpn-family**](cmdqueryname=l2vpn-family) **evpn** command to enter the BGP-EVPN address family view.
   3. Run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **import** **reoriginate** command to enable the function to re-originate routes received from BGP EVPN peers.
   4. Run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **advertise** **route-reoriginated** **evpn** { **mac-ip** | **ip** | **mac-ipv6** | **ipv6** } command to enable the function to advertise re-originated EVPN routes to BGP EVPN peers.
      
      
      
      After route re-origination is enabled, Leaf2 or Leaf3 changes the next hop of a received EVPN route to itself, replaces the router MAC address in the gateway MAC address attribute with its own router MAC address, and replaces the Layer 3 VNI with the VPN instance Layer 3 VNI.
   5. Run the [**quit**](cmdqueryname=quit) command to return to the BGP view.
5. (Optional) Configure local EVPN route leaking on Leaf2 and Leaf3. To use different VPN instances for different service access in a DC, and to shield the VPN instance allocation within the DC from outside by using an external VPN instance for communication with other DCs, perform the following steps on each edge leaf node:
   1. Run the [**ipv4-family vpn-instance**](cmdqueryname=ipv4-family+vpn-instance)*vpn-instance-name* or [**ipv6-family vpn-instance**](cmdqueryname=ipv6-family+vpn-instance)*vpn-instance-name* command to enter the BGP-VPN instance IPv4 or IPv6 address family view.
      
      
      
      Here, *vpn-instance-name* specifies the name of the source VPN instance for local route leaking, which corresponds to the name of the VPN instance used to provide access for different services in the local DC.
   2. Run the [**local-cross export evpn-rt-match**](cmdqueryname=local-cross+export+evpn-rt-match) command to allow the locally imported routes and routes received from VPN peers to be leaked to other local VPN instances.
   3. Run the [**local-cross allow-remote-cross-route**](cmdqueryname=local-cross+allow-remote-cross-route) command to allow the routes imported from the remote EVPN instance to be leaked to other local VPN instances.
   4. Run the [**quit**](cmdqueryname=quit) command to return to the BGP view.
   5. Run the [**ipv4-family vpn-instance**](cmdqueryname=ipv4-family+vpn-instance)*vpn-instance-name* or [**ipv6-family vpn-instance**](cmdqueryname=ipv6-family+vpn-instance)*vpn-instance-name* command to enter the BGP-VPN instance IPv4 or IPv6 address family view.
      
      
      
      Here, *vpn-instance-name* specifies the name of the destination VPN instance for local route leaking, which corresponds to the name of the VPN instance used for communication with the external network.
   6. Run the [**advertise l2vpn evpn**](cmdqueryname=advertise+l2vpn+evpn) **include-local-cross-route** command to enable the VPN instance to advertise routes leaked from other local VPN instances as EVPN IP prefix routes.
      
      
      
      By default, locally leaked routes in a VPN instance are not advertised to peers through BGP EVPN. After this step is performed, the external VPN instance can advertise routes leaked from other local service VPN instances to peers through EVPN IP prefix routes. In this way, the external VPN instance can communicate with other DCs.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The EVPN ERT of the source VPN instance must be in the EVPN IRT list of the destination VPN instance, so that local route leaking can be correctly implemented.
6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.