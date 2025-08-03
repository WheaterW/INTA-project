Configuring Route Advertisement on PEs
======================================

Route advertisement allows PEs to advertise default static routes to L2GWs/L3GWs through BGP VPNv4 peer relationships.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure default static VPN routes.
   
   
   * Run the [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-instance-name* **0.0.0.0** { **0.0.0.0** | **0** } { *nexthop-address* | *interface-type* *interface-number* [ *nexthop-address* ] } [ **tag** *tag* ] command to create a default static VPN IPv4 route.
   * Run the [**ipv6 route-static vpn-instance**](cmdqueryname=ipv6+route-static+vpn-instance) *vpn-instance-name* **::** **0** { *nexthop-ipv6âaddress* | *interface-type* *interface-number* [ *nexthop-ipv6-address* ] } [ **tag** *tag* ] command to create a default static VPN IPv6 route.
3. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
4. Enter the BGP-VPN instance IPv4 or IPv6 address family view.
   
   
   * Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv4 address family view.
   * Run the [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv6 address family view.
5. Run [**network**](cmdqueryname=network) { **0.0.0.0** **0** | **::** **0** }
   
   
   
   Default static VPN routes are imported into the BGP-VPN instance IPv4 or IPv6 address family.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the BGP-VPN instance IPv4 or IPv6 address family view.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the BGP view.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.