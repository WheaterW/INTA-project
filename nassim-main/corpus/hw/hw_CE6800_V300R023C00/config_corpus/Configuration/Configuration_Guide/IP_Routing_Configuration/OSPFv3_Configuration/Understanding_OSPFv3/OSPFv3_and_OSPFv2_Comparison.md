OSPFv3 and OSPFv2 Comparison
============================

OSPFv3 and OSPFv2 Comparison

#### Similarities

* Network types and interface types
* Interface and neighbor state machines
* LSDB
* Flooding mechanism
* Types of packets: Hello, DD, LSR, LSU, and LSAck
* Route calculation

#### Differences

**Table 1** Differences between OSPFv3 and OSPFv2
| Item | Difference |
| --- | --- |
| Address information carried in packets | In OSPFv3, only LSAs in LSU packets contain address information. |
| Protocol running mechanism | OSPFv3 runs over IPv6, which is based on links instead of network segments.  As such, the interfaces on which OSPFv3 is to be configured must be on the same link, rather than on the same network segment. In addition, the interfaces can establish OSPFv3 connections without IPv6 global addresses. |
| Dependency on IP addresses | OSPFv3 does not depend on IP addresses, so that topology calculation can be separated from IP addresses. OSPFv3 can calculate the OSPFv3 topology without knowing IPv6 global addresses, which are used only for virtual link interfaces and packet forwarding. |
| Formats of packets and LSAs | * OSPFv3 packets do not contain IP addresses. * OSPFv3 router-LSAs and network-LSAs do not contain IP addresses, which are advertised by link-LSAs and intra-area-prefix-LSAs. * In OSPFv3, router IDs, area IDs, and LSA link state IDs no longer indicate IP addresses. The IPv4 address format, however, is still reserved. * For OSPFv3, neighbors are identified by router IDs instead of IP addresses on broadcast, NBMA, or P2MP networks. |
| LSA flooding scope | Information about the flooding scope is added to the LSA Type field of OSPFv3 LSAs. Therefore, OSPFv3 routers can process LSAs of unidentified types.   * OSPFv3 can store or flood unidentified packets, whereas OSPF discards unidentified packets. * In OSPFv3, unknown LSAs with the U-bit set to 1 can be flooded, and the flooding scope of such LSAs is specified by the LSAs.   For example, DeviceA and DeviceB can identify LSAs of a certain type, and are connected through DeviceC, which cannot identify such LSAs. When DeviceA floods such LSAs, they can be received by DeviceC and flooded to DeviceB despite DeviceC being unable to identify them. Once received, DeviceB processes the LSAs.  If OSPFv2 is run, DeviceC discards the unidentified LSAs. As a result, these LSAs cannot reach DeviceB. |
| Multi-instance | OSPFv3 supports multiple instances on a link. In OSPFv2, one physical interface can be bound to only one instance. Conversely, in OSPFv3, one physical interface can be bound to multiple instances, which are identified by different instance IDs. Each of these instances can establish an OSPFv3 neighbor relationship with a device on the remote end of the link and transmit packets. These instances do not interfere with each other when running on the same physical link. As such, link resources can be fully shared among these instances. |
| Link-local address | OSPFv3 uses IPv6 link-local addresses. IPv6 implements neighbor discovery, automatic configuration, and other functions based on link-local addresses. Devices running IPv6 do not forward IPv6 packets to destinations with link-local addresses, and such packets can be exchanged only on the same link. The unicast link-local address starts from FE80/10.  As a routing protocol running over IPv6, OSPFv3 uses link-local addresses to maintain neighbor relationships and synchronize LSDBs. All OSPFv3 interfaces, except virtual link interfaces, use link-local addresses as the source address and the next hop address to transmit OSPFv3 packets. The advantages are as follows:  * OSPFv3 can calculate topologies without global IPv6 addresses. * The packets flooded on a link are not transmitted to other links. This minimizes unnecessary flooding and thereby saves bandwidth resources. |
| Support for new LSA types | OSPFv3 supports two new types of LSAs:  * Link LSA: A device floods a link LSA on the link where it resides to advertise its link-local address and the configured global IPv6 address. * Intra-area prefix LSA: A device advertises an intra-area prefix LSA in the local area to inform the other devices in the area or the network (either a broadcast network or an NBMA network) of its IPv6 global address. |
| Neighbor ID | On broadcast, NBMA, and P2MP networks, OSPFv2 identifies neighbors based on the IPv4 addresses of interfaces. OSPFv3 identifies neighbors based only on router IDs. |