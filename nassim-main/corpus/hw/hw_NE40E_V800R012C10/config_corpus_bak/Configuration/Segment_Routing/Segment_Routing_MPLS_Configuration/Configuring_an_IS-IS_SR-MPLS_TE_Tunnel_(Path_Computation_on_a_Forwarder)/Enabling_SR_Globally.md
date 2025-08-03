Enabling SR Globally
====================

Enabling SR globally on forwarders is a prerequisite for SR-MPLS TE tunnel configuration.

#### Context

SR must be enabled globally before the SR function becomes available.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**segment-routing**](cmdqueryname=segment-routing)
   
   
   
   Segment Routing is enabled globally, and the Segment Routing view is displayed.
3. (Optional) Run [**protected-adj-sid delete-delay**](cmdqueryname=protected-adj-sid+delete-delay)*delay-time*
   
   
   
   A delay in deleting protected adjacency SIDs is configured.
   
   
   
   In SR-MPLS TE scenarios, the corresponding entry cannot be deleted immediately when a protected adjacency SID fails. Otherwise, the backup path becomes invalid. As such, a delay needs to be configured to perform delayed entry deletion.
4. (Optional) Run [**protected-adj-sid update-delay**](cmdqueryname=protected-adj-sid+update-delay)*delay-time*
   
   
   
   A delay in delivering protected adjacency SIDs to the forwarding table is configured.
   
   
   
   The [**protected-adj-sid update-delay**](cmdqueryname=protected-adj-sid+update-delay) command mainly applies to scenarios where the outbound interface associated with a protected adjacency SID changes from Down to Up. For example, if a neighbor fails, the local interface connected to the neighbor goes Down, and the protected adjacency SID associated with the interface becomes invalid, causing traffic to be switched to the backup path for forwarding.
   
   If the neighbor recovers but route convergence has not completed yet, the neighbor may not have the forwarding capability. In this situation, you can run the [**protected-adj-sid update-delay**](cmdqueryname=protected-adj-sid+update-delay) command to configure a delay in delivering the protected adjacency SID to the forwarding table, preventing traffic from being forwarded to the neighbor. This helps avoid packet loss.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.