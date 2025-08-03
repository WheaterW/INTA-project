Enabling LDP Traffic Statistics Collection
==========================================

To check LDP LSP traffic statistics, enable LDP LSP statistics collection on the ingress and transit nodes.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   MPLS is enabled globally, and the MPLS view is displayed.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**mpls traffic-statistics**](cmdqueryname=mpls+traffic-statistics)
   
   
   
   MPLS traffic statistics collection is enabled globally, and the traffic statistics collection view is displayed.
5. Run [**ldp host**](cmdqueryname=ldp+host+ip-prefix) [ **ip-prefix** *ip-prefix* ]
   
   
   
   LDP traffic statistics collection is enabled.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.