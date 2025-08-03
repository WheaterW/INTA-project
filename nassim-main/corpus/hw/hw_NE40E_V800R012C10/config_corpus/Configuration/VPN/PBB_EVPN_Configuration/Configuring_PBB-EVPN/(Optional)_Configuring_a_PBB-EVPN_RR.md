(Optional) Configuring a PBB-EVPN RR
====================================

Configuring a provider backbone bridge Ethernet VPN (PBB-EVPN) route reflector (RR) helps reduce the number of required BGP EVPN peer relationships, and therefore conserves network resources.

#### Context

In an autonomous system (AS), one Router functions as an RR, and other Routers serve as RR clients. The clients establish BGP EVPN peer relationships with the RR. The RR and its clients form a cluster. The RR reflects routes among the clients, and the clients do not need to establish IBGP connections with each other.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
   
   
   
   The BGP-EVPN address family view is displayed.
4. Run [**peer**](cmdqueryname=peer+reflect-client) { *ipv4-address* | *group-name* } [**reflect-client**](cmdqueryname=reflect-client)
   
   
   
   An RR and its clients are specified.
   
   
   
   The Router where the [**peer reflect-client**](cmdqueryname=peer+reflect-client) command is run serves as the RR and the specified peers or peer groups serve as clients.
5. (Optional) Run [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients)
   
   
   
   Route reflection among clients through the RR is disabled.
   
   
   
   If the clients of an RR have established full-mesh connections with each other, you can run the [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients) command to disable route reflection among these clients through the RR to reduce the link cost. The [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients) command applies only to RRs.
6. (Optional) Run [**reflector cluster-id**](cmdqueryname=reflector+cluster-id) { *cluster-id-value* | *cluster-id-ipv4* }
   
   
   
   A cluster ID is configured for the RR.
   
   
   
   If a cluster has multiple RRs, you can use this command to set the same cluster ID for these RRs to prevent routing loops.
   
   The [**reflector cluster-id**](cmdqueryname=reflector+cluster-id) command applies only to RRs.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.