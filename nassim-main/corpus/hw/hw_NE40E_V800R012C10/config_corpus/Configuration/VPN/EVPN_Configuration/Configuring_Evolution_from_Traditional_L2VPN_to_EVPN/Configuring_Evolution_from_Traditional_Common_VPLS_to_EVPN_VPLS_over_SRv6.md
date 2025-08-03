Configuring Evolution from Traditional Common VPLS to EVPN VPLS over SRv6
=========================================================================

EVPN is today's mainstream transport solution. To prevent live network services from being affected, a new transport solution must be deployed based on these services. If a large number of traditional common VPLS services exist on the live network, you can configure evolution from traditional common VPLS to EVPN VPLS over SRv6 to prevent long-time traffic interruption caused by direct transition from traditional common VPLS to EVPN VPLS over SRv6.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0000001554738650__fig15171018161210), only traditional common VPLS over MPLS is deployed on PEs. After the evolution is complete, only EVPN VPLS over SRv6 is deployed on PEs, as shown in [Figure 2](#EN-US_TASK_0000001554738650__fig117910434294).

**Figure 1** Traditional common VPLS networking  
![](figure/en-us_image_0000001605080753.png)
**Figure 2** EVPN VPLS over SRv6 networking  
![](figure/en-us_image_0000001554640988.png)

#### Pre-configuration Tasks

Before configuring evolution from traditional common VPLS to EVPN VPLS over SRv6, complete the following tasks:

* [Configure LDP VPLS](dc_vrp_vpls_cfg_5003.html) between PE1, PE2, PE3, and PE4.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  In this task, a non-BD VSI must be created using the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** | **auto** ] command.
* Configure BGP EVPN IPv6 peer relationships, SRv6 BE, and IPv6 IS-IS between PE1, PE2, PE3, and PE4 and create a BD EVPN instance on each of these devices.

Perform the following steps on PE1, PE2, PE3, and PE4.


#### Procedure

1. Create a BD and configure evolution from common VPLS to EVPN.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to create a BD and enter its view.
   3. Run the [**vpls-to-evpn migration in-process**](cmdqueryname=vpls-to-evpn+migration+in-process) command to indicate that the BD is evolving from VPLS to EVPN.
   4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
2. Add all AC interfaces to the BD.
   1. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number.sub-number* command to enter the view of the AC interface that directly connects the PE to a CE.
   2. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to add the AC interface to the BD.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
3. (Optional) Configure TC notification on the AC interface's main interface.
   
   
   
   If the [**stp enable**](cmdqueryname=stp+enable) command is run on the AC interface's main interface to enable STP but the [**stp vpls-subinterface enable**](cmdqueryname=stp+vpls-subinterface+enable) command is not run before the evolution, during the evolution, the AC interface may be blocked when the broadcast domain switches from the VSI to the BD, and a traffic loop may occur when the broadcast domain switches from the BD to the VSI. You are advised to perform the following operations:
   
   
   
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
6. (Optional) After the evolution is complete, delete the configuration of evolution from common VPLS to EVPN as well as VSI-related configurations.
   1. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to enter the BD view.
   2. Run the [**undo vpls-to-evpn migration in-process**](cmdqueryname=undo+vpls-to-evpn+migration+in-process) command to disable evolution from common VPLS to EVPN.
      
      ![](../../../../public_sys-resources/caution_3.0-en-us.png) 
      
      The [**undo vpls-to-evpn migration in-process**](cmdqueryname=undo+vpls-to-evpn+migration+in-process) command is run after the evolution is complete. If the [**undo l2 binding**](cmdqueryname=undo+l2+binding) **vsi** *vsi-name* command is run following this command, all AC interfaces are unbound from the VSI, and services are switched to EVPN.
      
      If the [**undo vpls-to-evpn migration in-process**](cmdqueryname=undo+vpls-to-evpn+migration+in-process) command is not run in advance or encounters an error during execution, running the [**undo l2 binding**](cmdqueryname=undo+l2+binding) **vsi** *vsi-name* command does not unbind AC interfaces from the VSI. In this case, services are switched to the VSI.
   3. Run the [**undo l2 binding**](cmdqueryname=undo+l2+binding) **vsi** *vsi-name* command to unbind the BD from the VSI.
      
      
      
      Because the [**undo vpls-to-evpn migration in-process**](cmdqueryname=undo+vpls-to-evpn+migration+in-process) command has been run on the device, running this command unbinds all AC interfaces from the VSI.
   4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** | **prefix-route** } *prefix* command on the PE to check detailed BGP EVPN route information.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) **vpn-instance** *evpn-name-value* **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** } *prefix* command on the PE to check the EVPN route information of the specified EVPN instance.
* In a scenario where a CE is dual-homed to PEs, run the [**display evpn vpn-instance name**](cmdqueryname=display+evpn+vpn-instance+name) *vpn-instance-name* **df result** [ **esi** *esi* ] command on PEs to check the DF election result of the EVPN instance.