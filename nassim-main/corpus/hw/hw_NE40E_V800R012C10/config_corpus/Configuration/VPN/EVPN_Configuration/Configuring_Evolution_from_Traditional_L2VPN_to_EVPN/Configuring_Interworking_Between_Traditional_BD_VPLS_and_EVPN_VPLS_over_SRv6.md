Configuring Interworking Between Traditional BD VPLS and EVPN VPLS over SRv6
============================================================================

During the convergence of a traditional BD VPLS network and an EVPN VPLS over SRv6 network, interworking between traditional BD VPLS and EVPN VPLS over SRv6 must be configured.

#### Context

Traditional L2VPNs use VPLS over MPLS for Layer 2 communication. Compared with VPLS, EVPN â a next-generation VPN technology â has many advantages, such as support for multi-homing all-active networking and control plane-based MAC address learning. Particularly, EVPN over SRv6 can accommodate the growth of IPv6 networks and 5G services. Therefore, VPLS over MPLS is gradually evolving to EVPN over SRv6. However, the live network with a large number of existing VPLS services cannot be upgraded to EVPN VPLS over SRv6 at one time. In this case, you can configure interworking between BD VPLS and EVPN VPLS over SRv6.

On the network shown in [Figure 1](#EN-US_TASK_0263090300__fig94817594118), VPLS over MPLS is deployed between UPEs and SPEs to carry services; EVPN VPLS over SRv6 is deployed between SPEs and NPEs to carry services. In this case, you need to configure interworking between traditional BD VPLS and EVPN VPLS over SRv6 on SPE1 and SPE2.

**Figure 1** Configuring interworking between traditional BD VPLS and EVPN VPLS over SRv6  
![](figure/en-us_image_0000001187210102.png)

#### Pre-configuration Tasks

Before configuring interworking between traditional BD VPLS and EVPN VPLS over SRv6, complete the following tasks:

* [Configure LDP VPLS](dc_vrp_vpls_cfg_5003.html) between UPEs and SPEs.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Create a BD VSI using the [**vsi bd-mode**](cmdqueryname=vsi+bd-mode) command.
* Complete the task of [Configuring EVPN VPLS over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0023.html) or [Configuring EVPN VPLS over SRv6 TE Policy](dc_vrp_cfg_evpn-vpls_over_srv6-te_policy.html) between an SPE and an NPE.

Perform the following steps on SPE1 and SPE2.


#### Procedure

1. Configure an ESI instance and set its redundancy mode to single-active.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**evpn**](cmdqueryname=evpn) command to enter the global EVPN configuration view.
   3. Run the [**esi**](cmdqueryname=esi) *esi* command to configure a static ESI instance name.
   4. Run the [**evpn redundancy-mode**](cmdqueryname=evpn+redundancy-mode) **single-active** command to set the redundancy mode of the static ESI instance to single-active.
   5. Run the [**quit**](cmdqueryname=quit) command to return to the global EVPN configuration view.
   6. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   7. Run the **commit** command to commit the configuration.
2. Configure a specified SPE as a UPE and configure an ESI for the VSI.
   1. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* **bd-mode** command to enter the VSI view.
   2. Run the [**pwsignal**](cmdqueryname=pwsignal) **ldp** command to configure LDP as the PW signaling protocol and enter the VSI-LDP view.
   3. Run the [**vsi-id**](cmdqueryname=vsi-id) *vsi-id* command to configure a VSI ID.
   4. Run the [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] [ **tnl-policy** *policy-name* ] **upe** command to configure a specified SPE as a UPE.
   5. Run the [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] **pw** *pw-name* command to create a PW and enter the VSI-LDP-PW view.
   6. Run the [**esi**](cmdqueryname=esi) *esi* command to configure an ESI for the PW interface. The value of *esi* must be the same as the name of the static ESI instance.
   7. (Optional) Run the [**evpn e-tree-leaf**](cmdqueryname=evpn+e-tree-leaf) command to configure the leaf attribute for the PW interface. If you do not want the traffic sent from CE1 to UPE1 to be sent back to CE1 through SPE1, SPE2, and UPE1, you can configure the leaf attribute in the VSI-LDP-PW view of SPE1 and SPE2.
   8. Run the [**quit**](cmdqueryname=quit) command to return to the VSI-LDP view.
   9. Run the [**quit**](cmdqueryname=quit) command to return to the VSI view.
   10. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   11. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
3. Bind the BD to the VSI and EVPN instance.
   1. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to enter the BD view.
   2. Run the [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name* [ **pw-tag** *pw-tag-value* ] command to bind the BD to the VSI.
   3. Run the [**evpn binding vpn-instance**](cmdqueryname=evpn+binding+vpn-instance) *vpn-instance-name* command to bind the BD to the EVPN instance.
   4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** | **prefix-route** } *prefix* command on the SPE to check detailed BGP EVPN route information, including PW information.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) **vpn-instance** *vpn-instance-name* **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** } *prefix* command on the SPE to check the EVPN route information (including PW information) of the specified EVPN instance.
* Run the [**display evpn vpn-instance name**](cmdqueryname=display+evpn+vpn-instance+name) *vpn-instance-name* **df result** [ **esi** *esi* ] command on the SPE to check the DF election result (including access-side PW information) of an EVPN instance.