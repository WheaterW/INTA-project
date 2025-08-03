Configuring Traditional BD VPLS and EVPN VPLS over SRv6 to Coexist
==================================================================

If both a traditional VPLS network and an EVPN VPLS over SRv6 network are deployed, you need to configure traditional VPLS and EVPN VPLS over SRv6 to coexist.

#### Context

Traditional L2VPNs use VPLS over MPLS for Layer 2 communication. Compared with VPLS, EVPN â a next-generation VPN technology â has many advantages, such as support for multi-homing all-active networking and control plane-based MAC address learning. Particularly, EVPN over SRv6 can accommodate the growth of IPv6 networks and 5G services. Therefore, VPLS over MPLS is gradually evolving to EVPN over SRv6. However, there are still a large number of existing VPLS services on the live network. If EVPN VPLS over SRv6 services are added, configure the co-existence of traditional VPLS and EVPN VPLS over SRv6 to ensure that both services run properly.

On the network shown in [Figure 1](#EN-US_TASK_0263581209__fig579251613147), VPLS over MPLS is deployed on PE3, and both VPLS over MPLS and EVPN VPLS over SRv6 are deployed on PE1, PE2, and PE4. In this case, you need to configure VPLS and EVPN VPLS over SRv6 to coexist on PE1, PE2, and PE4.

**Figure 1** Configuring the co-existence of traditional VPLS and EVPN VPLS over SRv6  
![](figure/en-us_image_0000001232689697.png)

#### Pre-configuration Tasks

Before configuring the co-existence of traditional VPLS and EVPN VPLS over SRv6, complete the following tasks:

* Complete the task of [Configuring LDP VPLS](dc_vrp_vpls_cfg_5003.html) or [Configuring BGP VPLS](dc_vrp_vpls_cfg_6005.html) between PE3 and PE1, between PE3 and PE2, and between PE3 and PE4.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Create a BD VSI using the [**vsi bd-mode**](cmdqueryname=vsi+bd-mode) command.
* Complete the task of [Configuring EVPN VPLS over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0023.html) or [Configuring EVPN VPLS over SRv6 TE Policy](dc_vrp_cfg_evpn-vpls_over_srv6-te_policy.html) between PE1, PE2, and PE4.

Perform the following steps on PE1, PE2, and PE4.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
   
   
   
   The BD view is displayed.
3. Run [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name* [ **pw-tag** *pw-tag-value* ]
   
   
   
   The BD is bound to the VSI.
4. Run [**evpn binding vpn-instance**](cmdqueryname=evpn+binding+vpn-instance) *vpn-instance-name*
   
   
   
   The BD is bound to the EVPN instance.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** | **prefix-route** } *prefix* command on PE1, PE2, and PE4 to check detailed BGP EVPN route information, including PW information.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) **vpn-instance** *vpn-instance-name* **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** } *prefix* command on PE1, PE2, and PE4 to check the EVPN route information (including PW information) of the specified EVPN instance.
* In a scenario where a CE is dual-homed to PEs, run the [**display evpn vpn-instance name**](cmdqueryname=display+evpn+vpn-instance+name) *vpn-instance-name* **df result** [ **esi** *esi* ] command on PEs to check the DF election result (including PW information) of the specified EVPN instance.