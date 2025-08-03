Configuring Basic Detection Functions
=====================================

This section describes how to configure proper MPLS OAM parameters on both ends of an associated bidirectional LSP for network loads.

#### Context

Associated bidirectional LSPs are classified into the following types:

* Dynamic associated bidirectional LSP
* Static associated bidirectional LSP

A forward RSVP-TE LSP and a reverse RSVP-TE LSP between two nodes are established. Each LSP is bound to the ingress of its reverse LSP. The two LSPs then form a dynamic associated bidirectional LSP. If two static unidirectional CR-LSPs are deployed, the CR-LSPs can form a static associated bidirectional LSP. The associated bidirectional LSP is used to prevent traffic congestion. If a fault occurs on one end, the other end is notified of the fault so that both ends trigger traffic switchovers, preventing service interruptions.

For details about the differences between dynamic associated bidirectional LSPs and static associated bidirectional LSPs, see [Configuring an Associated Bidirectional CR-LSP](dc_vrp_te-p2p_cfg_0200.html).

A node functions as both the ingress and egress for an associated bidirectional LSP. Perform the following steps on both ends:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls oam**](cmdqueryname=mpls+oam)
   
   
   
   MPLS OAM is globally enabled.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run either of the following commands:
   
   
   * If a reverse tunnel is not specified, run the [**mpls oam ingress**](cmdqueryname=mpls+oam+ingress) **tunnel** *tunnel-number* [ **type** { **cv** | **ffd** **frequency** *ffd-fre* } ] [ **backward-lsp** **share** ] [ **compatibility-mode** { **ptn-mode** | **router-mode** } ] [ **bdi-frequency** { **detect-freq** | **per-second** } ] [ **exp** *exp-value* ] command to configure MPLS OAM parameters for the ingress.
   * If a reverse tunnel is specified, run the [**mpls oam ingress**](cmdqueryname=mpls+oam+ingress) **tunnel** *tunnel-number* [ **type** { **cv** | **ffd** **frequency** *ffd-fre* } ] [ **backward-lsp** { **lsp-name** *lsp-name* | **lsr-id** *rev-ingress-lsr-id* **tunnel-id** *rev-tunnel-id* | **share** } ] [ **compatibility-mode** { **ptn-mode** | **router-mode** } ] [ **bdi-frequency** { **detect-freq** | **per-second** } ] [ **exp** *exp-value* ] command to configure MPLS OAM parameters for the ingress.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If the source end of a static LSP is configured to work in shared mode, a TTSI must be configured on the destination end. If a TTSI is not configured on the destination end, BDI packets cannot be received.
   * It is recommended that you configure a reverse LSP for ingress OAM to verify BDI packets.
6. Run [**mpls oam ingress enable**](cmdqueryname=mpls+oam+ingress+enable) { *tunnel-type* *tunnel-number* | *tunnel-name* }
   
   
   
   OAM is enabled on the ingress.
7. Run either of the following commands:
   
   
   * To enable OAM auto protocol extension, run the [**mpls oam egress**](cmdqueryname=mpls+oam+egress) { **lsp-name** *lsp-name* | **lsr-id** *ingress-lsr-id* **tunnel-id** *tunnel-id* } **auto-protocol** [ **overtime** *over-time* ] [ **backward-lsp** { **tunnel** *tunnel-id* | *tunnel-name* } [ **private** | **share** ] ] [ **bdi-frequency** { **detect-freq** | **per-second** } ] command.
   * To configure OAM parameters when OAM auto protocol extension is disabled on the egress, run the [**mpls oam egress**](cmdqueryname=mpls+oam+egress) { **lsp-name** *lsp-name* | **lsr-id** *ingress-lsr-id* **tunnel-id** *tunnel-id* } [ **type** { **cv** | **ffd frequency** { **3** | **10** | **20** | **50** | **100** | **200** | **500** } } ] [ **backward-lsp** { *tunnel-type* *tunnel-number* | *tunnel-name* } [ **share** | **private** ] ] [ **bdi-frequency** *bdi-frep-value* ] command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If OAM auto protocol extension is enabled in Step 7, skip Step 8. After receiving the first CV or FFD packet, the egress automatically records OAM parameters, such as the detection packet type and interval at which detection packets are sent. The egress then uses these parameters to monitor link connectivity.
   * It is recommended that you configure a reverse LSP for egress OAM to send BDI packets.
8. (Optional) Run [**mpls oam egress enable**](cmdqueryname=mpls+oam+egress+enable) { **lsp-name** *lsp-name* | **lsr-id** *ingress-lsr-id* **tunnel-id** *tunnel-id* }
   
   
   
   OAM is enabled on the egress.
9. (Optional) Run [**mpls oam ingress loss-measure oam-packet loss-ratio**](cmdqueryname=mpls+oam+ingress+loss-measure+oam-packet+loss-ratio){ **threshold1** *threshold1-value* | **threshold2** *threshold2-value* } \* **tunnel** *tunnel-number*
   
   
   
   The packet loss alarm threshold on the ingress is set.
10. (Optional) Run [**mpls oam ingress lost-measure single-ended proactive**](cmdqueryname=mpls+oam+ingress+lost-measure+single-ended+proactive)[ **exp** *exp-value* ] **tunnel** *interface-number*
    
    
    
    The single-ended packet loss measurement is enabled on the ingress.
11. (Optional) Run [**mpls oam egress loss-measure oam-packet loss-ratio**](cmdqueryname=mpls+oam+egress+loss-measure+oam-packet+loss-ratio){ **threshold1** *threshold1-value* | **threshold2** *threshold2-value* } \* { **lsp-name** *lsp-name* | **lsr-id** *lsr-id* **tunnel-id** *tunnel-id* }
    
    
    
    The packet loss alarm threshold is set on the egress.
12. (Optional) Run [**mpls oam ingress delay-measure two-way proactive**](cmdqueryname=mpls+oam+ingress+delay-measure+two-way+proactive)[ **exp** *exp-value* | **packet-size** *packet-size-value* | [ **padding-value** { **0** | **1** } ] ] \* { *tunnel-type* *tunnel-number* | *tunnel-name* }
    
    
    
    The two-way delay measurement is enabled on the ingress.
13. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Exception Handling

If the transmit end has FFD configured and the receive end has **auto-protocol** configured, the receive end receives FFD packets at the interval that the transmit end sends packets. After the following operations are performed, an unknown alarm is automatically reported and cannot be cleared:

1. Run the [**shutdown**](cmdqueryname=shutdown) command on the service interface of the receive end to disable services.
2. Run the [**mpls oam ingress**](cmdqueryname=mpls+oam+ingress) command on the transmit end to modify the FFD packet sending interval by specifying the **frequency** *ffd-fre* parameter. The interval on the receive end remains unchanged.
3. Run the [**undo shutdown**](cmdqueryname=undo+shutdown) command on the service interface of the receive end to enable services. Then, the receive end will receive FFD packets at an interval different from the locally recorded one.

In this situation, run the [**undo mpls oam ingress enable**](cmdqueryname=undo+mpls+oam+ingress+enable) command on the transmit end to disable FFD. Then, reconfigure FFD.