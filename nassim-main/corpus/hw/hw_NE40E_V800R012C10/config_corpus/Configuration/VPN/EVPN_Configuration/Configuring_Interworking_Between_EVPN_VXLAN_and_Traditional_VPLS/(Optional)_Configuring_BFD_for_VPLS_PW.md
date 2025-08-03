(Optional) Configuring BFD for VPLS PW
======================================

Configuring BFD for VPLS PW accelerates PW fault detection, speeding up switching of upper-layer applications.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0172370538__fig_dc_vrp_evpn_cfg_110001), PE3 is dual-homed to PE1 and PE2, and an MPLS L2VPN is deployed between the PEs, with PW connections configured. To accelerate PW fault detection, static BFD for VPLS PW can be configured on PE1, PE2, and PE3. The configuration allows fast switching of upper-layer applications.

**Figure 1** VXLAN accessing VPLS (dual-homing networking)  
![](images/fig_vxlan_vpls_01.png)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   BFD is enabled globally, and the global BFD view is displayed.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**bfd**](cmdqueryname=bfd) *session-name* **bind pw** **vsi** *vsi-name* **peer** *peer-address* [ **vc-id** *vc-id* ] [ **remote-peer** *remote-peer-address* **pw-ttl** { **auto-calculate** | *ttl-number* } ]
   
   
   
   BFD configuration items are created.
5. Run the following commands to configure BFD session discriminators:
   
   
   * Run the [**discriminator**](cmdqueryname=discriminator) **local** *discr-value* command to set the local discriminator.
   * Run the [**discriminator**](cmdqueryname=discriminator) **remote** *discr-value* command to set the remote discriminator.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For a BFD session, the local discriminator on one end must be the remote discriminator on the other end.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
   
   
   
   If the status of a PW is Down, the BFD session can be established but cannot go Up.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * You must simultaneously configure or cancel BFD for PW on both PEs. Otherwise, the PW status on endpoint PEs may be inconsistent.
   * To modify parameters of a created BFD session, run the [**min-tx-interval**](cmdqueryname=min-tx-interval), [**min-rx-interval**](cmdqueryname=min-rx-interval), and [**detect-multiplier**](cmdqueryname=detect-multiplier) commands as needed.