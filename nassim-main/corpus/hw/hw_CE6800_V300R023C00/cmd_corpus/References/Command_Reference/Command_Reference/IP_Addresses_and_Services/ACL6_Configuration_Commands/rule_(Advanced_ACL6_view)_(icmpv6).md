rule (Advanced ACL6 view) (icmpv6)
==================================

rule (Advanced ACL6 view) (icmpv6)

Function
--------



The **rule** command creates or modifies an ACL6 rule in the advanced ACL6 view.

The **undo rule** command deletes an ACL6 rule in the advanced ACL6 view.



By default, no advanced ACL6 rule is created.


Format
------

**rule** [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } { **icmpv6** | *58* } [ **destination** { *destination-ipv6-address* { *prefix-length* | *destination-wildcard* } | *dest-ipv6-addr-prefix* | **any** } | **fragment** | **icmp6-type** { *icmp6-type-name* | *icmp6-type* [ *icmp6-code* ] } | **source** { *source-ipv6-address* { *prefix-length* | *source-wildcard* } | *src-ipv6-addr-prefix* | **any** } | **time-range** *time-name* | **dscp** *dscp* | **vpn-instance** *vpn-instance-name* | **logging** ] \*

**undo rule** [ **name** *rule-name* ] { **permit** | **deny** } { **icmpv6** | *58* } [ **destination** { *destination-ipv6-address* { *prefix-length* | *destination-wildcard* } | *dest-ipv6-addr-prefix* | **any** } | **fragment** | **icmp6-type** { *icmp6-type-name* | *icmp6-type* [ *icmp6-code* ] } | **source** { *source-ipv6-address* { *prefix-length* | *source-wildcard* } | *src-ipv6-addr-prefix* | **any** } | **time-range** *time-name* | **dscp** *dscp* | **vpn-instance** *vpn-instance-name* | **logging** ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rule-id* | Specifies the ID of an ACL6 rule. | The value is an integer ranging from 0 to 4294967294. |
| **name** *rule-name* | Specifies the name of an ACL rule. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces or start with an underscore (\_). |
| **permit** | Permits packets that match conditions. | - |
| **deny** | Denies the packets that match the rule. | - |
| **icmpv6** | Internet Control Message Protocol version 6 (58). | - |
| *58* | Specifies a protocol number. | - |
| **destination** | Matches packets based on the destination IPv6 address.  If no destination IPv6 address is specified, an ACL takes effect for packets with any destination IPv6 address. | - |
| *destination-ipv6-address* | Specifies the destination IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *prefix-length* | Specify the length of IPv6 address mask. | The value is an integer ranging from 1 to 128. |
| *dest-ipv6-addr-prefix* | Specifies the destination IPv6 address with a prefix. | The value is a string case-sensitive characters. It cannot contain spaces. |
| **any** | Matches packets with any IPv6 address. | - |
| **fragment** | Checks fragmented packets. | - |
| **icmp6-type** | Specifies the type of ICMPv6 messages. | The value is an integer ranging from 0 to 255. |
| *icmp6-type* | Specifies the type of ICMPv6 messages. | The value is an integer ranging from 0 to 255. |
| *icmp6-type-name* | Specifies the name of an ICMPv6 message. | The value is an enumerated type. You can select a value according to the prompt information after entering a question mark (?). |
| *icmp6-code* | Specifies an ICMPv6 message code. | The value is an integer ranging from 0 to 255. |
| **source** | Matches packets based on source IPv6 addresses.  If source is not configured, packets from any source IPv6 address are matched. | - |
| *source-ipv6-address* | Specifies the source IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *src-ipv6-addr-prefix* | Specifies the length of an IPv6 address mask. | The value is an integer ranging from 1 to 128. |
| **time-range** *time-name* | Specifies the time range during which the rule takes effect. If this parameter is not specified, the rule takes effect immediately after being configured.  The time range is configured using the time-range command. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces. |
| **dscp** *dscp* | Matches IPv6 packets based on the leftmost six bits of the TC field. | The value is an integer ranging from 0 to 63. |
| **vpn-instance** | Specifies a VPN instance. | - |
| **vpn-instance** *vpn-instance-name* | Matches packets based on an IPv6 VPN instance name. If the traffic is from L3VPN, this option must be configured in the ACL. If this option is not configured, it indicates the traffic belongs to the public network rather than L3VPN. | The name is a string of 1 to 31 characters and case sensitive. |
| *vpn-instance-name* | Matches packets based on the IPv6 VPN instance name. If IPv6 packets are from the L3VPN, this parameter needs to be added to the ACL. If this parameter is not specified, the packets are public IPv6 packets. | The name is a string of 1 to 31 characters and case sensitive. |
| **logging** | Indicates whether to log the matched packets. | - |
| **rule** | Specifies an ACL6 rule. | - |
| *destination-wildcard* | Specifies the wildcard of the destination IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *source-wildcard* | Specifies the wildcard mask of a source IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

Advanced ACL6 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After an advanced ACL6 is created, run the **rule** command to add rules to the ACL6.



**Prerequisites**



An advanced ACL6 has been created using the **acl ipv6** command in the system view.A time range has been configured using the **time-range** command in the system view if you want to specify a validity period when creating an advanced ACL6 rule.



**Configuration Impact**

When specifying an ACL rule ID, note the following:

* If a rule with a specified rule ID already exists, and the new rule conflicts with the existing one, the conflicting part in the new rule overwrites that in the existing rule.
* If no rule with the specified rule ID exists, a rule with the specified rule ID is created.When an ACL rule ID is not specified and a rule is added, the system automatically allocates an ID to this rule. ACL rules are arranged in ascending order of rule IDs, with the difference between two adjacent rules as an ACL increment.The rule IDs automatically generated by the system start from the ACL increment. For example, if the ACL increment is 5, the rule ID starts from 5; if the ACL increment is 2, the rule ID starts from 2. This allows you to add rules before the first rule.

**Precautions**



When you configure advanced ACL6 rules for ICMPv6, fragment and icmp6-type cannot be both configured.




Example
-------

# Configure an advanced ACL6 whose matching order is config.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 3000
[*HUAWEI-acl6-advance-3000] rule permit icmpv6 source 2001:db8::1 64

```