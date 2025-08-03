Creating VSIs and Configuring PW Connections
============================================

This section describes how to configure MPLS VPLS interconnection between PE1, PE2, and PE3.

#### Procedure

* Configure PE1 and PE2.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** | **auto** ] **bd-mode**
     
     
     
     A VSI in BD mode is created.
  3. Run [**pwsignal ldp**](cmdqueryname=pwsignal+ldp)
     
     
     
     LDP is configured as the VSI signaling protocol, and the VSI-LDP view is displayed.
  4. Run [**vsi-id**](cmdqueryname=vsi-id) *vsi-id*
     
     
     
     An ID is configured for the VSI.
  5. Run [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] **pw** *pw-name*
     
     
     
     PE3 is specified as the VSI peer.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure PE3.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** | **auto** ] **bd-mode**
     
     
     
     A VSI in BD mode is created.
  3. Run [**pwsignal ldp**](cmdqueryname=pwsignal+ldp)
     
     
     
     The VSI-LDP view is displayed.
  4. Run [**vsi-id**](cmdqueryname=vsi-id) *vsi-id*
     
     
     
     An ID is configured for the VSI.
  5. Run [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] **pw** *pw-name*
     
     
     
     PE1 and PE2 are specified as the VSI peers of the device.
  6. Run [**protect-group**](cmdqueryname=protect-group) *group-name*
     
     
     
     A PW protection group is created, and its view is displayed.
  7. Run [**protect-mode pw-redundancy**](cmdqueryname=protect-mode+pw-redundancy) { **master** | **independent** }
     
     
     
     The PW redundancy mode of the current PW protection group is specified.
     
     
     
     Network protection depends on the VPLS network's protection solution. It is recommended that PW redundancy in **master** instead of **independent** mode be configured on PE3.
  8. Run [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] **preference** *preference-value*
     
     
     
     The PWs connected to PE1 and PE2 are added to the PW protection group, and priorities of the PWs are specified. A smaller value indicates a higher priority. The PW with a higher priority serves as the primary PW.
  9. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit from the PW protection group view.
  10. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit from the VSI-LDP view.
  11. Run [**pw-redundancy mac-withdraw rfc-compatible**](cmdqueryname=pw-redundancy+mac-withdraw+rfc-compatible)
      
      
      
      The device is enabled to instruct the peer PEs to clear the MAC addresses of the PWs if their primary/secondary status is changed.
      
      
      
      In a scenario with VXLAN accessing VPLS and PW redundancy, if the active/standby status of PE1 and PE2 changes, PE3 performs a primary/secondary PW switchover. In this case, PE3 must notify PE1 and PE2 of the current PW status and instruct them to clear the MAC addresses.
  12. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.