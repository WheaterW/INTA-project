Creating a VLANIF Interface
===========================

Before configuring Layer 3 features on a Layer 2 device, create a VLANIF interface on the device first.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **vlanif** *vlan-id*
   
   
   
   A VLANIF interface is created, and its view is displayed.
   
   
   
   The VLAN ID specified in this command must be the ID of an existing VLAN.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A VLANIF interface is up only when at least one physical port added to the corresponding VLAN is up.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.