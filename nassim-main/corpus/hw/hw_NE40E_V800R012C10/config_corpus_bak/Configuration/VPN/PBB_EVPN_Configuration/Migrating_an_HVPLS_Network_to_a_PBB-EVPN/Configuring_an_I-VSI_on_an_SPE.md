Configuring an I-VSI on an SPE
==============================

This section describes how to change a common virtual switching instance (VSI) on a superstratum provider edge (SPE) to be a multipoint-to-multipoint (MP2MP) I-VSI and bind the I-VSI to a backbone Ethernet VPN (B-EVPN) instance.

#### Context

During migration from a large-scale hierarchical virtual private LAN service (HVPLS) network to a provider backbone bridge Ethernet VPN (PBB-EVPN), HVPLS and PBB-EVPN will coexist for some time. To switch service traffic from the HVPLS network to the PBB-EVPN, you have to change the VSIs on SPEs to be MP2MP I-VSIs and bind these I-VSIs to B-EVPN instances. The I-tag of an I-VSI must be the same as the service instance identifier (I-SID) of the remote I-EVPN instance. Otherwise, services cannot be forwarded.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name* **i-vsi** **b-evpn-interworking**
   
   
   
   An I-VSI is configured.
3. Run [**pwsignal**](cmdqueryname=pwsignal) **ldp**
   
   
   
   LDP is configured as the signaling protocol for the I-VSI, and its view is displayed.
4. Run [**vsi-id**](cmdqueryname=vsi-id) *vsi-id*
   
   
   
   An ID is configured for the I-VSI.
5. Run [**peer**](cmdqueryname=peer+upe) *peer-address* **upe**
   
   
   
   A UPE is specified as an I-VSI peer.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the VSI view.
7. Run [**ignore-ac-state**](cmdqueryname=ignore-ac-state)
   
   
   
   The I-VSI is configured to ignore attachment circuit (AC) status changes.
8. Run [**pbb i-tag**](cmdqueryname=pbb+i-tag) *i-tag*
   
   
   
   An I-tag is configured for the I-VSI.
   
   The I-tag of an I-VSI must be the same as the I-SID of the remote I-EVPN instance.
9. Run [**pbb binding b-evpn**](cmdqueryname=pbb+binding+b-evpn) *vpn-instance-name*
   
   
   
   The I-VSI is bound to the specified B-EVPN instance.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.