(Optional) Configuring a Router ID for a BGP-VPN Instance IPv4 Address Family
=============================================================================

You can configure different router IDs for BGP VPN instance
IPv4 address families on the same device.

#### Context

By default, no router ID is configured for a BGP-VPN instance
IPv4 address family, and the BGP router ID is used. As a result, different
BGP-VPN instance IPv4 address families on the same device have the
same router ID. In some cases, different router IDs need to be configured
for different BGP-VPN instance IPv4 address families. For example,
BGP peer relationships need to be established between different BGP-VPN
instance IPv4 address families on the same PE.

Two methods are
available for configuring a router ID for a BGP-VPN instance IPv4
address family. Choose either of the following methods as required:

* Configure router IDs for all BGP-VPN instance IPv4 address
  families.
* Configure a router ID for a specified BGP-VPN instance IPv4
  address family.

The router ID configured in the BGP-VPN instance IPv4
address family view takes precedence over the router ID configured
in the BGP view.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

If a BGP session has been
established in a BGP-VPN instance IPv4 address family, changing or
deleting the configured router ID resets the BGP session.



#### Procedure

* Configure router IDs for all BGP-VPN instance IPv4 address
  families.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**router-id**](cmdqueryname=router-id) { *ipv4-address* | **vpn-instance auto-select** }
     
     
     
     Automatic router ID selection is configured for all
     BGP-VPN instance IPv4 address families.
     
     In the BGP view, the [**router-id**](cmdqueryname=router-id) **vpn-instance auto-select** command
     takes precedence over the [**router-id**](cmdqueryname=router-id) *ipv4-address* command.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Rules for automatically
     selecting a router ID for a BGP VPN instance IPv4 address family are
     as follows:
     
     + If the loopback interfaces configured with IP addresses are
       bound to the VPN instance enabled with the IPv4 address family, the
       highest IP address among the IP addresses of the loopback interfaces
       is selected as the router ID.
     + If no loopback interfaces configured with IP addresses are
       bound to the VPN instance enabled with the IPv4 address family, the
       highest IP address among the IP addresses of other interfaces bound
       to the VPN instance is selected as the router ID, regardless of whether
       the interface is Up or Down.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is
     committed.
* Configure a router ID for a specified BGP-VPN instance
  IPv4 address family.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP-VPN instance IPv4 address family view is displayed.
  4. Run [**router-id**](cmdqueryname=router-id) { *ipv4-address* | **auto-select** }
     
     
     
     A router ID or automatic route ID selection is configured
     for the current BGP-VPN instance IPv4 address family.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is
     committed.