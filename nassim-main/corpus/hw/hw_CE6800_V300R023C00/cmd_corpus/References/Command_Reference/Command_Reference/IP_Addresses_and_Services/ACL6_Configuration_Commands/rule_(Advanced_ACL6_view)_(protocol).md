rule (Advanced ACL6 view) (protocol)
====================================

rule (Advanced ACL6 view) (protocol)

Function
--------



The **rule** command creates or modifies an ACL6 rule in the advanced ACL6 view.

The **undo rule** command deletes an ACL6 rule in the advanced ACL6 view.



By default, no advanced ACL6 rule is created.


Format
------

**rule** [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } { **hoport** | *protocol* | **gre** | **ipv6** | **ipv6-ah** | **ipv6-esp** | **ospf** | *7-16* | *18-57* | *59-255* | **ipv6-frag** | **ipv6-routing** | **ipv6-destination** } [ **destination** { *destination-ipv6-address* { *prefix-length* | *destination-wildcard* } | *dest-ipv6-addr-prefix* | **any** } | **fragment** | **source** { *source-ipv6-address* { *prefix-length* | *source-wildcard* } | *src-ipv6-addr-prefix* | **any** } | **time-range** *time-name* | **dscp** *dscp* | **vpn-instance** *vpn-instance-name* | **logging** ] \*

**undo rule** [ **name** *rule-name* ] { **permit** | **deny** } { **hoport** | *protocol* | **gre** | **ipv6** | **ipv6-ah** | **ipv6-esp** | **ospf** | *7-16* | *18-57* | *59-255* | **ipv6-frag** | **ipv6-routing** | **ipv6-destination** } [ **destination** { *destination-ipv6-address* { *prefix-length* | *destination-wildcard* } | *dest-ipv6-addr-prefix* | **any** } | **fragment** | **source** { *source-ipv6-address* { *prefix-length* | *source-wildcard* } | *src-ipv6-addr-prefix* | **any** } | **time-range** *time-name* | **dscp** *dscp* | **vpn-instance** *vpn-instance-name* | **logging** ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rule-id* | Specifies the number of an advanced ACL6 rule. | The value is an integer ranging from 0 to 4294967294. |
| **name** *rule-name* | Specifies the name of an ACL rule. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces or begin with an underscore (\_). |
| **permit** | Permits the packets that match conditions. | - |
| **deny** | Denies packets that match conditions. | - |
| **hoport** | Indicates the IPv6 hop-by-hop option. | - |
| *protocol* | Matches packets based on a protocol. | The value is an integer that ranges from 1 to 5. |
| **gre** | Indicates basic routing encapsulation (47). | - |
| **ipv6** | Indicates any IPv6 protocol. | - |
| **ipv6-ah** | Indicates the IPv6 Authentication header (51). | - |
| **ipv6-esp** | Indicates IPv6 Security Payload Encapsulation (50). | - |
| **ospf** | Indicates the Open Shortest Path First routing protocol (89). | - |
| *7-16* | Indicates the protocol number. | The value is an integer ranging from 7 to 16. |
| **destination** | Matches packets based on destination IPv6 addresses.  If destination is not configured, packets to any destination IPv6 address are matched. | - |
| *destination-ipv6-address* | Specifies a destination IPv6 address. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| *prefix-length* | Specifies the mask length of an IPv6 address.. | The value is an integer ranging from 1 to 128. |
| *dest-ipv6-addr-prefix* | Specifies the IPv6 destination address with a prefix. | The value is a string case-sensitive characters. It cannot contain spaces. |
| **any** | Indicates any IPv6 address. | - |
| **fragment** | Checks fragmented packets. | - |
| **source** | Matches packets based on the source IPv6 address.  If no source IPv6 address is configured, packets with any source IPv6 address are matched. | - |
| *source-ipv6-address* | Specifies the source IPv6 address. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| *src-ipv6-addr-prefix* | Specifies the mask length of the destination IPv6 address. | The value is an integer ranging from 1 to 128. |
| **time-range** *time-name* | Specifies a time range during which a rule takes effect. If time-range is not configured, the rule takes effect immediately.  A time range is configured using the time-range command. | The value is a string of 1 to 32 case-sensitive characters without spaces. |
| **dscp** *dscp* | Specifies the value of DSCP. | The value is an integer ranging from 0 to 63. |
| **vpn-instance** *vpn-instance-name* | Matches packets based on an IPv6 VPN instance name. If the traffic is from L3VPN, this option must be configured in the ACL. If this option is not configured, the traffic belongs to the public network rather than L3VPN. | The value is a string of 1 to 31 case-sensitive characters. |
| **logging** | Logs matched packets. | - |
| **rule** | Specifies an ACL6 rule. | - |
| *18-57* | Indicates the protocol number. | The value is an integer ranging from 18 to 57. |
| *59-255* | Indicates the protocol number. | The value is an integer ranging from 59 to 255. |
| *destination-wildcard* | Specifies the wildcard of a destination IPv6 address. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| *source-wildcard* | Specifies the wildcard mask of a source IPv6 address. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |



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



When you configure advanced ACL6 rules for ICMPv6, fragment and icmp6-type cannot be both configured.When you configure advanced ACL6 rules for TCP or UDP, fragment and destination-port or source-port cannot be both configured.If auto is configured when you run the **acl ipv6** command to create an ACL6, you cannot specify a rule ID when creating a rule. The system automatically uses the ACL6 step as the start rule ID, and the subsequent rules are numbered by a step in ascending order.If the auto mode based on the depth-first principle is specified as the matching order for an advanced ACL6 rule group, you cannot specify a rule ID when creating a rule.If rule-id is not specified when you run the **rule** command to create an ACL6, the system automatically assigns an ID to the ACL6 rule. You can run the **display acl ipv6** command to check the rule ID automatically assigned to an ACL6.If name rule-name is not specified when you run the **rule** command to create an ACL6, the system automatically generates a name for the ACL6 in the format of "rule"+"\_"+rule ID. Rule ID is the ID of an ACL6 rule that can be specified using the rule-id parameter or automatically assigned by the system. You can check the automatically generated name of an ACL6 rule through the NMS.You must specify the rule ID when deleting a rule. To check rule IDs, run the **display acl ipv6** command.Before deleting an ACL6 rule, run the **display acl ipv6** command to check whether the ACL6 rule has been applied to other services. Delete the rule only when it is not applied to other services.If the ID of an advanced ACL6 rule to be deleted is not specified, you must specify all parameters in the rule before deleting it.




Example
-------

# Configure an advanced ACL6 whose matching order is config.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 3000
[*HUAWEI-acl6-advance-3000] rule permit tcp source 2001:db8::1 64
[*HUAWEI-acl6-advance-3000] rule deny udp source 2001:db8::1 64

```