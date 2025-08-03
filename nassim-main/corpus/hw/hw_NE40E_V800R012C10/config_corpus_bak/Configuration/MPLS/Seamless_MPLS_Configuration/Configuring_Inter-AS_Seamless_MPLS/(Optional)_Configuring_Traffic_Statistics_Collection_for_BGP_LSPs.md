(Optional) Configuring Traffic Statistics Collection for BGP LSPs
=================================================================

To check the traffic statistics of BGP LSPs, configure traffic statistics collection on the ingress and transit nodes of the BGP LSPs.

#### Context

Traffic statistics collection for BGP LSPs allows you to query and monitor the traffic statistics of BGP LSPs in real time. To enable this function, run the [**bgp host**](cmdqueryname=bgp+host) command.![](../../../../public_sys-resources/note_3.0-en-us.png) 

Traffic statistics collection for BGP LSPs takes effect only for BGP LSPs of which the FEC mask length is 32 bits.




#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   MPLS is enabled globally, and the MPLS view is displayed.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**mpls traffic-statistics**](cmdqueryname=mpls+traffic-statistics)
   
   
   
   MPLS traffic statistics collection is enabled globally, and the traffic statistics collection view is displayed.
5. Run [**bgp host**](cmdqueryname=bgp+host+ip-prefix) [ **ip-prefix** *ip-prefix-name* ]
   
   
   
   Traffic statistics collection is enabled for BGP LSPs.
   
   
   
   If the **ip-prefix** parameter needs to be set to limit the range of BGP LSPs for which traffic statistics collection is to be enabled, run the [**ip ip-prefix**](cmdqueryname=ip+ip-prefix) command to create an IP prefix list first.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.