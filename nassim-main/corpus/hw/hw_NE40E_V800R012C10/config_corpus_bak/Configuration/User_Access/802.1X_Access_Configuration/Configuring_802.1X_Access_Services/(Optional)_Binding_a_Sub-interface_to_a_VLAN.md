(Optional) Binding a Sub-interface to a VLAN
============================================

When restrictions on broadcast packets are required in a LAN to enhance the LAN security or to set up virtual working groups, VLANs must be configured. VLANs can be used only on Ethernet sub-interfaces.

#### Context

When a user accesses the network through a main interface, you do not need to bind the main interface to a VLAN. When a user accesses the network through a sub-interface, you need to bind the sub-interface to a VLAN.

You can bind a sub-interface to a VLAN or configure QinQ on a sub-interface. When binding a sub-interface to a VLAN, you need the following parameters:

* Number of the sub-interface
* VLAN ID
* QinQ ID

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* Each main interface can be configured with only one any-other sub-interface. The [**user-vlan**](cmdqueryname=user-vlan) **any-other** parameter cannot be configured together with the [**user-vlan**](cmdqueryname=user-vlan) *start-vlan* parameter or the [**user-vlan**](cmdqueryname=user-vlan) **qinq** parameter on the same sub-interface.
* If a sub-interface has configured with dot1q termination, QinQ termination, QinQ stacking, or VLAN-type dot1q, the [**user-vlan**](cmdqueryname=user-vlan) command cannot be run on the sub-interface.
* User VLANs with the same VLAN ID cannot be configured on different sub-interfaces.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number. subinterface-number*
   
   
   
   A sub-interface is created and the sub-interface view is displayed.
3. Run [**user-vlan**](cmdqueryname=user-vlan) { *start-vlan-id* [ *end-vlan-id* ] | *cevlan* } **qinq** { *start-pe-vlan* [ *end-pe-vlan* ] | *pevlan* }
   
   
   
   A user-VLAN sub-interface is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.