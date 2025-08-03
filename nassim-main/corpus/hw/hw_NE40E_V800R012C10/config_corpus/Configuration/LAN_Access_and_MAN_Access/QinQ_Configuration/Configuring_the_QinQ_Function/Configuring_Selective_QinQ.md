Configuring Selective QinQ
==========================

You can configure selective QinQ on a Layer 2 interface. This configuration allows the interface to add a public virtual local area network (VLAN) tag to a user packet that carries a private VLAN tag so that the user packet can be forwarded over the public network.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
   
   
   
   A VLAN is created, and the VLAN view is displayed.
   
   The VLAN ID must be the same as the value of the outer VLAN tag specified in the command for configuring selective QinQ.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The user-side Ethernet interface view is displayed.
5. (Optional) Run [**portswitch**](cmdqueryname=portswitch)
   
   
   
   The Layer 3 interface is switched to a Layer 2 interface.
   
   If the interface is a Layer 2 interface, skip this step.
6. Run [**port link-type**](cmdqueryname=port+link-type) { **hybrid** | **trunk** }
   
   
   
   The link type of an Ethernet interface is set to hybrid or trunk.
7. Run [**port vlan-stacking vlan**](cmdqueryname=port+vlan-stacking+vlan) *vlan-id1* [ **to** *vlan-id2* ] **stack-vlan** *vlan-id3*The interface is configured as a Layer 2 selective QinQ interface.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   *vlan-id3* must be the same as the *vlan-id* created in Step 2.
8. (Optional) Run [**qinq protocol**](cmdqueryname=qinq+protocol) *ethertype-value*
   
   
   
   The protocol type of the outer tag is configured.
   
   
   
   The value of *ethertype-value* ranges from 0x0600 to 0xFFFF.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**qinq protocol**](cmdqueryname=qinq+protocol) command takes effect both on double-tagged and single-tagged packets.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.