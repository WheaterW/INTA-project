Configuring Route Advertisement on L2GWs/L3GWs
==============================================

Configuring Route Advertisement on L2GWs/L3GWs

#### Prerequisites

Before configuring route advertisement on an L2GW/L3GW, complete one of the following tasks based on the network type:

* [Establishing VXLAN Tunnels in BGP EVPN Mode (Distributed VXLAN Gateway)](../dc/dc_vrp_vxlan_cfg_1066.html)
* [Establishing IPv6 VXLAN Tunnels in BGP EVPN Mode (Distributed VXLAN Gateway)](../dc/dc_vrp_vxlan6_cfg_1066.html)

#### Context

[Figure 1](#EN-US_TASK_0000001150047634__fig14453146813) shows the networking diagram of NFVI distributed gateways. DC gateways are the DCN's border gateways and can be used to exchange Internet routes with the external network. L2GW/L3GW1 and L2GW/L3GW2 connect to virtualized network functions (VNFs). VNF1 and VNF2, as virtualized NEs, can be deployed to respectively provide vUGW and vMSE functions and connect to L2GW/L3GW1 and L2GW/L3GW2 through interface processing units (IPUs).

**Figure 1** NFVI distributed gateway networking  
![](figure/en-us_image_0000001196218629.png)

After route advertisement is configured on L2GWs/L3GWs, other devices can obtain routes to L2GWs/L3GWs, and L2GWs/L3GWs can generate their own forwarding entries based on the received EVPN or BGP routes.

![](../public_sys-resources/note_3.0-en-us.png) 

The NFVI distributed gateway function is supported for both IPv4 and IPv6 services. If a configuration step is not differentiated in terms of IPv4 and IPv6, this step applies to both IPv4 and IPv6 services.

This series of devices can function as L2GWs/L3GWs only.



#### Procedure

1. Use either of the following methods to configure a VPN route to a VNF:
   
   
   * Configure a VPN static route to a VNF. For details, see *Configuration Guide > IP Routing > IPv4 Static Route Configuration* or *Configuration Guide > IP Routing > IPv6 Static Route Configuration*.![](../public_sys-resources/note_3.0-en-us.png) 
     
     To load-balance east-west traffic between VNF1 and VNF2, use the **inter-protocol-ecmp** keyword when configuring VPN static routes to VNFs on L2GWs/L3GWs, and set the preference of the static routes to 255. (These routes must have the same preference as BGP EVPN routes.)
   * Configure L2GWs/L3GWs to establish VPN IGP neighbor relationships with VNFs. For details, see "Configuring Basic IPv4 IS-IS Functions" located under *Configuration Guide > IP Routing > IS-IS Configuration*, "Configuring Basic OSPF Functions" located under *Configuration Guide > IP Routing > OSPF Configuration*, "Configuring Basic IPv6 IS-IS Functions" located under *Configuration Guide > IP Routing > IS-IS Configuration*, or "Configuring Basic OSPFv3 Functions" located under *Configuration Guide > IP Routing > OSPFv3 Configuration*.![](../public_sys-resources/note_3.0-en-us.png) 
     
     In an active-active L2GW/L3GW scenario, a secondary IP address ([**ip address**](cmdqueryname=ip+address) *ip-address* **sub**) needs to be configured for the VBDIF interface on each L2GW/L3GW for the establishment of VPN IGP neighbor relationships with VNFs.
2. Configure an L3VPN instance to advertise VPN routes destined for VNFs to the EVPN instance.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Create a route-policy to filter VPN routes reachable to VNFs in the L3VPN instance.
      
      
      
      For details about how to create a route-policy, see "Routing Policy Configuration" located under *Configuration Guide > IP Routing Configuration > Configuring a Route-Policy*. When configuring the apply clause, you need to run the [**apply gateway-ip**](cmdqueryname=apply+gateway-ip) { **origin-nexthop** | *ipv4-address* } or [**apply ipv6 gateway-ip**](cmdqueryname=apply+ipv6+gateway-ip) { **origin-nexthop** | *ipv6-address* } command to set the original next hop address of a VPN route to the gateway address.
   3. Create a VPN instance and enter its view.
      
      
      ```
      [ip vpn-instance](cmdqueryname=ip+vpn-instance) vpn-instance-name
      ```
   4. Enter the VPN instance IPv4/IPv6 address family view.
      
      
      ```
      [ipv4-family](cmdqueryname=ipv4-family) or [ipv6-family](cmdqueryname=ipv6-family)
      ```
   5. Associate the current L3VPN instance with an export route-policy.
      
      
      ```
      [export route-policy](cmdqueryname=export+route-policy) policy-name evpn
      ```
      
      The route-policy is created in Step 2.b and used to filter routes advertised by the L3VPN instance to the EVPN instance. This ensures that the L3VPN instance advertises only VPN routes destined for the VNF to the EVPN instance.
   6. Return to the VPN instance view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   7. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   8. Enter the BGP view.
      
      
      ```
      [bgp](cmdqueryname=bgp) as-number
      ```
   9. Enter the BGP VPN instance IPv4/IPv6 address family view.
      
      
      ```
      [ipv4-family](cmdqueryname=ipv4-family) vpn-instance vpn-instance-name or [ipv6-family](cmdqueryname=ipv6-family) vpn-instance vpn-instance-name
      ```
   10. Import routes destined for the VNF into the routing table of the BGP VPN instance IPv4 or IPv6 address family.
       
       
       ```
       [import-route](cmdqueryname=import-route) { static | { ospf | isis } process-id } [ med med | route-policy route-policy-name ] *
       or
       [import-route](cmdqueryname=import-route) { static | { ospfv3 | isis } process-id } [ med med | route-policy route-policy-name ] *
       ```
       
       By default, other protocol routes are not imported into the routing table for the BGP VPN instance IPv4/IPv6 address family.
   11. Enable the VPN instance to advertise EVPN IP prefix routes.
       
       
       ```
       [advertise l2vpn evpn](cmdqueryname=advertise+l2vpn+evpn) { best-route | valid-routes }[ import-route-multipath ] [ include-local-cross-route ]
       ```
       
       By default, a VPN instance cannot advertise EVPN IP prefix routes. If load balancing is required, you are advised to specify the **import-route-multipath** keyword, so that a VPN instance can advertise all routes with the same destination address as EVPN IP prefix routes.
   12. Return to the BGP view.
       
       
       ```
       [quit](cmdqueryname=quit)
       ```
   13. Return to the system view.
       
       
       ```
       [quit](cmdqueryname=quit)
       ```
   14. Commit the configuration.
       
       
       ```
       [commit](cmdqueryname=commit)
       ```
3. Configure the device to advertise IRB or IRBv6 routes to the DC gateway.
   1. Enter the BGP view.
      
      
      ```
      [bgp](cmdqueryname=bgp) as-number
      ```
   2. Enter the BGP-EVPN address family view.
      
      
      ```
      [l2vpn-family evpn](cmdqueryname=l2vpn-family+evpn)
      ```
   3. Configure the device to advertise IRB or IRBv6 routes to the DC gateway.
      
      
      ```
      [peer](cmdqueryname=peer) { ipv4-address | group-name | ipv6-address } advertise { irb | irbv6 }
      ```
      
      By default, a device does not advertise IRB/IRBv6 routes to BGP EVPN peers.
   4. Return to the BGP view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   5. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   6. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```