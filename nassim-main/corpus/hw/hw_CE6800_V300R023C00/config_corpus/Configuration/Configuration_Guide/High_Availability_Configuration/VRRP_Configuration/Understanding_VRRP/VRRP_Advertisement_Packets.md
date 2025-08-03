VRRP Advertisement Packets
==========================

VRRP Advertisement packets are multicast packets that can be forwarded only within a single broadcast domain, such as a virtual local area network (VLAN). They are used to notify all backup devices in a VRRP group of the master's priority and status.

Two VRRP versions currently exist: VRRPv2 and VRRPv3.

VRRP is classified as VRRP for IPv4 or VRRP for IPv6 (VRRP6) by network type. VRRP for IPv4 supports VRRPv2 and VRRPv3, whereas VRRP6 supports only VRRPv3. On an IPv4 network, VRRP Advertisement packets are encapsulated into IPv4 packets and sent to a multicast address assigned to a VRRP group. In the IPv4 packet header, the source address is the primary IPv4 address of the interface that sends the packets (not the virtual IPv4 address), the destination address is 224.0.0.18, the TTL is 255, and the protocol number is 112.

![](public_sys-resources/note_3.0-en-us.png) 

You can manually switch VRRP versions on a device. Unless otherwise specified, VRRP packets in this document refer to VRRPv2 packets.


#### VRRP Advertisement Packet Structure

[Figure 1](#EN-US_CONCEPT_0000001176743715__fig_dc_vrp_vrrp_feature_012501) shows the VRRPv2 packet structure.

**Figure 1** VRRPv2 Advertisement packet structure  
![](figure/en-us_image_0000001130624304.png)
[Table 1](#EN-US_CONCEPT_0000001176743715__tab_dc_vrp_vrrp_feature_012501) describes the fields in a VRRPv2 Advertisement packet.

**Table 1** Fields in a VRRPv2 Advertisement packet
| Field | Meaning |
| --- | --- |
| Version | VRRP version number. The value is 2. |
| Type | Type of a VRRPv2 packet. The value is 1, indicating an Advertisement packet. |
| Virtual Rtr ID | Virtual router ID. |
| Priority | Priority of the master device in a VRRP group. |
| Count IPv4 Addrs | Number of virtual IPv4 addresses in a VRRP group. |
| Auth Type | Authentication type of a VRRPv2 packet. Three authentication types are defined:   * 0: Non Authentication, indicating that authentication is not performed. * 1: Simple Text Password, indicating that simple authentication is performed. * 2: IP Authentication Header, indicating that HMAC-MD5 authentication is performed. |
| Adver Int | Interval (in seconds) at which VRRPv2 packets are sent. |
| Checksum | 16-bit checksum, used to check the data integrity of a VRRPv2 packet. |
| IPv4 Address | Virtual IPv4 address configured for a VRRP group. The number of virtual IPv4 addresses configured is carried in the Count IPv4 Addrs field. |
| Authentication Data | Authentication key of a VRRPv2 packet. This field applies only when simple or HMAC-MD5 authentication is used. For other authentication types, this field is fixed at 0. |


[Figure 2](#EN-US_CONCEPT_0000001176743715__fig_dc_vrp_vrrp_feature_012502) shows the VRRPv3 packet structure.

**Figure 2** Format of a VRRPv3 packet  
![](figure/en-us_image_0000001176663851.png)
[Table 2](#EN-US_CONCEPT_0000001176743715__tab_dc_vrp_vrrp_feature_012502) describes the fields in a VRRPv3 packet.

**Table 2** Fields in a VRRPv3 packet
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



The main differences between VRRPv2 and VRRPv3 are as follows:

* Authentication: VRRPv3 does not support authentication, whereas VRRPv2 does.
* Time unit of the interval for sending VRRP Advertisement packets: VRRPv3 uses centiseconds, whereas VRRPv2 uses seconds.