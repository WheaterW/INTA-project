Configuring Multicast Static Routes
===================================

Multicast static routes are an important basis of the Reverse Path Forwarding (RPF) check. By configuring multicast static routes, you can specify an RPF interface and an RPF neighbor for the specific source of packets.

#### Context

Multicast static routes implement the following functions, depending on specific applicable environments:

* Change RPF routes.
  
  If the multicast topology is the same as the unicast topology, the transmission path of multicast data is the same as that of unicast data. You can configure multicast static routes on the NE40E to change the RPF routes. Thus, a transmission path dedicated for the multicast data is established, which is different from the transmission path of unicast data.
* Connect RPF routes.
  
  On the network segment where unicast routes are blocked, when multicast static routes are not configured, packets cannot be forwarded because there is no RPF route. In such a case, you can configure multicast static routes on the NE40E. The system can then generate RPF routes, complete the RPF check, create routing entries, and guide packet forwarding.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip rpf-route-static**](cmdqueryname=ip+rpf-route-static) [ **vpn-instance** *vpn-instance-name* ] *source-address* { *mask* | *mask-length* } { *rpf-nbr* | { *interface-name* | *interface-type interface-number* } } [ **preference** *preValue* ]
   
   
   
   A multicast static route is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the next-hop interface is a P2P interface, you can configure an outbound interface (RPF interface) by specifying the *interface-type* *interface-number* parameter in the command.
   
   If the next-hop interface is not a P2P interface, you must configure a next-hop address (IP address of the RPF neighbor) by specifying the *rpf-nbr* parameter in the command.
3. (Optional) Run [**ip rpf-route-static frr**](cmdqueryname=ip+route-static+frr+vpn-instance) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   FRR is configured for the multicast static route.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

After the [**ip rpf-route-static**](cmdqueryname=ip+rpf-route-static) command is configured, the multicast static route may not take effect. This is because the outbound interface may be unavailable for recursion or the specified interface may be Down. Therefore, after configuring the multicast static route, run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) **table-name msr** command to check whether the route is configured successfully.