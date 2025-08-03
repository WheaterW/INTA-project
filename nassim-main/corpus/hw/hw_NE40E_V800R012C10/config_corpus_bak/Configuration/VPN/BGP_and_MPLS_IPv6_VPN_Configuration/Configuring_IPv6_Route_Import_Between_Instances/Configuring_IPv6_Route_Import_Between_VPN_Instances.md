Configuring IPv6 Route Import Between VPN Instances
===================================================

IPv6 route import between VPN instances enables users in different VPNs to communicate.

#### Context

Perform the following steps for target VPN instances.![](../../../../public_sys-resources/note_3.0-en-us.png) 

If you do not want a VPN instance to change the next hops of imported routes when advertising these routes to its IBGP peers, run the [**import-rib route next-hop-invariable**](cmdqueryname=import-rib+route+next-hop-invariable) command for the VPN instance.




#### Procedure

* Configure a device to import IPv6 direct routes, static routes, or IGP routes from one VPN instance to another VPN instance.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     The VPN instance view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family)
     
     
     
     The VPN instance IPv6 address family view is displayed.
  4. Run [**import-rib**](cmdqueryname=import-rib) **vpn-instance** *vpn-instance-name* **protocol** { **direct** | **vlink-direct-route** | { **static** } [ **valid-route** ] } [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ]
     
     
     
     The device is configured to import direct routes, Vlink direct routes, static routes from the current VPN instance into a specified VPN instance's corresponding routing table.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a device to import IPv6 direct routes, static routes, or IGP routes from one VPN instance to another VPN instance.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP-VPN instance IPv6 address family view is displayed.
  4. Run [**import-rib**](cmdqueryname=import-rib) { **public** | **vpn-instance** *vpn-instance-name* } [ **include-label-route** ] [ **valid-route** ] [ **route-policy** *route-policy-name* ]
     
     
     
     The device is enabled to import BGP4+ routes from the specified VPN instance to the current VPN instance's BGP4+ routing table.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.