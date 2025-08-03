(Optional) Configuring a Timer for mLDP P2MP Tunnel Re-optimization
===================================================================

A timer can be set so that mLDP P2MP tunnel re-optimization is triggered at the specified time if the network topology changes.

#### Context

If the network topology changes, to prevent traffic congestion on paths of an mLDP P2MP tunnel that converge on a few links, appropriately perform mLDP P2MP re-optimization. If the upstream or downstream nodes are optional, an mLDP P2MP tunnel is reestablished over the updated path. To set the interval at which mLDP P2MP tunnel re-optimization is performed if the network topology changes, perform the following steps on a node along the mLDP P2MP tunnel:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
3. Run [**mldp p2mp**](cmdqueryname=mldp+p2mp)
   
   
   
   mLDP P2MP is enabled globally.
4. Run [**mldpreoptimize timer**](cmdqueryname=mldpreoptimize+timer) *reoptimize-time-value*
   
   
   
   An mLDP re-optimization timer value is set.
   
   
   
   After this step is performed, *reoptimize-time-value* becomes the interval between the network topology change and the actual mLDP re-optimization.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.