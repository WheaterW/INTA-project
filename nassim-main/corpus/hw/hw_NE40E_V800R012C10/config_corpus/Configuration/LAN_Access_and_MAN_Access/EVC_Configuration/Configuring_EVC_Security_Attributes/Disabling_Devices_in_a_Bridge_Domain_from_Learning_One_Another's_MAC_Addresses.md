Disabling Devices in a Bridge Domain from Learning One Another's MAC Addresses
==============================================================================

If a bridge domain has only one inbound interface and one outbound interface, the MAC address learning function can be disabled in the bridge domain.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0172363379__fig_dc_vrp_evc_cfg_001401), an enterprise has departments on different floors. Department 1 is assigned to VLAN2, department 2 is assigned to VLAN3, and the public department is assigned to VLAN10. All these departments are within a bridge domain with ID 10. After network deployment, VLAN2 and VLAN3 users can access VLAN10, VLAN2 users can communicate with each other, and VLAN2 and VLAN3 are isolated from each other. After the enterprise network is running a period of time, the network becomes stable, and no new users access this network. To help efficiently use MAC address table capacity on core devices and prevent unauthorized users from accessing the enterprise network, disable CE1 and CE2 from learning MAC addresses.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

CEs can also be disabled from learning MAC addresses in a specified VLAN. If a great number of VLANs are configured on CEs, manually disabling the VLAN-specific MAC address learning increases the maintenance expenditure.


**Figure 1** Networking diagram for preventing devices in a bridge domain from learning one another's MAC addresses  
![](images/fig_dc_vrp_evc_cfg_001401.png)  


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
   
   
   
   The bridge domain view is displayed.
3. Run [**mac-address learning disable**](cmdqueryname=mac-address+learning+disable)
   
   
   
   A device in a bridge domain is disabled from learning one another's MAC addresses.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.