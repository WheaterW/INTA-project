Configuring Interworking Between VPLS in PW Redundancy Mode and Anycast VXLAN with EVPN Active-Active Networking
================================================================================================================

This section describes how to configure interworking to enable communication between VPLS in PW redundancy mode and anycast VXLAN with EVPN active-active networking.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0172370495__fig_dc_vrp_dci_cfg_003301), anycast VXLAN with EVPN active-active networking is configured on the data center network. The egress devices of the data center network (PE1 and PE2) work in active-active mode with a bypass VXLAN tunnel deployed between them. They use an anycast VTEP address to establish a VXLAN tunnel with the EOR switch. PE1, PE2, and the EOR switch can then communicate with each other. PE1 and PE2 communicate with the external network through the VPLS network, on which PW redundancy is configured. Specifically, the PE-AGG connects to PE1 and PE2 through primary and secondary PWs, respectively.

**Figure 1** Configuring interworking between VPLS in PW redundancy mode and anycast VXLAN with EVPN active-active networking  
![](images/fig_vxlan_vpls_04.png)  

To configure interworking between VPLS in PW redundancy mode and anycast VXLAN with EVPN active-active networking, perform the following configurations:

* [Configure VPLS PW redundancy](dc_vrp_vpls_cfg_5049.html) on the PE-AGG, PE1, and PE2.
* [Configure dynamic VXLAN active-active](dc_vrp_dci_cfg_0024.html) on PE1 and PE2.
* Configure the PWs connecting to the VPLS network to work in AC mode on PE1 and PE2. This configuration is required on the anycast VXLAN with EVPN active-active networking to prevent split horizon, which is configured on PE1 and PE2, from interrupting traffic. For details, see [Procedure](#EN-US_TASK_0172370495__step_01).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name* **bd-mode**
   
   
   
   A BD VSI is created, and its view is displayed.
3. Run [**pwsignal**](cmdqueryname=pwsignal) **ldp**
   
   
   
   LDP is configured as the PW signaling protocol, and the VSI-LDP view is displayed.
4. Run [**vsi-id**](cmdqueryname=vsi-id) *vsi-id*
   
   
   
   A VSI ID is configured.
5. Run [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] [ **encapsulation** { **ethernet** | **vlan** } ] [ **tnl-policy** *policy-name* ] **ac-mode**
   
   
   
   A PW is set to AC mode.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, check VXLAN tunnel, primary PW, and secondary PW information. For details, see [Verifying the VXLAN Configuration](dc_vrp_vxlan_cfg_1053.html) and [Verifying the VPLS PW Redundancy Configuration](dc_vrp_vpls_cfg_5055.html).