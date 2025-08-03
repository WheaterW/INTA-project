(Optional) Configuring a Cluster ID for RRs
===========================================

If a cluster has multiple RRs, you can configure the same cluster ID for these RRs to prevent routing loops.

#### Context

Under some circumstances, more than one RR needs to be configured in a cluster to improve network reliability and prevent single points of failure. The same cluster ID needs to be configured for all the RRs in the cluster to reduce the number of routes received by each RR. This reduces network cost.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

To prevent clients' failures to learn routes reflected by RRs, ensure that the cluster ID of the RRs is different from the router ID of any client. If the cluster ID of the RRs is the same as the router ID of a client, the client will discard received routes.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv6-family**](cmdqueryname=ipv6-family+unicast) **unicast**
   
   
   
   The IPv6 unicast address family view is displayed.
4. Run [**reflector cluster-id**](cmdqueryname=reflector+cluster-id) { *cluster-id-value* | *cluster-id-ipv4* }
   
   
   
   A cluster ID is configured for RRs.
   
   If a cluster has multiple RRs, you can use this command to set the same cluster ID for these RRs.
   
   The [**reflector cluster-id**](cmdqueryname=reflector+cluster-id) command is run only on RRs.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.