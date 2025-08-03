Configuring a VLAN Tag Termination Sub-interface
================================================

A virtual local area network (VLAN) tag termination sub-interface can be a dot1q VLAN tag termination sub-interface or a QinQ VLAN tag termination sub-interface. In dot1q/QinQ termination, a device identifies whether a packet has one tag or two tags. The device then forwards the packet after stripping one or both tags or discards the packet.

#### Context

Applications of VLAN tag termination

* Inter-VLAN communication
  
  The VLAN technology is widely used because it allows Layer 2 packets of different users to be transmitted separately. With the VLAN technology, a physical LAN is divided into multiple logical broadcast domains (VLANs). Hosts in the same VLAN can communicate with each other at Layer 2, but hosts in different VLANs cannot. The Layer 3 routing technology is required for communication between hosts in different VLANs. The following interfaces can be used to implement inter-VLAN communication:
  + Layer 3 Ethernet interfaces on routers
    
    Conventional Layer 3 Ethernet interfaces do not identify VLAN packets. After receiving VLAN packets, they consider the packets invalid and discard them. To implement inter-VLAN communication, create Ethernet sub-interfaces on a Layer 3 Ethernet interface and configure the sub-interfaces to remove tags from VLAN packets.
* Communication between devices in the LAN and WAN
  
  Most LAN packets carry VLAN tags. Certain wide area network (WAN) protocols, such as Point-to-Point Protocol (PPP), cannot identify VLAN packets. Before forwarding VLAN packets from a LAN to a WAN, a device needs to record the VLAN information carried in the VLAN packets and then remove the VLAN tags.
  
  When the device receives return packets, it adds the locally stored VLAN information to the packets before forwarding them downstream to VLAN users.


#### Procedure

* Configure a dot1q VLAN tag termination sub-interface.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subinterface-number*
     
     The view of the PE's Ethernet sub-interface connecting to the user side is displayed.
  3. (Optional) Create a user VLAN group.
     
     1. Run [**vlan-group**](cmdqueryname=vlan-group) *group-id*
        
        A user VLAN group is created.
     2. Run [**group mode**](cmdqueryname=group+mode) { **single** | **multiple** }
        
        The working mode of the VLAN group is configured.
        
        + **single**: A VLAN group is considered as a user. This means that you cannot collect statistics about QinQ packets or deploy quality of service (QoS) policies based on a VLAN or a VLAN range.
        + **multiple**: VLANs and VLAN ranges in a VLAN group are considered as different users. This means that you can collect statistics about QinQ packets or deploy QoS policies based on a VLAN or VLAN range to implement refined management.
     3. Run [**quit**](cmdqueryname=quit)
        
        Return to the view of the PE's Ethernet sub-interface connecting to the user side.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Configuring a VLAN group allows you to achieve the following purposes:
     
     + Deploy QoS policies based on services or users so that higher priority service traffic is preferentially forwarded, improving user experience.
     + View statistics about QinQ packets to check whether a device is functioning properly.
  4. Run [**control-vid**](cmdqueryname=control-vid) *vid* **dot1q-termination** [ **rt-protocol** ] or [**encapsulation**](cmdqueryname=encapsulation) **dot1q-termination** [ **rt-protocol** ]
     
     The encapsulation type is configured as dot1q VLAN tag termination for the sub-interface.
     
     Specify **rt-protocol** so that the dot1q VLAN tag termination sub-interface supports routing protocols.
     
     To enable the dot1q VLAN tag termination sub-interface to support routing protocols, specify **rt-protocol**.
  5. Configure the dot1q VLAN tag termination sub-interface using one or more of the following commands based on site requirements:
     + To configure a dot1q VLAN tag termination sub-interface, run the [**dot1q termination vid**](cmdqueryname=dot1q+termination+vid) *low-pe-vid* [ **to** *high-pe-vid* ] [ **vlan-group** *group-id* ] command.
     + To configure a dot1q VLAN tag termination sub-interface and a matching policy for the sub-interface, run the [**dot1q termination vid**](cmdqueryname=dot1q+termination+vid) *low-pe-vid* [ **to** *high-pe-vid* ] { **8021p** { *val8021p1* [ **to** *val8021p2* ] } &<1-8> | **dscp** { *valdscp1* [ **to** *valdscp2* ] } &<1-10> | **eth-type PPPoE** | **default** } [ **vlan-group** *group-id* ] command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + The preceding commands are all used to configure a dot1q VLAN tag termination sub-interface. If you do not configure any matching policy, the dot1q VLAN tag termination sub-interface terminates the VLAN tags of packets carrying the specified VLAN ID. If you configure a matching policy, the dot1q VLAN tag termination sub-interface terminates the VLAN tags of packets carrying the specified VLAN ID+802.1p value/DSCP value/EthType.
     + After the [**dot1q termination vid**](cmdqueryname=dot1q+termination+vid) *low-pe-vid* [ **to** *high-pe-vid* ] [ **vlan-group** *group-id* ] command is run in the Ethernet sub-interface view, the specified VLAN range belongs to the sub-interface, and any VLAN ID in the VLAN range cannot be configured together with the 802.1p value/DSCP value/EthType on other sub-interfaces.
  6. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure a QinQ VLAN tag termination sub-interface.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subinterface-number*
     
     The view of the PE's Ethernet sub-interface connecting to the user side is displayed.
  3. (Optional) Create a user VLAN group.
     
     1. Run [**vlan-group**](cmdqueryname=vlan-group) *group-id*
        
        A user VLAN group is created.
     2. Run [**group mode**](cmdqueryname=group+mode) { **single** | **multiple** }
        
        The working mode of the VLAN group is configured.
        
        + **single**: A VLAN group is considered as a user. This means that you cannot collect statistics about QinQ packets or deploy quality of service (QoS) policies based on a VLAN or a VLAN range.
        + **multiple**: VLANs and VLAN ranges in a VLAN group are considered as different users. This means that you can collect statistics about QinQ packets or deploy QoS policies based on a VLAN or VLAN range to implement refined management.
     3. Run [**quit**](cmdqueryname=quit)
        
        Return to the view of the PE's Ethernet sub-interface connecting to the user side.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Configuring a VLAN group allows you to achieve the following purposes:
     
     + Deploy QoS policies based on services or users so that higher priority service traffic is preferentially forwarded, improving user experience.
     + View statistics about QinQ packets to check whether a device is functioning properly.
  4. Run [**control-vid**](cmdqueryname=control-vid) *vid* **qinq-termination** [ **local-switch** | **rt-protocol** ] or [**encapsulation**](cmdqueryname=encapsulation) **qinq-termination** [ **local-switch** | **rt-protocol** ]
     
     The encapsulation type is configured as QinQ VLAN tag termination for the sub-interface.
     
     + Specify **local-switch** so that the QinQ VLAN tag termination sub-interface supports local switching.
     + Specify **rt-protocol** so that the QinQ VLAN tag termination sub-interface supports routing protocols.
  5. Run [**qinq termination pe-vid**](cmdqueryname=qinq+termination+pe-vid) *pe-vid* [ **to** *high-pe-vid* ] **ce-vid** *ce-vid* [ **to** *high-ce-vid* ] [ **vlan-group** *group-id* ]
     
     The encapsulation type is configured as QinQ VLAN tag termination for the sub-interface.
     
     If **rt-protocol** is specified, the QinQ VLAN tag termination sub-interface terminates double-tagged packets whose inner and outer tags contain only single VLAN IDs (not VLAN ranges).
  6. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.