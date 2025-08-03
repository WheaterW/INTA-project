Configuring Static BFD to Detect the Connectivity of a VPLS SS-PW
=================================================================

This section describes how to configure static bidirectional forwarding detection (BFD) to detect the connectivity of a virtual private LAN service (VPLS) single-segment pseudo wire (SS-PW).

#### Usage Scenario

If provider edge devices (PEs) on a Multiprotocol Label Switching (MPLS) Layer 2 virtual private network (L2VPN) communicate over pseudo wires (PWs), service protection can be enhanced by configuring static BFD to detect PW connectivity.

#### Pre-configuration Tasks

Before you configure static BFD to detect the connectivity of a VPLS SS-PW, complete the following tasks:

* Configure network-layer parameters for devices to communicate.
* Configure a VPLS SS-PW.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   BFD is enabled globally, and the global BFD view is displayed.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Create BFD configurations based on the networking.
   
   
   * Create a BFD session and bind it to a VPLS PW.
     
     Run the [**bfd**](cmdqueryname=bfd) *session-name* **bind pw** **vsi** *vsi-name* **peer** *peer-address* [ **vc-id** *vc-id* ] [ **remote-peer** *remote-peer-address* **pw-ttl** { **auto-calculate** | *ttl-number* } ] command to create a BFD configuration item.
5. Configure BFD session discriminators:
   
   
   * To configure the local discriminator, run the [**discriminator**](cmdqueryname=discriminator) **local** *discr-value* command.
   * To configure the remote discriminator, run the [**discriminator**](cmdqueryname=discriminator) **remote** *discr-value* command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The local BFD session discriminator on one end must be the same as the remote BFD session discriminator on the other end.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
   
   
   
   If the status of a PW is down, the BFD session can be established but cannot go up.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * BFD for PW must be configured or cancelled on both endpoint PEs of a PW. Otherwise, the PW status on the endpoint PEs may be inconsistent.
   * If you want to modify the parameters of an existing BFD session, run corresponding commands, such as [**min-tx-interval**](cmdqueryname=min-tx-interval), [**min-rx-interval**](cmdqueryname=min-rx-interval), and [**detect-multiplier**](cmdqueryname=detect-multiplier).

#### Verifying the Configuration

After configuring static BFD for VPLS PW, verify the configuration.

Run the [**display bfd session**](cmdqueryname=display+bfd+session) command. The command output shows information about the BFD session status, BFD session discriminators, BFD session type, and type of the PW bound to the BFD session.