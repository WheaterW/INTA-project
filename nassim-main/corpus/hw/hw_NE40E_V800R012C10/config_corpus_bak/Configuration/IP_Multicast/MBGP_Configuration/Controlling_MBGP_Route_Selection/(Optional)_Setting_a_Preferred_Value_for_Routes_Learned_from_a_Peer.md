(Optional) Setting a Preferred Value for Routes Learned from a Peer
===================================================================

After preferred values are set for MBGP routes, the route with the greatest value is preferred when multiple routes to the same destination exist in the MBGP routing table.

#### Context

Perform the following steps on the Router that is configured as an MBGP peer:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
4. Run [**peer**](cmdqueryname=peer) { *group-name* | *peer-address* } **preferred-value** **preferredvalue**
   
   
   
   A preferred value is set for the routes learned from an MBGP peer group or a remote MBGP peer. Among multiple routes, the route with the highest preferred value is selected as the route to the specified network.
   
   
   
   * *group-name*: specifies the name of an MBGP peer group.
   * *peer-address*: specifies the IP address of a remote MBGP peer.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.