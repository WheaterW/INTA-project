(Optional) Enabling LDP Loop Detection Negotiation
==================================================

If the peer device is enabled with LDP loop detection, the local device must be enabled with the capability of negotiating LDP loop detection before it can set up an LDP session with the peer device.

#### Usage Scenario

The NE40E does not support LDP loop detection. To establish an LDP session with a device enabled with LDP loop detection, the NE40E needs to be enabled with the capability of negotiating LDP loop detection.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
3. Run [**loop-detect**](cmdqueryname=loop-detect)
   
   
   
   LDP loop detection negotiation is enabled. This allows the device to negotiate LDP parameters during the initialization phase and establish an LDP session with a peer device that is enabled with LDP loop detection.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the [**loop-detect**](cmdqueryname=loop-detect) command is run, the NE40E obtains the capability of negotiating LDP loop detection but still does not support LDP loop detection.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.