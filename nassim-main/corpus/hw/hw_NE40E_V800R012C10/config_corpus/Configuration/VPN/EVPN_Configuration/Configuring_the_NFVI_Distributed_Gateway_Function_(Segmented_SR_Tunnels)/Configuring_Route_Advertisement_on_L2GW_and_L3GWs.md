Configuring Route Advertisement on L2GW/L3GWs
=============================================

Route advertisement allows L2GW/L3GWs to construct their own forwarding entries based on received EVPN or BGP routes.

#### Procedure

1. Configure L2GW/L3GWs to generate ARP or ND entries for Layer 2 forwarding based on the ARP or ND information in EVPN routes.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) **vbdif** *bd-id*
      
      
      
      A VBDIF interface is created, and its view is displayed.
   3. Configure the L2GW/L3GW to generate ARP or ND entries for Layer 2 forwarding based on the ARP or ND information in EVPN routes.
      
      
      * Run the [**arp generate-rd-table enable**](cmdqueryname=arp+generate-rd-table+enable) command to configure the L2GW/L3GW to generate ARP entries for Layer 2 forwarding based on the ARP information in EVPN routes.
      * Run the [**ipv6 nd generate-rd-table enable**](cmdqueryname=ipv6+nd+generate-rd-table+enable) command to configure the L2GW/L3GW to generate ND entries for Layer 2 forwarding based on the ND information in EVPN routes.
   4. Configure the function of collecting host information by VBDIF interface.
      
      
      * To enable host information collection for IPv4 services, run the [**arp collect host enable**](cmdqueryname=arp+collect+host+enable) command.
      * To enable host information collection for IPv6 services, run the [**ipv6 nd collect host enable**](cmdqueryname=ipv6+nd+collect+host+enable) command.
   5. (Optional) Run [**ipv6 nd dad attempts**](cmdqueryname=ipv6+nd+dad+attempts) **0**
      
      
      
      DAD is prohibited. This command is mandatory in IPv6 scenarios. It helps prevent service interruptions that occur because the system detects that the IPv6 address of another device is the same as that of the VBDIF interface.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the VBDIF interface view.
2. Configure the L3VPN instance on L2GW/L3GWs to advertise the static VPN routes destined for VNFs to EVPN.
   1. Create a route-policy so that the static VPN routes destined for VNFs can be filtered out in the L3VPN instance. For detailed configurations, see [Configuring a Route-Policy](dc_vrp_route-policy_cfg_0007.html). During the configuration of an apply clause, run the [**apply gateway-ip**](cmdqueryname=apply+gateway-ip) { **origin-nexthop** | *ipv4-address* } or [**apply ipv6 gateway-ip**](cmdqueryname=apply+ipv6+gateway-ip) { **origin-nexthop** | *ipv6-address* } command to specify the original next hop address of a static VPN route as a gateway address.
   2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
      
      
      
      The VPN instance view is displayed.
   3. Enter the VPN instance IPv4 or IPv6 address family view.
      
      
      * Run the [**ipv4-family**](cmdqueryname=ipv4-family) command to enter the VPN instance IPv4 address family view.
      * Run the [**ipv6-family**](cmdqueryname=ipv6-family) command to enter the VPN instance IPv6 address family view.
   4. Run [**export route-policy**](cmdqueryname=export+route-policy) *policy-name* **evpn**
      
      
      
      An export route-policy is applied to the L3VPN instance, so that the L3VPN instance can filter routes to be advertised to EVPN. This ensures that the L3VPN instance advertises only static VPN routes reachable to VNFs to EVPN.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the VPN instance IPv4 or IPv6 address family view.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the VPN instance view.
   7. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   8. Enter the BGP-VPN instance IPv4 or IPv6 address family view.
      
      
      * Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv4 address family view.
      * Run the [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv6 address family view.
   9. Run [**import-route**](cmdqueryname=import-route) **static** [ **med** *med* | **route-policy** *route-policy-name* ] \*
      
      
      
      Static routes are imported into the routing table for the BGP-VPN instance IPv4 or IPv6 address family.
   10. Run [**advertise l2vpn evpn**](cmdqueryname=advertise+l2vpn+evpn) [ **import-route-multipath** ]
       
       
       
       The function to advertise IP routes from the VPN instance to the EVPN instance is enabled.
       
       If the load balancing function needs to be deployed on the network, specify the **import-route-multipath** parameter so that the VPN instance can advertise all the routes with the same destination address to the EVPN instance.
   11. (Optional) Run [**irb asymmetric**](cmdqueryname=irb+asymmetric)
       
       
       
       The asymmetric mode is enabled for IRB routes.
       
       If L2GW/L3GWs are configured to advertise ARP or ND routes to each other, skip this step. If L2GW/L3GWs are configured to advertise IRB or IRBv6 routes to each other, perform this step so that L2GW/L3GWs do not generate IP prefix routes. This prevents routing loops.
   12. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the BGP-VPN instance IPv4 or IPv6 address family view.
3. Configure L2GW/L3GWs to send IRB/IRBv6 or ARP/ND routes to DCGWs.
   1. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP-EVPN address family view is displayed.
   2. Run [**peer**](cmdqueryname=peer+advertise) { *ipv4-address* | *group-name* } **advertise** { **irb** | **arp** | **irbv6** | **nd** }
      
      
      
      L2GW/L3GWs are configured to advertise IRB/IRBv6 or ARP/ND routes.
      
      If L2GW/L3GWs are configured to advertise ARP or ND routes, L2GW/L3GWs send only the routes carrying MAC addresses and ARP information to DCGWs. If L2GW/L3GWs are configured to advertise IRB or IRBv6 routes, L2GW/L3GWs send routes carrying MAC address, ARP information, and L3 VNIs to DCGWs. In this case, you need to run the [**irb asymmetric**](cmdqueryname=irb+asymmetric) command on DCGWs so that DCGWs do not generate IP prefix routes based on IP addresses and L3 VNIs. This prevents routing loops.
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP-EVPN address family view.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP view.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.