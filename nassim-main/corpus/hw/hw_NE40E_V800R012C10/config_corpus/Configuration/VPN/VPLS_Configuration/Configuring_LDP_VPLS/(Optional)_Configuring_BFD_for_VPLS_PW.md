(Optional) Configuring BFD for VPLS PW
======================================

After a PW is configured for a VPLS using LDP as signaling, BFD can be configured to monitor the primary PW so that traffic can be immediately switched to the secondary PW in case of a primary PW fault.

#### Usage Scenario

On a VPLS LDP network, you can configure BFD to detect PW faults, which quickens link fault detection and enhances application-layer service protection.

Currently, static BFD and dynamic BFD are supported. Determine which one to use as needed.

#### Pre-configuration Tasks

Before you configure BFD to detect the connectivity of a VPLS PW, complete the following tasks:

* Configure network-layer parameters for devices to communicate.
* Configure PWs.
* If a remote peer cannot identify the BFD CV Type field value 0x08 used for VCCV, run the [**mpls l2vpn vccv bfd-cv-negotiation**](cmdqueryname=mpls+l2vpn+vccv+bfd-cv-negotiation) command to change the BFD CV Type field value carried in a Label Mapping message to be consistent with the remote peer's.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* The control word mode of static BFD for VPLS PW does not support the 0x10 or 0x20 BFD CV type. If the PW-negotiated CV values on both ends are 0x10 or 0x20, the BFD session cannot go up after negotiation.
* If dynamic BFD for VPLS is configured and the BFD CV Type field is negotiated to be 0x10 or 0x20 for the peers, the MTU value of the interface through which BFD control packets are transmitted cannot be less than the BFD control packet length. A BFD control packet's payload is in one of the following lengths:
  + Non-authentication: 24 bytes
  + MD5 authentication: 48 bytes (For the sake of security, using the HMAC-SHA256 algorithm rather than the MD5 algorithm is recommended.)
  + SHA1 authentication: 52 bytes
* For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function.



#### Procedure

* Configure a static BFD session.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is enabled globally, and the global BFD view is displayed.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**bfd**](cmdqueryname=bfd) *session-name* **bind pw** **vsi** *vsi-name* **peer** *peer-address* [ **vc-id** *vc-id* ] [ **remote-peer** *remote-peer-address* **pw-ttl** { **auto-calculate** | *ttl-number* } ]
     
     
     
     BFD configuration items are created.
  5. Configure BFD session discriminators:
     
     
     + To configure the local discriminator, run the [**discriminator**](cmdqueryname=discriminator) **local** *discr-value* command.
     + To configure the remote discriminator, run the [**discriminator**](cmdqueryname=discriminator) **remote** *discr-value* command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
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
     
     
     
     If the status of a service PW is down, the BFD session can be established but cannot go up.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + BFD for PW must be configured or cancelled on both endpoint PEs of a PW. Otherwise, the PW status on the endpoint PEs may be inconsistent.
     + If you want to modify the parameters of an existing BFD session, run corresponding commands, such as [**min-tx-interval**](cmdqueryname=min-tx-interval), [**min-rx-interval**](cmdqueryname=min-rx-interval), and [**detect-multiplier**](cmdqueryname=detect-multiplier).
* Configure a dynamic BFD session.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is enabled globally, and the global BFD view is displayed.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     The system view is displayed.
  4. Trigger the establishment of a dynamic BFD session.
     
     
     1. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* command to enter the VSI view.
     2. Run the [**pwsignal**](cmdqueryname=pwsignal) **ldp** command to enter the VSI-LDP view.
     3. Run the [**vsi-id**](cmdqueryname=vsi-id) *vsi-id* command to configure an ID for the VSI.
     4. Run the [**peer**](cmdqueryname=peer) *peer-address* command to configure a peer for the VSI.
     5. Run the [**peer**](cmdqueryname=peer) *peer-address* **pw** *pw-name* command to configure a VSI-LDP-PW template.
     6. Run the [**control-word enable**](cmdqueryname=control-word+enable) command to configure the control word function for the VSI.
     7. Run the [**bfd-detect**](cmdqueryname=bfd-detect) [ **detect-multiplier** *multiplier* | **min-rx-interval** *rx-interval* | **min-tx-interval** *tx-interval* | **option-tlv** ] \* [ **track** **group** *group-name* ] command to configure dynamic BFD for VPLS PW.![](../../../../public_sys-resources/note_3.0-en-us.png) The parameters are described as follows:
        + **detect-multiplier** *multiplier* indicates the BFD detection multiplier.
        + **min-rx-interval** *rx-interval* indicates the Required Min Rx Interval (RMRI), which is the supported minimum interval at which the local device receives BFD control packets.
        + **min-tx-interval** *tx-interval* indicates the Desired Min Tx Interval (DMTI), which is the desired minimum interval at which the local device sends BFD control packets.
        The BFD detection parameters actually used may be different from the ones configured:
        + Actual local detection interval = Actual interval at which the local device receives BFD control packets x Configured remote BFD detection multiplier
        + Actual interval at which the local device receives BFD control packets = Max { Configured remote DMTI, Configured local RMRI }
        + Actual interval at which the local device transmits BFD control packets = Max { Configured local DMTI, Configured remote RMRI }
     8. Run the [**quit**](cmdqueryname=quit) command to return to the VSI view.
     9. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After configuring BFD for VPLS PW, verify the configuration.

* Run the [**display bfd session**](cmdqueryname=display+bfd+session) command to check BFD session configurations.