(Optional) Setting the Cluster ID of a Route Reflector
======================================================

When there are multiple route reflectors in a cluster, you need to configure the same cluster ID for all the route reflectors in this cluster to avoid routing loops.

#### Context

To enhance network reliability and avoid single points of failure, more than one route reflector can be configured in a cluster. In this case, you need to set the same cluster ID for all the route reflectors in the same cluster. This can reduce the number of routes to be received by each route reflector and thereby save the memory.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

To ensure that a client can learn the routes reflected by a route reflector, the cluster ID of the route reflector must be different from the router ID of the client. If they are the same, the client discards the received routes.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
   
   
   
   The IPv4 unicast address family view is displayed.
4. Run [**reflector cluster-id**](cmdqueryname=reflector+cluster-id) { *cluster-id-value* | *cluster-id-ipv4* }
   
   
   
   The cluster ID of a route reflector is set.
   
   
   
   When there are multiple route reflectors in a cluster, you need to run the command to configure the same *cluster-id* for all the route reflectors in this cluster.
   
   The [**reflector cluster-id**](cmdqueryname=reflector+cluster-id) command can be configured only on route reflectors.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.