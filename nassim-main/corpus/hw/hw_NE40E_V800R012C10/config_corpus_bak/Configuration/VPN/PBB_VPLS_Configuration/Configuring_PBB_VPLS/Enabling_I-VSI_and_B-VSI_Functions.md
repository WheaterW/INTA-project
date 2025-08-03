Enabling I-VSI and B-VSI Functions
==================================

Enabling I-VSI and B-VSI functions is the prerequisite for configuring PBB VPLS.

#### Procedure

* Enable the I-VSI function.
  
  Use either of the following methods:
  + Enable the I-VSI function while creating a VSI.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] **i-vsi** **p2p**
       
       A P2P I-VSI is configured.
    3. Run [**pwsignal**](cmdqueryname=pwsignal) **ldp**
       
       LDP is configured as the signaling protocol for the I-VSI.
    4. Run [**vsi-id**](cmdqueryname=vsi-id) *vsi-id*
       
       An ID is configured for the I-VSI.
       
       The ID of an I-VSI does not participate in PW negotiation and therefore only needs to be locally unique.
       
       - The local I-VSI and B-VSI must have different IDs.
       - The local and remote I-VSIs can have either the same ID or different IDs.
    5. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
  + Enable the I-VSI function after creating a VSI.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ]
       
       A VSI is created.
    3. Run [**pwsignal**](cmdqueryname=pwsignal) **ldp**
       
       LDP is configured as the signaling protocol for the VSI.
    4. Run [**vsi-id**](cmdqueryname=vsi-id) *vsi-id*
       
       An ID is configured for the VSI.
       
       The ID of an I-VSI does not participate in PW negotiation and therefore only needs to be locally unique.
       
       - The local I-VSI and B-VSI must have different IDs.
       - The local and remote I-VSIs can have either the same ID or different IDs.
    5. Run [**quit**](cmdqueryname=quit)
       
       Exit from the VSI-LDP view.
    6. Run [**pbb i-vsi enable**](cmdqueryname=pbb+i-vsi+enable)
       
       The I-VSI function is enabled.
    7. Run [**pbb service-type p2p**](cmdqueryname=pbb+service-type+p2p)
       
       A service type is configured for the I-VSI.
    8. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
* Enable the B-VSI function.
  
  Use either of the following methods:
  + Enable the B-VSI function while creating a VSI.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] **b-vsi**
       
       A B-VSI is created.
    3. Run [**pwsignal**](cmdqueryname=pwsignal) **ldp**
       
       LDP is configured as the signaling protocol for the B-VSI.
    4. Run [**vsi-id**](cmdqueryname=vsi-id) *vsi-id*
       
       An ID is configured for the B-VSI.
       
       - The ID of a B-VSI must be locally unique.
       - The ID of a B-VSI participates in the PW negotiation. In a VPLS domain, the local and remote B-VSIs must have the same ID.
    5. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
  + Enable the B-VSI function after a VSI is created.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ]
       
       A VSI is created.
    3. Run [**pwsignal**](cmdqueryname=pwsignal) **ldp**
       
       LDP is configured as the signaling protocol for the VSI.
    4. Run [**vsi-id**](cmdqueryname=vsi-id) *vsi-id*
       
       An ID is configured for the VSI.
       
       The ID of a B-VSI does not participate in PW negotiation and therefore only needs to be locally unique.
       
       - The ID of a B-VSI must be locally unique.
       - The ID of a B-VSI participates in the PW negotiation. In a VPLS domain, the local and remote B-VSIs must have the same ID.
    5. Run [**quit**](cmdqueryname=quit)
       
       Exit from the VSI-LDP view.
    6. Run [**pbb b-vsi enable**](cmdqueryname=pbb+b-vsi+enable)
       
       The B-VSI function is enabled.
    7. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.