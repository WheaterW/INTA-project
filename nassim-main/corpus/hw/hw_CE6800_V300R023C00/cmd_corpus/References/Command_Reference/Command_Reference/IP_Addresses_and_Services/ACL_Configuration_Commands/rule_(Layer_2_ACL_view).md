rule (Layer 2 ACL view)
=======================

rule (Layer 2 ACL view)

Function
--------



The **rule** command creates or modifies an ACL rule in the Layer 2 ACL view.

The **undo rule** command deletes an ACL rule in the Layer 2 ACL view.



By default, no Layer 2 ACL rule is created.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**undo rule** *rule-id* [ **to** *end-rule-id* ]

For CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE6885-LL (low latency mode), CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ:

**rule** [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } [ [ **ether-ii** | **snap** ] | [ **type** { *type* | **arp** | **ip** | **ipv6** | **mpls** | **rarp** } [ *type-mask* ] ] | **source-mac** *source-mac* [ *source-mac-mask* ] | **destination-mac** *dest-mac* [ *dest-mac-mask* ] | **vlan** *vlan-id* [ *vlan-mask* ] | **8021p** *8021p* | **inner-vlan** *inner-vlan-id* [ *inner-vlan-mask* ] | **inner-8021p** *cvlan-8021p* | **double-tag** | **time-range** *time-name* ] \*

**undo rule** [ **name** *rule-name* ] { **permit** | **deny** } [ [ **ether-ii** | **snap** ] | [ **type** { *type* | **arp** | **ip** | **ipv6** | **mpls** | **rarp** } [ *type-mask* ] ] | **source-mac** *source-mac* [ *source-mac-mask* ] | **destination-mac** *dest-mac* [ *dest-mac-mask* ] | **vlan** *vlan-id* [ *vlan-mask* ] | **8021p** *8021p* | **inner-vlan** *inner-vlan-id* [ *inner-vlan-mask* ] | **inner-8021p** *cvlan-8021p* | **double-tag** | **time-range** *time-name* ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rule-id* | Specifies the ID of an ACL rule. | The value is an integer ranging from 0 to 4294967294. |
| **name** *rule-name* | Specifies the name of an ACL rule. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces or begin with an underscore (\_). |
| **permit** | Permits packets that match conditions. | - |
| **deny** | Denies packets that match conditions. | - |
| **ether-ii** | Indicates that the encapsulation format of matched packets is Ethernet II. | - |
| **snap** | Matches the SNAP encapsulation format of packets. | - |
| **type** *type* | Matches packets based on Ethernet frame protocol types.  If type is not specified, all Ethernet frames are matched. | The value must be a hexadecimal number and start with 0x. The length ranges from 3 to 6 digits.   * If the value of type is greater than 0x600, this field indicates an upper-layer protocol of Ethernet II frames.   + 0x0800: The upper-layer protocol is IPv4.   + 0x0806: The upper-layer protocol is ARP.   + 0x0835: The upper-layer protocol is RARP. * If the value of type is less than 0x600, this field indicates the length of IEEE 802.3 frames. |
| **arp** | Indicates the address resolution protocol. | - |
| **ip** | Indicates any IP protocol. | - |
| **ipv6** | Indicates any IPv6 protocol. | - |
| **mpls** | Indicates the Multiprotocol Label Switching (MPLS). | - |
| **rarp** | Indicates the Inverse Address Resolution Protocol (InARP). | - |
| *type-mask* | Specifies the mask for an Ethernet frame protocol. | The value is a hexadecimal number and starts with 0x. The length ranges from 3 to 6 digits. The type and type-mask parameters together identify the value range of the field. For example, to match all IEEE 802.3 frames (with the value of type less than 0x600), two commands are required: rule { permit | deny } type 0x0000 0xFc00 and rule { permit | deny } type 0x0400 0xFe00. To match IPv4 traffic, run the rule { permit | deny } type 0x0800 0xFFFF command. |
| **source-mac** *source-mac* | Specifies a source MAC address. | The value is in the format of H-H-H, in which H is a hexadecimal number of 1 to 4 digits. |
| *source-mac-mask* | Specifies the mask for a source MAC address. | The value is in the format of H-H-H, in which H is a hexadecimal number of 1 to 4 digits. |
| **destination-mac** *dest-mac* | Specifies a destination MAC address. | The value is in the format of H-H-H, in which H is a hexadecimal number of 1 to 4 digits. |
| *dest-mac-mask* | Specifies the destination MAC address mask of ARP packets. | The value is in H-H-H format. Each H represents four hexadecimal digits. |
| **vlan** *vlan-id* | Specifies an outer VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer in the range 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| *vlan-mask* | Specifies the mask for an outer VLAN ID. | The value is a 12-digit hexadecimal number. |
| **8021p** *8021p* | Specifies the 802.1p priority in an outer VLAN tag. | The value is an integer ranging from 0 to 7. |
| **inner-vlan** *inner-vlan-id* | Specifies an inner VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer in the range 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| *inner-vlan-mask* | Specifies the mask for an inner VLAN ID. | The value is a 12-digit hexadecimal number. |
| **inner-8021p** *cvlan-8021p* | Specifies the 802.1p priority in an inner VLAN tag. | The value is an integer ranging from 0 to 7. |
| **double-tag** | Matches double-tagged packets. | - |
| **time-range** *time-name* | Specifies a time range during which an ACL rule takes effect.  The time range is defined by the time-range time-range-name command. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **undo** | Cancels the current setting. | - |
| **to** *end-rule-id* | Specifies the end ID of Layer 2 ACL rules. end-rule-id must be greater than rule-id. | The value is an integer ranging from 0 to 4294967294. |



Views
-----

Layer 2 ACL view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a Layer 2 ACL is created, run the **rule** command to add rules to the ACL.

**Prerequisites**

A Layer 2 ACL has been created using the **acl** command in the system view. A time range has been configured using the **time-range** command in the system view if you want to specify a validity period when creating a Layer 2 ACL rule.

**Configuration Impact**

When specifying an ACL rule ID, note the following:

* If a rule with a specified rule ID already exists, and the new rule conflicts with the existing one, the conflicting part in the new rule overwrites that in the existing rule.
* If no rule with the specified rule ID exists, a rule with the specified rule ID is created.When an ACL rule ID is not specified and a rule is added, the system automatically allocates an ID to this rule. ACL rules are arranged in ascending order of rule IDs, with the difference between two adjacent rules as an ACL increment.The rule IDs automatically generated by the system start from the ACL increment. For example, if the ACL increment is 5, the rule ID starts from 5; if the ACL increment is 2, the rule ID starts from 2. This allows you to add rules before the first rule.

**Precautions**

If auto is configured when you run the **acl** command to create an ACL, you cannot specify a rule ID when creating a rule. The system automatically uses the ACL increment as the start rule ID, and the subsequent rules are numbered by an ACL increment in ascending order.You must specify the rule ID when deleting a rule. To check rule IDs, run the **display acl** command.Before deleting an ACL rule, run the **display acl** command to check whether the ACL rule has been applied to other services. Delete the rule only when it is not applied to other services.


Example
-------

# Create a Layer 2 ACL numbered 4999 and add a rule to ACL 4999 to match packets with the destination MAC address 0-0-1, source MAC address 0-0-2, and Layer 2 protocol type value 0x0800.
```
<HUAWEI> system-view
[~HUAWEI] acl number 4999
[*HUAWEI-acl-L2-4999] rule permit destination-mac 0-0-1 source-mac 0-0-2 type 0x0800

```