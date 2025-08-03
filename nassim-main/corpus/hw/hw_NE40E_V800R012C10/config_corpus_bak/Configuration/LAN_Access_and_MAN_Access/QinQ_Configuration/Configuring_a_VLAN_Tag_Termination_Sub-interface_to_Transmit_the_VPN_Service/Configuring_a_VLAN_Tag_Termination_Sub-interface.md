Configuring a VLAN Tag Termination Sub-interface
================================================

A virtual local area network (VLAN) tag termination sub-interface can be a dot1q VLAN tag termination sub-interface or a QinQ VLAN tag termination sub-interface. In dot1q/QinQ termination, a device identifies whether a packet has one tag or two tags. The device then forwards the packet after stripping one or both tags or discards the packet.

#### Context

An increasing number of QinQ encapsulation and termination modes have been developed to distinguish users or services and reduce the use of virtual local area network (VLAN) IDs. These QinQ encapsulation and termination modes enable carriers to implement refined operation.

Users may communicate over various types of Layer 2 virtual private networks (L2VPNs), such as a virtual private wire service (VPWS) or virtual private LAN service (VPLS). To achieve more flexibility in managing packets for these users, you can configure QinQ VLAN tag termination sub-interfaces on edge devices on the L2VPN and configure the attributes of the sub-interfaces to provide L2VPN access.

QinQ VLAN tag termination sub-interfaces can access VPWS or VPLS in symmetrical or asymmetrical mode. User packets are sent to the L2VPN in different modes after being processed by the PE, as described in [Table 1](#EN-US_TASK_0172363264__tab_01) and [Table 2](#EN-US_TASK_0172363264__tab_02).

**Table 1** Packet processing on an inbound interface
| Inbound Interface Type | VPWS/VPLS | |
| --- | --- | --- |
| Ethernet Encapsulation | VLAN Encapsulation |
| Symmetry mode | Removes the outer tag. | Keeps both inner and outer tags unchanged. |
| Asymmetrical mode | Removes both inner and outer tags. | Removes both inner and outer tags and adds another tag. |


**Table 2** Packet processing on an outbound interface
| Outbound Interface Type | VPWS/VPLS | |
| --- | --- | --- |
| Ethernet Encapsulation | VLAN Encapsulation |
| Symmetry mode | Adds an outer tag. | Replaces the outer tag. |
| Asymmetrical mode | Adds two tags. | Removes the existing tag, and adds two tags. |


![](../../../../public_sys-resources/note_3.0-en-us.png) To configure VLAN encapsulation or Ethernet encapsulation, run the [**encapsulation (VSI view)**](cmdqueryname=encapsulation+%28VSI+view%29) command.

* VLAN encapsulation
  
  Each Ethernet frame transmitted between CEs and PEs carries a VLAN tag called a Provider-Tag (P-tag). The tag is a service delimiter required by a carrier for user differentiation.
* Ethernet encapsulation
  
  Ethernet frames transmitted between CEs and PEs do not carry P-tags. If an Ethernet frame carries a VLAN tag, the tag is an internal VLAN tag called a User-Tag (U-tag). It is carried in a user packet before the packet is sent to a CE. The U-tag is used by the CE to identify the packet and is meaningless to the PE.



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
  5. Run [**qinq termination l2**](cmdqueryname=qinq+termination+l2) { **asymmetry** | **symmetry** [ **user-mode** ] }
     
     The termination mode is configured for the QinQ VLAN tag termination sub-interface that provides L2VPN access.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     This step takes effect only on QinQ VLAN tag termination sub-interfaces that provide L2VPN access, not L3VPN access. This means that before you configure a QinQ VLAN tag termination sub-interface that provides L2VPN access, configure the termination mode of the sub-interface.
     
     + If the [**qinq termination l2**](cmdqueryname=qinq+termination+l2) **symmetry** command is used on a QinQ VLAN tag termination sub-interface, the sub-interface connects to the L2VPN in symmetrical mode. MAC address learning is performed only on the outer tags carried in packets. The sub-interface sends inner tags as part of the data to the peer, implementing inner tag isolation. To configure QoS for inner tags, run the [**qinq termination l2**](cmdqueryname=qinq+termination+l2) **symmetry** **user-mode** command.
     + If the [**qinq termination l2**](cmdqueryname=qinq+termination+l2) **asymmetry** command is used on a QinQ VLAN tag termination sub-interface, the sub-interface connects to the L2VPN in asymmetrical mode. MAC address learning is performed on both inner and outer tags carried in packets. The sub-interface does not send inner tags as part of the data to the peer.
     + If the [**qinq termination l2**](cmdqueryname=qinq+termination+l2) **asymmetry** command is run on a QinQ VLAN tag termination sub-interface, the sub-interface can terminate single inner and outer VLAN tags carried in packets but cannot terminate VLAN tag ranges.
  6. Run [**qinq termination pe-vid**](cmdqueryname=qinq+termination+pe-vid) *pe-vid* [ **to** *high-pe-vid* ] **ce-vid** *ce-vid* [ **to** *high-ce-vid* ] [ **vlan-group** *group-id* ]
     
     The encapsulation type is configured as QinQ VLAN tag termination for the sub-interface.
     
     If **rt-protocol** is specified, the QinQ VLAN tag termination sub-interface terminates double-tagged packets whose inner and outer tags contain only single VLAN IDs (not VLAN ranges).
  7. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.