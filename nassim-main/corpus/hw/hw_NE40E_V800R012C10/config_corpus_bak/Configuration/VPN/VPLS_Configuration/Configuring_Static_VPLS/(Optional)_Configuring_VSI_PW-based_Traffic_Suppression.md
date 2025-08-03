(Optional) Configuring VSI PW-based Traffic Suppression
=======================================================

You can configure VSI PW-based suppression of broadcast packets, multicast packets, and unknown unicast packets.

#### Context

To prevent a network from being overburdened, set a traffic rate limit.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** | **auto** ]
   
   
   
   The VSI view is displayed.
3. Run [**pwsignal ldp**](cmdqueryname=pwsignal+ldp)
   
   
   
   The VSI-LDP view is displayed.
4. Run [**vsi-id**](cmdqueryname=vsi-id) *vsi-id*
   
   
   
   The VSI ID is configured.
5. (Optional) Run [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] **pw** *pw-name*
   
   
   
   A PW is created, and the VSI-LDP-PW view is displayed.
   
   
   
   If a PW has been created, you can run the [**pw**](cmdqueryname=pw) *pw-name* command to enter the VSI-BGP-PW view corresponding to *pw-name*.
6. Run either of the following commands to limit the packet rate of the VSI:
   
   
   * To limit the rate of broadcast packets on the VSI PW, run the [**broadcast-suppression**](cmdqueryname=broadcast-suppression) **cir** *cir-value* [ **cbs** *cbs-value* ] command.
   * To limit the rate of multicast packets on the VSI PW, run the [**multicast-suppression**](cmdqueryname=multicast-suppression) **cir** *cir-value* [ **cbs** *cbs-value* ] command.
   * To limit the rate of unknown unicast packets on the VSI PW, run the [**unknown-unicast-suppression**](cmdqueryname=unknown-unicast-suppression) **cir** *cir-value* [ **cbs** *cbs-value* ] command.
   
   When the packet rate reaches the CIR, subsequent packets are discarded.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.