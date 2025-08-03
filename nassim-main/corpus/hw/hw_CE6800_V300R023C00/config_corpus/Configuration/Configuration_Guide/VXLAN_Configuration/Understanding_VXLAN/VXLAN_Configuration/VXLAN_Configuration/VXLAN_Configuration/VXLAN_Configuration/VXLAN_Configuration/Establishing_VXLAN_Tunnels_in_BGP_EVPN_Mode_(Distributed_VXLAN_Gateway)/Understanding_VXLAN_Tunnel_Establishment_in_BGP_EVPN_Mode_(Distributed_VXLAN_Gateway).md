Understanding VXLAN Tunnel Establishment in BGP EVPN Mode (Distributed VXLAN Gateway)
=====================================================================================

In a BGP EVPN-based VXLAN tunnel establishment scenario where VXLAN gateways are deployed in distributed mode, the control plane is responsible for VXLAN tunnel establishment and dynamic MAC address learning, while the forwarding plane is responsible for intra-subnet known unicast packet forwarding, intra-subnet BUM packet forwarding, and inter-subnet packet forwarding. BGP EVPN provides various functions, including host IP route advertisement, host MAC address advertisement, and host ARP notification ([EVPN VXLAN Fundamentals](dc_vrp_feature_vxlan_1034.html)). ARP broadcast suppression can be enabled directly. If VXLAN gateways are deployed in distributed VXLAN mode, BGP EVPN-based VXLAN tunnel establishment is recommended.

