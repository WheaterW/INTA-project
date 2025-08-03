Understanding VXLAN Tunnel Establishment in Static Mode (Centralized VXLAN Gateway)
===================================================================================

In a static VXLAN tunnel establishment scenario where VXLAN gateways are deployed in centralized mode, the control and forwarding planes have different responsibilities. The control plane is responsible for VXLAN tunnel establishment and dynamic MAC address learning, whereas the forwarding plane is responsible for intra-subnet known unicast packet forwarding, intra-subnet BUM packet forwarding, and inter-subnet packet forwarding.

Static VXLAN tunnel establishment involves a significant workload and is inflexible. As such, it is not suitable for large networks. VXLAN tunnel establishment using BGP EVPN (centralized VXLAN gateway) is therefore recommended.

The following uses IPv4 over IPv4 as an example. For implementation differences between IPv6 over IPv4 and IPv4 over IPv4, see [Table 1](#EN-US_CONCEPT_0000001130784302__table_01).

**Table 1** Implementation differences
| Combination Category | Implementation Difference |
| --- | --- |
| IPv6 over IPv4 | * During dynamic MAC address learning, a Layer 2 gateway learns a host's MAC address from the neighbor solicitation (NS) messages sent by the host. * In an inter-subnet interworking scenario, an IPv6 address must be configured for the Layer 3 gateway's VBDIF interface. During inter-subnet packet forwarding, the Layer 3 gateway searches its IPv6 routing table for the next hop address of the destination IPv6 address. It then queries the ND table based on the next-hop address to obtain information such as the destination MAC address. |



#### VXLAN Tunnel Establishment

A VXLAN tunnel is identified by a pair of VTEP IP addresses and can be established if its VTEPs are reachable at Layer 3. A static VXLAN tunnel can be created by manually specifying local and remote VNIs, VTEP IP addresses, and an ingress replication list.

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001130784302__fig_dc_vrp_feature_vxlan_103601), Leaf1 connects to Host1 and Host3, Leaf2 connects to Host2, and Spine functions as a Layer 3 gateway.

* To allow Host3 and Host2 to communicate, L2VNIs and an ingress replication list must be configured on Leaf1 and Leaf2. The peer VTEP IP addresses must be specified in the ingress replication list. A VXLAN tunnel can be established between Leaf1 and Leaf2 if their VTEPs have reachable Layer 3 routes to one another.
* To allow Host1 and Host2 to communicate, L2VNIs and an ingress replication list must be configured on Leaf1, Leaf2, and Spine. The peer VTEP IP addresses must be specified in the ingress replication list. A VXLAN tunnel can be established between Leaf1 and Spine if their VTEPs have reachable Layer 3 routes to one another. Similarly, a VXLAN tunnel can be established between Leaf2 and Spine if their VTEPs have reachable Layer 3 routes to one another.
  
  ![](../public_sys-resources/note_3.0-en-us.png) 
  
  Although Host1 and Host3 both connect to Leaf1, they belong to different subnets. To allow Host1 and Host3 to communicate, a Layer 3 gateway needs to be deployed (on Spine). As such, a VXLAN tunnel is also required between Leaf1 and Spine.

**Figure 1** VXLAN tunnel establishment  
![](figure/en-us_image_0000001176664085.png)

#### Dynamic MAC Address Learning

