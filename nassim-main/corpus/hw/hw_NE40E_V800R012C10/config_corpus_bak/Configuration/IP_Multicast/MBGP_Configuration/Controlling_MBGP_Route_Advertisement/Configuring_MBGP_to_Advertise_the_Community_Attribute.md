Configuring MBGP to Advertise the Community Attribute
=====================================================

The community and extended community attributes are used to simplify routing policy management.

#### Context

The community attribute is transmitted between MBGP peers, and its transmission is not restricted within ASs. With the community attribute, a group of routes can share the same routing policy. Before sending a route with the community attribute to peers, MBGP can change the original community attribute carried by the route.

Perform the following steps on the Router that is configured as an MBGP peer:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
4. Run one of the following commands as needed.
   
   
   * To advertise the community attribute to an MBGP peer or peer group, run the [**peer**](cmdqueryname=peer) { *group-name* | *peer-address* } **advertise-community** command.
     
     + *group-name*: specifies the name of an MBGP peer group.
     + *peer-address*: specifies the IP address of an MBGP peer.
   * To advertise the extended community attribute to an MBGP peer or peer group, run the [**peer**](cmdqueryname=peer) { *group-name* | *peer-address* } **advertise-ext-community** command.
     
     + *group-name*: specifies the name of an MBGP peer group.
     + *peer-address*: specifies the IP address of an MBGP peer.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.