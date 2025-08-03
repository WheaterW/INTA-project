rule (Advanced ACL view) (gre-igmp-ip-ipinip-ospf)
==================================================

rule (Advanced ACL view) (gre-igmp-ip-ipinip-ospf)

Function
--------



The **rule** command creates or modifies an ACL rule in the advanced ACL view.

The **undo rule** command deletes an ACL rule in the advanced ACL view.



By default, no advanced ACL rule is created.


Format
------

**rule** [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } { **zero** | *protocol* | **gre** | **ip** | **ipinip** | **ospf** | *7-16* | *18-255* } [ [ **dscp** { *dscp* | **af11** | **af12** | **af13** | **af21** | **af22** | **af23** | **af31** | **af32** | **af33** | **af41** | **af42** | **af43** | **cs1** | **cs2** | **cs3** | **cs4** | **cs5** | **cs6** | **cs7** | **default** | **ef** } | [ **tos** { *value* | **max-reliability** | **max-throughput** | **min-delay** | **min-monetary-cost** | **normal** } | **precedence** { *precedence* | **critical** | **flash** | **flash-override** | **immediate** | **internet** | **network** | **priority** | **routine** } ] \* ] | { **destination** { *destination-ip-address* { *destination-wildcard* | **0** | *des-netmask* } | **any** } | **destination-pool** *destination-pool-name* } | **fragment-type** **fragment** | { **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **source-pool** *source-pool-name* } | **time-range** *time-name* | **ttl** { { **gt** | **lt** | **eq** | **neq** } *ttl-value* | **range** *ttl-value* *ttl-value* } | **vpn-instance** *vpn-instance-name* | **logging** ] \*

**rule** [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } { **igmp** | *2* } [ [ **dscp** { *dscp* | **af11** | **af12** | **af13** | **af21** | **af22** | **af23** | **af31** | **af32** | **af33** | **af41** | **af42** | **af43** | **cs1** | **cs2** | **cs3** | **cs4** | **cs5** | **cs6** | **cs7** | **default** | **ef** } | [ **tos** { *value* | **max-reliability** | **max-throughput** | **min-delay** | **min-monetary-cost** | **normal** } | **precedence** { *precedence* | **critical** | **flash** | **flash-override** | **immediate** | **internet** | **network** | **priority** | **routine** } ] \* ] | { **destination** { *destination-ip-address* { *destination-wildcard* | **0** | *des-netmask* } | **any** } | **destination-pool** *destination-pool-name* } | **fragment-type** **fragment** | { **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **source-pool** *source-pool-name* } | **time-range** *time-name* | **ttl** { { **gt** | **lt** | **eq** | **neq** } *ttl-value* | **range** *ttl-value* *ttl-value* } | **vpn-instance** *vpn-instance-name* | **logging** ] \*

**undo rule** [ **name** *rule-name* ] { **permit** | **deny** } { **zero** | *protocol* | **gre** | **ip** | **ipinip** | **ospf** | *7-16* | *18-255* } [ [ **dscp** { *dscp* | **af11** | **af12** | **af13** | **af21** | **af22** | **af23** | **af31** | **af32** | **af33** | **af41** | **af42** | **af43** | **cs1** | **cs2** | **cs3** | **cs4** | **cs5** | **cs6** | **cs7** | **default** | **ef** } | [ **tos** { *value* | **max-reliability** | **max-throughput** | **min-delay** | **min-monetary-cost** | **normal** } | **precedence** { *precedence* | **critical** | **flash** | **flash-override** | **immediate** | **internet** | **network** | **priority** | **routine** } ] \* ] | { **destination** { *destination-ip-address* { *destination-wildcard* | **0** | *des-netmask* } | **any** } | **destination-pool** *destination-pool-name* } | **fragment-type** **fragment** | { **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **source-pool** *source-pool-name* } | **time-range** *time-name* | **ttl** { { **gt** | **lt** | **eq** | **neq** } *ttl-value* | **range** *ttl-value* *ttl-value* } | **vpn-instance** *vpn-instance-name* | **logging** ] \*

