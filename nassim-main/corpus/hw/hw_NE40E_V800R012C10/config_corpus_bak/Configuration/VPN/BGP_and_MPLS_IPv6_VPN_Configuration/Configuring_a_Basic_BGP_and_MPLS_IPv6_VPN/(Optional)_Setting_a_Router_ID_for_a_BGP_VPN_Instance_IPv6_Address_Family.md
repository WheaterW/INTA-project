(Optional) Setting a Router ID for a BGP VPN Instance IPv6 Address Family
=========================================================================

You can set different router IDs for BGP VPN instance IPv6 address families on the same device.

#### Context

By default, no router ID is set for a BGP VPN instance IPv6 address family, and the BGP router ID is used. In this case, different BGP VPN instance IPv6 address families on the same device have the same router ID. In some cases, different router IDs need to be set for different BGP VPN instance IPv6 address families. For example, BGP peer relationships need to be established between different BGP VPN instance IPv6 address families on the same PE.

There are two methods of setting a router ID for a BGP VPN instance IPv6 address family. You can choose either of the two methods as required.

* Set router IDs for all BGP VPN instance IPv6 address families.
* Set a router ID for a specified BGP VPN instance IPv6 address family.

The router ID configured in the BGP-VPN instance IPv6 address family view takes precedence over the router ID configured in the BGP view.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

If a BGP session has been established in a BGP-VPN instance IPv6 address family, changing or deleting the configured router ID resets the BGP session.



#### Procedure

* Set router IDs for all BGP VPN instance IPv6 address families.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**router-id**](cmdqueryname=router-id) **vpn-instance auto-select**
     
     
     
     Automatic router ID selection is configured for all BGP VPN instance IPv6 address families. The [**router-id**](cmdqueryname=router-id) **vpn-instance auto-select** command takes precedence over the [**router-id**](cmdqueryname=router-id) *ipv4-address* command in the BGP view.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Rules for automatically selecting a router ID for a BGP VPN instance IPv6 address family are as follows:
     
     + If the loopback interfaces assigned IP addresses are bound to the VPN instance enabled with the IPv6 address family, the largest IP address among the IP addresses of the loopback interfaces is selected as the router ID.
     + If no loopback interfaces assigned IP addresses are bound to the VPN instance enabled with the IPv6 address family, the largest IP address among the IP addresses of other interfaces bound to the VPN instance is selected as the router ID, regardless of whether the interface is up or down.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set a router ID for a specified BGP VPN instance IPv6 address family.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP-VPN instance IPv6 address family view is displayed.
  4. Run [**router-id**](cmdqueryname=router-id) { *ipv4-address* | **auto-select** }
     
     
     
     A router ID or automatic route ID selection is configured for the current BGP VPN instance IPv6 address family.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.