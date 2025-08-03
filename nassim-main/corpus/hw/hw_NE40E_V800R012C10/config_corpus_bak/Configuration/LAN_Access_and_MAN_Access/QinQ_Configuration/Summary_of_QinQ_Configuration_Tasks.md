Summary of QinQ Configuration Tasks
===================================

This section describes the QinQ features supported by the NE40E in terms of the QinQ configuration.

The QinQ configuration is described as follows:

1. A QinQ-enabled device is capable of virtual local area network (VLAN) stacking, which expands VLAN space and reduces the consumption of VLAN ID resources.If Layer 2 selective QinQ is configured, the device can add different outer VLAN tags to packets and transmit the packets.
2. QinQ supports the following functions to meet the requirements of special applications and extended functions:
   
   * Configuring QinQ-based VLAN tag swapping: The device can swap the inner tag with the outer tag in a double-tagged packet.
   * Configuring QinQ mapping: The device can map the user VLAN ID in a packet to a carrier VLAN ID.
   * Configuring VLAN tag termination sub-interfaces for IP service access: Proxy Address Resolution Protocol (ARP), Dynamic Host Configuration Protocol (DHCP) server/DHCP relay, Virtual Router Redundancy Protocol (VRRP) can be configured on QinQ/dot1q VLAN tag termination sub-interfaces.
   * Configuring VLAN tag termination sub-interfaces for virtual private network (VPN) service access: L2VPN (VPWS/VPLS) and L3VPN services can be configured on QinQ/dot1q VLAN tag termination sub-interfaces.
   * Configuring QinQ VLAN tag termination sub-interfaces to support 802.1p mappings: The mappings include the 802.1p-to-DSCP mapping and 802.1p-to-MPLS-EXP mapping.
   * Configuring L2VPN access on QinQ stacking sub-interfaces: With this configuration, QinQ stacking sub-interfaces can implement L2VPN (VPWS/VPLS).
3. QinQ stacking sub-interfaces can be used to solve the problem that one physical interface cannot provide L2VPN access for multiple users.

#### Access Services Provided by VLAN Tag Termination Sub-Interfaces

