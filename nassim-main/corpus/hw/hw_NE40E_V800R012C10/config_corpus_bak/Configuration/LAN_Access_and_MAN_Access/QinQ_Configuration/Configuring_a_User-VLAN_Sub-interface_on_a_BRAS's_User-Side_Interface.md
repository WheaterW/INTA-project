Configuring a User-VLAN Sub-interface on a BRAS's User-Side Interface
=====================================================================

When VLAN users access an IP core network through a BRAS, the IP core network cannot identify users' VLAN tags. In this situation, configure a user-VLAN sub-interface on the BRAS to remove the VLAN tags carried in the user VLAN packets.

#### Usage Scenario

If a Layer 2 network connects to an IP core network through a BRAS, it is recommended that you configure a dot1q or QinQ VLAN tag termination sub-interface on the BRAS to remove the VLAN tags before sending user VLAN packets to the IP core network.

If a Layer 3 network connects to an IP core network through a BRAS, it is recommended that you configure a dot1q or QinQ VLAN tag termination sub-interface on the BRAS to remove the VLAN tags before sending user VLAN packets to the IP core network.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration is supported only in user access scenarios.

#### Pre-configuration Tasks

Before configuring a user-VLAN sub-interface on a BRAS's user-side interface, correctly plan the user VLANs to allow the user packets that the sub-interface receives to carry one or two VLAN tags.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subinterface-number*
   
   
   
   The view of a BRAS's user-side Ethernet sub-interface is displayed.
3. (Optional) Run [**qinq-vlan**](cmdqueryname=qinq-vlan) *pe-vlan* **description** *description*
   
   
   
   A description is configured for the outer VLAN tag carried in double-tagged packets received by the sub-interface.
   
   
   
   To learn only the users' service information in scenarios where users send double-tagged VLAN packets (with the outer VLAN tag representing services and the inner VLAN tag representing users) to go online in batches through a BRAS, configure a description for the outer VLAN tag carried in double-tagged packets received by the BRAS's user-side sub-interface.
4. Run [**user-vlan**](cmdqueryname=user-vlan) { *start-vlan-id* [ *end-vlan-id* ] | [ *cevlan* ] } **qinq** { *start-pe-vlan* [ *end-pe-vlan* ] | [ *pevlan* ] }
   
   
   
   The Ethernet sub-interface is configured as a user-VLAN sub-interfaced, and the user-VLAN view is displayed.
5. (Optional) Run [**vlan**](cmdqueryname=vlan) *vlan-id* [ **qinq** *pe-vlan* ] **description** *description*
   
   
   
   A description is configured for the user VLAN.
   
   
   
   In VS mode, this command is supported only by the admin VS.
   
   To learn not only online service information but also user information, configure a user VLAN description.

#### Verifying the Configuration

Run the [**display sub-interface**](cmdqueryname=display+sub-interface) *interface-type interface-number* **pevlan** *pevlan* [ **cevlan** *cevlan* ] command to check information about user-VLAN sub-interfaces.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this command is supported only by the admin VS.