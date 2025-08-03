Configuring Basic Detection Functions
=====================================

This section describes how to configure proper MPLS OAM parameters on both ends of a PW for network loads.

#### Context

Perform the following steps on both ends:


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
6. Run [**mpls oam l2vc**](cmdqueryname=mpls+oam+l2vc) **peer-ip** *peer-ip* **vc-id** *vc-id* **vc-type** *vc-type* [ **remote-peer-ip** *remote-peer-ip* **remote-vc-id** *remote-vc-id* **remote-vc-type** *remote-vc-type* ] **type** { **cv** | **ffd** **frequency** { **3** | **10** | **20** | **50** | **100** | **200** | **500** } } [ **auto-protocol** [ **overtime** *overtime* ] ] [ **compatibility-mode** *compati-mode-val* ] [ **bdi-frequency** *bdi-freq-val* ] [ **exp** *exp-value* ]
   
   
   
   MPLS OAM parameters are configured on nodes at both ends of the PW.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If OAM auto protocol extension is enabled in Step 6, Step 7 does not need to be performed. When OAM auto protocol extension is enabled, a device automatically sends or receives OAM detection packets.
   * After receiving the first CV or FFD packet, the egress automatically records OAM parameters, such as the detection packet type and interval at which detection packets are sent. The egress then uses these parameters to monitor link connectivity.
   * The same compatibility mode must be set to ensure interworking between different products.
   * When OAM auto protocol extension is enabled, the modification of configurations on the local and peer devices must be in the same mode. Otherwise, the interconnection may fail.
7. (Optional) Run [**mpls oam l2vc enable**](cmdqueryname=mpls+oam+l2vc+enable) { **send** | **receive** } **peer-ip** *peer-ip* **vc-id** *vc-id* **vc-type** *vc-type*
   
   
   
   MPLS OAM is enabled on the node at each end of the PW.
8. (Optional) Run [**mpls oam l2vc loss-measure oam-packet loss-ratio**](cmdqueryname=mpls+oam+l2vc+loss-measure+oam-packet+loss-ratio) { **threshold1** *threshold1-value* | **threshold2** *threshold2-value* } \* **peer-ip** *peer-ip* **vc-id** *vc-id* **vc-type** *vc-type*
   
   
   
   The packet loss alarm threshold of OAM packets is set.
9. (Optional) Run [**mpls oam l2vc lost-measure single-ended proactive**](cmdqueryname=mpls+oam+l2vc+lost-measure+single-ended+proactive) [ **exp** *exp-value* ] **peer-ip** *peer-ip* **vc-id** *vc-id* **vc-type** *vc-type*
   
   
   
   The single-ended packet loss measurement of PW MPLS OAM is enabled.
10. (Optional) Run [**mpls oam l2vc delay-measure two-way proactive**](cmdqueryname=mpls+oam+l2vc+delay-measure+two-way+proactive) [ **exp** *exp-value* | **packet-size** *packet-size-value* [ **padding-value** { **0** | **1** } ] ] \* **peer-ip** *peer-ip* **vc-id** *vc-id* **vc-type** *vc-type*
    
    
    
    The proactive PW two-way delay measurement is enabled.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Exception Handling

If the transmit end has FFD configured and the receive end has **auto-protocol** configured, the receive end receives FFD packets at the interval that the transmit end sends packets. After the following operations are performed, an unknown alarm is automatically reported and cannot be cleared:

1. Run the [**shutdown**](cmdqueryname=shutdown) command on the service interface of the receive end to disable services.
2. Run the [**mpls oam l2vc**](cmdqueryname=mpls+oam+l2vc) command on the transmit end to modify **frequency** *ffd-fre*.
3. Run the [**undo shutdown**](cmdqueryname=undo+shutdown) command on the service interface of the receive end to enable services. Then, the receive end will receive FFD packets at an interval different from the locally recorded one.

In this situation, run the [**undo mpls oam l2vc enable**](cmdqueryname=undo+mpls+oam+l2vc+enable) command on the transmit end to disable FFD. Then, reconfigure FFD.