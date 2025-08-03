Overview of ACL6s
=================

An access control list (ACL) is a set of sequential packet filtering rules. After an ACL is configured on a routing device, the routing device permits or denies packets based on the matched rules defined in the ACL. ACL6s are the ACLs that support IPv6, and can be applied to various services, such as routing policies, traffic management, and QoS.

#### Introduction

As the name indicates, an access control list (ACL) is a list. The list contains matching clauses, which are actually matching rules and used to tell the device to perform action on the packet or not. ACL6s are the ACLs that support IPv6, and can be applied to various services, such as routing policies, traffic management, and QoS.

Device communication networks need to provide reliable data transmission. To this end, ACL6s can be used on access or core devices to achieve network security and stability.

* Defend against various network attacks, such as attacks by using IPv6, TCP, and ICMPv6 packets.
* Control network access. For example, ACL6s can be used to control enterprise network user access to external networks, to specify the network resources accessible to users, and to define the time ranges in which users can access networks.
* Limit network traffic and improve network performance. For example, ACL6s can be used to limit bandwidth for upstream and downstream traffic and to apply charging rules to user requested bandwidth, therefore achieving efficient utilization of network resources.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

An ACL6 classifies packets based only on its predefined rules. To filter packets, the ACL6 must be used together with specific functions such as device management, routing policy, multicast packet filtering, and traffic management.



#### ACL6 Classification

The following table outlines ACL6 classification based on functions.

**Table 1** ACL6 types
| ACL6 Type | Function | ACL6 Number |
| --- | --- | --- |
| Interface-based ACL6 | Defines rules based on packets' inbound interfaces. | 1000 to 1999 |
| Basic ACL6 | Defines rules based on packets' source addresses. | 2000 to 2999 |
| Advanced ACL6 | Defines rules based on packets' source or destination addresses, source or destination port numbers, and protocol types. | 3000 to 3999 |
| User ACL6 (UCL6) | Defines rules based on the source/destination IPv6 address, source/destination service group, source/destination user group, source/destination port number, and protocol type. | 6000 to 9999 |




#### Validity Period of ACL6 Rules

To control a type of traffic in a specified period of time, users can configure the validity period of an ACL rule to determine the time during which that traffic type is allowed to pass through. For example, to ensure reliable transmission of video services in prime time in the evening, restrict the traffic volume of common online users. The validity period can be an absolute or cyclic time range.

* An absolute time range start from *yyyy-mm-dd* to *yyyy-mm-dd*. This time range is effective once and does not repeat.
* A cyclic time range is cyclic, with a one week cycle. For example, an ACL rule takes effect from 8:00 to 12:00 every Sunday.


#### ACL6 Description

Configuring the description for a created ACL6 helps you learn the ACL6 quickly.


#### ACL6 Rules

ACL6 rules are configured for each ACL6 and used to classify packets in different scenarios. [Table 2](#EN-US_CONCEPT_0172365045__tab_dc_vrp_acl6_cfg_004102) lists ACL6 rules and their functions.

**Table 2** ACL6 rules
| ACL6 Rule | ACL6 Type | Function |
| --- | --- | --- |
| Validity period | Interface-based ACL6, basic ACL6, advanced ACL6, user ACL6 | Sets a validity period in which ACL6 rules take effect. This rule is used for:  * Flow control * Access time control |
| Inbound interface | Interface-based ACL6 | Classifies packets based on their inbound interfaces. This rule is used for:  * Flow control * Access authority control |
| Non-first fragment | Basic ACL6, advanced ACL6, user ACL6 | Classifies packets based on whether a packet is the first packet fragment. This rule is used for:  * Attack defense * Flow control |
| Source IPv6 address | Basic ACL6, advanced ACL6, user ACL6 | Classifies packets based on their source IPv6 addresses. This rule is used for:  * Flow control * Access authority control * Route filtering * Multicast packet filtering |
| VPN instance | Basic ACL6 and advanced ACL6 | Classifies packets based on the VPN instances to which the packets belong. This rule is used for:  * Flow control * Access authority control |
| Destination IPv6 address | Advanced ACL6, user ACL6 | Classifies packets based on their destination IPv6 addresses. This rule is used for:  * Flow control * Access authority control * Route filtering * Multicast packet filtering |
| Protocol type | Advanced ACL6, user ACL6 | Classifies packets based on their protocol types. |
| Source port number | Advanced ACL6, user ACL6 | Classifies packets based on source TCP or UDP port numbers. This rule is used for:  * Flow control * Access authority control * Route filtering |
| Destination port number | Advanced ACL6, user ACL6 | Classifies packets based on destination TCP or UDP port numbers. This rule is used for:  * Flow control * Access authority control * Route filtering |
| IPv6 DSCP value | Advanced ACL6, user ACL6 | Classifies IPv6 packets based on their DSCP values. This rule is used for route filtering. |
| IPv6 precedence value | Advanced ACL6, user ACL6 | Classifies IPv6 packets based on the IPv6 precedence. This rule is used for flow control. |
| IPv6 ToS value | Advanced ACL6, user ACL6 | Classifies IPv6 packets based on their ToS values. This rule is used for flow control. |
| Source/destination service group, or source/destination user group | User ACL6 | Classifies IPv6 packets based on source/destination service group, or source/destination user group. This rule is used for flow control. |



#### Matching Order of ACL6 Rules

A device configured with ACL6s matches the received packets against ACL6 rules according to the matching order of rules.

The rule sequence in an ACL6 depends on ACL6 rule-matching orders and ACL6 rule numbers.

Rule matching orders include the configuration order and the automatic order.

* Automatic order: The system sequences rules automatically and places the most precise rule in the front of the ACL6 based on the depth-first principle.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  + ACL6 rules are sequenced based on rule precision. For an ACL6 rule (where a protocol type, a source IPv6 address range, or a destination IPv6 address range is specified), the stricter the rule, the more precise it is. For example, an ACL6 rule can be configured based on the wildcard of an IPv6 address. The smaller the wildcard, the smaller the specified network segment and the stricter the ACL6 rule.
  + If rules have the same precision, they are matched based on the configuration order.
* Configuration order: The system sequences ACL6 rules based on the rules' configuration order.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The mechanism in which ACL6 rules are matched based on their configuration order applies only when rule numbers are not specified. If rule numbers are specified, the ACL6 rules are matched based on their numbers in ascending order.