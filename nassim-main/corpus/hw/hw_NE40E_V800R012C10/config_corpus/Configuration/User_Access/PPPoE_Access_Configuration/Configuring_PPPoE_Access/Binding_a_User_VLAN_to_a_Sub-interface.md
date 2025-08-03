Binding a User VLAN to a Sub-interface
======================================

To restrict broadcast packets on a LAN and enhance LAN security or create virtual groups, configure VLANs. VLANs apply only to Ethernet sub-interfaces.

#### Context

If users access the network through a sub-interface, you must bind a user VLAN to the sub-interface.

You can bind a user VLAN to a sub-interface or configure QinQ on a sub-interface. When binding a user VLAN to a sub-interface, you need the following parameters:

* Sub-interface number
* VLAN ID
* QinQ ID

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* On each interface, you can set [**user-vlan**](cmdqueryname=user-vlan) **any-other** only on one sub-interface. On one sub-interface, [**user-vlan**](cmdqueryname=user-vlan) **any-other** cannot be set together with [**user-vlan**](cmdqueryname=user-vlan) *start-vlan* or [**user-vlan**](cmdqueryname=user-vlan) **qinq**.
* The [**user-vlan**](cmdqueryname=user-vlan) command cannot be configured on a sub-interface of a Layer 2 interface.
* If dot1q termination, QinQ termination, QinQ stacking, or vlan-type dot1q has been configured on a sub-interface, the [**user-vlan**](cmdqueryname=user-vlan) command cannot be configured on this sub-interface.
* Different sub-interfaces cannot be configured with user VLANs with the same VLAN ID.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**set vlan-statistics subinterface enable**](cmdqueryname=set+vlan-statistics+subinterface+enable)
   
   
   
   PPPoE statistics collection is enabled on QinQ interfaces.
3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number. subinterface-number*
   
   
   
   A sub-interface is created and the sub-interface view is displayed.
4. Run [**user-vlan**](cmdqueryname=user-vlan) { *start-vlan-id* [ *end-vlan-id* ] | *cevlan* } **qinq** { *start-pe-vlan* [ *end-pe-vlan* ] | *pevlan* }
   
   
   
   A user VLAN is bound to the sub-interface.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.