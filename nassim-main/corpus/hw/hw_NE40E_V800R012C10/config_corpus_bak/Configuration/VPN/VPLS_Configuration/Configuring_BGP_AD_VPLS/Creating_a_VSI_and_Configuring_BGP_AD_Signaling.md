Creating a VSI and Configuring BGP AD Signaling
===============================================

When configuring BGP AD VPLS, you need to create a VSI and configure BGP AD signaling.

#### Context

When configuring BGP AD VPLS, you need to create a VSI, enable automatic VPLS member discovery and automatic PW deployment, configure BGP AD signaling, and set the VPLS ID and VPN targets in the VSI-BGP AD view on PEs.

Perform the following steps on the endpoint PEs of a PW.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
   
   
   
   A VSI is created.
3. (Optional) Run [**description**](cmdqueryname=description) *description*
   
   
   
   A description is configured for the VSI.
4. Run [**encapsulation**](cmdqueryname=encapsulation) { **ethernet** | **vlan** }
   
   
   
   An encapsulation mode is configured for the VSI.
   
   
   
   * VSIs have two encapsulation modes: Ethernet and VLAN. When being transmitted over the public network, packets encapsulated in Ethernet mode cannot carry any VLAN tags, whereas packets encapsulated in VLAN mode must carry VLAN tags.
   * The two ends of a PW must use the same encapsulation mode.
5. Run [**bgp-ad**](cmdqueryname=bgp-ad)
   
   
   
   Automatic VPLS member discovery and automatic PW deployment are enabled for the VSI, and the VSI-BGP AD view is displayed.
6. Run [**vpls-id**](cmdqueryname=vpls-id) *vplsIdValue*
   
   
   
   A VPLS ID is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * By default, a BGP AD VPLS uses its VPLS ID value as its RD value. If the VPLS ID has been set, the RD does not need to be set. The VSI ID is equal to the local LSR ID and does not need to be set.
   * The VPLS IDs for VSIs in the same VPLS domain must be the same.
7. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* & <1-16> [ **both** | **export-extcommunity** | **import-extcommunity** ]
   
   
   
   VPN targets are configured for the VSI.
   
   
   
   Note that the mapping between local and remote VPN targets must be correct:
   
   * **export-extcommunity** on the local end is the same as **import-extcommunity** on the peer end.
   * **import-extcommunity** on the local end is the same as **export-extcommunity** on the peer end.
   
   Traffic can be transmitted bidirectionally only if the preceding two conditions are both met. If only one condition is met, traffic is transmitted only unidirectionally. For convenience, these four parameters are usually set to the same value.
8. (Optional) Run [**pw spoke-mode**](cmdqueryname=pw+spoke-mode)
   
   
   
   The PW attribute of the BGP AD VSI is set to spoke.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command is generally used in star or tree network topologies where one PE serves as the hub PE and the other PEs act as spoke PEs. The hub PE can be a server or an authentication device, among others. This command functions similarly to configuring a peer PE as a UPE on an LDP HVPLS network. The difference lies in that this command configures the attributes of all PWs in the BGP AD VSI as spoke.
9. Run [**peer**](cmdqueryname=peer) *peer-address* **pw** *pw-name*
   
   
   
   A PW is created, and its view is displayed.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.