The following uses IPv4 over IPv4 as an example. For implementation differences between IPv6 over IPv4 and IPv4 over IPv4, see [Table 1](#EN-US_CONCEPT_0000001176664071__table_01).

**Table 1** Implementation differences
| Combination Category | Implementation Difference |
| --- | --- |
| IPv6 over IPv4 | * When a VXLAN tunnel is established using BGP EVPN in inter-subnet interworking scenarios, if IRBv6 routes are used to advertise host IPv6 routes, NS multicast suppression can be directly configured on gateways and IPv6 VMs can be migrated. During VXLAN tunnel establishment, IRBv6 routes are used to flood ND entries between gateways. * During dynamic MAC address learning, a Layer 2 gateway learns a local host's MAC address through neighbor discovery. Hosts at both ends of a tunnel learn each other's MAC address by exchanging NS or NA messages. * During inter-subnet packet forwarding, a gateway must search the IPv6 routing table in the local L3VPN instance. |



#### VXLAN Tunnel Establishment

A VXLAN tunnel is identified by a pair of VTEP IP addresses. During VXLAN tunnel establishment, the local and remote VTEPs attempt to obtain each other's IP addresses, and a VXLAN tunnel can be established if the VTEP IP addresses are reachable at Layer 3. When BGP EVPN is used to dynamically establish a VXLAN tunnel, the local and remote VTEPs first establish a BGP EVPN peer relationship and then exchange BGP EVPN routes to transmit VNIs and VTEPs' IP addresses.

In distributed VXLAN gateway scenarios, leaf nodes function as both Layer 2 and Layer 3 VXLAN gateways. Spine nodes are unaware of the VXLAN tunnels and only forward VXLAN packets between different leaf nodes. On the control plane, a VXLAN tunnel only needs to be established between leaf nodes. On the network shown in [Figure 1](#EN-US_CONCEPT_0000001176664071__fig_dc_vrp_feature_vxlan_103901), a VXLAN tunnel is established between Leaf1 and Leaf2 in order for Host1 and Host2 or Host3 and Host2 to communicate. Because Host1 and Host3 both connect to Leaf1, they can directly communicate through Leaf1 instead of over a VXLAN tunnel.

**Figure 1** VXLAN tunnel establishment  
![](figure/en-us_image_0000001176664149.png)

In distributed gateway scenarios, BGP EVPN can be used to dynamically establish VXLAN tunnels in either of the following situations:

**Intra-Subnet Communication**

On the network shown in [Figure 2](#EN-US_CONCEPT_0000001176664071__fig_dc_vrp_feature_vxlan_103902), intra-subnet communication between Host2 and Host3 requires only Layer 2 forwarding. The process for establishing a VXLAN tunnel using BGP EVPN is as follows.

**Figure 2** Dynamic VXLAN tunnel establishment (1)  
![](figure/en-us_image_0000001130624592.png)

1. Configure Leaf1 and Leaf2 to establish a BGP EVPN peer relationship, configure Layer 2 BDs on Leaf1 and Leaf2, and then associate L2VNIs with the Layer 2 BDs. Create EVPN instances in the Layer 2 BDs, and configure RDs, export VPN targets (ERTs), and import VPN targets (IRTs) for the EVPN instances. After the local VTEP IP address is configured on Leaf1 and Leaf2, they generate a BGP EVPN route and send it to each other. This BGP EVPN route carries the local EVPN instance's ERT and an inclusive multicast route (Type 3 route defined in BGP EVPN). [Figure 3](#EN-US_CONCEPT_0000001176664071__fig_dc_vrp_feature_vxlan_103303) shows the format of an inclusive multicast route, which is comprised of a prefix and a PMSI attribute. VTEP IP addresses are stored in the Originating Router's IP Address field in the inclusive multicast route prefix, and L2VNIs are stored in the MPLS Label field in the PMSI attribute.
   
   **Figure 3** Format of an inclusive multicast route  
   ![](figure/en-us_image_0000001176744077.png)
2. After receiving the BGP EVPN route from each other, Leaf1 and Leaf2 match the ERT of the route against the IRT of the local EVPN instance. If a match is found, the route is accepted; otherwise, it is discarded. After the route is accepted, Leaf1 and Leaf2 obtain the peer VTEP IP address and Layer 2 VNI carried in the route. If the peer VTEP IP address is reachable, a VXLAN tunnel to the peer end is established. Moreover, the local end creates a VNI-based ingress replication list and adds the peer VTEP IP address to the list for BUM packet forwarding.

![](../public_sys-resources/note_3.0-en-us.png) 

A VPN target is a BGP extended community attribute. An EVPN instance can have the IRT and ERT configured. The local EVPN instance's ERT must match the remote EVPN instance's IRT for EVPN route advertisement. Otherwise, VXLAN tunnels cannot be dynamically established. If only one end can successfully accept the BGP EVPN route, this end can establish a VXLAN tunnel to the other end, but cannot exchange data packets with it. The other end drops packets after confirming that there is no VXLAN tunnel to the source end.

In terms of BGP EVPN Type 2 and Type 3 routes, a device that has an all-zero Ethernet Tag ID cannot interoperate with another device that has a non-zero Ethernet Tag ID.

**Inter-Subnet Communication**

Inter-subnet communication between Host1 and Host2 requires Layer 3 forwarding. When VXLAN tunnels are established using BGP EVPN, Leaf1 and Leaf2 must advertise host IP routes. Typically, 32-bit host IP routes are advertised. As different leaf nodes may connect to the same VXLAN segment, the network segment routes advertised by the leaf nodes may conflict, impacting host reachability. Leaf nodes can advertise network segment routes in the following scenarios:

* The network segment that a leaf node connects to is unique on a VXLAN, and a large number of specific host routes are available. In this case, the routes of the network segment to which the host IP routes belong can be advertised so that leaf nodes are not required to store all these routes.
* When hosts on a VXLAN need to access external networks, leaf nodes can advertise routes destined for the external networks onto the VXLAN to allow other leaf nodes to learn the routes.

Before establishing a VXLAN tunnel, perform the configurations listed in the following table on Leaf1 and Leaf2.

| Configuration Task | Purpose |
| --- | --- |
| Create a Layer 2 BD and associate an L2VNI with it. | A BD functions as a VXLAN network entity to transmit VXLAN data packets. |
| Establish a BGP EVPN peer relationship between Leaf1 and Leaf2. | This configuration is used to exchange BGP EVPN routes. |
| Configure an EVPN instance in a Layer 2 BD, and configure an RD, an ERT, and an IRT for the EVPN instance. | This configuration is used to generate BGP EVPN routes. |
| Configure L3VPN instances for tenants and bind the L3VPN instances to the VBDIF interfaces of the Layer 2 BD. | This configuration is used to differentiate and isolate IP routing tables of different tenants. |
| Specify an L3VNI for an L3VPN instance. | This configuration allows the leaf nodes to determine the L3VPN routing table for forwarding data packets. |
| Configure the eERT used by the L3VPN instance to export routes to an EVPN instance as well as the eIRT used by the L3VPN instance to import routes from the EVPN instance. | This configuration controls advertisement and reception of BGP EVPN routes between the local L3VPN instance and the remote EVPN instance. |
| Configure the type of route to be advertised between Leaf1 and Leaf2. | This configuration is used to advertise IP routes between Host1 and Host2. Two types of routes are available, IRB and IP prefix routes, which can be selected as needed.   * IRB routes advertise only 32-bit host IP routes. As IRB routes carry ARP routes, ARP broadcast suppression can be enabled on leaf nodes after IRB routes are advertised, which also facilitates VM migration. For details, see [EVPN VXLAN Fundamentals](dc_vrp_feature_vxlan_1034.html). If only 32-bit host IP route advertisement is required, advertising IRB routes is recommended. * IP prefix routes can advertise both 32-bit host IP routes and network segment routes. However, before IP prefix routes advertise 32-bit host IP routes, direct routes to the host IP addresses must be generated, which affects VM migration. If only 32-bit host IP route advertisement is required, advertising IP prefix routes is not recommended. Instead, advertise IP prefix routes only when network segment route advertisement is required. |

Dynamic VXLAN tunnel establishment varies according to how host IP routes are advertised.

* Host IP routes are advertised through IRB routes, as shown in [Figure 4](#EN-US_CONCEPT_0000001176664071__fig_dc_vrp_feature_vxlan_103903).
  
  **Figure 4** Dynamic VXLAN tunnel establishment (2)  
  ![](figure/en-us_image_0000001130624578.png)
  1. When Host1 communicates with Leaf1 for the first time, Leaf1 learns the ARP entry of Host1 after receiving dynamic ARP packets. Leaf1 then finds the L3VPN instance bound to the VBDIF interface of the Layer 2 BD where Host1 resides, and obtains the L3VNI associated with the L3VPN instance. The EVPN instance of Leaf1 then generates an IRB route based on the information obtained. [Figure 5](#EN-US_CONCEPT_0000001176664071__fig_dc_vrp_feature_vxlan_103904) shows the IRB route. The host IP address is stored in the IP Address Length and IP Address fields, and the L3VNI is stored in the MPLS Label2 field.
     
     **Figure 5** IRB route  
     ![](figure/en-us_image_0000001130624576.png)
  2. Leaf1 sends a BGP EVPN route to Leaf2. This route carries the local EVPN instance's ERT, extended community attribute, Next\_Hop attribute, and the IRB route. The extended community attribute carries the tunnel type (VXLAN tunnel), and the Next\_Hop attribute carries the local VTEP IP address.
  3. After Leaf2 receives the BGP EVPN route from Leaf1, Leaf2 processes the route as follows:
     
     + If the ERT carried in the route is the same as the IRT of the local EVPN instance, the route is accepted. After the EVPN instance obtains IRB routes, it can extract ARP routes from the IRB routes to implement ARP advertisement.
     + If the ERT carried in the route is the same as the eIRT of the local L3VPN instance, the route is accepted. The L3VPN instance then obtains the IRB route carried in the route, extracts the host IP address and L3VNI of Host1, and saves the host IP route of Host1 to the routing table. The outbound interface is obtained through recursion based on the next hop of the route, and the final recursion result is the VXLAN tunnel to Leaf1, as shown in [Figure 6](#EN-US_CONCEPT_0000001176664071__fig_dc_vrp_feature_vxlan_103907).
       
       ![](../public_sys-resources/note_3.0-en-us.png) 
       
       A BGP EVPN route is discarded only when the ERT in the route is different from the local EVPN instance's IRT and the local L3VPN instance's eIRT.
       
       
       **Figure 6** Remote host IP route  
       ![](figure/en-us_image_0000001130624616.png)
     + If the route is accepted by the EVPN instance or L3VPN instance, Leaf2 obtains Leaf1's VTEP IP address from the Next\_Hop attribute. If the VTEP IP address is routable at Layer 3, a VXLAN tunnel to Leaf1 is established.
  
  Leaf1 establishes a VXLAN tunnel to Leaf2 through a similar process.
* Host IP routes are advertised through IP prefix routes, as shown in [Figure 7](#EN-US_CONCEPT_0000001176664071__fig_dc_vrp_feature_vxlan_103911).
  
  **Figure 7** Dynamic VXLAN tunnel establishment (3)  
  ![](figure/en-us_image_0000001176744027.png)
  1. Leaf1 generates a direct route to Host1's IP address. Leaf1 then has an L3VPN instance configured to import the direct route, so that Host1's IP route is saved to the routing table of the L3VPN instance and the L3VNI associated with the L3VPN instance is added. [Figure 8](#EN-US_CONCEPT_0000001176664071__fig_dc_vrp_feature_vxlan_103912) shows the local host IP route.
     
     **Figure 8** Local host IP route  
     ![](figure/en-us_image_0000001176664153.png)
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     If network segment route advertisement is required, use a dynamic routing protocol such as OSPF. Then, configure an L3VPN instance to import the routes of the dynamic routing protocol.
  2. An L3VPN instance is configured on Leaf1 to advertise EVPN IP prefix routes. As shown in [Figure 9](#EN-US_CONCEPT_0000001176664071__fig_dc_vrp_feature_vxlan_103905), host IP address information is stored in the IP Prefix Length and IP Prefix fields, and the L3VNI information is stored in the MPLS Label field. Leaf1 sends a BGP EVPN route to Leaf2. This route carries the local L3VPN instance's eERT, extended community attribute, Next\_Hop attribute, and the IP prefix route. The extended community attribute carries the tunnel type (VXLAN tunnel), and the Next\_Hop attribute carries the local VTEP IP address.
     
     **Figure 9** IP prefix route information  
     ![](figure/en-us_image_0000001130784386.png)
  3. After Leaf2 receives the BGP EVPN route from Leaf1, Leaf2 processes the route as follows:
     
     + The eERT of the route is matched against the eIRT of the local L3VPN instance. If a match is found, the route is accepted. The L3VPN instance obtains the IP prefix route, extracts Host1's IP address and L3VNI, stores Host1's IP route in the routing table, and sets the next hop's recursive outbound interface to the VXLAN tunnel interface. [Figure 10](#EN-US_CONCEPT_0000001176664071__fig_dc_vrp_feature_vxlan_103913) shows the remote host IP route.
       
       **Figure 10** Remote host IP route  
       ![](figure/en-us_image_0000001130624616.png)
     + If the route is accepted by the L3VPN instance, Leaf2 obtains Leaf1's VTEP IP address from the Next\_Hop attribute. If the VTEP IP address is routable at Layer 3, a VXLAN tunnel to Leaf1 is established.
  
  Leaf1 establishes a VXLAN tunnel to Leaf2 through a similar process.

#### Dynamic MAC Address Learning

VXLAN supports dynamic MAC address learning to facilitate communication between end tenants. With this function enabled, MAC address entries are dynamically created and do not require manual maintenance, greatly reducing the maintenance workload. In distributed VXLAN gateway scenarios, inter-subnet communication requires Layer 3 forwarding; MAC address learning is implemented using dynamic ARP packets between the local host and gateway. The following example illustrates dynamic MAC address learning for intra-subnet communication of hosts on the network shown in [Figure 11](#EN-US_CONCEPT_0000001176664071__fig_dc_vrp_feature_vxlan_103703).

**Figure 11** Dynamic MAC Address Learning  
![](figure/en-us_image_0000001176664133.png)

1. Host3 sends dynamic ARP packets when first communicating with Leaf1. Leaf1 learns Host3's MAC address and the mapping between the BDID and packet inbound interface (that is, the physical interface Port 1 corresponding to the Layer 2 sub-interface). It then generates a MAC address entry relating to Host3 in the local MAC address table, with the outbound interface being Port 1. Leaf1 also generates a BGP EVPN route based on Host3's ARP entry and sends it to Leaf2. The BGP EVPN route carries the local EVPN instance's ERT, Next\_Hop attribute, and a Type 2 route (MAC/IP route) defined in BGP EVPN. The Next\_Hop attribute carries the local VTEP's IP address, while the MAC Address Length and MAC Address fields identify Host3's MAC address. The L2VNI is stored in the MPLS Label1 field. [Figure 12](#EN-US_CONCEPT_0000001176664071__fig_dc_vrp_feature_vxlan_103305) shows the format of a MAC/IP route.
   
   **Figure 12** MAC/IP route  
   ![](figure/en-us_image_0000001176664145.png)
2. After receiving the BGP EVPN route from Leaf1, Leaf2 matches the ERT of the EVPN instance carried in the route against the IRT of the local EVPN instance. If a match is found, the route is accepted; otherwise, it is discarded. After accepting the route, Leaf2 obtains Host3's MAC address and the mapping between the BDID and the VTEP IP address (Next\_Hop attribute) of Leaf1. It then generates the MAC address entry of Host3 in the local MAC address table. The recursion to the outbound interface must be performed based on the next hop, and the final recursion result is the VXLAN tunnel destined for Leaf1.

Leaf1 learns the MAC route of Host2 through a similar process.

When Host3 communicates with Host2 for the first time, Host3 sends an ARP request for Host2's MAC address. The ARP request carries a destination MAC address containing all Fs and a destination IP address being IP2. By default, Leaf1 broadcasts the ARP request onto the network segment after receiving it. To reduce broadcast packets, ARP broadcast suppression can be enabled on Leaf1. If ARP broadcast suppression is enabled and Leaf1 receives the ARP request, Leaf1 checks whether it has Host2's MAC address based on the destination IP address of the ARP request. If Leaf1 has Host2's MAC address, it replaces the destination MAC address of the ARP request with Host2's MAC address and unicasts the ARP request to Leaf2 through the VXLAN tunnel. Upon receipt, Leaf2 forwards the ARP request to Host2, which then learns Host3's MAC address and responds with an ARP reply in unicast mode. After Host3 receives the ARP reply, it learns Host2's MAC address. At this point, Host3 and Host2 have learned each other's MAC address, and can communicate in unicast mode.

![](../public_sys-resources/note_3.0-en-us.png) 

Leaf nodes can learn the MAC addresses of hosts during data forwarding if they are enabled to do so. If VXLAN tunnels are established using BGP EVPN, leaf nodes can dynamically learn the MAC addresses of hosts through BGP EVPN routes, without depending on data forwarding.



#### Intra-Subnet Known Unicast Packet Forwarding

Intra-subnet known unicast packets are forwarded between only Layer 2 VXLAN gateways, without being processed by Layer 3 VXLAN gateways. [Figure 13](#EN-US_CONCEPT_0000001176664071__fig_dc_vrp_feature_vxlan_103306) shows the intra-subnet known unicast packet forwarding process.

**Figure 13** Intra-subnet known unicast packet forwarding  
![](figure/en-us_image_0000001176664127.png)

1. After receiving a packet from Host3, Leaf1 determines the Layer 2 BD of the packet based on the access interface and VLAN information, searches the MAC address table for the outbound interface in the Layer 2 BD, and searches the VXLAN tunnel table for encapsulation information.
2. Leaf1's VTEP then performs VXLAN encapsulation based on the encapsulation information and forwards the packet through the outbound interface.
3. After receiving the VXLAN packet, Leaf2's VTEP checks the UDP destination port number, source and destination IP addresses, and VNI of the packet to determine the packet validity. The VTEP then obtains the Layer 2 BD based on the VNI and performs VXLAN decapsulation to obtain the inner Layer 2 packet.
4. Leaf2 obtains the destination MAC address of the inner Layer 2 packet, adds a VLAN tag to the packet based on the outbound interface and encapsulation information in the local MAC address table, and forwards the packet to Host2.

Host2 sends packets to Host3 through a similar process.


#### Intra-Subnet BUM Packet Forwarding

Intra-subnet BUM packets are forwarded between Layer 2 VXLAN gateways only, and are invisible to Layer 3 VXLAN gateways. Such packets can be forwarded in ingress replication, multicast replication, or centralized replication mode.

**Ingress Replication**

In ingress replication mode, after a BUM packet enters a VXLAN tunnel, the ingress VTEP performs VXLAN encapsulation based on the ingress replication list and forwards the packet to all egress VTEPs in the list. When the BUM packet leaves the VXLAN tunnel, it is decapsulated by the egress VTEPs. [Figure 14](#EN-US_CONCEPT_0000001176664071__fig_dc_vrp_feature_vxlan_103307) shows the forwarding process of a BUM packet in ingress replication mode.**Figure 14** Intra-subnet forwarding process of a BUM packet in ingress replication mode  
![](figure/en-us_image_0000001130624612.png)

1. After receiving a packet from TerminalA, Leaf1 determines the Layer 2 BD of the packet based on the access interface and VLAN information in the packet.
2. Leaf1's VTEP obtains the ingress replication list for the VNI, replicates the packet based on the list, and performs VXLAN encapsulation. The VTEP then forwards the VXLAN packet through the outbound interface.
3. After receiving the VXLAN packet, Leaf2/Leaf3's VTEP checks the UDP destination port number, source and destination IP addresses, and VNI of the packet to determine the packet validity. The VTEP then obtains the Layer 2 BD based on the VNI and performs VXLAN decapsulation to obtain the inner Layer 2 packet.
4. Leaf2/Leaf3 checks the destination MAC address of the inner Layer 2 packet and determines it is a BUM MAC address. In this case, Leaf2/Leaf3 broadcasts the packet to the network connected to the terminals (not the VXLAN tunnel side) in the Layer 2 BD. Specifically, Leaf2/Leaf3 finds the outbound interfaces and encapsulation information not related to the VXLAN tunnel, adds VLAN tags to the packet, and forwards the packet to TerminalB/TerminalC.

![](../public_sys-resources/note_3.0-en-us.png) 

TerminalB/TerminalC responds to TerminalA through the same process as that used in [intra-subnet known unicast packet forwarding](#EN-US_CONCEPT_0000001176664071__section_01).


**Centralized Replication**

In ingress replication mode, when a BUM packet enters a VXLAN tunnel, the ingress VTEP must send a copy of the packet to each remote VTEP, flooding traffic on the network. Configuring centralized replication can resolve this issue. In centralized replication mode, the centralized replication function is configured on the ingress VTEP, and the flood proxy IP address is configured on the centralized replicator. When a BUM packet enters a VXLAN tunnel, the ingress VTEP only needs to send one copy of the packet to the centralized replicator, reducing flooded traffic on the network. The centralized replicator, also known as the flood gateway, decapsulates and encapsulates the BUM packet and sends it to each egress VTEP. When the BUM packet leaves the VXLAN tunnel, it is decapsulated by the egress VTEPs. [Figure 15](#EN-US_CONCEPT_0000001176664071__fig_dc_dc_feature_vxlan_103910) shows the forwarding process of a BUM packet in centralized replication mode.![](../public_sys-resources/note_3.0-en-us.png) 

Centralized replication takes precedence over ingress replication. If both replication modes are configured (using the [**vni flood-vtep**](cmdqueryname=vni+flood-vtep) and [**vni head-end peer-list**](cmdqueryname=vni+head-end+peer-list) commands) on a device, a VXLAN tunnel works in centralized replication mode.


**Figure 15** Forwarding process of an intra-subnet BUM packet in centralized replication mode  
![](figure/en-us_image_0000001130624572.png "Click to enlarge")

1. After receiving a packet from TerminalA, Leaf1 determines the Layer 2 BD of the packet based on the access interface and VLAN information in the packet.
2. Leaf1's VTEP obtains the centralized replication tunnel for the VNI based on the Layer 2 BD and performs VXLAN encapsulation. The VTEP then forwards the VXLAN packet through the outbound interface.
3. After receiving the VXLAN packet, Leaf4 (centralized replicator) checks the UDP destination port number, source and destination IP addresses, and VNI of the packet to determine the packet validity. If the packet is valid, Leaf4 obtains the Layer 2 BD based on the VNI, decapsulates the VXLAN packet to obtain the inner Layer 2 packet, and performs VXLAN encapsulation based on the matching ingress replication list. It then forwards the encapsulated packet with the source IP address being Leaf1's VTEP address. Inter-VTEP MAC address learning is not affected.
4. After receiving the VXLAN packet, Leaf2/Leaf3's VTEP checks the UDP destination port number, source and destination IP addresses, and VNI of the packet to determine the packet validity. The VTEP then obtains the Layer 2 BD based on the VNI and performs VXLAN decapsulation to obtain the inner Layer 2 packet.
5. Leaf2/Leaf3 checks the destination MAC address of the inner Layer 2 packet and determines it is a BUM MAC address. In this case, Leaf2/Leaf3 broadcasts the packet to the network connected to the terminals (not the VXLAN tunnel side) in the Layer 2 BD. Specifically, Leaf2/Leaf3 finds the outbound interfaces and encapsulation information not related to the VXLAN tunnel, adds VLAN tags to the packet, and forwards the packet to TerminalB/TerminalC.

![](../public_sys-resources/note_3.0-en-us.png) 

TerminalB/TerminalC responds to TerminalA through the same process as that used in [intra-subnet known unicast packet forwarding](#EN-US_CONCEPT_0000001176664071__section_01).


**Multicast Replication**

To reduce flooded traffic caused by the use of ingress replication to send BUM packets, you can also configure multicast replication. In multicast replication mode, all VTEPs with the same VNI join the same multicast group. A multicast routing protocol, such as PIM, is used to create a multicast forwarding entry for the multicast group. When the source VTEP receives a BUM packet, it adds a multicast destination IP address, such as 225.0.0.1, to the BUM packet before sending the packet to the remote VTEPs based on the created multicast forwarding entry, reducing flooded packets. The remote VTEPs decapsulate the VXLAN packet. [Figure 16](#EN-US_CONCEPT_0000001176664071__fig_dc_dc_feature_vxlan_103911) shows the forwarding process of a BUM packet in multicast replication mode.**Figure 16** Forwarding process of an intra-subnet BUM packet in multicast replication mode  
![](figure/en-us_image_0000001218196483.png)

1. After receiving a packet from TerminalA, Leaf1 determines the Layer 2 BD of the packet based on the access interface and VLAN information in the packet.
2. Leaf1's VTEP obtains the multicast replication address for the VNI based on the Layer 2 BD and performs VXLAN encapsulation. The encapsulated VXLAN packet is presented as a multicast packet. The VTEP forwards it to Leaf4 based on the matching multicast forwarding entry.
3. After receiving the multicast packet, Leaf4 directly forwards the packet to Leaf2 and Leaf3 based on the matching multicast forwarding entry.![](../public_sys-resources/note_3.0-en-us.png) 
   
   Leaf4 functions as a non-gateway node and forwards only multicast packets. Leaf4 can also be configured as a gateway node. In this case, Leaf4 needs to forward multicast packets, decapsulate VXLAN packets, and broadcast BUM packets on the VLAN network and is called a BUD node.
4. After receiving the multicast packet, Leaf2/Leaf3 determines that the packet is a VXLAN packet based on the outbound interface (NVE interface) in a matching multicast forwarding entry. Leaf2/Leaf3's VTEP checks the UDP destination port number, source and destination IP addresses, and VNI of the packet to determine the packet validity. The VTEP then obtains the Layer 2 BD based on the VNI and performs VXLAN decapsulation to obtain the inner Layer 2 packet.
5. Leaf2/Leaf3 checks the destination MAC address of the inner Layer 2 packet and determines it is a BUM MAC address. In this case, Leaf2/Leaf3 broadcasts the packet to the network connected to the terminals (not the VXLAN tunnel side) in the Layer 2 BD. Specifically, Leaf2/Leaf3 finds the outbound interfaces and encapsulation information not related to the VXLAN tunnel, adds VLAN tags to the packet, and forwards the packet to TerminalB/TerminalC.

![](../public_sys-resources/note_3.0-en-us.png) 

* After multicast or centralized replication is configured, the ingress replication list is used to generate the remote VTEP address list for VXLAN tunnel establishment. Then the multicast replication or centralized replication mode, not the ingress replication mode, applies to BUM packets.
* TerminalB/TerminalC responds to TerminalA through the same process as that used in [intra-subnet known unicast packet forwarding](#EN-US_CONCEPT_0000001176664071__section_01).



#### Inter-Subnet Packet Forwarding

Inter-subnet packet forwarding requires Layer 3 gateways. [Figure 17](#EN-US_CONCEPT_0000001176664071__fig_dc_vrp_feature_vxlan_103908) shows inter-subnet packet forwarding in distributed VXLAN gateway scenarios.

**Figure 17** Inter-subnet packet forwarding  
![](figure/en-us_image_0000001176744075.png)

1. After Leaf1 receives a packet from Host1, it finds that the destination MAC address of the packet is a gateway MAC address, and so the packet must be forwarded at Layer 3.
2. Leaf1 first determines the Layer 2 BD of the packet based on the inbound interface and then finds the L3VPN instance to which the VBDIF interface of the Layer 2 BD is bound. Leaf1 searches the routing table of the L3VPN instance for a matching host route based on the destination IP address of the packet, and obtains the L3VNI and next hop address corresponding to the route. [Figure 18](#EN-US_CONCEPT_0000001176664071__fig_dc_vrp_feature_vxlan_103909) shows the host route in the L3VPN routing table. If the outbound interface is a VXLAN tunnel, Leaf1 determines that VXLAN encapsulation is required and then performs the following:
   * Obtains MAC addresses based on the VXLAN tunnel's source and destination IP addresses and replaces the source and destination MAC addresses in the inner Ethernet header.
   * Encapsulates the L3VNI into the packet.
   * Encapsulates the source and destination IP addresses of the VXLAN tunnel into the outer header.**Figure 18** Host route information in the L3VPN routing table  
   ![](figure/en-us_image_0000001130784412.png)
3. The VXLAN packet is then transmitted over the IP network based on the IP and MAC addresses in the outer headers before finally reaching Leaf2.
4. After Leaf2 receives the VXLAN packet, it decapsulates the packet and finds that the destination MAC address is its own MAC address. It then determines that the packet must be forwarded at Layer 3.
5. Leaf2 finds the corresponding L3VPN instance based on the L3VNI carried in the packet, searches the routing table of the L3VPN instance, and finds that the next hop of the packet is the gateway interface address. Leaf2 then forwards the packet to Host2.

Host2 sends packets to Host1 through a similar process.

![](../public_sys-resources/note_3.0-en-us.png) 

To enable hosts on different network segments to communicate with each other or hosts on the same network segment to communicate with external networks, configure VPN instances, deploy Layer 3 VXLAN gateways, and configure the types of routes advertised between VXLAN gateways. If only hosts on the same network segment need to communicate with each other, you do not need to configure the preceding functions.