Sub-interfaces for QinQ/dot1q VLAN tag termination support IP services (for example, proxy ARP, DHCP, and VRRP), VPN services (for example, L2VPN and L3VPN), 802.1p-to-DSCP mapping, and 802.1p-to-MPLS-EXP mapping. [Table 1](#EN-US_CONCEPT_0172363210__tab_dc_vrp_qinq_cfg_000202) shows the application scenario of a VLAN tag termination sub-interface providing access services.

**Table 1** Application scenario of VLAN tag termination sub-interfaces providing access services
| Sub-Interface Type | Service Type | Application Scenario |
| --- | --- | --- |
| QinQ/Dot1q | Proxy ARP | If users on the same network segment belong to different VLANs, they cannot communicate at Layer 2. To implement communication between VLANs at Layer 3, proxy ARP can be enabled on VLAN tag termination sub-interfaces.  For details about proxy ARP, see the chapter "ARP" in the *NE40E Feature Description - IP Services*. |
| DHCP  * DHCP server * DHCP relay | * To assign IP addresses to users on a VLAN tag termination sub-interface, the DHCP server function needs to be enabled on this sub-interface. * If the DHCP client and DHCP server belong to different sub-nets, you need to deploy a DHCP relay agent to forward DHCP request packets from the client to the server so that the client can dynamically obtain IP addresses from the DHCP server.  DHCP relay can be configured on the VLAN tag termination sub-interface to insert tag information into Option82. The tag information provides a reference for the DHCP server in IP address allocation.  For details about DHCP, see the chapter "DHCP" in the *NE40E Feature Description - IP Services*. |
| VRRP | When a VLAN tag termination sub-interface is used to access a VRRP-enabled, this sub-interface also needs to be enabled with VRRP to ensure reliable and stable communication.  For details about VRRP, see the chapter "VRRP" in the *NE40E Feature Description - Reliability*. |
| L2VPN  * Virtual private wire service (VPWS) * Virtual private LAN service (VPLS) | When a VLAN tag termination sub-interface is used to access a L2VPN network, this sub-interface needs to be bound to a Virtual Switching Instance (VSI) or virtual private wire service (VPWS) to enable Layer 2 communication.  For details about L2VPN, see the chapters "VPWS" and "VPLS" in the *NE40E Feature Description - VPN*. |
| L3VPN | When a VLAN tag termination sub-interface is used to access an L3VPN network, this sub-interface needs to be bound to a VPN instance to enable Layer 3 communication.  For details about L3VPN, see the chapter "BGP/MPLS IP VPN" in the *NE40E Feature Description - VPN*. |
| QinQ | 802.1p, DiffServ Code Point (DSCP) remark | After a packet is terminated on a PE, the packet is sent to the carrier network. To ensure the completeness of the QoS information in the packet, the 802.1p values in the outer and inner tags need to be mapped to the DSCP remark field. |
| 802.1p, EXP (MPLS) remark | After a packet is terminated on a PE, the packet is sent to the carrier MPLS network. To ensure the completeness of the QoS information in the packet, the 802.1p values in the outer and inner tags need to be mapped to the MPLS EXP field. |

[Figure 1](#EN-US_CONCEPT_0172363210__fig_dc_vrp_qinq_cfg_000201) shows how to configure sub-interfaces for QinQ/dot1q VLAN tag termination.

**Figure 1** Flowchart of configuring sub-interfaces for QinQ/dot1q VLAN tag termination  
![](images/fig_dc_vrp_qinq_cfg_000201.png)

#### Differences Between the VLAN Tag Termination Sub-interface and Dot1q Sub-interface

[Table 2](#EN-US_CONCEPT_0172363210__tab_dc_vrp_qinq_cfg_000203) shows the differences between the VLAN tag termination sub-interface and dot1q sub-interface.

**Table 2** Differences between interfaces
| Interface Type | Supported VPN Service | | | | Description | Difference |
| --- | --- | --- | --- | --- | --- | --- |
| VPWS (CCC mode) | VPWS | VPLS | L3VPN |
| Dot1q sub-interface | Supported | Supported | Supported | Supported | You can run the [**vlan-type dot1q**](cmdqueryname=vlan-type+dot1q) command to configure an Ethernet sub-interface to be a dot1q sub-interface. | * The dot1q sub-interface and dot1q VLAN tag termination sub-interface have the same function. The difference between them is that packets sent from the dot1q sub-interface are encapsulated with only one VLAN tag whereas packets sent from the dot1q VLAN tag termination sub-interface can be encapsulated with multiple VLAN tags. * You can configure both dot1q VLAN tag termination sub-interfaces and QinQ VLAN tag termination sub-interfaces on a main interface. With this configuration, the main interface can terminate both single-tagged packets and double-tagged packets. You can configure a dot1q VLAN tag termination sub-interface or a dot1q sub-interface on a main interface to terminate single-tagged packets. |
| Dot1q VLAN tag termination sub-interface | Supported | Supported | Supported | Supported | You can run the [**dot1q termination vid**](cmdqueryname=dot1q+termination+vid) command to configure a dot1q VLAN tag termination sub-interface to terminate single-tagged packets.  NOTE:   * VPWS  The VLAN tag to be terminated must be a specific value. * VPLS  The VLAN tag to be terminated can be either a specific value or a value range. |
| QinQ VLAN tag termination sub-interface | Supported | Supported | Supported | Supported | You can run the [**qinq termination pe-vid ce-vid**](cmdqueryname=qinq+termination+pe-vid+ce-vid) command to configure a QinQ VLAN tag termination sub-interface to terminate double-tagged packets.  NOTE:   * VPWS  In asymmetrical mode, both VLAN tags to be terminated must be specific values.  In symmetrical mode, the outer VLAN tag to be terminated must be a specific value, but the inner VLAN tag to be terminated can be either a specific value or value range. * VPLS  In asymmetrical mode, both VLAN tags to be terminated can be either specific values or value ranges.  In symmetrical mode, the outer VLAN tag to be terminated must be a specific value, but the inner VLAN tag to be terminated can be either a specific value or value range.   You can run the [**qinq termination l2**](cmdqueryname=qinq+termination+l2) command to configure the asymmetrical or symmetrical mode. |

[Table 3](#EN-US_CONCEPT_0172363210__tab_dc_vrp_qinq_cfg_000204) and [Table 4](#EN-US_CONCEPT_0172363210__tab_dc_vrp_qinq_cfg_000205) show how different types of interfaces process VLAN tags carried in packets to be transmitted across a VPLS network.

**Table 3** Packet processing on an inbound interface
| Inbound Interface Type | Packet Processing for VPLS Network Access | |
| --- | --- | --- |
| Ethernet-Encapsulated Packets | VLAN-Encapsulated Packets |
| Dot1q sub-interface | Tags are stripped. | No action is performed. |
| Dot1q VLAN tag termination sub-interface | Tags are stripped. | No action is performed. |
| QinQ VLAN tag termination sub-interface | * In symmetric mode, the outer tags are stripped. * In symmetric mode, both inner and outer tags are stripped. | * In symmetric mode, no action is performed. * In asymmetric mode, both inner and outer tags are stripped and then a different tag is added. |
| QinQ stacking sub-interface | The outer tag is added. | The outer tag is added. |
| QinQ mapping sub-interface | The outer tag is replaced. | The outer tag is replaced. |


**Table 4** Packet processing on an outbound interface
| Outbound Interface Type | Packet Processing for VPLS Network Access | |
| --- | --- | --- |
| Ethernet-Encapsulated Packets | VLAN-Encapsulated Packets |
| Dot1q sub-interface | A specific tag is added. | The tag is replaced. |
| Dot1q VLAN tag termination sub-interface | A specific tag is added. | The tag is replaced. |
| QinQ VLAN tag termination sub-interface | * In symmetric mode, outer tags are added. * In asymmetric mode, both inner and outer tags are added. | * In symmetric mode, outer tags are replaced. * In asymmetric mode, one tag is stripped and both inner and outer tags are added. |
| QinQ stacking sub-interface | The outer tag is stripped. | The outer tag is stripped. |
| QinQ mapping sub-interface | The outer tag is replaced. | The outer tag is replaced. |


![](../../../../public_sys-resources/note_3.0-en-us.png) To configure VLAN encapsulation or Ethernet encapsulation, run the [**encapsulation (VSI view)**](cmdqueryname=encapsulation+%28VSI+view%29) command.

* VLAN encapsulation
  
  Each Ethernet frame transmitted between CEs and PEs carries a VLAN tag called a Provider-Tag (P-tag). The tag is a service delimiter required by a carrier for user differentiation.
* Ethernet encapsulation
  
  Ethernet frames transmitted between CEs and PEs do not carry P-tags. If an Ethernet frame carries a VLAN tag, the tag is an internal VLAN tag called a User-Tag (U-tag). It is carried in a user packet before the packet is sent to a CE. The U-tag is used by the CE to identify the packet and is meaningless to the PE.