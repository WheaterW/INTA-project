Configuring IPv6 Multicast Static Routes
========================================

Multicast static routes are an important basis for Reverse Path Forwarding (RPF) check. By configuring multicast static routes, you can specify an RPF interface and an RPF neighbor for a specified packet source.

#### Context

Multicast static routes implement the following functions, depending on specific applicable environments:

* Changing RPF routes
  
  If the multicast topology is the same as the unicast topology, the transmission path of multicast data is the same as that of unicast data. You can configure multicast static routes on the NE40E to change RPF routes. In this case, a multicast transmission path that is different from the unicast transmission path is created.
* Connecting RPF routes
  
  On the network segment where unicast routes are blocked, when multicast static routes are not configured, packets cannot be forwarded because there is no RPF route. In such a case, you can configure multicast static routes on the NE40E. The system can then generate RPF routes, complete the RPF check, create routing entries, and guide packet forwarding.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 rpf-route-static**](cmdqueryname=ipv6+rpf-route-static) [ **vpn-instance** *vpn-instance-name* ] *source-address* { *mask-length* } { *rpf-nbr6* | { *interface-name* | *interface-type interface-number* } } [ **preference** *preValue* ]
   
   
   
   A multicast static route is created.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the next hop interface is a P2P interface, you can specify *interface-type* *interface-number* in the command to configure an outbound interface (RPF interface).
   
   If the next-hop interface is not a P2P interface, you must specify the *rpf-nbr6* parameter to configure a next hop address (IP address of the RPF neighbor).
3. (Optional) Run [**ipv6 rpf-route-static frr**](cmdqueryname=ipv6+rpf-route-static+frr) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   FRR is configured for the multicast static route.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

After the [**ipv6 rpf-route-static**](cmdqueryname=ipv6+rpf-route-static) command is run, the multicast static route may not take effect because no outbound interface may be unavailable for recursion or the specified interface may be down. Therefore, after configuring the multicast static route, run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) **table-name msr** command to check whether the route is configured successfully or whether the route takes effect.