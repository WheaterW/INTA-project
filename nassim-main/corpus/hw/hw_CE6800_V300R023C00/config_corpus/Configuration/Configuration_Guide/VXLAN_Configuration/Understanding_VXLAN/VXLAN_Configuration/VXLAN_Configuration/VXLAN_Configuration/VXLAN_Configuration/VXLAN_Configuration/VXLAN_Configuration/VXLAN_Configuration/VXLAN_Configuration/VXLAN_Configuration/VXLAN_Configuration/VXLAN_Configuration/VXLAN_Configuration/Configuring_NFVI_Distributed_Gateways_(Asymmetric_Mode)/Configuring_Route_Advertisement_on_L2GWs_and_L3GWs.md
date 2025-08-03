Configuring Route Advertisement on L2GWs/L3GWs
==============================================

Configuring Route Advertisement on L2GWs/L3GWs

#### Prerequisites

Before configuring route advertisement on an L2GW/L3GW, complete one of the following tasks based on the network type:

* [Establish VXLAN tunnels in BGP EVPN mode (distributed VXLAN gateway).](../dc/dc_vrp_vxlan_cfg_1066.html)
* [Establish IPv6 VXLAN tunnels in BGP EVPN mode (distributed VXLAN gateway).](../dc/dc_vrp_vxlan6_cfg_1066.html)

#### Context

