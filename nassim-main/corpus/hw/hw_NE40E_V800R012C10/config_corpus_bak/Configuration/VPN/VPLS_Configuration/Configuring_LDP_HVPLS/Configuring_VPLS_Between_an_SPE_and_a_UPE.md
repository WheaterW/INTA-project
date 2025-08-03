Configuring VPLS Between an SPE and a UPE
=========================================

A switching provider edge (SPE) and an underlayer provider edge (UPE) set up a spoke PW, which does not comply with the split horizon principle.

#### Context

When you configure VPLS between an SPE and a UPE, note the following:

* The VPLS configuration on the UPE is similar to the configuration of common VPLS except that you need to specify an SPE as the peer. For details, see [Configuring LDP VPLS](dc_vrp_vpls_cfg_5003.html).
* The VPLS configuration on the SPE is similar to the configuration of common VPLS except that you need to configure **upe** to indicate that the peer is a UPE.

Perform the following steps on the SPE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ]
   
   
   
   The VSI view is displayed.
3. Run [**pwsignal**](cmdqueryname=pwsignal) **ldp**
   
   
   
   LDP is configured as the PW signaling protocol, and the VSI-LDP view is displayed.
4. Run [**vsi-id**](cmdqueryname=vsi-id) *vsi-id*
   
   
   
   An ID is configured for the VSI.
5. Run [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] [ **tnl-policy** *policy-name* ] [ [ **endpoint** *endpoint4-address* ] **color** *color-value* ] **upe**
   
   
   
   The UPE is specified as a VSI peer of the SPE.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.