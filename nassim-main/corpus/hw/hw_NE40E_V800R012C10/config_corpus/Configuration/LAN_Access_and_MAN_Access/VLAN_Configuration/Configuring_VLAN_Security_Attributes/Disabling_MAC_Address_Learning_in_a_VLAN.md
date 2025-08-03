Disabling MAC Address Learning in a VLAN
========================================

If a device has only one inbound port and one outbound port, or the network topology is stable, MAC address learning in a VLAN can be disabled.

#### Context

A company has multiple departments located in different stories of a building. It is required that PCs of one department be grouped into a VLAN and PCs in different departments be grouped into different VLANs.

On the network shown in [Figure 1](#EN-US_TASK_0172363121__fig_dc_vrp_vlan_cfg_002501), department 1 belongs to VLAN 2; department 2 belongs to VLAN 3; the public sector belongs to VLAN 10. Users in VLANs 2 and 3 can access VLAN 10. Users in VLAN 2 or 3 can communicate with each other. Users in VLAN 2 cannot communicate with users in VLAN 3. To reduce the number of MAC address entries saved on the core switching device and prevent visitors from accessing the company's network, you can disable MAC address learning in a VLAN on CE 1 and CE 5.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Disabling MAC address learning in a VLAN is suitable for a device that has only one inbound port and one outbound port or a network with a stable topology.


**Figure 1** Disabling MAC address learning in a VLAN  
![](images/fig_dc_vrp_vlan_cfg_002501.png)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
   
   
   
   The VLAN view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If a device is configured with multiple VLANs, configuring VLAN names to facilitate management and maintenance is recommended:
   
   Run the [**name**](cmdqueryname=name) *vlan-name* command in the VLAN view. After a VLAN name is configured, you can run the [**vlan vlan-name**](cmdqueryname=vlan+vlan-name) *vlan-name* command in the system view to enter the corresponding VLAN view.
3. Run [**mac-address learning disable**](cmdqueryname=mac-address+learning+disable)
   
   
   
   MAC address learning in a VLAN is disabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.