VXLAN supports dynamic MAC address learning to facilitate communication between end tenants. With this function enabled, MAC address entries are dynamically created and do not require manual maintenance, greatly reducing the maintenance workload. The following example illustrates dynamic MAC address learning for intra-subnet communication of hosts on the network shown in [Figure 2](#EN-US_CONCEPT_0000001130784302__fig_dc_vrp_feature_vxlan_103602).

**Figure 2** Dynamic MAC address learning  
![](figure/en-us_image_0000001176743993.png)

1. Host3 sends an ARP request for Host2's MAC address. In the ARP request, the source MAC address is MAC3, the destination MAC address is all Fs, the source IP address is IP3, and the destination IP address is IP2.
2. Upon receipt of the ARP request, Leaf1 determines that the Layer 2 sub-interface receiving the ARP request belongs to a BD that has been bound to a VNI (20). This indicates that the ARP request packet needs to be transmitted over the VXLAN tunnel identified by VNI 20. Leaf1 then learns the mapping between Host3's MAC address, BDID (Layer 2 BD ID), and inbound interface (Port1 for the Layer 2 sub-interface) that has received the ARP request. Leaf1 generates a MAC address entry for Host3, with an outbound interface of Port1.
3. Leaf1 performs VXLAN encapsulation on the ARP request. In this case, the VNI is that bound to the BD, the source IP address in the outer IP header is Leaf1's VTEP IP address, the destination IP address in the outer IP header is Leaf2's VTEP IP address, the source MAC address in the outer Ethernet header is Leaf1's NVE1 MAC address, and the destination MAC address in the outer Ethernet header is the MAC address of the next hop to the destination IP address. [Figure 3](#EN-US_CONCEPT_0000001130784302__fig_dc_vrp_feature_vxlan_103603) shows the VXLAN packet format. The VXLAN packet is then transmitted over the IP network based on the IP and MAC addresses in the outer headers before finally reaching Leaf2.
   
   **Figure 3** VXLAN packet format  
   ![](figure/en-us_image_0000001176664083.png)
4. After receiving the VXLAN packet, Leaf2 decapsulates it and obtains the ARP request sent by Host3. Leaf2 learns the mapping between Host3's MAC address and BDID and Leaf1's VTEP IP address before generating a MAC address entry for Host3. Based on the next hop (Leaf1's VTEP IP address), the MAC address entry's outbound interface recurses to the VXLAN tunnel destined for Leaf1.
5. Leaf2 broadcasts the ARP request in the Layer 2 BD. Upon receipt of the ARP request, Host2 checks whether the destination IP address is a local IP address. If so, Host2 saves Host3's MAC address to the local MAC address table, and then responds with an ARP reply.

Because it has learned Host3's MAC address, Host2 unicasts the ARP reply, and subsequent ARP reply packets are transmitted in the same manner. After Host2 and Host3 learn each other's MAC addresses, subsequent communication occurs in unicast mode.

![](../public_sys-resources/note_3.0-en-us.png) 

Dynamic MAC address learning is required only between hosts and Layer 3 gateways in inter-subnet communication scenarios. The process is similar to that for intra-subnet communication.



#### Intra-Subnet Known Unicast Packet Forwarding

Intra-subnet known unicast packets are forwarded between Layer 2 VXLAN gateways only, without being processed by Layer 3 VXLAN gateways. [Figure 4](#EN-US_CONCEPT_0000001130784302__fig_dc_vrp_feature_vxlan_103306) shows the intra-subnet known unicast packet forwarding process.

**Figure 4** Intra-subnet known unicast packet forwarding  
![](figure/en-us_image_0000001130624542.png)

1. After receiving a packet from Host3, Leaf1 determines the Layer 2 BD of the packet based on the access interface and VLAN information, searches the MAC address table for the outbound interface in the Layer 2 BD, and searches the VXLAN tunnel table for encapsulation information.
2. Leaf1's VTEP then performs VXLAN encapsulation based on the encapsulation information and forwards the packet through the outbound interface.
3. After receiving the VXLAN packet, Leaf2's VTEP checks the UDP destination port number, source and destination IP addresses, and VNI of the packet to determine the packet validity. The VTEP then obtains the Layer 2 broadcast domain based on the VNI and performs VXLAN decapsulation to obtain the inner Layer 2 packet.
4. Leaf2 obtains the destination MAC address of the inner Layer 2 packet, adds a VLAN tag to the packet based on the outbound interface and encapsulation information in the local MAC address table, and forwards the packet to Host2.

Host2 sends packets to Host3 through a similar process.


#### Intra-Subnet BUM Packet Forwarding

Intra-subnet BUM packets are forwarded between Layer 2 VXLAN gateways only, and are invisible to Layer 3 VXLAN gateways. Such packets can be forwarded in ingress replication, multicast replication, or centralized replication mode.

**Ingress Replication**

In ingress replication mode, after a BUM packet enters a VXLAN tunnel, the ingress VTEP performs VXLAN encapsulation based on the ingress replication list and forwards the packet to all egress VTEPs in the list. When the BUM packet leaves the VXLAN tunnel, it is decapsulated by the egress VTEPs. [Figure 5](#EN-US_CONCEPT_0000001130784302__fig_dc_vrp_feature_vxlan_103307) shows the forwarding process of a BUM packet in ingress replication mode.**Figure 5** Intra-subnet forwarding process of a BUM packet in ingress replication mode  
![](figure/en-us_image_0000001130784336.png)

1. After receiving a packet from TerminalA, Leaf1 determines the Layer 2 BD of the packet based on the access interface and VLAN information in the packet.
2. Leaf1's VTEP obtains the ingress replication list for the VNI, replicates the packet based on the list, and performs VXLAN encapsulation. The VTEP then forwards the VXLAN packet through the outbound interface.
3. After receiving the VXLAN packet, Leaf2/Leaf3's VTEP checks the UDP destination port number, source and destination IP addresses, and VNI of the packet to determine the packet validity. The VTEP then obtains the Layer 2 broadcast domain based on the VNI and performs VXLAN decapsulation to obtain the inner Layer 2 packet.
4. Leaf2/Leaf3 checks the destination MAC address of the inner Layer 2 packet and determines it is a BUM MAC address. In this case, Leaf2/Leaf3 broadcasts the packet to the network connected to the terminals (not the VXLAN tunnel side) in the Layer 2 broadcast domain. Specifically, Leaf2/Leaf3 finds the outbound interfaces and encapsulation information not related to the VXLAN tunnel, adds VLAN tags to the packet, and forwards the packet to TerminalB/TerminalC.

![](../public_sys-resources/note_3.0-en-us.png) 

TerminalB/TerminalC responds to TerminalA through the same process as that used in [intra-subnet known unicast packet forwarding](#EN-US_CONCEPT_0000001130784302__section_01).


**Centralized Replication**

In ingress replication mode, when a BUM packet enters a VXLAN tunnel, the ingress VTEP must send a copy of the packet to each remote VTEP, flooding traffic on the network. Configuring centralized replication can resolve this issue. In centralized replication mode, the centralized replication function is configured on the ingress VTEP, and the flood proxy IP address is configured on the centralized replicator. When a BUM packet enters a VXLAN tunnel, the ingress VTEP only needs to send one copy of the packet to the centralized replicator, reducing flooded traffic on the network. The centralized replicator, also known as the flood gateway, decapsulates and encapsulates the BUM packet and sends it to each egress VTEP. When the BUM packet leaves the VXLAN tunnel, it is decapsulated by the egress VTEPs. [Figure 6](#EN-US_CONCEPT_0000001130784302__fig_dc_dc_feature_vxlan_103910) shows the forwarding process of a BUM packet in centralized replication mode.![](../public_sys-resources/note_3.0-en-us.png) 

Centralized replication takes precedence over ingress replication. If both replication modes are configured (using the [**vni flood-vtep**](cmdqueryname=vni+flood-vtep) and [**vni head-end peer-list**](cmdqueryname=vni+head-end+peer-list) commands) on a device, a VXLAN tunnel works in centralized replication mode.


**Figure 6** Forwarding process of an intra-subnet BUM packet in centralized replication mode  
![](figure/en-us_image_0000001176743987.png "Click to enlarge")

1. After receiving a packet from TerminalA, Leaf1 determines the Layer 2 BD of the packet based on the access interface and VLAN information in the packet.
2. Leaf1's VTEP obtains the centralized replication tunnel for the VNI based on the Layer 2 BD and performs VXLAN encapsulation. The VTEP then forwards the VXLAN packet through the outbound interface.
3. After receiving the VXLAN packet, Leaf4 (centralized replicator) checks the UDP destination port number, source and destination IP addresses, and VNI of the packet to determine the packet validity. If the packet is valid, Leaf4 obtains the Layer 2 BD based on the VNI, decapsulates the VXLAN packet to obtain the inner Layer 2 packet, and performs VXLAN encapsulation based on the matching ingress replication list. It then forwards the encapsulated packet with the source IP address being Leaf1's VTEP address. Inter-VTEP MAC address learning is not affected.
4. After receiving the VXLAN packet, Leaf2/Leaf3's VTEP checks the UDP destination port number, source and destination IP addresses, and VNI of the packet to determine the packet validity. The VTEP then obtains the Layer 2 BD based on the VNI and performs VXLAN decapsulation to obtain the inner Layer 2 packet.
5. Leaf2/Leaf3 checks the destination MAC address of the inner Layer 2 packet and determines it is a BUM MAC address. In this case, Leaf2/Leaf3 broadcasts the packet to the network connected to the terminals (not the VXLAN tunnel side) in the Layer 2 BD. Specifically, Leaf2/Leaf3 finds the outbound interfaces and encapsulation information not related to the VXLAN tunnel, adds VLAN tags to the packet, and forwards the packet to TerminalB/TerminalC.

![](../public_sys-resources/note_3.0-en-us.png) 

TerminalB/TerminalC responds to TerminalA through the same process as that used in [intra-subnet known unicast packet forwarding](#EN-US_CONCEPT_0000001130784302__section_01).


**Multicast Replication**

To reduce flooded traffic caused by the use of ingress replication to send BUM packets, you can also configure multicast replication. In multicast replication mode, all VTEPs with the same VNI join the same multicast group. A multicast routing protocol, such as PIM, is used to create a multicast forwarding entry for the multicast group. When the source VTEP receives a BUM packet, it adds a multicast destination IP address, such as 225.0.0.1, to the BUM packet before sending the packet to the remote VTEPs based on the created multicast forwarding entry, reducing flooded packets. The remote VTEPs decapsulate the VXLAN packet. [Figure 7](#EN-US_CONCEPT_0000001130784302__fig_dc_dc_feature_vxlan_103911) shows the forwarding process of a BUM packet in multicast replication mode.**Figure 7** Forwarding process of an intra-subnet BUM packet in multicast replication mode  
![](figure/en-us_image_0000001173075198.png)

1. After receiving a packet from TerminalA, Leaf1 determines the Layer 2 BD of the packet based on the access interface and VLAN information in the packet.
2. Leaf1's VTEP obtains the multicast replication address for the VNI based on the Layer 2 BD and performs VXLAN encapsulation. The encapsulated VXLAN packet is presented as a multicast packet. The VTEP forwards it to Leaf4 based on the matching multicast forwarding entry.
3. After receiving the multicast packet, Leaf4 directly forwards the packet to Leaf2 and Leaf3 based on the matching multicast forwarding entry.![](../public_sys-resources/note_3.0-en-us.png) 
   
   Leaf4 functions as a non-gateway node and forwards only multicast packets. Leaf4 can also be configured as a gateway node. In this case, Leaf4 needs to forward multicast packets, decapsulate VXLAN packets, and broadcast BUM packets on the VLAN network and is called a BUD node.
4. After receiving the multicast packet, Leaf2/Leaf3 determines that the packet is a VXLAN packet based on the outbound interface (NVE interface) in a matching multicast forwarding entry. Leaf2/Leaf3's VTEP checks the UDP destination port number, source and destination IP addresses, and VNI of the packet to determine the packet validity. The VTEP then obtains the Layer 2 BD based on the VNI and performs VXLAN decapsulation to obtain the inner Layer 2 packet.
5. Leaf2/Leaf3 checks the destination MAC address of the inner Layer 2 packet and determines it is a BUM MAC address. In this case, Leaf2/Leaf3 broadcasts the packet to the network connected to the terminals (not the VXLAN tunnel side) in the Layer 2 BD. Specifically, Leaf2/Leaf3 finds the outbound interfaces and encapsulation information not related to the VXLAN tunnel, adds VLAN tags to the packet, and forwards the packet to TerminalB/TerminalC.

![](../public_sys-resources/note_3.0-en-us.png) 

* After multicast or centralized replication is configured, the ingress replication list is used to generate the remote VTEP address list for VXLAN tunnel establishment. Then the multicast replication or centralized replication mode, not the ingress replication mode, applies to BUM packets.
* TerminalB/TerminalC responds to TerminalA through the same process as that used in [intra-subnet known unicast packet forwarding](#EN-US_CONCEPT_0000001130784302__section_01).



#### Inter-Subnet Packet Forwarding

Inter-subnet packet forwarding requires Layer 3 gateways. [Figure 8](#EN-US_CONCEPT_0000001130784302__fig_dc_vrp_feature_vxlan_103308) shows inter-subnet packet forwarding in centralized VXLAN gateway scenarios.

**Figure 8** Inter-subnet packet forwarding  
![](figure/en-us_image_0000001176664091.png)

1. After receiving a packet from Host1, Leaf1 determines the Layer 2 BD of the packet based on the access interface and VLAN information, and searches for the outbound interface and encapsulation information in the BD.
2. Leaf1's VTEP performs VXLAN encapsulation based on the outbound interface and encapsulation information, and forwards the packets to Spine.
3. After receiving the VXLAN packet, Spine decapsulates it and finds that the destination MAC address of the inner packet is the MAC address (MAC3) of the Layer 3 gateway interface (VBDIF10). As such, the packet must be forwarded at Layer 3.
4. Spine removes the inner Ethernet header, parses the destination IP address, and searches the routing table for a next hop address. Spine then searches the ARP table based on the next hop address to obtain the destination MAC address, VXLAN tunnel's outbound interface, and VNI.
5. Spine performs VXLAN encapsulation on the inner packet again and forwards the VXLAN packet to Leaf2, with the source MAC address in the inner Ethernet header being the MAC address (MAC4) of the Layer 3 gateway interface (VBDIF20).
6. After receiving the VXLAN packet, Leaf2's VTEP checks the UDP destination port number, source and destination IP addresses, and VNI of the packet to determine the packet validity. Leaf2 determines the Layer 2 BD based on the VNI, removes the VXLAN header, and obtains the inner Layer 2 packet. It then searches for the outbound interface and encapsulation information in the Layer 2 BD.
7. Leaf2 adds a VLAN tag to the packet based on the outbound interface and encapsulation information and forwards the packet to Host2.

Host2 sends packets to Host1 through a similar process.

![](../public_sys-resources/note_3.0-en-us.png) 

If only hosts on the same subnet need to communicate with each other, Layer 3 VXLAN gateways do not need to be deployed. However, if hosts on different subnets need to communicate with each other or hosts on the same subnet need to communicate with external networks, Layer 3 VXLAN gateways must be deployed.