Configuring 802.1Q Encapsulation
================================

When a Layer 3 device and a Layer 2 device are directly connected through Ethernet interfaces and the interface that directly connects the Layer 2 device to the Layer 3 device is added to a VLAN, configure an encapsulation mode for the Ethernet sub-interface on the Layer 3 device to ensure that the two devices normally communicate with each other.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=ip+address+sub) *interface-type interface-number.subinterface-number*
   
   
   
   The view of the Ethernet sub-interface that needs to be configured with 802.1Q encapsulation is displayed.
3. Run one or more of the following commands as needed to configure dot1q sub-interfaces:
   
   
   * To configure a dot1q sub-interface, run the [**vlan-type dot1q**](cmdqueryname=vlan-type+dot1q) *vlan-id* command.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Each Ethernet sub-interface can be associated with only one VLAN. Sub-interfaces of different main interfaces can be bound to the same VLAN, but sub-interfaces of the same main interface cannot be bound to the same VLAN.
   * To configure a matching policy for the dot1q sub-interface, run the [**vlan-type dot1q**](cmdqueryname=vlan-type+dot1q) *vlanid* { **8021p** { *8021p-value1* [ **to** *8021p-value2* ] } &<1-8> | **dscp** { *dscp-value1* [ **to** *dscp-value2* ] } &<1-10> | **default** | **eth-type** **PPPoE** } command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If you do not configure a matching policy, the dot1q sub-interface matches packets according to the VLAN ID. If you configure a matching policy, the dot1q sub-interface matches packets according to both the VLAN ID and the specified 802.1p value, DSCP value, or EthType.
   * After the [**vlan-type dot1q**](cmdqueryname=vlan-type+dot1q) *vlan-id* command is run in the Ethernet sub-interface view, the specified VLAN is exclusively used by this sub-interface and cannot be specified during 802.1p value/DSCP value/EthType configuration on other sub-interfaces that belong to the same main interface as this sub-interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In the scenario where an interface has a large number of sub-interfaces, if you run the [**shutdown**](cmdqueryname=shutdown) command in the sub-interface view to shut down the sub-interfaces one after another, the work load is huge. In this case, you can shut down the sub-interfaces in batches by running the [**shutdown interface**](cmdqueryname=shutdown+interface) command in the system view.