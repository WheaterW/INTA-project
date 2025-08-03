Understanding VXLAN Tunnel Establishment in BGP EVPN Mode (Centralized VXLAN Gateway)
=====================================================================================

In a BGP EVPN-based VXLAN tunnel establishment scenario where VXLAN gateways are deployed in centralized mode, the control and forwarding planes have different responsibilities. The control plane is responsible for VXLAN tunnel establishment and dynamic MAC address learning, whereas the forwarding plane is responsible for intra-subnet known unicast packet forwarding, intra-subnet BUM packet forwarding, and inter-subnet packet forwarding. Because EVPN enables automatic VTEP discovery and dynamic VXLAN tunnel establishment, this deployment mode is flexible and suitable for large networks. If VXLAN gateways are deployed in centralized mode, BGP EVPN-based VXLAN tunnel establishment is recommended.

The following uses IPv4 over IPv4 as an example to describe the implementation differences between IPv6 over IPv4 and IPv4 over IPv4. [Table 1](#EN-US_CONCEPT_0000001130784318__table_01) describes the implementation differences between the underlay and overlay networks.

**Table 1** Implementation differences
| Combination Category | Implementation Difference |
| --- | --- |
| IPv6 over IPv4 | * During dynamic MAC address learning, a Layer 2 gateway learns a local host's MAC address through neighbor discovery. Hosts at both ends of a tunnel learn each other's MAC address by exchanging NS or NA messages. * In an inter-subnet interworking scenario, an IPv6 address must be configured for the Layer 3 gateway's VBDIF interface. During inter-subnet packet forwarding, the Layer 3 gateway searches its IPv6 routing table for the next hop address of the destination IPv6 address. It then queries the ND table based on the next-hop address to obtain information such as the destination MAC address. |



#### VXLAN Tunnel Establishment

A VXLAN tunnel is identified by a pair of VTEP IP addresses. During VXLAN tunnel establishment, the local and remote VTEPs attempt to obtain each other's IP addresses, and a VXLAN tunnel can be established if the VTEP IP addresses are reachable at Layer 3. When BGP EVPN is used to dynamically establish a VXLAN tunnel, the local and remote VTEPs first establish a BGP EVPN peer relationship and then exchange BGP EVPN routes to transmit VNIs and VTEPs' IP addresses.

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001130784318__fig_dc_vrp_feature_vxlan_103701), Leaf1 connects to Host1 and Host3, Leaf2 connects to Host2, and Spine functions as a Layer 3 gateway. To allow Host3 and Host2 to communicate, establish a VXLAN tunnel between Leaf1 and Leaf2. To allow Host1 and Host2 to communicate, establish a VXLAN tunnel between Leaf1 and Spine and between Spine and Leaf2. Although Host1 and Host3 both connect to Leaf1, they belong to different subnets. To allow Host1 and Host3 to communicate, a Layer 3 gateway needs to be deployed (on Spine). As such, a VXLAN tunnel is also required between Leaf1 and Spine.

**Figure 1** VXLAN tunnel establishment  
![](figure/en-us_image_0000001130624602.png)

