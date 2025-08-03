Understanding QinQ
==================

Understanding QinQ

#### Basic Concepts

802.1Q-in-802.1Q (QinQ), also called VLAN stacking or double VLANs, expands VLAN space by adding an additional 802.1Q tag to 802.1Q-tagged packets. Of the two 802.1Q tags, one is a public tag, whereas the other is a private one.

Using QinQ, devices forward packets over a public network based on the carried outer VLAN tag, that is, the public VLAN tag. On the other hand, the private VLAN tag is forwarded as the payload of the packets. In this case, QinQ is a simple and practical VPN technology. In [Figure 1](#EN-US_CONCEPT_0000001130622834__fig166101851450), user network A is divided into private VLANs 1 through 10, and user network B is divided into private VLANs 1 through 20. Public VLANs 3 and 4 are allocated to user networks A and B, respectively. When VLAN-tagged packets from user networks A and B arrive at the public network, they are tagged with an additional VLAN tag, that is, VLAN 3 for user network A's packets and VLAN 4 for user network B's packets. In this way, packets from user networks A and B are separately transmitted on the public network, even though the two networks have overlapping VLAN IDs. After traversing the public network, packets at the receiving PE are stripped of their public VLAN tags and forwarded to the CE device of their respective user network.

**Figure 1** Typical QinQ application  
![](figure/en-us_image_0000001176662437.png)

#### Benefits

QinQ technology provides the following benefits:

* Expands VLAN space.
  
  The 802.1Q tag defined in IEEE 802.1Q includes a 12-bit VLAN ID field and can identify only 4096 VLANs, that is, VLANs ranging from 0 to 4095. QinQ adds an additional 802.1Q tag to 802.1Q-tagged packets, expanding VLAN space to 4094 x 4094 = 16777216 (0 and 4095 are protocol-reserved values).
* Represents different information to facilitate service deployment.
  
  For example, during service deployment, the inner tag can represent a user, and the outer tag can represent a service.


#### QinQ Packet Encapsulation Format

An outer 802.1Q tag is added to the existing 802.1Q tag of a packet, as shown in [Figure 2](#EN-US_CONCEPT_0000001130622834__fig92256371387).

A QinQ packet has four more bytes than an 802.1Q-tagged packet. As such, the maximum frame length allowed by each interface on a network should be at least 1504 bytes to accommodate the additional length of QinQ packets. By default, the frame length allowed on a device exceeds 1504 bytes, meeting this requirement. If you need to change the allowed frame length, see "Configuring General Attributes for Ethernet Interfaces" under "Ethernet Interface Configuration" in *Configuration Guide > Interface Management Configuration* for detailed operations.

**Figure 2** QinQ packet encapsulation format  
![](figure/en-us_image_0000001176662439.png)

#### QinQ Implementation

QinQ can be implemented in either of the following ways:

**Basic QinQ**

Basic QinQ, which is also known as QinQ tunneling, is implemented based on interfaces. After basic QinQ is configured on an interface, the device adds the interface's default VLAN tag to the packet received on the interface:

* If the packet received is single-tagged, the packet becomes a double-tagged one.
* If the packet received is untagged, it becomes a single-tagged packet.

Basic QinQ adds the same outer VLAN tag to all Ethernet frames received on an interface; therefore, it is an inflexible method.

**Selective QinQ**

Selective QinQ is implemented based on interfaces and VLAN IDs. Specifically, an interface can forward packets according to a single VLAN tag or double VLAN tags. In addition, the interface can perform different operations on packets received from the same interface based on VLAN tags. For example, it can add different outer VLAN tags to packets depending on their different inner VLAN IDs or 802.1p priorities.

Currently, devices support multiple selective QinQ functions.

* MQC-based selective QinQ filters specified service flows using diverse matching rules configured in traffic classifiers and adds outer VLAN tags to packets matching those rules. This function is equivalent to a global, VLAN-based, or interface-based traffic policy associated with the traffic behavior of VLAN stacking.
* VLAN ID-based selective QinQ adds different outer VLAN tags to packets with different VLAN tags.
* If incoming packets do not carry any VLAN tag, you can the function of adding double VLAN tags to untagged packets to implement VLAN stacking.