**undo rule** [ **name** *rule-name* ] { **permit** | **deny** } { **igmp** | *2* } [ [ **dscp** { *dscp* | **af11** | **af12** | **af13** | **af21** | **af22** | **af23** | **af31** | **af32** | **af33** | **af41** | **af42** | **af43** | **cs1** | **cs2** | **cs3** | **cs4** | **cs5** | **cs6** | **cs7** | **default** | **ef** } | [ **tos** { *value* | **max-reliability** | **max-throughput** | **min-delay** | **min-monetary-cost** | **normal** } | **precedence** { *precedence* | **critical** | **flash** | **flash-override** | **immediate** | **internet** | **network** | **priority** | **routine** } ] \* ] | { **destination** { *destination-ip-address* { *destination-wildcard* | **0** | *des-netmask* } | **any** } | **destination-pool** *destination-pool-name* } | **fragment-type** **fragment** | { **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **source-pool** *source-pool-name* } | **time-range** *time-name* | **ttl** { { **gt** | **lt** | **eq** | **neq** } *ttl-value* | **range** *ttl-value* *ttl-value* } | **vpn-instance** *vpn-instance-name* | **logging** ] \*

**undo rule** *rule-id* [ **to** *end-rule-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rule-id* | Specifies the ID of an advanced ACL rule. | The value is an integer ranging from 0 to 4294967294. |
| **name** *rule-name* | Specifies the name of an ACL rule. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces or begin with an underscore (\_). |
| **permit** | Permits the packets that match conditions. | - |
| **deny** | Denies packets that match conditions. | - |
| **zero** | IPv4 Zero Protocol. | - |
| *protocol* | Indicates the protocol number. | The value is a number, it is an integer ranging from 3 to 5. |
| **gre** | GRE tunnelling(47). | - |
| **ip** | Any IP protocol. | - |
| **ipinip** | IP in IP tunnelling(4). | - |
| **ospf** | Open Shortest Path First (OSPF) (89). | - |
| *7-16* | Indicates the protocol number. | The value is an integer ranging from 7 to 16. |
| *18-255* | Indicates the protocol number. | The value is an integer ranging from 18 to 255. |
| **dscp** *dscp* | Matches packets based on the 6-bit DSCP field in an IPv4 packet as defined in standard protocols. DSCP can be used together neither with ToS nor with IP Precedence.  DSCP is 6-bit, and left bit is high bit, and right bit is low bit. The DSCP shown in the following figure equals to 32 in decimal number (100000 in binary number), rather than 1. | The value is an integer ranging from 0 to 63. |
| **af11** | Matches packets based on a DSCP value AF11 DSCP (001010). | - |
| **af12** | Matches packets based on a priority value AF12 DSCP (001100). | - |
| **af13** | Matches packets based on a priority value AF13 DSCP (001110). | - |
| **af21** | Matches packets based on a DSCP value AF21 DSCP (010010). | - |
| **af22** | Matches packets based on a DSCP value AF22 DSCP (010100). | - |
| **af23** | Matches packets based on a DSCP value AF23 DSCP (010110). | - |
| **af31** | Matches packets based on a DSCP value AF31 DSCP (011010). | - |
| **af32** | Matches packets based on a DSCP value AF32 DSCP (011100). | - |
| **af33** | Matches packets based on a DSCP value AF33 DSCP (011110). | - |
| **af41** | Matches packets based on a DSCP value AF41 DSCP (100010). | - |
| **af42** | Matches packets based on a DSCP value AF42 DSCP (100100). | - |
| **af43** | Matches packets based on a DSCP value AF43 DSCP (100110). | - |
| **cs1** | Class selector 1 service (8). | - |
| **cs2** | Class selector 2 service (16). | - |
| **cs3** | Class selector 3 service (24). | - |
| **cs4** | Class selector 4 service (32). | - |
| **cs5** | Class selector 5 service (40). | - |
| **cs6** | Class selector 6 service (48). | - |
| **cs7** | Class selector 7 service (56). | - |
| **default** | Matches packets based on the 6-bit DSCP field in an IPv4 packet as defined in standard protocols, Default DSCP (000000). | - |
| **ef** | Expedited forwarding service (46). | - |
| **tos** *value* | Matches packets based on the 4-bit ToS field in an IPv4 packet as defined in standard protocols.  ToS in Advanced ACL is 4 bits long as defined in standard protocols. The ToS shown in the following figure equals to 8 in decimal number (1000 in binary number), rather than 1. | The value is an integer in the range 0 to 15. |
| **max-reliability** | Matches packets with max reliability TOS (2). | - |
| **max-throughput** | Matches packets with max throughput TOS (4). | - |
| **min-delay** | Matches packets with min delay TOS (8). | - |
| **min-monetary-cost** | Matches packets with min monetary cost TOS (1). | - |
| **normal** | Matches packets with normal TOS (0). | - |
| **precedence** *precedence* | Matches packets based on the three most significant bits of the ToS field in an IP packet. The Precedence field has three bits. The left bit is the most significant bit, and the right bit is the least significant bit. For the IPv4 packet header, the value of the Precedence field is 100 in binary mode, and its decimal value is 4 instead of 1. | The value is an integer ranging from 0 to 7. |
| **critical** | Indicates the critical precedence (5). | - |
| **flash** | Indicates the flash precedence (3). | - |
| **flash-override** | Indicates the flash-override precedence (4). | - |
| **immediate** | Indicates the immediate precedence (2). | - |
| **internet** | Indicates the internetwork control precedence (6). | - |
| **network** | Indicates the network control precedence (7). | - |
| **priority** | Indicates the priority of an ACL. | - |
| **routine** | Indicates the routine precedence (0). | - |
| **destination** | Matches packets based on destination IP addresses.  If destination is not configured, packets to any destination IP address are matched. | - |
| *destination-ip-address* | Specifies a destination IP address. | It is in dotted decimal notation. |
| *destination-wildcard* | Specifies the wildcard of a destination IP address. A wildcard mask is a 32-bit number string that indicates which bits of an IP address are checked. Its form is the same as that of an IP address. A source or destination IP address range can be determined by a wildcard mask and an IP address of criteria conditions. If a packet address is within this range, the packet meets the criteria conditions; otherwise, the packet does not. Among bits of wildcard masks, 0 represents "Check corresponding bits" and 1 "Do not check corresponding bits". | The value is in dotted decimal notation. The wildcard of the destination IP address can be 0, equivalent to 0.0.0.0, indicating that the destination IP address is a host address. |
| **0** | Indicates the address wildcard 0.0.0.0 (matching a single host). | - |
| *des-netmask* | Specifies the mask length of the destination IP address. | The value is an integer ranging from 1 to 32. |
| **any** | Matches packets with any IP address. | - |
| **destination-pool** *destination-pool-name* | Specifies an ACL destination IP address pool.  An ACL IP address pool is created using the acl ip-pool command. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **fragment-type** | Matches packets based on the fragment type of the packets. | - |
| **fragment** | Checks fragmented packets. | - |
| **source** | Matches packets based on the source IP address.  If no source IP address is specified, packets with any source IP address are matched. | - |
| *source-ip-address* | Specifies the source IP address. | It is in dotted decimal notation. |
| *source-wildcard* | Specifies the wildcard of the source IP address.  A wildcard mask is a 32-bit number string that indicates which bits of an IP address are checked. Its form is the same as that of an IP address. A source or destination IP address range can be determined by a wildcard mask and an IP address of criteria conditions. If a packet address is within this range, the packet meets the criteria conditions; otherwise, the packet does not. Among bits of wildcard masks, 0 represents "Check corresponding bits" and 1 "Do not check corresponding bits". | The value is in dotted decimal notation. The wildcard of a source IP address can be 0, equivalent to 0.0.0.0, indicating that the source IP address is a host address.  192.168.1.16 0.0.0.15 indicates that the address range is from 192.168.1.16 to 192.168.1.28.  The wildcard mask 255.255.255.255 represents all IP addresses. As all bits are 1s, it indicates that all 32 bits are not checked. In this case, use "any" to replace the IP addresses.  The wildcard mask 0.0.0.0 indicates that all 32 bits need to be matched. The working principles of wildcard masks and IP subnet masks are different. For subnet masks, numbers 1 and 0 determine whether the IP address belongs to a network, subnet, or host. |
| *src-netmask* | Specifies the mask length of a source IP address. | The value is an integer ranging from 1 to 32. |
| **source-pool** *source-pool-name* | Specifies an advanced ACL source IP address pool.  An ACL IP address pool is created using the acl ip-pool command. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **time-range** *time-name* | Specifies a time range during which an ACL rule takes effect. If the time-range is not configured for ACL, it indicates the ACL takes effect immediately.  A time range is configured using the time-range command. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **ttl** | Matches packets based on TTL values of packets. | - |
| **gt** | Indicates that packets with TTL values greater than the specified TTL value are matched. | - |
| **lt** | Indicates that packets with TTL values less than the specified TTL value are matched. | - |
| **eq** | Indicates that packets with TTL values equal to the specified TTL value are matched. | - |
| **neq** | Matches the packets whose TTL values are not equal to the specified TTL value. | - |
| **range** *ttl-value* | Matches packets based on a specified TTL value. If range is specified for ttl-operation, specify ttl-value twice to specify a range. | The value is an integer ranging from 1 to 255. |
| **vpn-instance** *vpn-instance-name* | Matches packets based on a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **logging** | Logs matched packets. | - |
| **rule** | Indicates an ACL rule. | - |
| **igmp** | Internet Group Management Protocol(2). | - |
| *2* | Indicates the protocol number. | - |
| **undo** | Cancels the current setting. | - |
| **to** *end-rule-id* | Specifies an end rule ID for advanced ACL rules to be deleted in batches. | The value is an integer ranging from 0 to 4294967294. |



Views
-----

Advanced ACL view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After an advanced ACL is created, run the **rule** command to add rules to the ACL.Advanced ACL rules with the fragment-type can prevent such attacks by permitting only non-fragmented packets.



**Prerequisites**



An advanced ACL has been created using the **acl** command in the system view.



**Configuration Impact**

When specifying an ACL rule ID, note the following:

* If a rule with a specified rule ID already exists, and the new rule conflicts with the existing one, the conflicting part in the new rule overwrites that in the existing rule.
* If no rule with the specified rule ID exists, a rule with the specified rule ID is created.When an ACL rule ID is not specified and a rule is added, the system automatically allocates an ID to this rule. ACL rules are arranged in ascending order of rule IDs, with the difference between two adjacent rules as an ACL increment.The rule IDs automatically generated by the system start from the ACL increment. For example, if the ACL increment is 5, the rule ID starts from 5; if the ACL increment is 2, the rule ID starts from 2. This allows you to add rules before the first rule.By default, if an ACL is not configured with the fragment-type,
* If only Layer 3 information is configured to the rule, the ACL rules will filter all packets (including the first fragment of a packet, non-first fragments, and non-fragmented packets).
* If both Layer 3 and Layer 4 information is configured to the rule,
  + The ACL filters the first fragment of a packet and non-fragmented packets, as these packets contain Layer 3 and Layer 4 information.
  + Only Layer 3 information about non-first fragments is filtered, as they contain Layer 3 information never Layer 4 information. If Layer 3 information matches the "permit" rule, the non-first fragment is allowed to pass through; if Layer 3 information matches the "deny" rule, continue matching the non-first fragment against the next rule. (Note: This is different to the normal ACL working process.)

**Precautions**



If you specify the fragment type of packets as fragment when you configure advanced ACL rules for TCP or UDP, fragment-type and destination-port or source-port cannot be both configured.If you specify the fragment type of packets as fragment when you configure advanced ACL rules for TCP, fragment-type and tcp-flag cannot be both configured.If you specify the fragment type of packets as fragment when you configure advanced ACL rules for ICMP, fragment-type and icmp-type cannot be both configured.




Example
-------

# Create an advanced ACL numbered 3999 and add a rule to ACL 3999 to match packets with the source and destination IP addresses 10.1.1.1 and 10.2.1.1, respectively.
```
<HUAWEI> system-view
[~HUAWEI] acl number 3999
[*HUAWEI-acl4-advance-3999] rule deny ip source 10.1.1.1 0 destination 10.2.1.1 0

```