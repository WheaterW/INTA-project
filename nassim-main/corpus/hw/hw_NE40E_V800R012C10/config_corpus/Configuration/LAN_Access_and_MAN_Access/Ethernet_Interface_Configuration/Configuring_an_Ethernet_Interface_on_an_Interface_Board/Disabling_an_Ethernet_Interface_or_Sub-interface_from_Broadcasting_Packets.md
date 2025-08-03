Disabling an Ethernet Interface or Sub-interface from Broadcasting Packets
==========================================================================

To protect a device against attacks from broadcast packets and improve network security, disable the Ethernet interfaces or sub-interfaces on the device from broadcasting packets.

#### Context

An Ethernet interface or sub-interface broadcasts the packets they receive. Broadcasting attack packets from attackers consumes a lot of device resources, causing device performance deterioration and even device breakdown. To resolve this problem, disable the Ethernet interface or sub-interface from broadcasting packets.

You can disable the Ethernet interface or sub-interface from broadcasting packets if the network has fixed topologies or is configured with routes specified by static MAC addresses.


#### Procedure

* Disable an Ethernet interface from broadcasting packets.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The Ethernet interface must work in Layer 2 mode. Otherwise, it cannot be disabled from broadcasting packets.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     The view of the Ethernet interface to be disabled from broadcasting packets is displayed.
  3. Run [**portswitch**](cmdqueryname=portswitch)
     
     The interface is switched to the Layer 2 mode.
     
     If the Ethernet interface is already in Layer 2 mode, skip this step.
  4. Run [**broadcast discard**](cmdqueryname=broadcast+discard)
     
     The interface is disabled from broadcasting packets.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Disable an Ethernet sub-interface from broadcasting packets.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Before disabling an Ethernet sub-interface from broadcasting packets, make sure that the sub-interface is configured as a Dot1q sub-interface, QinQ VLAN tag termination sub-interface, Dot1q VLAN tag termination sub-interface, or QinQ stacking sub-interface.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subinterface-number*
     
     The view of the Ethernet sub-interface to be disabled from broadcasting packets is displayed.
  3. Run any of the following commands:
     
     + To configure the Ethernet sub-interface as a dot1q sub-interface, run the [**vlan-type dot1q**](cmdqueryname=vlan-type+dot1q) *vlan-id* command.
     + To configure a matching policy for the dot1q sub-interface, run the [**vlan-type dot1q**](cmdqueryname=vlan-type+dot1q) *vlanid* { **8021p** { *8021p-value1* [ **to** *8021p-value2* ] } &<1-8> | **dscp** { *dscp-value1* [ **to** *dscp-value2* ] } &<1-10> | **default** | **eth-type PPPoE** *eth-type-value* } command.
     + To configure the Ethernet sub-interface as a Dot1q VLAN tag termination sub-interface, run the [**dot1q termination vid**](cmdqueryname=dot1q+termination+vid) *low-pe-vid* [ **to** *high-pe-vid* ] [ **vlan-group** *group-id* ] command.
     + To configure a matching policy for the dot1q VLAN tag termination sub-interface, run the [**dot1q termination vid**](cmdqueryname=dot1q+termination+vid+to+8021p+to+dscp+to+eth-type+PPPoE+default) *low-pe-vid* [ **to** *high-pe-vid* ] { **8021p** { *val8021p1* [ **to** *val8021p2* ] } &<1-8> | **dscp** { *valdscp1* [ **to** *valdscp2* ] } &<1-10> | **eth-type PPPoE** *eth-type-value* | **default** } [ **vlan-group** *group-id* ] command.
     + To configure the Ethernet sub-interface as a QinQ VLAN tag termination sub-interface, run the [**qinq termination pe-vid**](cmdqueryname=qinq+termination+pe-vid+to+ce-vid+to+vlan-group) *pe-vid* [ **to** *high-pe-vid* ] **ce-vid** *ce-vid* [ **to** *high-ce-vid* ] [ **vlan-group** *group-id* ] command.
     + To configure the Ethernet sub-interface as a QinQ stacking sub-interface, run the [**qinq stacking vid**](cmdqueryname=qinq+stacking+vid+to+vlan-group) *low-ce-vid* [ **to** *high-ce-vid* ] [ **vlan-group** *group-id* ] command.
     + To configure a matching policy for the QinQ stacking sub-interface, run the [**qinq stacking vid**](cmdqueryname=qinq+stacking+vid+to+8021p+to+dscp+to+eth-type+PPPoE+default) *low-ce-vid* [ **to** *high-ce-vid* ] { **8021p** { *val8021p1* [ **to** *val8021p2* ] } &<1-8> | **dscp** { *valdscp1* [ **to** *valdscp2* ] } &<1-10> | **eth-type PPPoE** *eth-type-value* | **default** } [ **vlan-group** *group-id* ] command.
  4. Run [**broadcast discard**](cmdqueryname=broadcast+discard)
     
     The sub-interface is disabled from broadcasting packets.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.