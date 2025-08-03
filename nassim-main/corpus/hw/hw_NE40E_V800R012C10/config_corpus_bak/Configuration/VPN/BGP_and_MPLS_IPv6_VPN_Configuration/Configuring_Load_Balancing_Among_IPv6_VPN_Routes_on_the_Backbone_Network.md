Configuring Load Balancing Among IPv6 VPN Routes on the Backbone Network
========================================================================

This section describes how to configure load balancing of VPN traffic among multiple links on the backbone network of an IPv6 VPN.

#### Usage Scenario

Deploying load balancing among IPv6 VPN routes allows even distribution of VPN traffic to different links on the backbone network, improving the link usage.

A PE may receive multiple IPv6 VPN routes with the same prefix from different VPNv6 peers. Usually, the PE selects an optimal route and delivers it to the forwarding information base (FIB) to guide data forwarding. If load balancing is configured on the PE, it delivers multiple routes to the FIB. VPN data then can be distributed to different links on the backbone network in a packet-by-packet or session-by-session manner.


#### Pre-configuration Tasks

Before configuring load balancing among IPv6 VPN routes, complete the following tasks:

* Configure a BGP/MPLS IPv6 VPN.
* Ensure that the PE receives IPv6 VPN routes with the same prefix from different VPNv6 peers.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
   
   
   
   The BGP-VPN instance IPv6 address family view is displayed.
4. Run [**maximum load-balancing**](cmdqueryname=maximum+load-balancing) *number*
   
   
   
   Load balancing among BGP routes is configured for the BGP VPN instance IPv6 address family.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

After completing the configurations, run the following commands to check the configurations:

Run the [**displayipv6 routing-table vpn-instance**](cmdqueryname=displayipv6+routing-table+vpn-instance) *vpn-instance-name* *ipv6-address* [ *prefix-length* ] [ **longer-match** ] [ **verbose** ] command on a PE to check that the IPv6 VPN route with a specified prefix has multiple next hops. If the IPv6 VPN route with the specified prefix has more than one next hop, load balancing among IPv6 VPN routes on the backbone network is successfully configured.