[Figure 1](#EN-US_TASK_0000001179227126__fig14453146813) shows the networking diagram of NFVI distributed gateways. DC gateways are the DCN's border gateways and can be used to exchange Internet routes with the external network. L2GW/L3GW1 and L2GW/L3GW2 connect to virtualized network functions (VNFs). VNF1 and VNF2, as virtualized NEs, can be deployed to respectively provide vUGW and vMSE functions and connect to L2GW/L3GW1 and L2GW/L3GW2 through interface processing units (IPUs).

**Figure 1** NFVI distributed gateway networking  
![](figure/en-us_image_0000001179736844.png)

After route advertisement is configured on L2GWs/L3GWs, other devices can obtain routes to L2GWs/L3GWs, and L2GWs/L3GWs can generate their own forwarding entries based on the received EVPN or BGP routes.

![](../public_sys-resources/note_3.0-en-us.png) 

The NFVI distributed gateway function is supported for both IPv4 and IPv6 services. If a configuration step is not differentiated in terms of IPv4 and IPv6, this step applies to both IPv4 and IPv6 services.

This series of devices can function as L2GWs/L3GWs only.



#### Procedure

1. Configure an L2GW/L3GW to generate ARP (ND) entries for Layer 2 forwarding based on ARP/ND information in EVPN routes.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Create a VBDIF interface and enter its view.
      
      
      ```
      [interface](cmdqueryname=interface) vbdif bd-id
      ```
      
      By default, no VBDIF interface is created.
   3. Configure an L2GW/L3GW to generate ARP (ND) entries for Layer 2 forwarding based on ARP/ND information in EVPN routes.
      
      
      * Configure the L2GW/L3GW to generate ARP entries used for Layer 2 forwarding based on ARP information.
        
        ```
        [arp generate-rd-table enable](cmdqueryname=arp+generate-rd-table+enable)
        ```
      * Configure the L2GW/L3GW to generate ND entries used for Layer 2 forwarding based on ND information.
        
        ```
        [ipv6 nd generate-rd-table enable](cmdqueryname=ipv6+nd+generate-rd-table+enable)
        ```
      
      By default, a device cannot generate ARP (ND) entries for Layer 2 forwarding based on ARP/ND information in EVPN routes.
   4. Exit the VBDIF interface view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
2. Configure an L3VPN instance on the L2GW/L3GW to advertise VPN static routes destined for the VNF to EVPN.
   1. Create a route-policy to filter VPN static routes reachable to the VNF in the L3VPN instance. For details about how to create a route-policy, see "Routing Policy Configuration". When configuring the apply clause, you need to run the [**apply gateway-ip**](cmdqueryname=apply+gateway-ip) { **origin-nexthop** | *ipv4-address* } or [**apply ipv6 gateway-ip**](cmdqueryname=apply+ipv6+gateway-ip) { **origin-nexthop** | *ipv6-address* } command to set the original next hop addresses of VPN static routes to the gateway address.
   2. Enter the VPN instance view.
      
      
      ```
      [ip vpn-instance](cmdqueryname=ip+vpn-instance) vpn-instance-name
      ```
      
      By default, no VPN instance is created.
   3. Enter the VPN instance IPv4/IPv6 address family view.
      
      
      ```
      [ipv4-family](cmdqueryname=ipv4-family) or [ipv6-family](cmdqueryname=ipv6-family)
      ```
      
      By default, the VPN instance IPv4/IPv6 address family view is not created.
   4. Associate the current L3VPN instance with an export route-policy, which filters routes that the L3VPN instance will advertise to an EVPN instance. This ensures that the L3VPN instance advertises only VPN static routes destined for the VNF to the EVPN instance.
      
      
      ```
      [export route-policy](cmdqueryname=export+route-policy) policy-name evpn
      ```
      
      By default, the L3VPN instance is not associated with any export route-policy.
   5. Exit the VPN instance IPv4/IPv6 address family view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   6. Exit the VPN instance view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   7. Enter the BGP view.
      
      
      ```
      [bgp](cmdqueryname=bgp) { as-number-plain | as-number-dot }
      ```
      
      By default, BGP is not enabled.
   8. Enter the BGP VPN instance IPv4/IPv6 address family view.
      
      
      ```
      [ipv4-family](cmdqueryname=ipv4-family) vpn-instance vpn-instance-name or [ipv6-family](cmdqueryname=ipv6-family) vpn-instance vpn-instance-name
      ```
      
      By default, the BGP-VPN instance IPv4/IPv6 address family view is not created.
   9. Import static routes into the routing table of the BGP-VPN instance IPv4/IPv6 address family.
      
      
      ```
      [import-route](cmdqueryname=import-route) static [ med med | route-policy route-policy-name ] *
      ```
      
      By default, static routes are not imported into the routing table for the BGP VPN instance IPv4/IPv6 address family.
   10. Enable the VPN instance to advertise EVPN IP prefix routes.
       
       
       ```
       [advertise l2vpn evpn](cmdqueryname=advertise+l2vpn+evpn) { best-route | valid-routes }[ import-route-multipath ] [ include-local-cross-route ]
       ```
       
       By default, a VPN instance cannot advertise EVPN IP prefix routes. If load balancing is required, you are advised to specify the **import-route-multipath** keyword, so that a VPN instance can advertise all routes with the same destination address as EVPN IP prefix routes.
   11. (Optional) Enable the asymmetric mode for IRB routes.
       
       
       ```
       [irb asymmetric](cmdqueryname=irb+asymmetric)
       ```
       
       By default, the asymmetric mode is not enabled for IRB routes. If L2GWs/L3GWs are configured to advertise ARP (ND) routes to each other, skip this step. If L2GWs/L3GWs are configured to advertise IRB (IRBv6) routes to each other, perform this step, so that the L2GWs/L3GWs do not generate IP prefix routes. This helps prevent routing loops.
   12. Exit the BGP-VPN instance IPv4/IPv6 address family view.
       
       
       ```
       [quit](cmdqueryname=quit)
       ```
3. Configure L2GWs/L3GWs to advertise IRB (IRBv6) or ARP (ND) routes to DC gateways.
   1. Enter the BGP-EVPN address family view.
      
      
      ```
      [l2vpn-family evpn](cmdqueryname=l2vpn-family+evpn)
      ```
      
      By default, the BGP-EVPN address family view is not created.
   2. The device is configured to advertise IRB (IRBv6) or ARP (ND) routes.
      
      
      ```
      [peer](cmdqueryname=peer) { ipv4-address | group-name | ipv6-address } advertise { irb | arp | irbv6 | nd }
      ```
      
      By default, a device does not advertise ND, IRBv6, ARP, or IRB routes to a BGP EVPN peer.
      
      During the advertisement of ARP (ND) routes, L2GWs/L3GWs send only routes carrying MAC address and ARP information to DC gateways. During the advertisement of IRBv6 (IRB) routes, L2GWs/L3GWs send routes carrying MAC address, ARP, and L3VNI information to DC gateways. In this case, however, the asymmetric mode for IRB routes must be enabled on DC gateways, so that DC gateways do not generate IP prefix routes based on IP address and L3VNI information. This helps prevent routing loops on the network.
   3. Exit the BGP-EVPN address family view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   4. Exit the BGP view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```