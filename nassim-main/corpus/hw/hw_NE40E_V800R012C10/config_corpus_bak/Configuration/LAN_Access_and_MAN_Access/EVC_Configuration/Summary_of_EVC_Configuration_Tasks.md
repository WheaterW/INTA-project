Summary of EVC Configuration Tasks
==================================

This section describes EVC features supported by the NE40E.

Ethernet virtual connection (EVC) defines a unified Layer 2 service transport and configuration model. According to MEF, an EVC can be associated with two or more user network interfaces on an Internet service provider (ISP) network. In the EVC model, bridge domains (BDs) are used to isolate user networks.

The EVC configuration roadmap is as follows:

1. Establish an EVC model to forward Layer 2 packets.
2. Configure a BD-based MAC address table to better guide service forwarding.
3. Configure EVC security attributes to securely transmit packets within the BD.

#### Services or Protocols Supported by EVCs

EVC defines a unified Layer 2 service transport and configuration model. The EVC model can carry various services, as shown in [Table 1](#EN-US_CONCEPT_0172363334__tab_5). This simplifies configuration management and enhances O&M efficiency.

**Table 1** Services or protocols supported by EVC
| **Service/Protocol Type** | | **Description** |
| --- | --- | --- |
| IP services | Local Address Resolution Protocol (ARP) proxy | To allow isolated users in a BD to communicate, enable local ARP proxy on the VBDIF interface. |
| Dynamic Host Configuration Protocol (DHCP) server/client | If DHCP clients and a DHCP server reside on different network segments, a DHCP relay agent can be configured based on BDs to forward DHCP messages between the clients and server. In this way, you do not need to deploy a DHCP server on each network segment, reducing costs and facilitating centralized management. |
| VPN services | Virtual private LAN service (VPLS) | To allow users connected over a VPLS network to communicate, establish the EVC model on VPLS network edge devices and bind BDs to virtual switch instances (VSIs) for VPLS access. |
| Layer 3 virtual private network (L3VPN) | To allow users connected over a Border Gateway Protocol (BGP)/Multiprotocol Label Switching (MPLS) IP VPN network to communicate, establish the EVC model on BGP/MPLS IP VPN edge devices and bind VBDIF interfaces to VPN instances for BGP/MPLS IP VPN access. |
| Virtual private wire service (VPWS) | To allow users connected over a VPWS network to communicate, establish the EVC model on VPWS network edge devices and bind Layer 2 sub-interfaces to virtual leased lines (VLLs) for VPWS access. |
| Multicast services | Layer 2 multicast | After IGMP snooping is deployed for a device based on BDs, the device learns whether there are multicast receivers attached to its interfaces by listening to IGMP messages exchanged between the multicast router and hosts. The device then multicasts the packets on the Layer 2 network so that only members in the multicast group can receive the packets. |
| Multicast services | Layer 3 multicast | After IGMP is deployed on VBDIF interfaces, a multicast forwarding table and routing table are created. When the device receives the multicast protocol packet from the user side, the device can identify and send the packet to the upstream device based on service VLAN tags. When the device sends multicast traffic, the device can replicate and deliver the multicast traffic based on the created multicast forwarding table. |
| Reliability | Virtual Router Redundancy Protocol (VRRP) | To ensure reliable and stable network communication, deploy VRRP backup groups on the VBDIF interfaces of the gateways to implement redundancy backup between gateways. If the master gateway fails, services are immediately switched to the backup gateway, ensuring communication continuity and reliability. |
| Routing protocols | IS-IS | To allow users on different network segments in a BD to communicate, deploy a routing protocol to implement Layer 3 reachability.  * Interior Gateway Protocol (IGP)    + RIP: an IP-layer protocol applicable to small-sized networks, such as campus networks.   + OSPF: an IP-layer protocol applicable to medium-sized networks with hundreds of devices supported, such as enterprise networks.   + IS-IS: a link-layer protocol applicable to large networks, such as large Internet Service Provider (ISP) networks. * BGP is a dynamic routing protocol used between autonomous systems (ASs). |
| Routing Information Protocol (RIP) |
| Open Shortest Path First (OSPF) |
| Border Gateway Protocol (BGP) |
| NTP | - | To implement clock synchronization between devices equipped with clocks on a network so that all devices can have the same clock, deploy NTP on VBDIF interfaces. |
| Network monitoring | Network Quality Analysis (NQA) | To allow carriers to monitor QoS in real time and effectively diagnose and locate network faults, deploy NQA to test network operating status and output statistics. |
| Security | DHCP snooping | When DHCP servers and clients reside in the same BD, to allow DHCP clients to obtain IP addresses from valid DHCP servers, configure DHCP snooping to defend against bogus DHCP servers. |

[Figure 1](#EN-US_CONCEPT_0172363334__fig_dc_vrp_evc_cfg_000202) shows the flowchart for configuring services or protocols carried over EVCs.

**Figure 1** Flowchart for configuring services or protocols carried over EVCs  
![](images/fig_dc_vrp_evc_cfg_000202.png)