Configuring Basic Detection Functions
=====================================

This section describes how to configure proper MPLS OAM parameters on both ends of a static bidirectional co-routed LSP for network loads.

#### Context

A static bidirectional co-routed LSP is similar to two LSPs in opposite directions. A static bidirectional co-routed LSP, however, is only one LSP. It is mapped to two forwarding entries for traffic in opposite directions and goes Up only when both forwarding entries are available. If the LSP is Down in one direction, the LSP is in the Down state. The two forwarding entries are associated with each other. When the IP forwarding capability is unavailable, any intermediate node can send back a response packet along the original path.

A node functions as both the ingress and egress for a static bidirectional co-routed LSP. Perform the following steps on both ends:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls oam**](cmdqueryname=mpls+oam)
   
   
   
   MPLS OAM is globally enabled.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**mpls-oam**](cmdqueryname=mpls-oam)
   
   
   
   The MPLS-OAM view is displayed.
6. Run [**mpls oam bidirectional-tunnel**](cmdqueryname=mpls+oam+bidirectional-tunnel) { *tunnelName* | *tunnelType* *tunnelNum* } **type** { **cv** | **ffd frequency** { **3** | **10** | **20** | **50** | **100** | **200** | **500** } } [ **auto-protocol** [ **overtime** *overtime-value* ] ] [ **compatibility-mode** *compati-mode-val* ] [ **bdi-frequency** *bdi-frep-value* ] [ **exp** *exp-value* ]
   
   
   
   MPLS OAM for the static bidirectional co-routed LSP is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The same compatibility mode must be set to ensure interworking between different products.
   * When OAM auto protocol extension is enabled, the modification of configurations on the local and peer devices must be in the same mode. Otherwise, the interconnection may fail.
   * If OAM auto protocol extension is enabled and the shared reverse tunnel is specified in Step 6, Step 7 does not need to be performed. After receiving the first CV or FFD packet, the egress automatically records OAM parameters, such as the detection packet type and interval at which detection packets are sent. The egress then uses these parameters to monitor link connectivity.
7. (Optional) Run [**mpls oam bidirectional-tunnel enable**](cmdqueryname=mpls+oam+bidirectional-tunnel+enable) { **send** | **receive** } { *tunnel-type* *tunnel-number* | *tunnel-name* }
   
   
   
   MPLS OAM is enabled for the static bidirectional co-routed LSP.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To prevent detection errors, specify **send** and then **receive** when enabling MPLS OAM, or specify **receive** and then **send** when disabling MPLS OAM. Otherwise, detection error may occur.
8. (Optional) Run [**mpls oam bidirectional-tunnel loss-measure oam-packet loss-ratio**](cmdqueryname=mpls+oam+bidirectional-tunnel+loss-measure+oam-packet+loss-ratio)  **threshold1** *threshold1-value* **threshold2** *threshold2-value* { *tunnel-type*  *tunnel-number* | *tunnel-name* }
   
   
   
   The alarm threshold for OAM packet loss is set.
9. (Optional) Run [**mpls oam bidirectional-tunnel lost-measure single-ended proactive**](cmdqueryname=mpls+oam+bidirectional-tunnel+lost-measure+single-ended+proactive) [ **exp** *exp-value* ] { *tunnel-type*  *tunnel-number* |*tunnel-name* }
   
   
   
   Single-ended proactive frame loss measurement is configured.
10. (Optional) Run [**mpls oam bidirectional-tunnel delay-measure two-way proactive**](cmdqueryname=mpls+oam+bidirectional-tunnel+delay-measure+two-way+proactive) [ **exp** *expvalue* | **packet-size** *packSizeValue* [ **padding-value** { **0** | **1** } ] ] \* {**tunnelType** *tunnelNum* | *tunnelName* }
    
    
    
    Proactive two-way frame delay measurement is configured for a bidirectional LSP.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Exception Handling

If the transmit end has FFD configured and the receive end has **auto-protocol** configured, the receive end receives FFD packets at the interval that the transmit end sends packets. After the following operations are performed, an unknown alarm is automatically reported and cannot be cleared:

1. Run the [**shutdown**](cmdqueryname=shutdown) command on the service interface of the receive end to disable services.
2. Run the [**mpls oam bidirectional-tunnel**](cmdqueryname=mpls+oam+bidirectional-tunnel) command on the transmit end to modify **frequency** *ffd-fre*.
3. Run the [**undo shutdown**](cmdqueryname=undo+shutdown) command on the service interface of the receive end to enable services. Then, the receive end will receive FFD packets at an interval different from the locally recorded one.

In this situation, run the [**undo mpls oam bidirectional-tunnel enable**](cmdqueryname=undo+mpls+oam+bidirectional-tunnel+enable) command on the transmit end to disable FFD. Then, reconfigure FFD.