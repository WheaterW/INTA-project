Configuring a Policy for Receiving MBGP Routes
==============================================

MBGP filters received routes by using a policy. Only the routes that match the policy can be added to a routing table.

#### Context

MBGP can apply a routing policy to all received routes or only routes received from a specific peer or peer group.

MBGP provides peer-specific route control to limit the number of routes received from a peer or peer group. If a device is under malicious attacks or some network configurations are incorrect, the device will receive a large number of routes from its MBGP peers, consuming resources. Therefore, you need to limit resources consumed by MBGP devices based on network planning and device capacities.


#### Procedure

* Configure MBGP to filter all received routes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
  4. Run [**filter-policy**](cmdqueryname=filter-policy) { *acl-number* | **acl-name** *acl-name* | **ip-prefix** *ip-prefix-name* } [**import**](cmdqueryname=import)
     
     
     
     A policy is configured to filter the routes received from all MBGP peers.
     
     
     
     Routes exchanged between the device and any of its MBGP peers can thus be controlled.
     
     
     
     + *basic-acl-number or acl-name acl-name: specifies an ACL.*
     + *ip-prefix-name*: specifies an IP prefix list.
     + **import**: filters routes received from any MBGP peers. Only the routes that pass the filtering are permitted.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure MBGP to filter routes received from a specific peer or peer group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
  4. Run the following commands as needed to configure MBGP to use different filters to filter routes received from peers:
     
     
     + To use an ACL for route filtering, run the [**peer**](cmdqueryname=peer) { *peer-address* | *group-name* } [**filter-policy**](cmdqueryname=filter-policy) { *basic-acl-number* | **acl-name** *acl-name* } **import** command.
     + To use the AS\_Path filter for route filtering, run the [**peer**](cmdqueryname=peer) { *peer-address* | *group-name* } [**as-path-filter**](cmdqueryname=as-path-filter) { *as-path-filter-number* | *as-path-filter-name* } **import** command.
     + To use a prefix list for route filtering, run the [**peer**](cmdqueryname=peer) { *peer-address* | *group-name* } [**ip-prefix**](cmdqueryname=ip-prefix) *ip-prefix-name* **import** command.
     
     A peer group and its members can use different inbound policies when receiving routes. This means that each member in a peer group can select its own policy to filter received routes.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Limit the number of routes received from peers.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
  4. Run [**peer**](cmdqueryname=peer) { *group-name* | *peer-address* } [**route-limit**](cmdqueryname=route-limit) *maximum-limit* [ *percentage* ] [ **alert-only** | **idle-forever** | **idle-timeout** *minutes* ]
     
     
     
     The number of routes that can be received from a peer or peer group is set.
     
     The command provides peer-specific control. You can set specific parameters as needed to control the MBGP device's behaviors after the number of the routes received from a peer exceeds the limit.
     
     + If **alert-only** is set, the device does not end the peer relationship but does not receive any subsequent routes after the number of received routes exceeds the limit. In addition, the device generates an alarm and a log.
     + If **idle-forever** is set, the device ends the peer relationship, and does not attempt to establish a connection. In addition, the device generates an alarm and a log. If you run the [**display bgp multicast peer**](cmdqueryname=display+bgp+multicast+peer) [ **verbose** ] command, you will see that the peer relationship is in the Idle state. To restore the MBGP connection, run the [**reset bgp**](cmdqueryname=reset+bgp) command.
     + If **idle-timeout** is set, the device ends the peer relationship, and attempts to re-establish the connection after the corresponding timer expires. In addition, the device generates an alarm and a log. If you run the [**display bgp multicast peer**](cmdqueryname=display+bgp+multicast+peer) [ **verbose** ] command, you will see that the peer relationship is in the Idle state. To restore the MBGP connection before the timer expires, run the [**reset bgp**](cmdqueryname=reset+bgp) command.
     + If none of the preceding parameters are set, the device ends the peer relationship, and attempts to establish a connection after 30 seconds. In addition, the device generates an alarm and a log.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the number of routes received by a Router exceeds the upper threshold and the [**peer route-limit**](cmdqueryname=peer+route-limit) command is used for the first time, the Router and its peer re-establish the peer relationship, regardless of whether **alert-only** is specified.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.