Configuring a QinQ Tunnel
=========================

After the QinQ tunnel is configured, the interface adds an outer VLAN tag to packets that carry an inner VLAN tag. These packets can then be forwarded on the public network.

#### Context

Perform the following steps on the device on which the QinQ tunnel is to be configured:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
   
   
   
   A VLAN is created, and its view is displayed.
   
   The VLAN ID refers to the value of the outer tag specified in the QinQ tunnel. The VLAN ID ranges from 1 to 4094.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The user-side Ethernet interface view is displayed.
5. (Optional) Run [**portswitch**](cmdqueryname=portswitch)
   
   
   
   The interface is configured as a Layer 2 interface.
   
   Skip this step if the interface is already a Layer 2 interface.
6. Run [**port link-type**](cmdqueryname=port+link-type) **dot1q-tunnel**
   
   
   
   The interface is configured as a QinQ interface.
7. Run [**port default vlan**](cmdqueryname=port+default+vlan) *vlan-id*
   
   
   
   An outer VLAN tag is configured for packets passing through the QinQ Layer 2 interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   *vlan-id* must be the same as the VLAN ID created in Step 2.
8. (Optional) Run [**qinq protocol**](cmdqueryname=qinq+protocol) *ethertype-value*
   
   
   
   The protocol type of the outer tag is configured.
   
   
   
   The value of *ethertype-value* ranges from 0x0600 to 0xFFFF.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**qinq protocol**](cmdqueryname=qinq+protocol) command takes effect both on double-tagged and single-tagged packets.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.