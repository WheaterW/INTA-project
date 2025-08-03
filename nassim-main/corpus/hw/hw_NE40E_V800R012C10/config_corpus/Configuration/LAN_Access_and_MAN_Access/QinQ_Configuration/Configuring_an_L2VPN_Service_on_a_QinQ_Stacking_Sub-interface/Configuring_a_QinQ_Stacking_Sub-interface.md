Configuring a QinQ Stacking Sub-interface
=========================================

This section describes how to configure a QinQ stacking sub-interface on a provider edge (PE) to provide Layer 2 virtual private network (L2VPN) access so that the inner virtual local area network (VLAN) tags of user packets are transparently transmitted over an ISP network.

#### Context

After you enable QinQ stacking on an Ethernet sub-interface:

* When the QinQ stacking sub-interface receives a packet, the sub-interface checks whether the VLAN ID or VLAN range in the VLAN tag of the packet matches the VLAN ID or VLAN range specified using the [**qinq stacking vid**](cmdqueryname=qinq+stacking+vid) command. If they are consistent, the sub-interface adds an outer VLAN tag to the packet.
  
  + If the packet carries one VLAN tag and the VLAN ID in the tag is in the VLAN range specified by *low-ce-vid* [ **to** *high-ce-vid* ] in the [**qinq stacking vid**](cmdqueryname=qinq+stacking+vid) command, the sub-interface adds an outer VLAN tag to the packet. If the VLAN ID in the VLAN tag is not in the specified VLAN range, the sub-interface discards the packet.
  + If the packet carries two VLAN tags and the VLAN ID in the outer tag is in the VLAN range specified by *low-ce-vid* [ **to** *high-ce-vid* ] in the [**qinq stacking vid**](cmdqueryname=qinq+stacking+vid) command, the sub-interface adds another outer VLAN tag to the packet and forwards the packet. In this case, the inner VLAN tag is transmitted transparently. If the VLAN ID in the outer tag is not in the specified VLAN range, the sub-interface discards the packet.
  + If the packet does not carry any VLAN tag, the sub-interface directly discards the packet.
* When the QinQ stacking sub-interface sends a packet, the sub-interface strips the outer VLAN tag of the packet.

![](../../../../public_sys-resources/note_3.0-en-us.png) After you run the [**qinq stacking vid**](cmdqueryname=qinq+stacking+vid) command on an Ethernet sub-interface:

* If you do not run the [**qinq stacking**](cmdqueryname=qinq+stacking) **pe-vid** *pe-vid* command to specify an outer VLAN tag to be added to packets, the Ethernet sub-interface will add a default outer VLAN tag to received packets.
  
  The default outer VLAN tag is assigned by the device and cannot be modified.
* If you run the [**qinq stacking**](cmdqueryname=qinq+stacking) **pe-vid** *pe-vid* command to specify an outer VLAN tag to be added to packets, the Ethernet sub-interface will add the specified outer VLAN tag to received packets.
  
  Before you run the [**qinq stacking**](cmdqueryname=qinq+stacking) **pe-vid** *pe-vid* command on an Ethernet sub-interface, you must run the [**qinq stacking vid**](cmdqueryname=qinq+stacking+vid) command on the sub-interface. Otherwise, the QinQ stacking function does not take effect.




#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subinterface-number*
   
   
   
   The view of an Ethernet sub-interface on the user side of a PE is displayed.
3. (Optional) Create a user VLAN group.
   
   
   1. Run [**vlan-group**](cmdqueryname=vlan-group) *group-id*
      
      A user VLAN group is created.
   2. Run [**group mode**](cmdqueryname=group+mode) { **single** | **multiple** }
      
      The working mode of the VLAN group is configured.
      
      * **single**: A VLAN group is considered as a user. This means that you cannot collect statistics about QinQ packets or deploy quality of service (QoS) policies based on a VLAN or a VLAN range.
      * **multiple**: VLANs and VLAN ranges in a VLAN group are considered as different users. This means that you can collect statistics about QinQ packets or deploy QoS policies based on a VLAN or VLAN range to implement refined management.
   3. Run [**quit**](cmdqueryname=quit)
      
      Return to the view of the PE's Ethernet sub-interface connecting to the user side.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Configuring a VLAN group allows you to achieve the following purposes:
   
   * Deploy QoS policies based on services or users so that higher priority service traffic is preferentially forwarded, improving user experience.
   * View statistics about QinQ packets to check whether a device is functioning properly.
4. Run one or more of the following commands to configure a QinQ stacking sub-interface as required.
   
   
   * To configure a QinQ stacking sub-interface, run the [**qinq stacking vid**](cmdqueryname=qinq+stacking+vid) *low-ce-vid* [ **to** *high-ce-vid* ] [ **vlan-group** *group-id* ] command.
   * To configure a QinQ stacking sub-interface with a matching policy specified based on VLAN ID+802.1p value/DSCP value/EthType, run the [**qinq stacking vid**](cmdqueryname=qinq+stacking+vid) *low-ce-vid* [ **to** *high-ce-vid* ] { **8021p** { *val8021p1* [ **to** *val8021p2* ] } &<1-8> | **dscp** { *valdscp1* [ **to** *valdscp2* ] } &<1-10> | **eth-type PPPoE** *eth-type-value* | **default** } [ **vlan-group** *group-id* ] command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If you have run the [**vlan-group**](cmdqueryname=vlan-group) command to configure a VLAN group on the sub-interface, specify **vlan-group** in the preceding commands.
   * If you have not run the [**vlan-group**](cmdqueryname=vlan-group) command to configure a VLAN group on the sub-interface, do not specify **vlan-group** in the preceding commands.
   * If you configure QinQ stacking on different Ethernet sub-interfaces of the same main interface, the **ce-vid** ranges cannot overlap between these sub-interfaces.
   * The preceding commands are both used to configure a QinQ stacking sub-interface. If you do not configure any matching policy, the QinQ stacking sub-interface adds an outer VLAN tag to packets based on the specified VLAN. If you configure a matching policy, the QinQ stacking sub-interface adds an outer VLAN tag to packets based on the specified VLAN ID+802.1p value/DSCP value/EthType.
   * When a QinQ stacking sub-interface is bound to a VLAN group, the VLAN group can work only in single mode, not multiple mode.
5. (Optional) Run [**qinq stacking**](cmdqueryname=qinq+stacking) **pe-vid** *pe-vid*
   
   
   
   The QinQ stacking sub-interface is enabled to add a specified outer VLAN tag to received packets.
   
   
   
   If you skip this step, the QinQ stacking sub-interface will add a system-assigned outer VLAN tag to received packets.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.