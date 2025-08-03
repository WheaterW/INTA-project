Configuring Attr\_Set Attribute Encapsulation or Parsing
========================================================

Configuring the Attr\_Set attribute for BGP routes ensures that CE route attributes are transparently transmitted over the backbone network.

#### Context

On BGP MPLS/VPN networks, EBGP peer relationships are established between PEs and CEs in most cases. Attributes of the routes advertised by CEs are modified during transmission over the intermediate backbone network, or the attributes affect the backbone network. In this case, BGP has been extended to allow the intermediate backbone network to transparently transmit the routes advertised by CEs. After receiving a route from a CE, the local PE encapsulates the attributes of the route in the Attr\_Set attribute and then sends the route to the remote PE. Upon receipt of the route, the remote PE parses the Attr\_Set attribute. This process ensures that the route attributes are transparently transmitted over the backbone network.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family+vpn-instance+vpn-instance) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv4 address family view or run the [**ipv6-family**](cmdqueryname=ipv6-family+vpn-instance) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv6 address family view.
4. Run [**attr-set**](cmdqueryname=attr-set+both+send+receive) { **both** | **send** | **receive** }
   
   
   
   The device is configured to encapsulate the Attr\_Set attribute when sending VPN routes, parse the Attr\_Set attribute when receiving VPN routes, or encapsulate the Attr\_Set attribute when sending VPN routes and parse the Attr\_Set attribute when receiving VPN routes.
5. (Optional) Run [**attr-set**](cmdqueryname=attr-set+as-path-check+enable) **as-path-check enable**
   
   
   
   AS\_Path check is enabled for loop detection.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.