(Optional) Configure a Device to Globally Block Spoke PWs by Default After Loops Are Detected Based on MAC Flapping
===================================================================================================================

Hub PWs on a hierarchical virtual private LAN service (HVPLS) network may be incorrectly configured as spoke PWs. To eliminate loops after they are detected based on MAC flapping, configure a device to globally block spoke PWs by default.

#### Context

Spoke PWs on an HVPLS network do not support split horizon. Even if MAC flapping-based loop detection is configured, loops may still occur. In this case, configure a device to globally block spoke PWs by default after loops are detected based on MAC flapping. The device then blocks the spoke PWs by default upon detecting loops.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is entered.
2. Run [**loop-detect eth-loop upe-pw default-block enable**](cmdqueryname=loop-detect+eth-loop+upe-pw+default-block+enable)
   
   
   
   The device is enabled to globally block spoke PWs by default after loops are detected based on MAC flapping.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If precise blocking is not enabled on a device, PWs that are not configured with blocking priorities may be blocked at the same time, leading to the loss of user traffic. You are therefore advised to enable precise blocking by running the [**loop-detect eth-loop precise-block enable**](cmdqueryname=loop-detect+eth-loop+precise-block+enable) command. The device then blocks only untrusted interfaces, preventing loss of key traffic.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.