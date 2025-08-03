Configuring a Policy for Advertising MBGP Routes
================================================

After MBGP filters the imported routes, only routes that pass the filtering are added to the local MBGP routing table and advertised to MBGP peers.

#### Context

MBGP can apply a routing policy to all routes to be advertised.


#### Procedure

* Configure MBGP to filter all routes to be advertised.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
  4. Run [**filter-policy**](cmdqueryname=filter-policy) { *acl-number* | **acl-name** *acl-name* | **ip-prefix** *ip-prefix-name* } [**export**](cmdqueryname=export) [ *protocol* [ *process-id* ] ]
     
     
     
     A filtering policy is configured for routes to be advertised.
     
     
     
     + *acl-number* or **acl-name** *acl-name*: specifies an ACL.
     + *ip-prefix-name*: specifies the name of an IP prefix list.
     + [**export**](cmdqueryname=export) [ *protocol* [ *process-id* ] ]: filter routes to be advertised to any MBGP peers. After the [**filter-policy export**](cmdqueryname=filter-policy+export) command is used, MBGP filters routes to be imported by using the [**import-route**](cmdqueryname=import-route) command before importing them. Only routes that pass the filtering are added to the MBGP routing table and are advertised by MBGP.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure MBGP to filter routes to be advertised to a specified peer or peer group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
  4. Run the following commands as needed to configure MBGP to use different filters to filter routes to be advertised to a peer:
     
     
     + To use an ACL for route filtering, run the [**peer**](cmdqueryname=peer) { *peer-address* | *group-name* } [**filter-policy**](cmdqueryname=filter-policy) { *basic-acl-number* | **acl-name** *acl-name* } **export** command.
     + To use the AS\_Path filter for route filtering, run the [**peer**](cmdqueryname=peer) { *peer-address* | *group-name* } [**as-path-filter**](cmdqueryname=as-path-filter) { *as-path-filter-number* | *as-path-filter-name* } **export** command.
     + To use a prefix list for route filtering, run the [**peer**](cmdqueryname=peer) { *peer-address* | *group-name* } [**ip-prefix**](cmdqueryname=ip-prefix) *ip-prefix-name* **export** command.
     
     A peer group and its members can use different export policies when advertising routes. This means that each member in a peer group can select its own policy when advertising routes.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.