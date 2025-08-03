VRRP Packets
============

VRRP Advertisement packets are multicast packets that can be forwarded only within a single broadcast domain, such as a virtual local area network (VLAN). They are used to notify all backup devices in a VRRP group of the master's priority and status.

Two VRRP versions currently exist: VRRPv2 and VRRPv3.

VRRP is classified as VRRP for IPv4 or VRRP for IPv6 (VRRP6) by network type. VRRP for IPv4 supports VRRPv2 and VRRPv3, whereas VRRP6 supports only VRRPv3. On an IPv4 network, VRRP Advertisement packets are encapsulated into IPv4 packets and sent to a multicast address assigned to a VRRP group. In the IPv4 packet header, the source address is the primary IPv4 address of the interface that sends the packets (not the virtual IPv4 address), the destination address is 224.0.0.18, the TTL is 255, and the protocol number is 112.

On an IPv6 network, VRRP packets are encapsulated into IPv6 packets and sent to an IPv6 multicast address assigned to a VRRP6 group. In the IPv6 packet header, the source address is the link-local address of the interface that sends the packets (not the virtual IPv6 address), the destination address is FF02::12, the TTL is 255, and the protocol number is 112.

#### VRRPv3 Packet Structure

[Figure 1](#EN-US_CONCEPT_0000001176661763__fig_dc_vrp_vrrp_feature_012502) shows the VRRPv3 packet structure.

**Figure 1** Format of a VRRPv3 packet  
![](figure/en-us_image_0000001176663851.png)
[Table 1](#EN-US_CONCEPT_0000001176661763__en-us_concept_0000001176743715_tab_dc_vrp_vrrp_feature_012502) describes the fields in a VRRPv3 packet.

**Table 1** Fields in a VRRPv3 packet
| Field | Meaning |
| --- | --- |
| Version | VRRP protocol version. The value is 3. |
| Type | Type of a VRRPv3 packet. The value is 1, indicating an Advertisement packet. |
| Virtual Rtr ID | Virtual router ID. |
| Priority | Priority of the master device in a VRRP group. |
| Count IPvX Addrs | Number of virtual IPvX addresses configured for a VRRP group. |
| rsvd | Field reserved in a VRRPv3 packet. The value is fixed at 0. |
| Adver Int | Interval (in centiseconds) at which VRRPv3 packets are sent. |
| Checksum | 16-bit checksum, used to check the data integrity of a VRRPv3 packet. |
| IPvX Address | Virtual IPvX address configured for a VRRP group. The number of configured virtual IPvX addresses is carried in the Count IPvX Addrs field. |