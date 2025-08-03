Configuring Interworking Between Traditional BD VPLS and EVPN VPLS over MPLS
============================================================================

On an IP RAN where traditional BD VPLS is still used at the access layer but the aggregation network has evolved to MPLS EVPN, you need to configure interworking between traditional BD VPLS and EVPN VPLS over MPLS.

#### Context

During IP RAN evolution toward EVPN, if traditional BD VPLS is still widely used on access-layer devices, it is difficult to evolve the IP RAN to MPLS EVPN in an E2E manner at one time. If the aggregation network has evolved to MPLS EVPN, you need to configure interworking between traditional BD VPLS and EVPN VPLS over MPLS on the IP RAN.

On the network shown in [Figure 1](#EN-US_TASK_0172370524__fig18509102501920), VPLS is deployed to carry services on the access network between CSGs and ASGs, and BD EVPN is deployed to carry services on the aggregation network between ASGs and RSGs. On ASGs, a BD needs to be configured and bound to a BD EVPN instance and a VSI to achieve interworking between traditional BD VPLS and EVPN VPLS over MPLS.

**Figure 1** Configuring interworking between traditional BD VPLS and EVPN VPLS over MPLS  
![](figure/en-us_image_0000001232035217.png)

#### Pre-configuration Tasks

Before configuring interworking between traditional BD VPLS and EVPN VPLS over MPLS, complete the following tasks:

* [Configure LDP VPLS](dc_vrp_vpls_cfg_5003.html) between CSGs and ASGs.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  A BD VSI must be configured using the [**vsi bd-mode**](cmdqueryname=vsi+bd-mode) command here.
* Configure [EVPN VPLS over MPLS (BD EVPN instance)](dc_vrp_evpn_cfg_0065.html) between ASGs and RSGs.

Perform the following operations on each ASG:


#### Procedure

1. Configure an ESI instance and set its redundancy mode to single-active.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**evpn**](cmdqueryname=evpn) command to enter the global EVPN configuration view.
   3. Run the [**esi**](cmdqueryname=esi) *esi* command to configure a static ESI instance name.
   4. Run the [**evpn redundancy-mode**](cmdqueryname=evpn+redundancy-mode) **single-active** command to set the redundancy mode of the static ESI instance to single-active.
   5. Run the [**quit**](cmdqueryname=quit) command to return to the global EVPN configuration view.
   6. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   7. Run the **commit** command to commit the configuration.
2. Configure a specified CSG as a UPE and configure an ESI for the VSI.
   1. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* **bd-mode** command to enter the VSI view.
   2. Run the [**pwsignal**](cmdqueryname=pwsignal) **ldp** command to configure LDP as the PW signaling protocol and enter the VSI-LDP view.
   3. Run the [**vsi-id**](cmdqueryname=vsi-id) *vsi-id* command to configure a VSI ID.
   4. Configure a specified CSG as a UPE.
      
      
      * Run the [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] [ **tnl-policy** *policy-name* ] **upe** command to configure a specified CSG as a UPE.
      * Run the [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] [ **tnl-policy** *policy-name* ] **static-npe** **trans** *transmit-label* **recv** *receive-label* command to configure a static VPLS PW.
   5. Run the [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] **pw** *pw-name* command to create a PW and enter the VSI-LDP-PW view.
   6. Run the [**esi**](cmdqueryname=esi) *esi* command to configure an ESI for the PW interface. The value of *esi* must be the same as the name of the static ESI instance.
   7. (Optional) Run the [**evpn e-tree-leaf**](cmdqueryname=evpn+e-tree-leaf) command to configure the leaf attribute for the PW interface. If you do not want the traffic sent from CE1 to CSG1 to be sent back to CE1 through ASG1, ASG2, and CSG2, you can configure the leaf attribute in the VSI-LDP-PW view of ASG1 and ASG2.
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

* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** | **prefix-route** } *prefix* command on the ASG to check detailed BGP EVPN route information, including PW information.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) **vpn-instance** *vpn-instance-name* **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** } *prefix* command on the ASG to check the EVPN route information (including PW information) of the specified EVPN instance.
* Run the [**display evpn vpn-instance name**](cmdqueryname=display+evpn+vpn-instance+name) *vpn-instance-name* **df result** [ **esi** *esi* ] command on an ASG to check the DF election result (including access-side PW information) of an EVPN instance.