Security Protection Capabilities on the Forwarding Plane
========================================================

To ensure the device's CPU runs normally, the forwarding plane on NE40E provides the following security defense capabilities:

* ACLs
* Unicast reverse path forwarding (URPF)
* DHCP snooping
* CAR for packets sent to the CPU (CPCAR)
* ACL-based user-defined flow

#### ACLs

An access control list (ACL) is a collection of ordered rules, each containing the source and destination addresses and port number of packets. It classifies packets based on these rules. When applied to a router, these rules enable the router to determine whether to permit or deny packets.

For example, an ACL can be used to deny all Telnet access terminals from accessing the local device or allow terminals to send emails to the local device over Simple Mail Transfer Protocol (SMTP).

Multiple rules can be defined for one ACL. The rules are classified as interface, MPLS, basic, or advanced ACL rules based on their functions. An ACL rule is a set of matching options, and users can select and configure it based on services.

ACLs can be classified from different perspectives. See the following table.

**Table 1** ACL classification
| ACL Classification Basis | ACL Type |
| --- | --- |
| Whether to support IPv4 or IPv6 | * ACL4 * ACL6 |
| Functions of ACL rules | * Interface ACLs: Permit or deny packets on an interface. Interface ACLs are numbered from 1000 to 1999. A maximum of 1000 interface ACLs can be configured. * Basic ACLs: Filter packets based on source addresses. Basic ACLs are numbered from 2000 to 2999. A maximum of 1000 basic ACLs can be configured. * Advanced ACLs: Filter packets based on 5-tuples of packets. A 5-tuple is comprised of the source IP address, destination IP address, protocol type (TCP or UDP), source port number, and destination port number. Advanced ACLs are numbered from 3000 to 3999. A maximum of 1000 advanced ACLs can be configured.  * Layer 2 ACLs: Filter packets based on the Ethernet frame header information of packets. Layer 2 ACLs are numbered from 4000 to 4999. A maximum of 1000 Layer 2 ACLs can be configured. * User ACLs: Filter packets based on the source IP address, source service group, source user group, source port number, destination IP address, destination service group, destination user group, destination port number, and protocol type of packets. User ACLs are numbered from 6000 to 9999. A maximum of 4000 user ACLs can be configured. * MPLS ACLs: Filter packets based on the Exp, Label, and TTL values of MPLS packets. MPLS ACLs are numbered from 10000 to 10999. A maximum of 1000 MPLS ACLs can be configured. |

The following table describes the filter options supported by different ACL types classified based on ACL functions.

