rule (basic ACL view)
=====================

rule (basic ACL view)

Function
--------



The **rule** command creates or modifies an ACL rule in the basic ACL view.

The **undo rule** command deletes an ACL rule in the basic ACL view.



By default, no basic ACL rule is created.


Format
------

**rule** [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } [ **fragment-type** **fragment** | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* | **logging** ] \*

**undo rule** [ **name** *rule-name* ] { **permit** | **deny** } [ **fragment-type** **fragment** | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* | **logging** ] \*

**undo rule** *rule-id* [ **to** *end-rule-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rule-id* | Specifies the ID of an ACL rule. | The value is an integer ranging from 0 to 4294967294. |
| **name** *rule-name* | Specifies the name of an ACL rule. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces or start with an underscore (\_). |
| **permit** | Permits packets that match conditions. | - |
| **deny** | Denies the packets that match the rule. | - |
| **fragment-type** | Matches packets based on the fragment type of the packets. | - |
| **fragment** | Checks fragmented packets. | - |
| **source** | Matches packets based on source IP addresses.  If source is not configured, packets from any source IP address are matched. | - |
| *source-ip-address* | Specifies the source IP address.   * This parameter specifies the source address of a packet when it is used for packet filtering and access control. * This parameter specifies the route prefix when it is used for route filtering. * This parameter specifies the multicast source address or multicast group address when it is used for multicast. | The value is in dotted decimal notation.   * The parameter indicates source of the traffic in most case. * The parameter indicates the route prefix if the ACL application is routing protocol. * The parameter indicates multicast source address or multicast group address if the ACL application is multicast protocol. |
| *source-wildcard* | Specifies the wildcard of a source IP address.  A wildcard mask is a 32-bit number string that indicates which bits of an IP address are checked. Its form is the same as that of an IP address. A source or destination IP address range can be determined by a wildcard mask and an IP address of criteria conditions. If a packet address is within this range, the packet meets the criteria conditions; otherwise, the packet does not. Among bits of wildcard masks, 0 represents "Check corresponding bits", and 1 "Do not check corresponding bits". | The value is in dotted decimal notation.  The wildcard of a source IP address can be 0, equivalent to 0.0.0.0, indicating that the source IP address is a host address.  192.168.1.16 0.0.0.15 indicates that the IP address ranges from 192.168.1.16 to 192.168.1.31.  The wildcard mask 255.255.255.255 indicates all IP addresses. If all bits are set to 1, all 32 bits are not checked. In this case, you can use any to replace it. The wildcard mask 0.0.0.0 indicates that all 32 bits need to be matched.  The wildcard mask and IP subnet mask work in different ways. Among subnet masks, number 1 and 0 decide the network, subnet, or corresponding host IP addresses. |
| **0** | Wildcard bits : 0.0.0.0 ( a host ). | - |
| *src-netmask* | Specifies the mask length of a specified IP address. | The value is an integer ranging from 1 to 32. |
| **any** | Matches packets with any source IP address. | - |
| **time-range** *time-name* | Specifies a time range during which an ACL rule takes effect.  A time range is configured using the time-range command. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces. |
| **vpn-instance** *vpn-instance-name* | Matches packets based on a VPN instance name.  The parameter indicates the L3VPN that the traffic belongs to. If the traffic is from L3VPN, this option must be configured in the ACL. If this option is not configured, it indicates the traffic belongs to the public network rather than L3VPN. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **logging** | Indicates whether to log the matched packets. | - |
| **rule** | Specifies an ACL rule. | - |
| **to** *end-rule-id* | Specifies an end rule ID for ACL rules to be deleted in batches. | The value is an integer ranging from 0 to 4294967294. |



Views
-----

Basic ACL view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After a basic ACL is created, run the **rule** command to add rules to the ACL."rule permit" and "rule permit source any" have the same matching result."rule deny" and "rule deny source any" have the same matching result.Advanced ACL rules with the fragment-type can prevent such attacks by permitting only non-fragmented packets. In normal situations, Maximum Transmission Unit (MTU) is set on networks so that packets cannot be fragmented.



**Prerequisites**



A basic ACL has been created using the **acl** command in the system view.



**Configuration Impact**

When specifying an ACL rule ID, note the following:

* If a rule with a specified rule ID already exists, and the new rule conflicts with the existing one, the conflicting part in the new rule overwrites that in the existing rule.
* If no rule with the specified rule ID exists, a rule with the specified rule ID is created.When an ACL rule ID is not specified and a rule is added, the system automatically allocates an ID to this rule. ACL rules are arranged in ascending order of rule IDs, with the difference between two adjacent rules as an ACL increment.The rule IDs automatically generated by the system start from the ACL increment. For example, if the ACL increment is 5, the rule ID starts from 5; if the ACL increment is 2, the rule ID starts from 2. This allows you to add rules before the first rule.By default, if an ACL is not configured with the fragment-type,
* If only Layer 3 information is configured to the rule, the ACL rules will filter all packets (including the first fragment of a packet, non-first fragments, and non-fragmented packets).
* If both Layer 3 and Layer 4 information is configured to the rule,
  + The ACL filters the first fragment of a packet and non-fragmented packets, as these packets contain Layer 3 and Layer 4 information.
  + Only Layer 3 information about non-first fragments is filtered, as they contain Layer 3 information never Layer 4 information. If Layer 3 information matches the "permit" rule, the non-first fragment is allowed to pass through; if Layer 3 information matches the "deny" rule, continue matching the non-first fragment against the next rule. (Note: this is different to the normal ACL working process.)

**Precautions**



If auto is configured when you run the **acl** command to create an ACL, you cannot specify a rule ID when creating a rule. The system automatically uses the ACL increment as the start rule ID, and the subsequent rules are numbered by an ACL increment in ascending order.You must specify the rule ID when deleting a rule. To check rule IDs, run the **display acl** command.Before deleting an ACL rule, run the **display acl** command to check whether the ACL rule has been applied to other services. Delete the rule only when it is not applied to other services.




Example
-------

# Create a basic ACL numbered 2999 and add a rule to ACL 2999 to match packets with the source IP address 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] acl number 2999
[*HUAWEI-acl4-basic-2999] rule deny source 10.1.1.1 0

```