Configuring Load Balancing Among IPv4 VPN Routes on the Backbone Network
========================================================================

This section describes how to configure load balancing among IPv4 VPN routes to load-balance VPN traffic among different links on the backbone network.

#### Usage Scenario

Deploying load balancing among IPv4 VPN routes allows even distribution of VPN traffic among different links on the backbone network, improving the link utilization.

A PE may receive multiple IPv4 VPN routes with the same prefix from different VPNv4 peers. Usually, the PE selects an optimal route and delivers it to the forwarding information base (FIB) to guide data forwarding. If load balancing is configured on the PE, it delivers multiple routes to the FIB. VPN data then can be distributed to different links on the backbone network in a per-packet or per-session manner.


#### Pre-configuration Tasks

Before configuring load balancing among IPv4 VPN routes, complete the following tasks:

* Configure a BGP/MPLS IP VPN.
* Ensure that the PE receives IPv4 VPN routes with the same prefix from different VPNv4 peers.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name*
   
   
   
   The BGP-VPN instance IPv4 address family view is displayed.
4. Run [**maximum load-balancing**](cmdqueryname=maximum+load-balancing) *number*
   
   
   
   Load balancing among BGP routes is configured for the BGP VPN instance IPv4 address family.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Example

After completing the configurations, run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* *ip-address* [ *mask-length* ] [ **longer-match** ] [ **verbose** ] command on the PE. If the IPv4 VPN route has more than one next hop, load balancing among IPv4 VPN routes on the backbone network is configured.