Configuring Traditional Common VPLS and EVPN VPLS over MPLS to Coexist
======================================================================

If both a traditional common VPLS network and an EVPN VPLS over MPLS network are deployed, you need to configure traditional common VPLS and EVPN VPLS over MPLS to coexist.

#### Context

Traditional L2VPNs use VPLS over MPLS for Layer 2 communication. Compared with VPLS, EVPN â a next-generation VPN technology â has many advantages, such as support for multi-homing all-active networking and control plane-based MAC address learning. Therefore, VPLS over MPLS is gradually evolving to EVPN over MPLS. However, there are still a large number of existing traditional common VPLS services on the live network. If EVPN VPLS over MPLS services are added, you need to configure traditional common VPLS and EVPN VPLS over MPLS to coexist, so that both types of services can run properly.

On the network shown in [Figure 1](#EN-US_TASK_0000001540902602__fig579251613147), common VPLS over MPLS is deployed on PE3, and both traditional common VPLS over MPLS and EVPN VPLS over MPLS are deployed on PE1, PE2, and PE4. In this case, you need to configure traditional common VPLS and EVPN VPLS over MPLS to coexist on PE1, PE2, and PE4.

**Figure 1** Configuring traditional common VPLS and EVPN VPLS over MPLS to coexist  
![](figure/en-us_image_0000001591462153.png)

#### Pre-configuration Tasks

Before configuring traditional common VPLS and EVPN VPLS over MPLS to coexist, complete the following tasks:

* [Configure LDP VPLS](dc_vrp_vpls_cfg_5003.html) between PE3 and PE1, between PE3 and PE2, and between PE3 and PE4.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  In this task, a non-BD VSI must be created using the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** | **auto** ] command.
* Configure BGP EVPN peer relationships between PE1, PE2, and PE4 and create a BD EVPN instance on each of these devices.

Perform the following steps on PE1, PE2, and PE4.


#### Procedure

1. Create a BD and configure evolution from common VPLS to EVPN.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to create a BD and enter its view.
   3. Run the [**vpls-to-evpn migration in-process**](cmdqueryname=vpls-to-evpn+migration+in-process) command to indicate that the BD is evolving from VPLS to EVPN.
   4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
2. Add all AC interfaces to the BD (sub-interfaces are used as AC interfaces in this case).
   1. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number.sub-number* command to enter the view of the AC interface that directly connects the PE to a CE.
   2. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to add the AC interface to the BD.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
3. (Optional) Configure TC notification on the AC interface's main interface.
   
   
   
   If the [**stp enable**](cmdqueryname=stp+enable) command is run on the AC interface's main interface to enable STP but the [**stp vpls-subinterface enable**](cmdqueryname=stp+vpls-subinterface+enable) command is not run before the evolution, during the evolution, the AC interface may be blocked when the broadcast domain switches from the VSI to the BD, and a traffic loop may occur when the broadcast domain switches from the BD to the VSI. In response, you are advised to perform the following operations:
   
   
   
   1. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the view of the AC interface's main interface.
   2. Run the [**stp vpls-subinterface enable**](cmdqueryname=stp+vpls-subinterface+enable) command to enable TC notification on the main interface.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
4. (Optional) Configure the maximum volume of unknown unicast traffic allowed by the BD.
   
   
   
   During the evolution, broadcast domain switching occurs, resulting in MAC address relearning. In this case, traffic is forwarded in unknown unicast mode within a short period of time. In response, you are advised to configure unknown unicast traffic suppression in the BD.
   
   
   
   1. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to enter the BD view.
   2. Run the [**unknown-unicast-suppression**](cmdqueryname=unknown-unicast-suppression) **cir** *cir-value* [ **cbs** *cbs-value* ] { **uni-inbound** | **uni-outbound** } command to configure the maximum unknown unicast traffic volume allowed by the BD.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
5. Bind the BD to both the VSI and EVPN instance.
   1. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to enter the BD view.
   2. Run the [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name* command to bind the BD to the VSI.
   3. Run the [**evpn binding vpn-instance**](cmdqueryname=evpn+binding+vpn-instance) *vpn-instance-name* command to bind the BD to the EVPN instance.
   4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** | **prefix-route** } *prefix* command on the PE to check detailed BGP EVPN route information.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) **vpn-instance** *evpn-name-value* **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** } *prefix* command on the PE to check the EVPN route information of the specified EVPN instance.
* In a scenario where a CE is dual-homed to PEs, run the [**display evpn vpn-instance name**](cmdqueryname=display+evpn+vpn-instance+name) *vpn-instance-name* **df result** [ **esi** *esi* ] command on PEs to check the DF election result of the EVPN instance.