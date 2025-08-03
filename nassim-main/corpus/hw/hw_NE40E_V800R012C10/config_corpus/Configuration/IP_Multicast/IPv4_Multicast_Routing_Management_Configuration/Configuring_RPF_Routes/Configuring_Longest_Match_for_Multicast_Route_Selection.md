Configuring Longest Match for Multicast Route Selection
=======================================================

If the longest match principle is configured for route selection, an optimal intra-domain unicast route, an optimal inter-domain unicast route, and an optimal multicast static route are selected. One of them is finally selected as the multicast data forwarding path.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Configurations related to VPN instances apply only to PE devices. When configuring the longest match of multicast routes for a VPN instance on a PE, perform the configuration in the VPN instance. In other cases, the longest match is configured in the public network instance.

If the longest match principle is configured for route selection, a multicast device prefers the route with the longest matched mask. If the mask lengths of multiple routes are the same, the device selects a route as the multicast data forwarding path in the order of the static multicast route, inter-domain unicast route, and intra-domain unicast route.

By default, a route with the highest priority is selected.

Perform the following steps on the multicast Router:


#### Procedure

* Configure longest match of multicast routes in the public network instance.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**multicast longest-match**](cmdqueryname=multicast+longest-match)
     
     
     
     Routes are selected based on the longest match rule.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure longest match of multicast routes in the VPN instance.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     The VPN instance view is displayed.
  3. Run [**multicast longest-match**](cmdqueryname=multicast+longest-match)
     
     
     
     Routes are selected based on the longest match rule.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.