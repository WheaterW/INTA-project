(Optional) Configuring an IP Address of a Next Hop to Which a Route Is Redirected
=================================================================================

This section describes how to set the IP address of a next hop to which a route is redirected.

#### Context

A DS-Lite instance is a platform used to configure DS-Lite attributes. After user traffic enters a DS-Lite instance, DS-Lite translates information in the user traffic and forwards traffic based on the redirect next-hop IP address.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* **id** *id*
   
   
   
   A DS-Lite instance is created, and the DS-Lite instance view is displayed.
3. Run [**redirect ip-nexthop**](cmdqueryname=redirect+ip-nexthop) *ip-address* **outbound** or [**redirect ip-nexthop**](cmdqueryname=redirect+ip-nexthop) *ipv6-address* **inbound**
   
   
   
   The IP address of a next hop to which a route is redirected is specified.
   
   
   
   Although both the inbound- and outbound-related commands can be run simultaneously in a DS-Lite instance, network-to-user traffic's next-hop address can be set only to an IPv6 address, and user-to-network traffic's next-hop address can be set only to an IPv4 address. Only a single address can be set for each of network-to-user and user-to-network traffic.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.