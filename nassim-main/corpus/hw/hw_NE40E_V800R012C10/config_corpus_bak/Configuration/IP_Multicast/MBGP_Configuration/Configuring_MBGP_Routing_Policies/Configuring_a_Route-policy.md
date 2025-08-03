Configuring a Route-policy
==========================

A route-policy is used to filter routes.

#### Context

A route-policy is used to match routes or route attributes, and to change route attributes when the matching rules are met.

Perform the following steps on the Router that is configured as an MBGP peer:

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration is optional.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
4. Run [**peer**](cmdqueryname=peer) { *group-name* | *peer-address* } [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **import** | **export** }
   
   
   
   A route-policy is configured to filter MBGP routes. Routes exchanged between the device and its remote MBGP peer can thus be controlled.
   
   
   
   * *group-name*: specifies an MBGP peer group.
   * *peer-address*: specifies the IP address of the remote MBGP peer.
   * *route-policy-name*: specifies the name of a route-policy.
   * **import**: filters routes received from a specified remote MBGP peer. Only the routes that pass the filtering will be permitted.
   * **export**: filters routes sent to a specified remote MBGP peer. Only the routes that pass the filtering will be sent.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.