(Optional) Configuring PW APS Parameters
========================================

This section describes how to configure PW APS parameters, such as the switchback mode, hold time for PW switchover, and WTR time for PW switchback. In network O&M, you can manually trigger PW switching with commands.

#### Context

By default, when the primary PW fails, the secondary PW quickly takes over traffic. After the primary PW recovers, traffic switches back to the primary PW. To prevent frequent service switching caused by PW flapping, configure a hold time for PW switchover and a WTR time for PW switchback.

Besides PW APS triggered by PW faults, you can manually trigger PW switching with commands in network O&M.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pw-aps**](cmdqueryname=pw-aps) *apsId* [ **frr** ]
   
   
   
   The PW APS view is displayed.
3. Run [**operation-type**](cmdqueryname=operation-type) { **revertive** | **non-revertive** }
   
   
   
   The switchback mode for the PW APS instance is configured.
   
   
   
   Usually, the revertive mode is used. After the primary PW recovers, services quickly switch back to the primary PW. To reduce traffic switching times and maintain service topology stability, use the non-revertive mode.
4. Run [**holdoff**](cmdqueryname=holdoff) *holdoffTime*
   
   
   
   A hold time for PW switchover is configured for the PW APS instance.
   
   
   
   By default, when the primary PW fails, the secondary PW quickly takes over traffic. To prevent frequent traffic switching caused by primary PW flapping or detection mechanism errors, configure a hold time for PW switchover.
5. Run [**wtr**](cmdqueryname=wtr) *wtr-value*
   
   
   
   A WTR time is configured for the PW APS instance.
   
   
   
   By default, traffic switches back to the primary PW after the primary PW recovers. To prevent traffic loss caused by primary PW flapping, configure a WTR time for PW switchback.
6. Run [**protect-switch**](cmdqueryname=protect-switch) { **force** | **clear** | **lock** | **manual** }
   
   
   
   A manual request is configured for the PW APS instance.
   
   
   
   This operation allows you to switch traffic to the secondary PW or lock traffic to the primary PW for link monitoring and debugging in network O&M. After the maintenance operations are complete, delete this configuration.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.