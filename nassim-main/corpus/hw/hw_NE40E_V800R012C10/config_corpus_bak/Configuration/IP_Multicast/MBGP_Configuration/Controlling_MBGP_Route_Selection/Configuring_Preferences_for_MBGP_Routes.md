Configuring Preferences for MBGP Routes
=======================================

To control route selection among MBGP and other routing protocols, set the MBGP preference.

#### Context

Perform the following steps on the Router that is configured as an MBGP peer:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
4. Run [**preference**](cmdqueryname=preference) { *external-preference* *internal-preference* *local-preference* | **route-policy** *route-policy-name* | **route-filter** *route-filter-name* }
   
   
   
   MBGP preferences are set for internal, external, and local routes.
   
   
   
   * *external-preference*: specifies the preference for routes learned from EBGP peers.
   * *internal-preference*: specifies the preference for routes learned from IBGP peers.
   * *local-preference*: specifies the preference for locally originated routes.
   * **route-policy** *route-policy-name*: specifies a routing policy. The specified MBGP preference will be applied to the routes that match the policy.
   * **route-filter** *route-filter-name*: specifies a routing filter. The specified MBGP preference will be applied to the routes that match the policy.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.