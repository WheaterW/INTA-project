(Optional) Enabling the Upstream CAR Function and Statistics Function for Layer 3 Packets
=========================================================================================

You can implement CAR and the statistics function for Layer 3 packets to adjust the link bandwidth.

#### Context

Perform the following steps on the Router:

In VS mode, this configuration is supported only by the admin VS.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**qos link-adjustment**](cmdqueryname=qos+link-adjustment) { **link-layer-exclude** | **l2tp-layer-exclude** } [ **slot** *slot-id* ]
   
   
   
   The upstream CAR function and statistics function are enabled for Layer 3 packets.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The parameter **link-layer-exclude** cannot be specified to a slot.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.