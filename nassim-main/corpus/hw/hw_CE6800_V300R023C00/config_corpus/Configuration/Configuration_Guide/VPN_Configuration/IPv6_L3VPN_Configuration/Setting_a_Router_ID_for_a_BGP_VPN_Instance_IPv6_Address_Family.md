Setting a Router ID for a BGP VPN Instance IPv6 Address Family
==============================================================

Setting a Router ID for a BGP VPN Instance IPv6 Address Family

#### Context

No router ID is configured for a BGP VPN instance IPv6 address family by default, so the BGP router ID is used. As such, different BGP VPN instance IPv6 address families on the same device have the same router ID. However, some cases require different router IDs. For example, they are required if BGP peer relationships need to be established between different BGP VPN instance IPv6 address families on the same PE.

Two methods are available to configure a router ID for a BGP VPN instance IPv6 address family. You can choose either of them as required.

* Set router IDs for all BGP VPN instance IPv6 address families.
* Configure a router ID for a specified BGP VPN instance IPv6 address family.

The router ID configured in the BGP VPN instance IPv6 address family view takes precedence over that configured in the BGP view.

![](public_sys-resources/notice_3.0-en-us.png) 

If a BGP session has been established in a BGP VPN instance IPv6 address family, changing or deleting the configured router ID resets the BGP session.



#### Procedure

* Set router IDs for all BGP VPN instance IPv6 address families.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Configure router IDs for all BGP VPN instance IPv6 address families.
     
     
     ```
     [router-id](cmdqueryname=router-id) vpn-instance auto-select
     ```
     
     Automatic router ID selection is configured for all BGP VPN instance IPv6 address families. The [**router-id**](cmdqueryname=router-id) **vpn-instance auto-select** command takes precedence over the [**router-id**](cmdqueryname=router-id) *ipv4-address* command in the BGP view.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     Rules for automatically selecting a router ID for a BGP VPN instance IPv6 address family are as follows:
     
     + If loopback interfaces configured with IP addresses are bound to a VPN instance enabled with the IPv6 address family, the largest IP address among them is selected as the router ID.
     + If no loopback interfaces configured with IP addresses are bound to a VPN instance enabled with the IPv6 address family, the largest IP address among those of other interfaces bound to the VPN instance is selected as the router ID, regardless of whether the interface is up or down.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure a router ID for a specified BGP VPN instance IPv6 address family.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Enter the BGP VPN instance IPv6 address family view.
     
     
     ```
     [ipv6-family](cmdqueryname=ipv6-family) vpn-instance vpn-instance-name
     ```
  4. Manually configure or automatically select a router ID for the BGP VPN instance IPv6 address family.
     
     
     ```
     [router-id](cmdqueryname=router-id) { ipv4-address | auto-select }
     ```
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```