Configuring a VSI and BGP Signaling
===================================

This section describes how to configure BGP VPLS, specifically, a VSI with BGP signaling.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name* [ **auto** | **static** ]
   
   
   
   A VSI is created.
3. (Optional) Run [**description**](cmdqueryname=description) *description*
   
   
   
   A description is configured for the VSI.
4. (Optional) Run [**encapsulation**](cmdqueryname=encapsulation) { **ethernet** | **vlan** }
   
   
   
   An encapsulation mode is set for the VSI.
   
   
   
   * VSIs have two encapsulation modes: Ethernet and VLAN. On the public network, packets encapsulated in Ethernet mode do not carry any VLAN tags, but packets encapsulated in VLAN mode do.
   * The two ends of a PW must use the same encapsulation mode.
5. Run [**pwsignal**](cmdqueryname=pwsignal) **bgp**
   
   
   
   BGP is configured as the signaling protocol for the VSI, and the VSI-BGP view is displayed.
6. (Optional) Run [**control-word enable**](cmdqueryname=control-word+enable)
   
   
   
   The control word function is enabled for the VSI.
7. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
   
   
   
   An RD is set for the VSI.
   
   After BGP is configured as a PW signaling protocol, an RD must be set so that other configurations can be performed.
8. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-16> [ **both** | **export-extcommunity** | **import-extcommunity** ]
   
   
   
   A VPN target is configured for the VSI.
   
   
   
   When using this command, note the mapping between the VPN target attribute on the local end and that on the remote end. Specifically:
   
   * **export-extcommunity** on the local end must be the same as **import-extcommunity** on the remote end
   * .**import-extcommunity** on the local end must be the same as **export-extcommunity** on the remote end.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If VPN targets are added or modified in batches, a large number of route update packets will be received from the remote end. To resolve this issue, configuring a BGP VSI in two-phase validation mode is recommended.
9. Run [**site**](cmdqueryname=site) *site-id* [ **range** *site-range* ] [ **default-offset** { **0** | **1** } ]
   
   
   
   A site ID is set for the VSI.
   
   
   
   The site IDs on PEs in the same VSI must be different. The local site ID must be less than remote *site-range* plus remote **default-offset**, but greater than or equal to remote **default-offset**.
10. (Optional) Run [**peer**](cmdqueryname=peer) *peer-address* **remote-site** *remote-site-id* **pw** *pw-name*
    
    
    
    A PW is created, and the VSI-BGP-PW view is displayed.
    
    
    
    If a PW has been created, you can run the [**pw**](cmdqueryname=pw) *pw-name* command to enter the VSI-BGP-PW view corresponding to *pw-name*.
11. (Optional) Run the following commands to configure BUM traffic suppression for the BGP VPLS VSI:
    
    
    * Run the [**broadcast-suppression**](cmdqueryname=%7B+unknown-unicast-suppression+%7C+broadcast-suppression+%7C+multicast-suppression+%7C+unicast-suppression+%7D+cir) **cir** *cir-value* [ **cbs** *cbs-value* ] command to set the maximum traffic volume of broadcast traffic that is allowed to pass.
    * Run the [**multicast-suppression**](cmdqueryname=%7B+unknown-unicast-suppression+%7C+broadcast-suppression+%7C+multicast-suppression+%7C+unicast-suppression+%7D+cir) **cir** *cir-value* [ **cbs** *cbs-value* ] command to set the maximum volume of multicast traffic that is allowed to pass.
    * Run the [**unknown-unicast-suppression**](cmdqueryname=%7B+unknown-unicast-suppression+%7C+broadcast-suppression+%7C+multicast-suppression+%7C+unicast-suppression+%7D+cir) **cir** *cir-value* [ **cbs** *cbs-value* ] command to set the maximum unknown-unicast traffic that is allowed to pass.
    
    If the actual traffic rate reaches the configured maximum limit, the excess packets are discarded.
12. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.