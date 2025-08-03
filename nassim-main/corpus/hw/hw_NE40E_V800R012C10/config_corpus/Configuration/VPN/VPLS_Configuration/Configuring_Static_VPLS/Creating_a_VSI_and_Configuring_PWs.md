Creating a VSI and Configuring PWs
==================================

Static VPLS allows you to manually manage and allocate VC labels.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name* **static**
   
   
   
   A VSI is created, and its view is displayed.
   
   
   
   VSIs on the same device cannot use the same name.
3. (Optional) Run [**description**](cmdqueryname=description) *description*
   
   
   
   A description is configured for the VSI.
4. (Optional) Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
   
   
   
   A public network tunnel policy is referenced by the VSI.
   
   
   
   A tunnel policy specified during VSI peer configuration takes precedence over one specified in the VSI view. If tunnel policies are specified using both methods, only the tunnel policy specified during VSI peer configuration takes effect.
5. Run [**pwsignal**](cmdqueryname=pwsignal) **ldp**
   
   
   
   LDP is configured as the VSI signaling protocol, and the VSI-LDP view is displayed.
6. Run [**vsi-id**](cmdqueryname=vsi-id) *vsi-id*
   
   
   
   A VSI ID is configured.
   
   
   
   * The VSI IDs at the two ends of a PW must be the same, or the VSI cannot be created. If the VSI IDs at the two ends of a PW are different, specify **negotiation-vc-id** *vc-id* for PW negotiation when running the [**peer**](cmdqueryname=peer) command.
   * VSIs can exist only on PEs. A PE can be configured with multiple VSIs, but the ID of each VSI must be unique on the PE.
7. Run [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] [ **tnl-policy** *policy-name* ] [ [ **endpoint** *endpoint4-address* ] **color** *color-value* ] { **static-npe** | **static-upe** } **trans** *transmit-label* **recv** *receive-label*
   
   
   
   A static VPLS PW is configured.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.