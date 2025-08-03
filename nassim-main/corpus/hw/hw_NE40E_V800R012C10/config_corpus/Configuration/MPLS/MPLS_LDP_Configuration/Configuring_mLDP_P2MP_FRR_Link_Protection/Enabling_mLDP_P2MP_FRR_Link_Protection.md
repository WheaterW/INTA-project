Enabling mLDP P2MP FRR Link Protection
======================================

mLDP P2MP FRR link protection can be configured in the MPLS-LDP view.

#### Context

mLDP P2MP FRR link protection configured in the MPLS-LDP view speeds up convergence when link faults are detected, which minimizes traffic loss.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
3. Run [**mldp p2mp**](cmdqueryname=mldp+p2mp)
   
   
   
   mLDP P2MP is enabled globally.
4. Run [**mldp p2mp frr link-protection**](cmdqueryname=mldp+p2mp+frr+link-protection)
   
   
   
   mLDP P2MP FRR link protection is enabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After mLDP FRR link protection is enabled and a link fault is rectified, traffic needs to be switched back after a delay. During the delayed switchback, the backup path must remain unchanged. When the link fault is rectified, IGP route convergence is fast, causing mLDP to recalculate a new backup path. During path calculation, the old backup path is deleted. To prevent packet loss caused by the deletion of the old backup path, run the [**mpls p2mp frr-wtr**](cmdqueryname=mpls+p2mp+frr-wtr) command to set a hold-off time for the maximum IGP cost to a value greater than the mLDP FRR switchback delay.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.