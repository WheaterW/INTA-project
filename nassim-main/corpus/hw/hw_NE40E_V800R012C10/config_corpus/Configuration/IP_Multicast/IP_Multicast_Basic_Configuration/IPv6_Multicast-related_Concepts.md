IPv6 Multicast-related Concepts
===============================

Before configuring IPv6 multicast services, except the basic multicast concepts and multicast models described in the section [IPv4 Multicast-related Concepts](dc_vrp_multicast_cfg_2232.html), familiarize yourself with IPv6 multicast addresses and IPv6 multicast protocols.

#### IPv6 Multicast Addresses

On an IPv6 network, to implement intercommunication between multicast sources and multicast group members, IPv6 multicast addresses are needed. An IPv6 multicast address begins with FF. [Table 1](#EN-US_CONCEPT_0172366670__tab_dc_vrp_multicast_cfg_222901) lists address segments and describes the usage of each address segment.

**Table 1** IPv6 multicast address segments and their meanings
| Scope | Description |
| --- | --- |
| FF0x::/32 | Well-known multicast addresses defined by the IANA. |
| FF1x::/32 (x cannot be 1 or 2)  FF2x::/32 (x cannot be 1 or 2) | Any-Source Multicast (ASM) addresses. The addresses are valid on the entire network. |
| FF3x::/32 (x cannot be 1 or 2) | Default Source-Specific Multicast (SSM) addresses. The addresses are valid on the entire network. |



#### IPv6 Multicast Protocols

[Table 2](#EN-US_CONCEPT_0172366670__tab_dc_vrp_multicast_cfg_222902) describes IPv6 multicast protocols.

**Table 2** IPv6 multicast protocols
| Protocol | Function | Remarks |
| --- | --- | --- |
| PIM-IPv6 | Protocol Independent Multicast (PIM)-IPv6 is a multicast routing solution used on an IPv6 network to forward multicast data to the Router that has attached multicast group members requesting the multicast data. It implements multicast data routing and forwarding. | In PIM-SM, ASM and SSM models are differentiated based on the multicast addresses in multicast data and protocol packets.  * If the multicast addresses are in the SSM group address range, PIM-SSM is used. PIM-SSM has a high forwarding capability and simplifies multicast address allocation. It is especially applicable to the scenario where a multicast group corresponds to only one multicast source. * If the multicast addresses are in the ASM group address range, PIM-ASM is used. |
| MLD | The Multicast Listener Discovery (MLD) protocol runs between a Layer 3 multicast router and its attached user hosts. At the host side, MLD enables the hosts to dynamically join or leave groups; at the network side, MLD maintains and manages group memberships and completes interaction with the upper layer multicast routing protocol. | At present, MLD has two versions, MLDv1 and MLDv2.  MLDv2 supports the Source-Specific Multicast (SSM) model, whereas MLDv1 supports the SSM model only when the SSM mapping technology is used.  MLD functions the same as the Internet Group Management Protocol (IGMP) for IPv6. Implementations of MLD and IGMP are similar. For example, MLDv1 is similar to IGMPv2 and MLDv2 is similar to IGMPv3. |