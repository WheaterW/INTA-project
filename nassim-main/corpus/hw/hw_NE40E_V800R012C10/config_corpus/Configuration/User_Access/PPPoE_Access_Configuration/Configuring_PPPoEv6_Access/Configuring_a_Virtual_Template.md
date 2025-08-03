Configuring a Virtual Template
==============================

Layer 2 protocols cannot directly communicate with each other. As such, you need to create a virtual template (VT) before configuring PPPoE access.

#### Context

Layer 2 protocols, such as Point-to-Point Protocol (PPP) can communicate only over a virtual access (VA) session. A VA session, however, cannot be manually created or configured. Instead, a VA session is automatically generated after PPP over Ethernet (PPPoE) services are configured and PPPoE parameters are defined in a VT.

Based on parameters defined in a VT, a device can automatically create VA interfaces for Layer 2 communication.

* PPP packets are encapsulated based on parameters defined in a VT. A VT defines NCP parameters, such as IP addresses and upper-layer application protocols.
* A VA session transmits data between the local and remote ends based on parameters defined in a VT.

When a VT is used for PPPoE services, the link layer protocol can only be PPP, and the network layer protocol can only be IP.

Before deleting a VT, ensure that the VT is not in use and the VA session automatically generated upon VT creation has been deleted.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface virtual-template**](cmdqueryname=interface+virtual-template) *virtual-template-number*
   
   
   
   A VT is created and its view is displayed, or the view of an existing VT is displayed.
3. Run [**ppp authentication-mode**](cmdqueryname=ppp+authentication-mode) { **auto** | { **pap** | **chap** | **mschapv1** | **mschapv2** } \* }
   
   
   
   A PPP authentication mode used by the local device to authenticate the remote device is configured.
4. (Optional) Run [**ppp chap user**](cmdqueryname=ppp+chap+user) *user-name*
   
   
   
   A local username is configured.
5. (Optional) Configure PPP negotiation parameters.
   
   
   * Run [**ppp timer**](cmdqueryname=ppp+timer) { **negotiate** *seconds* | **retransmit** *retry-times* } \*
     
     A PPP negotiation timeout period and the maximum number of retransmissions allowed are configured.
   * Run [**ppp delay-lcp-negotiation**](cmdqueryname=ppp+delay-lcp-negotiation) [ **force** ]
     
     Delayed LCP packet transmission is configured.
   * Run [**ppp keepalive**](cmdqueryname=ppp+keepalive) { **interval** *interval-time* | **retransmit** *times* | **response-timeout** *response-timeout-time* } \* [ **datacheck** | **no-datacheck** ]
     
     A PPP detection interval and the maximum number of retransmissions allowed are configured.
   * Run [**ppp keepalive adjustment**](cmdqueryname=ppp+keepalive+adjustment) { **system-state** | **retransmit** }
     
     Adjustment of the number of PPP detections is enabled.
   * Run [**mtu**](cmdqueryname=mtu) *mtu*
     
     An MTU is configured in the VT.
   * Run [**ppp mru**](cmdqueryname=ppp+mru) *mru*
     
     An MRU is configured for PPP negotiation.
   * Run [**pppoe-motm**](cmdqueryname=pppoe-motm) *motm-value*
     
     The device is configured to encapsulate clock synchronization information to the MOTM tag in a PPPoE active discovery message (PADM).
   * Run [**quit**](cmdqueryname=quit)
     
     Return to the system view.
   * Run [**pppoe ppp-max-payload enable**](cmdqueryname=pppoe+ppp-max-payload+enable)
     
     The device is enabled to negotiate the MRU in compliance with standard protocols.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.