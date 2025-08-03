Configuring Interworking Between Traditional Common VPLS and EVPN VPLS over SRv6 (HVPLS Scenario)
=================================================================================================

To configure interworking between traditional common VPLS and EVPN VPLS over SRv6 in an HVPLS scenario, you need to first configure EVPN VPLS over SRv6 on one side of the HVPLS network and then reconstruct the HVPLS network on the other side as required.

#### Context

It is feasible to evolve traditional common VPLS to EVPN VPLS over SRv6 in an HVPLS scenario. However, because the entire network involves a large number of devices, the evolution needs to be performed step by step. During the evolution, interworking between traditional common VPLS and EVPN VPLS over SRv6 is needed temporarily.

**Figure 1** Interworking between traditional common VPLS and EVPN VPLS over SRv6 (HVPLS)  
![](figure/en-us_image_0000001560662414.png)

#### Pre-configuration Tasks

Before configuring traditional common VPLS and EVPN VPLS over SRv6 to coexist, complete the following tasks:

* [Configure LDP HVPLS](dc_vrp_vpls_cfg_5009.html) between UPEs, SPEs, and NPEs.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  In this task, a non-BD VSI must be created using the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** | **auto** ] command.
* Configure SRv6 BE, IPv6 IS-IS, and BGP EVPN IPv6 peer relationships between SPEs and NPEs and create a BD EVPN instance on each of these devices.

#### Procedure

1. Create a BD on SPEs and NPEs and configure evolution from common VPLS to EVPN.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to create a BD and enter its view.
   3. Run the [**vpls-to-evpn migration in-process**](cmdqueryname=vpls-to-evpn+migration+in-process) command to indicate that the BD is evolving from VPLS to EVPN.
   4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
2. On NPEs, add all AC interfaces to the BD (sub-interfaces are used as AC interfaces in this case).
   1. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number.sub-number* command to enter the view of the AC interface that directly connects the PE to a CE.
   2. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to add the AC interface to the BD.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
3. (Optional) On NPEs, configure TC notification on the AC interface's main interface.
   
   
   
   If the [**stp enable**](cmdqueryname=stp+enable) command is run on the AC interface's main interface to enable STP but the [**stp vpls-subinterface enable**](cmdqueryname=stp+vpls-subinterface+enable) command is not run before the evolution, during the evolution, the AC interface may be blocked when the broadcast domain switches from the VSI to the BD, and a traffic loop may occur when the broadcast domain switches from the BD to the VSI. You are advised to perform the following operations:
   
   
   
   1. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the view of the AC interface's main interface.
   2. Run the [**stp vpls-subinterface enable**](cmdqueryname=stp+vpls-subinterface+enable) command to enable TC notification on the main interface.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
4. (Optional) On SPEs and NPEs, configure the maximum volume of unknown unicast traffic allowed by the BD.
   
   
   
   During the evolution, broadcast domain switching occurs, resulting in MAC address relearning. In this case, traffic is forwarded in unknown unicast mode within a short period of time. In response, you are advised to configure unknown unicast traffic suppression in the BD.
   
   
   
   1. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to enter the BD view.
   2. Run the [**unknown-unicast-suppression**](cmdqueryname=unknown-unicast-suppression) **cir** *cir-value* [ **cbs** *cbs-value* ] { **uni-inbound** | **uni-outbound** } command to configure the maximum unknown unicast traffic volume allowed by the BD.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
5. On SPEs and NPEs, bind the BD to both the VSI and EVPN instance.
   1. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to enter the BD view.
   2. Run the [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name* command to bind the BD to the VSI.
   3. Run the [**evpn binding vpn-instance**](cmdqueryname=evpn+binding+vpn-instance) *vpn-instance-name* command to bind the BD to the EVPN instance.
   4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
6. (Optional) After the evolution is complete, delete the configuration indicating that the BD is evolving from VPLS to EVPN as well as VSI-related configurations from NPEs.
   1. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to enter the BD view.
   2. Run the [**undo vpls-to-evpn migration in-process**](cmdqueryname=undo+vpls-to-evpn+migration+in-process) command to indicate that the BD has completed evolution from VPLS to EVPN.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   4. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to enter the BD view.
   5. Run the [**undo l2 binding**](cmdqueryname=undo+l2+binding) **vsi** *vsi-name* command to unbind the BD from the VSI.
      
      
      
      Because the [**undo vpls-to-evpn migration in-process**](cmdqueryname=undo+vpls-to-evpn+migration+in-process) command has been run on the device, running this command unbinds all AC interfaces from the VSI.
   6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
7. (Optional) After the evolution is complete, delete the configuration indicating that the BD is evolving from VPLS to EVPN from SPEs.
   1. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to enter the BD view.
   2. Run the [**undo vpls-to-evpn migration in-process**](cmdqueryname=undo+vpls-to-evpn+migration+in-process) command to indicate that the BD has completed evolution from VPLS to EVPN.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** | **prefix-route** } *prefix* command on the SPE and NPE to check detailed BGP EVPN route information.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) **vpn-instance** *evpn-name-value* **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** } *prefix* command on the SPE and NPE to check the EVPN route information of the specified EVPN instance.
* In a scenario where a CE is dual-homed to PEs, run the [**display evpn vpn-instance name**](cmdqueryname=display+evpn+vpn-instance+name) *vpn-instance-name* **df result** [ **esi** *esi* ] command on SPEs and NPEs to check the DF election result of the EVPN instance.