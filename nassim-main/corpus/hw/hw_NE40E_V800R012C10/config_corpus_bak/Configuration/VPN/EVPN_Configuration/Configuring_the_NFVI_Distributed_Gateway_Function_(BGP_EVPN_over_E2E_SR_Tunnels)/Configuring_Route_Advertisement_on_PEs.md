Configuring Route Advertisement on PEs
======================================

Route advertisement allows PEs to advertise default static routes to L2GWs/L3GWs through a BGP EVPN RR.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Create a route-policy to filter and modify received routes. For configuration details, see [Configuring a Route-Policy](dc_vrp_route-policy_cfg_0007.html). You can run the [**apply gateway-ip none**](cmdqueryname=apply+gateway-ip+none) or [**apply ipv6 gateway-ip none**](cmdqueryname=apply+ipv6+gateway-ip+none) command to delete gateway IP addresses from the VNF routes received from L2GWs/L3GWs, so that the traffic sent from PEs to VNFs can recurse to SR tunnels, instead of being forwarded based on gateway IP addresses.
3. Configure default static VPN routes.
   
   
   * Run the [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-instance-name* **0.0.0.0** { **0.0.0.0** | **0** } { *nexthop-address* | *interface-type* *interface-number* [ *nexthop-address* ] } [ **tag** *tag* ] command to create a default static VPN IPv4 route.
   * Run the [**ipv6 route-static vpn-instance**](cmdqueryname=ipv6+route-static+vpn-instance) *vpn-instance-name* **::** **0** { *nexthop-ipv6âaddress* | *interface-type* *interface-number* [ *nexthop-ipv6-address* ] } [ **tag** *tag* ] command to create a default static VPN IPv6 route.
4. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
   
   
   
   The VPN instance view is displayed.
5. Enter the VPN instance IPv4 or IPv6 address family view.
   
   
   * Run the [**ipv4-family**](cmdqueryname=ipv4-family) command to enter the VPN instance IPv4 address family view.
   * Run the [**ipv6-family**](cmdqueryname=ipv6-family) command to enter the VPN instance IPv6 address family view.
6. Run [**import route-policy**](cmdqueryname=import+route-policy) *policy-name* **evpn**
   
   
   
   The L3VPN instance is associated with an import route-policy. This route-policy is used to filter the routes received by the L3VPN instance from the EVPN instance, so that the L3VPN instance can delete gateway IP addresses from the routes received from L2GWs/L3GWs.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the VPN instance IPv4 or IPv6 address family view.
8. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the VPN instance view.
9. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
10. Enter the BGP-VPN instance IPv4 or IPv6 address family view.
    
    
    * Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv4 address family view.
    * Run the [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv6 address family view.
11. Run [**network**](cmdqueryname=network) { **0.0.0.0** **0** | **::** **0** }
    
    
    
    Default static VPN routes are imported into the BGP-VPN instance IPv4 or IPv6 address family.
12. Run [**advertise l2vpn evpn**](cmdqueryname=advertise+l2vpn+evpn)
    
    
    
    The function to advertise IP routes from the VPN instance to the EVPN instance is enabled.
13. Run [**quit**](cmdqueryname=quit)
    
    
    
    Exit the BGP-VPN instance IPv4 or IPv6 address family view.
14. Run [**quit**](cmdqueryname=quit)
    
    
    
    Exit the BGP view.
15. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.