The following example illustrates how to use BGP EVPN to dynamically establish a VXLAN tunnel between Leaf1 and Leaf2 on the network shown in [Figure 2](#EN-US_CONCEPT_0000001130784318__fig_dc_vrp_feature_vxlan_103702).

**Figure 2** Dynamic VXLAN tunnel establishment  
![](figure/en-us_image_0000001130624610.png)

1. Configure Leaf1 and Leaf2 to establish a BGP EVPN peer relationship, configure Layer 2 BDs on Leaf1 and Leaf2, and associate VNIs with these BDs. Then create EVPN instances in the Layer 2 BDs, and configure RDs, ERTs, and IRTs for the EVPN instances. After the local VTEP IP address is configured on Leaf1 and Leaf2, they generate a BGP EVPN route and send it to each other. This BGP EVPN route carries the local EVPN instance's ERT and an inclusive multicast route (Type 3 route defined in BGP EVPN). [Figure 3](#EN-US_CONCEPT_0000001130784318__fig_dc_vrp_feature_vxlan_103303) shows the format of an inclusive multicast route, which is comprised of a prefix and a PMSI attribute. VTEP IP addresses are stored in the Originating Router's IP Address field in the inclusive multicast route prefix, and VNIs are stored in the MPLS Label field in the PMSI attribute.
   
   **Figure 3** Format of an inclusive multicast route  
   ![](figure/en-us_image_0000001176744041.png)
2. After receiving the BGP EVPN route from each other, Leaf1 and Leaf2 match the ERT of the route against the IRT of the local EVPN instance. If a match is found, the route is accepted; otherwise, it is discarded. After the route is accepted, Leaf1 and Leaf2 obtain the peer VTEP IP address and VNI carried in the route. If the peer VTEP IP address is reachable, a VXLAN tunnel to the peer end is established. Moreover, the local end creates a VNI-based ingress replication list and adds the peer VTEP IP address to the list for BUM packet forwarding.

The process of dynamically establishing VXLAN tunnels between Leaf1 and Spine and between Leaf2 and Spine using BGP EVPN is similar to that described above.

![](../public_sys-resources/note_3.0-en-us.png) 

A VPN target is a BGP extended community attribute. An EVPN instance can have the IRT and ERT configured. The local EVPN instance's ERT must match the remote EVPN instance's IRT for EVPN route advertisement. Otherwise, VXLAN tunnels cannot be dynamically established. If only one end can successfully accept the BGP EVPN route, this end can establish a VXLAN tunnel to the other end, but cannot exchange data packets with it. The other end drops packets after confirming that there is no VXLAN tunnel to the source end.

In terms of BGP EVPN Type 2 and Type 3 routes, a device that has an all-zero Ethernet Tag ID cannot interoperate with another device that has a non-zero Ethernet Tag ID.



#### Dynamic MAC Address Learning

VXLAN supports dynamic MAC address learning to facilitate communication between end tenants. With this function enabled, MAC address entries are dynamically created and do not require manual maintenance, greatly reducing the maintenance workload. The following example illustrates dynamic MAC address learning for intra-subnet communication of hosts on the network shown in [Figure 4](#EN-US_CONCEPT_0000001130784318__fig_dc_vrp_feature_vxlan_103703).

**Figure 4** Dynamic MAC address learning  
![](figure/en-us_image_0000001176744033.png)

1. Host3 sends dynamic ARP packets when first communicating with Leaf1. Leaf1 learns Host3's MAC address and the mapping between the BDID and packet inbound interface (that is, physical interface Port 1 corresponding to the Layer 2 sub-interface). It then generates a MAC address entry relating to Host3 in the local MAC address table, with the outbound interface being Port 1. Leaf1 also generates a BGP EVPN route based on Host3's ARP entry and sends it to Leaf2. The BGP EVPN route carries the local EVPN instance's ERT, Next\_Hop attribute, and a Type 2 route (MAC/IP route) defined in BGP EVPN. The Next\_Hop attribute carries the local VTEP's IP address, while the MAC Address Length and MAC Address fields identify Host3's MAC address. The L2VNI is stored in the MPLS Label1 field. [Figure 5](#EN-US_CONCEPT_0000001130784318__fig_dc_vrp_feature_vxlan_103305) shows the format of a MAC/IP route.
   
   **Figure 5** MAC/IP route  
   ![](figure/en-us_image_0000001130624606.png)
2. After receiving the BGP EVPN route from Leaf1, Leaf2 matches the ERT of the EVPN instance carried in the route against the IRT of the local EVPN instance. If a match is found, the route is accepted; otherwise, it is discarded. After accepting the route, Leaf2 obtains Host3's MAC address and the mapping between the BDID and the VTEP IP address (Next\_Hop attribute) of Leaf1. It then generates the MAC address entry of Host3 in the local MAC address table. The recursion to the outbound interface must be performed based on the next hop, and the final recursion result is the VXLAN tunnel destined for Leaf1.

Leaf1 learns the MAC route of Host2 through a similar process.

When Host3 communicates with Host2 for the first time, Host3 sends an ARP request for Host2's MAC address. The ARP request carries a destination MAC address containing all Fs and a destination IP address being IP2. By default, Leaf1 broadcasts the ARP request onto the network segment after receiving it. To reduce broadcast packets, ARP broadcast suppression can be enabled on Leaf1. If ARP broadcast suppression is enabled and Leaf1 receives the ARP request, Leaf1 checks whether it has Host2's MAC address based on the destination IP address of the ARP request. If Leaf1 has Host2's MAC address, it replaces the destination MAC address of the ARP request with Host2's MAC address and unicasts the ARP request to Leaf2 through the VXLAN tunnel. Upon receipt, Leaf2 forwards the ARP request to Host2, which then learns Host3's MAC address and responds with an ARP reply in unicast mode. After Host3 receives the ARP reply, it learns Host2's MAC address. At this point, Host3 and Host2 have learned each other's MAC address, and can communicate in unicast mode.

![](../public_sys-resources/note_3.0-en-us.png) 

* Dynamic MAC address learning is required only between hosts and Layer 3 gateways in inter-subnet communication scenarios. The process is similar to that for intra-subnet communication.
* Leaf nodes can learn the MAC addresses of hosts during data forwarding if they are enabled to do so. If VXLAN tunnels are established using BGP EVPN, leaf nodes can dynamically learn the MAC addresses of hosts through BGP EVPN routes, without depending on data forwarding.


#### Intra-Subnet Known Unicast Packet Forwarding

Intra-subnet known unicast packets are forwarded between only Layer 2 VXLAN gateways, without being processed by Layer 3 VXLAN gateways. [Figure 6](#EN-US_CONCEPT_0000001130784318__fig_dc_vrp_feature_vxlan_103306) shows the intra-subnet known unicast packet forwarding process.

**Figure 6** Intra-subnet known unicast packet forwarding  
![](figure/en-us_image_0000001130624594.png)

1. After receiving a packet from Host3, Leaf1 determines the Layer 2 BD of the packet based on the access interface and VLAN information, searches the MAC address table for the outbound interface in the Layer 2 BD, and searches the VXLAN tunnel table for encapsulation information.
2. Leaf1's VTEP then performs VXLAN encapsulation based on the encapsulation information and forwards the packet through the outbound interface.
3. After receiving the VXLAN packet, Leaf2's VTEP checks the UDP destination port number, source and destination IP addresses, and VNI of the packet to determine the packet validity. The VTEP then obtains the Layer 2 BD based on the VNI and performs VXLAN decapsulation to obtain the inner Layer 2 packet.
4. Leaf2 obtains the destination MAC address of the inner Layer 2 packet, adds a VLAN tag to the packet based on the outbound interface and encapsulation information in the local MAC address table, and forwards the packet to Host2.

Host2 sends packets to Host3 through a similar process.


#### Intra-Subnet BUM Packet Forwarding

Intra-subnet BUM packets are forwarded between Layer 2 VXLAN gateways only, and are invisible to Layer 3 VXLAN gateways. Such packets can be forwarded in ingress replication, multicast replication, or centralized replication mode.

**Ingress Replication**

In ingress replication mode, after a BUM packet enters a VXLAN tunnel, the ingress VTEP performs VXLAN encapsulation based on the ingress replication list and forwards the packet to all egress VTEPs in the list. When the BUM packet leaves the VXLAN tunnel, it is decapsulated by the egress VTEPs. [Figure 7](#EN-US_CONCEPT_0000001130784318__fig_dc_vrp_feature_vxlan_103307) shows the forwarding process of a BUM packet in ingress replication mode.**Figure 7** Intra-subnet forwarding process of a BUM packet in ingress replication mode  
![](figure/en-us_image_0000001130624598.png)

1. After receiving a packet from TerminalA, Leaf1 determines the Layer 2 BD of the packet based on the access interface and VLAN information in the packet.
2. Leaf1's VTEP obtains the ingress replication list for the VNI, replicates the packet based on the list, and performs VXLAN encapsulation. The VTEP then forwards the VXLAN packet through the outbound interface.
3. After receiving the VXLAN packet, Leaf2/Leaf3's VTEP checks the UDP destination port number, source and destination IP addresses, and VNI of the packet to determine the packet validity. The VTEP then obtains the Layer 2 BD based on the VNI and performs VXLAN decapsulation to obtain the inner Layer 2 packet.
4. Leaf2/Leaf3 checks the destination MAC address of the inner Layer 2 packet and determines it is a BUM MAC address. In this case, Leaf2/Leaf3 broadcasts the packet to the network connected to the terminals (not the VXLAN tunnel side) in the Layer 2 BD. Specifically, Leaf2/Leaf3 finds the outbound interfaces and encapsulation information not related to the VXLAN tunnel, adds VLAN tags to the packet, and forwards the packet to TerminalB/TerminalC.

![](../public_sys-resources/note_3.0-en-us.png) 

TerminalB/TerminalC responds to TerminalA through the same process as that used in [intra-subnet known unicast packet forwarding](#EN-US_CONCEPT_0000001130784318__section_01).


**Centralized Replication**

In ingress replication mode, when a BUM packet enters a VXLAN tunnel, the ingress VTEP must send a copy of the packet to each remote VTEP, flooding traffic on the network. Configuring centralized replication can resolve this issue. In centralized replication mode, the centralized replication function is configured on the ingress VTEP, and the flood proxy IP address is configured on the centralized replicator. When a BUM packet enters a VXLAN tunnel, the ingress VTEP only needs to send one copy of the packet to the centralized replicator, reducing flooded traffic on the network. The centralized replicator, also known as the flood gateway, decapsulates and encapsulates the BUM packet and sends it to each egress VTEP. When the BUM packet leaves the VXLAN tunnel, it is decapsulated by the egress VTEPs. [Figure 8](#EN-US_CONCEPT_0000001130784318__fig_dc_dc_feature_vxlan_103910) shows the forwarding process of a BUM packet in centralized replication mode.![](../public_sys-resources/note_3.0-en-us.png) 

Centralized replication takes precedence over ingress replication. If both replication modes are configured (using the [**vni flood-vtep**](cmdqueryname=vni+flood-vtep) and [**vni head-end peer-list**](cmdqueryname=vni+head-end+peer-list) commands) on a device, a VXLAN tunnel works in centralized replication mode.


**Figure 8** Forwarding process of an intra-subnet BUM packet in centralized replication mode  
![](figure/en-us_image_0000001176664159.png "Click to enlarge")

1. After receiving a packet from TerminalA, Leaf1 determines the Layer 2 BD of the packet based on the access interface and VLAN information in the packet.
2. Leaf1's VTEP obtains the centralized replication tunnel for the VNI based on the Layer 2 BD and performs VXLAN encapsulation. The VTEP then forwards the VXLAN packet through the outbound interface.
3. After receiving the VXLAN packet, Leaf4 (centralized replicator) checks the UDP destination port number, source and destination IP addresses, and VNI of the packet to determine the packet validity. If the packet is valid, Leaf4 obtains the Layer 2 BD based on the VNI, decapsulates the VXLAN packet to obtain the inner Layer 2 packet, and performs VXLAN encapsulation based on the matching ingress replication list. It then forwards the encapsulated packet with the source IP address being Leaf1's VTEP address. Inter-VTEP MAC address learning is not affected.
4. After receiving the VXLAN packet, Leaf2/Leaf3's VTEP checks the UDP destination port number, source and destination IP addresses, and VNI of the packet to determine the packet validity. The VTEP then obtains the Layer 2 BD based on the VNI and performs VXLAN decapsulation to obtain the inner Layer 2 packet.
5. Leaf2/Leaf3 checks the destination MAC address of the inner Layer 2 packet and determines it is a BUM MAC address. In this case, Leaf2/Leaf3 broadcasts the packet to the network connected to the terminals (not the VXLAN tunnel side) in the Layer 2 BD. Specifically, Leaf2/Leaf3 finds the outbound interfaces and encapsulation information not related to the VXLAN tunnel, adds VLAN tags to the packet, and forwards the packet to TerminalB/TerminalC.

![](../public_sys-resources/note_3.0-en-us.png) 

TerminalB/TerminalC responds to TerminalA through the same process as that used in [intra-subnet known unicast packet forwarding](#EN-US_CONCEPT_0000001130784318__section_01).


**Multicast Replication**

To reduce flooded traffic caused by the use of ingress replication to send BUM packets, you can also configure multicast replication. In multicast replication mode, all VTEPs with the same VNI join the same multicast group. A multicast routing protocol, such as PIM, is used to create a multicast forwarding entry for the multicast group. When the source VTEP receives a BUM packet, it adds a multicast destination IP address, such as 225.0.0.1, to the BUM packet before sending the packet to the remote VTEPs based on the created multicast forwarding entry, reducing flooded packets. The remote VTEPs decapsulate the VXLAN packet. [Figure 9](#EN-US_CONCEPT_0000001130784318__fig_dc_dc_feature_vxlan_103911) shows the forwarding process of a BUM packet in multicast replication mode.**Figure 9** Forwarding process of an intra-subnet BUM packet in multicast replication mode  
![](figure/en-us_image_0000001173075196.png)

1. After receiving a packet from TerminalA, Leaf1 determines the Layer 2 BD of the packet based on the access interface and VLAN information in the packet.
2. Leaf1's VTEP obtains the multicast replication address for the VNI based on the Layer 2 BD and performs VXLAN encapsulation. The encapsulated VXLAN packet is presented as a multicast packet. The VTEP forwards it to Leaf4 based on the matching multicast forwarding entry.
3. After receiving the multicast packet, Leaf4 directly forwards the packet to Leaf2 and Leaf3 based on the matching multicast forwarding entry.![](../public_sys-resources/note_3.0-en-us.png) 
   
   Leaf4 functions as a non-gateway node and forwards only multicast packets. Leaf4 can also be configured as a gateway node. In this case, Leaf4 needs to forward multicast packets, decapsulate VXLAN packets, and broadcast BUM packets on the VLAN network and is called a BUD node.
4. After receiving the multicast packet, Leaf2/Leaf3 determines that the packet is a VXLAN packet based on the outbound interface (NVE interface) in a matching multicast forwarding entry. It checks the UDP destination port number, source and destination IP addresses, and VNI of the packet to determine the packet validity. The VTEP then obtains the Layer 2 BD based on the VNI and performs VXLAN decapsulation to obtain the inner Layer 2 packet.
5. Leaf2/Leaf3 checks the destination MAC address of the inner Layer 2 packet and determines it is a BUM MAC address. In this case, Leaf2/Leaf3 broadcasts the packet to the network connected to the terminals (not the VXLAN tunnel side) in the Layer 2 BD. Specifically, Leaf2/Leaf3 finds the outbound interfaces and encapsulation information not related to the VXLAN tunnel, adds VLAN tags to the packet, and forwards the packet to TerminalB/TerminalC.

![](../public_sys-resources/note_3.0-en-us.png) 

* After multicast or centralized replication is configured, the ingress replication list is used to generate the remote VTEP address list for VXLAN tunnel establishment. Then the multicast replication or centralized replication mode, not the ingress replication mode, applies to BUM packets.
* TerminalB/TerminalC responds to TerminalA through the same process as that used in [intra-subnet known unicast packet forwarding](#EN-US_CONCEPT_0000001130784318__section_01).



#### Inter-Subnet Packet Forwarding

Inter-subnet packet forwarding requires Layer 3 gateways. [Figure 10](#EN-US_CONCEPT_0000001130784318__fig_dc_vrp_feature_vxlan_103308) shows inter-subnet packet forwarding in centralized VXLAN gateway scenarios.

**Figure 10** Inter-subnet packet forwarding  
![](figure/en-us_image_0000001130784378.png)

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