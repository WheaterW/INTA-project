Creating a VLAN
===============

Creating a VLAN isolates PCs that do not need to communicate with each other. This improves network security, reduces broadcast traffic, and prevents broadcast storms.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
   
   
   
   A VLAN is created, and its view is displayed. If the specified VLAN has been created, the VLAN view is directly displayed.
   
   
   
   A VLAN ID ranges from 1 to 4094. If VLANs need to be created in batches, you can run the [**vlan batch**](cmdqueryname=vlan+batch) command to create VLANs in batches, and then run the [**vlan**](cmdqueryname=vlan) *vlan-id* command to enter the view of a specified VLAN.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If a device is configured with multiple VLANs, configuring VLAN names to facilitate management is recommended:
   
   Run the [**name**](cmdqueryname=name) *vlan-name* command in the VLAN view. After a VLAN name is configured, you can run the [**vlan vlan-name**](cmdqueryname=vlan+vlan-name) *vlan-name* command in the system view to enter the corresponding VLAN view.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.