**Table 2** Filter options supported by different ACLs
| ACL Type | Supported Filter Option |
| --- | --- |
| Interface ACL | Interface name: Indicates the interface through which a packet is received. **any** indicates all interfaces.  Validity period: Indicates the period in which an ACL rule is effective. If the validity period is not set, the ACL rule takes effect immediately after being configured. |
| Basic ACL | Source IP address: Specifies the source IP address for an ACL rule. If no source address is configured, packets with any source addresses are allowed to pass.  Validity period: Indicates the period in which an ACL rule is effective. If the validity period is not set, the ACL rule takes effect immediately after being configured. |
| Advance ACL | Protocol type: Specifies a protocol name or a protocol number. The value can be an integer ranging from 1 to 255. When a protocol name is specified, the value can be gre, icmp, igmp, ip, ipinip, ospf, tcp, or udp. Different protocols have different parameters. For example, source and destination port numbers can be set only for TCP and UDP.  Source IP address: Specifies the source IP address for an ACL rule. If no source address is specified, packets with any source address are matched.  Destination IP address: Specifies the destination IP address for an ACL rule. If no destination address is specified, packets with any destination address are matched.  Source/Destination port number: Specifies the TCP or UDP source/destination port number. This option is valid only when the protocol type is TCP or UDP. If no source or destination port number is configured, TCP or UDP packets with any source or destination address are matched.  Differentiated services code point (DSCP): It refers to the six most significant bits of the type of service (ToS) field in IP headers. The value ranges from 0 to 63.  Fragment packet type: Whether a rule is valid only for non-first fragments. If this parameter is specified, the rule is valid only for non-first fragments.  Priority: Indicates that packets can be filtered based on the priority field (most significant three bits of the ToS field in IP headers). The value is a keyword or number (integer ranging from 0 to 7).  TCP flag: Indicates the value of the TCP flag. The value ranges from 0 to 63.  ToS: Indicates that packets can be filtered based on the ToS field.  ICMP: ICMP packets can be filtered based on the name, type, and code of the ICMP packets. The option is effective only for ICMP. If this parameter is not specified, all types of ICMP packets are matched.  Validity period: Indicates the period in which an ACL rule is effective. If the validity period is not set, the ACL rule takes effect immediately after being configured. |
| Layer 2 ACL | Protocol type of Ethernet frames: If this option is not specified, all Ethernet frames are matched.  Source MAC address: Specifies the source MAC address in an ACL. If no source address is specified, packets with any source MAC address are matched.  Destination MAC address: Specifies the destination MAC address for an ACL rule. If no destination address is specified, packets with any destination MAC address are matched.  Validity period: Indicates the period in which an ACL rule is effective. If the validity period is not set, the ACL rule takes effect immediately after being configured. |
| User ACL | Protocol type: Specifies a protocol name or a protocol number.  Source IP address: Specifies the source IP address for an ACL rule. If no source address is specified, packets with any source address are matched.  Destination IP address: Specifies the destination IP address for an ACL rule. If no destination address is specified, packets with any destination address are matched.  Service group: Indicates that packets are filtered based on service groups. If no service group is specified, an ACL takes effect for packets with any source service group.  User group: Indicates that packets are filtered based on user groups. If no source user group is specified, an ACL takes effect for packets with any source user group.  Validity period: Indicates the period in which an ACL rule is effective. If the validity period is not set, the ACL rule takes effect immediately after being configured.  ToS: Matches packets based on the 4-bit ToS field in an IPv4 packet as defined in standard protocols.  DSCP: Matches packets based on a DSCP value.  Only some filter options are listed here. For details, see Command Reference > IP Services Commands > ACL Configuration Commands > rule (UCL view). |
| MPLS ACL | Exp: indicates the Exp value of MPLS packets. If the Exp value is not configured, MPLS packets with all Exp values are matched.  Label: Indicates the label value of MPLS packets. If this value is not configured, MPLS packets with all Label values are matched.  Time to live (TTL): Indicates the TTL value of MPLS packets. If the TTL value is not configured, MPLS packets with all TTL values are matched. |



#### URPF

A URPF-capable router queries forwarding information bases (FIBs) when Layer 3 IP packets arrive at the NP. If these packets take a local route, the router performs the URPF check before sending them to the control processor (CP). During the URPF check, the router checks whether the source IP addresses of packets are valid based on the routing table.

URPF can be set to work in either strict mode or loose mode:

* In strict mode, if a packet matches a specific route and the inbound interface of the packet is the same as the outbound interface of the route, the packet is allowed to pass. Otherwise, the packet is discarded.
* In loose mode, if a packet matches a specific route, the packet is allowed to pass. Otherwise, the packet is discarded. By default, matching of default routes is not performed unless configured.

Matching of default routes must work with strict URPF. When a packet matches a either specific route or default route and the packet's inbound interface is the same as the outbound interface of the matched route, the packet is allowed to pass. Otherwise, the packet is discarded. Loose URPF and strict URPF are mutually exclusive.


#### Security Defense Based on Access Control

The NE40E provide complete ACL capabilities. ACLs can be used to implement CPCAR and user-defined flows can be implemented.

* CPCAR classifies packets destined for the CPU and applies rules for limiting the rate of each type of packet. It allows you to set the average rate, committed burst size (CBS), and priority of packets. Setting particular CAR rules for each type of packet helps reduce mutual impact between different types of packets, protecting the CPU. CAR can also be used to set the total rate of packets sent to the CPU. When the total rate exceeds the upper limit, the system discards the excess packets to prevent CPU overload.
* A user-defined flow is bound to ACL rules defined by a user to filter packets. It comes into effect when unknown attacks are detected on a network. You can flexibly specify data characteristics of attack flows so that flows with these characteristics are not sent.
  
  To prevent the NE40E from being controlled by unauthorized users or attacked by flooding management packets, a CPU defense policy can be deployed. With the CPU defense policy, only specified interfaces are allowed to receive management packets, while packets received by other interfaces will be directly discarded to conserve resources. You can also configure the interface to receive management packets of specified protocols, and packets of other protocols are directly discarded to prevent attacks.