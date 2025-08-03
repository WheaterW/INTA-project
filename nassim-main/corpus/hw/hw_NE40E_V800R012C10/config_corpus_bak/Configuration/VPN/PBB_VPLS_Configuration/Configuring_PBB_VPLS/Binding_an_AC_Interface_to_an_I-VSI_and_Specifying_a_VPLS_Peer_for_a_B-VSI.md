Binding an AC Interface to an I-VSI and Specifying a VPLS Peer for a B-VSI
==========================================================================

In PBB VPLS, an AC interface must be bound to each I-VSI and a VPLS peer must be specified for each B-VSI.

#### Procedure

* Bind an AC interface to an I-VSI.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The AC interface view is displayed.
  3. Run [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name* [ **access-port** ]
     
     
     
     The AC interface is bound to the specified I-VSI.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a PW in a B-VSI.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
     
     
     
     The B-VSI view is displayed.
  3. Run [**pwsignal**](cmdqueryname=pwsignal) **ldp**
     
     
     
     The VSI-LDP view is displayed.
  4. Run [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] [ **tnl-policy** *policy-name* ] [ **upe** ]
     
     
     
     A VPLS peer is specified.
     
     
     
     + **negotiation-vc-id** *vc-id* specifies a unique identifier for a VC. This parameter allows two devices with different VSI IDs to communicate. The specified **negotiation-vc-id** must be different from local VSI IDs and VSI IDs specified locally using the **negotiation-vc-id** command.
     + **upe**: indicates whether the specified VPLS peer is a UPE. This parameter applies to HVPLS.
     + In PBB VPLS, an SPE can have either common VSIs or B-VSIs configured. If an SPE directly connects to a CE, a B-VSI must be configured on the SPE.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.