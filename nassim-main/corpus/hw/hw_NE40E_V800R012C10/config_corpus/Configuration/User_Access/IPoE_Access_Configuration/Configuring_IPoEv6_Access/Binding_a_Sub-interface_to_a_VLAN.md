Binding a Sub-interface to a VLAN
=================================

The NE40E processes tagged user packets received from different types of users in different manners to ensure proper packet forwarding.

#### Context

If users access the network through a sub-interface, the sub-interface needs to be bound to a VLAN.

You can bind a sub-interface to a VLAN or configure QinQ on a sub-interface. When binding a sub-interface to a VLAN, you need the following parameters:

* Sub-interface number
* VLAN ID
* QinQ ID

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number. subinterface-number*
   
   
   
   A sub-interface is created and the sub-interface view is displayed.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Each main interface can have only one sub-interface with the [**user-vlan**](cmdqueryname=user-vlan) **any-other** command configured. You cannot configure **any-other** together with *start-vlan* or **qinq** in the [**user-vlan**](cmdqueryname=user-vlan) command on the same sub-interface.
   * If dot1q termination, QinQ termination, QinQ stacking, or dot1q VLAN encapsulation (configured using the [**vlan-type dot1q**](cmdqueryname=vlan-type+dot1q) command) has been configured on a sub-interface, the [**user-vlan**](cmdqueryname=user-vlan) command cannot be configured on this sub-interface.
   * Different sub-interfaces cannot be configured with user-side VLANs with the same VLAN ID.
3. Depending on the user access type, run either of the following commands to create a user-side VLAN:
   
   
   * To create a user-side VLAN for Layer 2 subscriber access, run the [**user-vlan**](cmdqueryname=user-vlan) { *start-vlan* [ *end-vlan* ] [ **dot1q** *start-qinq-id* [ *end-qinq-id* ] ] | *any-other* } command.
   * To create a user-side VLAN for Layer 3 subscriber access, run the [**vlan-type**](cmdqueryname=vlan-type) **dot1q** *vlan-id* command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.