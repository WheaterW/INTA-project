(Optional) Activating the CC Function
=====================================

You can activate the CC function to detect link status and report faults in real time without service interruption.

#### Context

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [.*subinterface* ]
   
   
   
   The ATM interface view is displayed.
3. Run [**oam**](cmdqueryname=oam)
   
   
   
   The OAM interface view is displayed.
4. Run [**attribute**](cmdqueryname=attribute) { *start*-*vpi* [ *end-vpi* ] | *vpi/start-vci* [ *vpi/end-vci* ] } { **end-point** | **seg-point** }
   
   
   
   The OAM attributes of the connection point are configured.
   
   When IPoA services are configured on a PVC, the PVC attribute can be configured only as end-point.
   
   When the PVC attribute is **end-point**, the PVC can respond to the OAM F5 loopback cells.
5. Run [**cc**](cmdqueryname=cc) { *start*-*vpi* [ *end-vpi* ] | *vpi*/*start-vci* [ *vpi*/*end-vci* ] } { **end-to-end** | **segment** } { **both** |**sink** |**source** }
   
   
   
   The CC function is activated.
   
   When activating the CC function for a PVC or PVP, note the following:
   
   * Before activating the CC function, configure OAM attributes on both ends.
   * The type of the CC function to be activated must match OAM attributes.
   * During fault recovery, do not deactivate the CC function.
   * If the related NE board is functioning properly, you must stop the CC before deleting the OAM connection.
   * If the parameter **sink** or **both** is configured, a clear alarm will be generated when either of the following conditions is met:
     + The local end receives CC cells from the peer end.
     + The local end receives data cells from the peer end.