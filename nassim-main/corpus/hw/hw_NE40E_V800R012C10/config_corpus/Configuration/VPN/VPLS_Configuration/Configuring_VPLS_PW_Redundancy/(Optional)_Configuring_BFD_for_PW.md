(Optional) Configuring BFD for PW
=================================

After configuring PWs, configure BFD for PW to detect the faults of the primary PW to speed up fault detection and improve PW switching performance.

#### Context

If no signaling is used to detect PW faults, PWs are notified of MPLS tunnel faults. However, PWs are slow to perceive faults in this case. To quicken PW fault detection, configure BFD for PW.

Generally, BFD for PW only needs to be configured for the primary PW. When BFD for PW detects a fault on the primary PW, BFD for PW immediately triggers a primary/secondary PW switchover.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   BFD is enabled globally, and the global BFD view is displayed.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. On the UPE, SPE, or NPE configured with a VSI, run [**bfd**](cmdqueryname=bfd) *cfg-name* **bind pw** **vsi** *vsi-name* [**peer**](cmdqueryname=peer) *peer-address* [ **vc-id** *vc-id* ] [ **remote-peer** *remote-peer-address* **pw-ttl** { **auto-calculate** | *ttl-number* } ]
   
   
   
   BFD for VSI PW is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When configuring BFD for PW, you need to configure the [**ignore-standby-state**](cmdqueryname=ignore-standby-state) command on the SPE. Otherwise, the secondary PW remains blocked and the BFD session cannot go up. Similarly, if you do not configure the [**ignore-standby-state**](cmdqueryname=ignore-standby-state) command, the primary PW stays in the backup state during a delayed traffic switchback, and the BFD session cannot go up.
5. Configure BFD session discriminators:
   
   
   * To configure the local discriminator, run the [**discriminator**](cmdqueryname=discriminator) **local** *discr-value* command.
   * To configure the remote discriminator, run the [**discriminator**](cmdqueryname=discriminator) **remote** *discr-value* command.
   
   The local BFD session discriminator on one end must be the same as the remote BFD session discriminator on the other end.
6. (Optional) Configure BFD for VPLS LDP PW.
   1. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   2. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* command to enter the view of the created VSI.
   3. Run the [**pwsignal**](cmdqueryname=pwsignal) **ldp** command to enter the VSI-LDP view.
   4. Run the **[**vsi-id**](cmdqueryname=vsi-id)** *vsi-id* command to configure an ID for the VSI.
   5. Run the [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] **pw** *pw-name* command to enter the VSI-LDP-PW view.
   6. Run the [**track bfd**](cmdqueryname=track+bfd) *bfd-session* command to configure BFD for VPLS LDP PW.
      
      
      
      In a VPLS PW redundancy protection scenario, a BD is used for interworking between a VPLS network and a VXLAN network. If a fault occurs on the VXLAN side, the VPLS PW cannot detect the VXLAN fault. As a result, PW switching fails. After this command is run, a PW can detect VXLAN faults. If BFD detects a down event, it triggers PW status switching to implement protection switching.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
   
   
   
   If the status of a PW is down, the BFD session can be established but cannot go up.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You must configure or cancel BFD for PW on both endpoint PEs of a PW. Otherwise, the PW status on both endpoint PEs may be inconsistent.