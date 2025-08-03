(Optional) Enabling the Capability of Establishing a Best-Effort Path for an mLDP P2MP Tunnel
=============================================================================================

The capability of establishing a best-effort path for an mLDP P2MP tunnel can be enabled to rectify link faults of outbound interfaces, which helps speed up route convergence and reduce traffic loss.

#### Context

On a network with the mLDP MBB capability enabled, if mLDP FRR is disabled and an outbound interface fails, the capability of establishing a best-effort path for an mLDP P2MP tunnel can be enabled to resolve the problem.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
3. Run [**mldp p2mp**](cmdqueryname=mldp+p2mp)
   
   
   
   mLDP P2MP is enabled globally.
4. Run [**mldp p2mp best-effort**](cmdqueryname=mldp+p2mp+best-effort)
   
   
   
   The capability of establishing a best-effort path for an mLDP P2MP tunnel is enabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.