rule (ARP ACL view)
===================

rule (ARP ACL view)

Function
--------



The **rule** command creates or modifies an ACL rule in the ARP-based ACL view.

The **undo rule** command deletes an ACL rule in the ARP-based ACL view.



By default, no ARP-based ACL rule is created.


Format
------

**rule** [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } [ **request** ] [ **source-ip** { *source-ip-address* { *source-wildcard* | **0** | *source-netmask* } | **any** } | **source-mac** { *source-mac-address* [ *source-mac-mask* ] | **any** } | **time-range** *time-name* ] \*

**rule** [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } **reply** [ **source-ip** { *source-ip-address* { *source-wildcard* | **0** | *source-netmask* } | **any** } | **destination-ip** { *destination-ip-address* { *destination-wildcard* | **0** | *destination-netmask* } | **any** } | **source-mac** { *source-mac-address* [ *source-mac-mask* ] | **any** } | **destination-mac** { *destination-mac-address* [ *destination-mac-mask* ] | **any** } | **time-range** *time-name* ] \*

**undo rule** [ **name** *rule-name* ] { **permit** | **deny** } [ **request** ] [ **source-ip** { *source-ip-address* { *source-wildcard* | **0** | *source-netmask* } | **any** } | **source-mac** { *source-mac-address* [ *source-mac-mask* ] | **any** } | **time-range** *time-name* ] \*

**undo rule** [ **name** *rule-name* ] { **permit** | **deny** } **reply** [ **source-ip** { *source-ip-address* { *source-wildcard* | **0** | *source-netmask* } | **any** } | **destination-ip** { *destination-ip-address* { *destination-wildcard* | **0** | *destination-netmask* } | **any** } | **source-mac** { *source-mac-address* [ *source-mac-mask* ] | **any** } | **destination-mac** { *destination-mac-address* [ *destination-mac-mask* ] | **any** } | **time-range** *time-name* ] \*

**undo rule** *rule-id* [ **to** *end-rule-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rule-id* | Specifies the ID of an ACL rule. | The value is an integer ranging from 0 to 4294967294. |
| **name** *rule-name* | Specifies the name of an ACL rule. | The value is a string of 1 to 32 case-sensitive characters that cannot begin with an underscore (\_), spaces not supported. |
| **permit** | Permits packets that match conditions. | - |
| **deny** | Denies packets that match conditions. | - |
| **request** | Matches ARP request messages. | - |
| **source-ip** | Matches ARP packets with a specified source IP address.  If no source IP address is specified, an ACL takes effect for ARP packets with any source IP address. | - |
| *source-ip-address* | Specifies a source IP address. | The value is in dotted decimal notation. |
| *source-wildcard* | Specifies a source IP address wildcard mask. | The value is in dotted decimal notation.  The wildcard of a source IP address can be 0, equivalent to 0.0.0.0, indicating that the source IP address is a host address. |
| **0** | Wildcard bits: 0.0.0.0 (a host). | - |
| *source-netmask* | Specifies the mask length of a source IP address. | The value is an integer ranging from 1 to 32. |
| **any** | Matches ARP packets with any IP address or MAC address. | - |
| **source-mac** | Matches ARP packets with a specified source MAC address.  If no source MAC address is specified, an ACL takes effect for ARP packets with any source MAC address. | - |
| *source-mac-address* | Specifies a source MAC address. | The value is in the format of H-H-H. Each H is a 4-digit hexadecimal number. |
| *source-mac-mask* | Specifies a source MAC address mask. | The value is in the format of H-H-H. Each H is a 4-digit hexadecimal number. |
| **time-range** *time-name* | Specifies a time range during which an ACL rule takes effect.  A time range is configured using the time-range command. | The value is an integer ranging from 1 to 32. |
| **reply** | Matches ARP reply messages. | - |
| **destination-ip** | Matches ARP packets with a specified destination IP address.  This parameter takes effect only for ARP reply messages. If no destination IP address is specified, an ACL takes effect for ARP packet with any destination IP address. | - |
| *destination-ip-address* | Specifies a destination IP address. | The value is in dotted decimal notation. |
| *destination-wildcard* | Specifies a destination IP address wildcard. | The value is in dotted decimal notation.  The wildcard of a destination IP address can be 0, equivalent to 0.0.0.0, indicating that the destination IP address is a host address. |
| *destination-netmask* | Specifies the length of a destination IP address mask. | The value is an integer ranging from 1 to 32. |
| **destination-mac** | Matches ARP packets with a specified destination MAC address.  This parameter takes effect only for ARP reply messages. If no destination MAC address is specified, an ACL takes effect for ARP packets with any destination MAC address. | - |
| *destination-mac-address* | Specifies a destination MAC address. | The value is in the format of H-H-H. Each H is a 4-digit hexadecimal number. |
| *destination-mac-mask* | Specifies a destination MAC address mask. | The value is in the format of H-H-H. Each H is a 4-digit hexadecimal number. |
| **to** *end-rule-id* | Specifies an end rule ID for ARP-based ACL rules to be deleted in batches. end-rule-id must be greater than rule-id. | The value is an integer ranging from 0 to 4294967294. |



Views
-----

ARP ACL view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



An ARP-based ACL defines rules for packet filtering based on the source or destination IP or MAC addresses of ARP packets, reducing the impact of ARP attack packets on network devices. To configure an ARP-based ACL rule, run the rule command in the ARP-based ACL view.



**Prerequisites**



An ARP-based ACL has been created using the **acl** command in the system view.A time range has been configured using the **time-range** command in the system view if you want to specify a validity period when creating an ARP-based ACL rule.



**Configuration Impact**

When specifying an ACL rule ID, note the following:

* If a rule with the specified rule ID exists and the new rule is different from the existing rule, the new rule overwrites the existing one.
* If no rule with the specified rule ID exists, a rule with the specified rule ID is created.When an ACL rule ID is not specified and a rule is added, the system automatically allocates an ID to this rule. ACL rules are arranged in ascending order of rule IDs, with the difference between two adjacent rules as an ACL increment.The rule IDs automatically generated by the system start from the ACL increment. For example, if the ACL increment is 5, the rule ID starts from 5; if the ACL increment is 2, the rule ID starts from 2. This allows you to add rules before the first rule.

**Precautions**



If rule-id is not specified when you run the rule command to create an ACL, the system automatically assigns an ID to the ACL rule. You can run the **display acl** command to check the rule ID automatically assigned to an ACL.If name rule-name is not specified when you run the rule command to create an ACL, the system automatically generates a name for the ACL in the format of "rule"+"\_"+rule ID. Rule ID is the ID of an ACL rule that can be specified using the rule-id parameter or automatically assigned by the system. You can check the automatically generated name of an ACL rule through the NMS.You must specify the rule ID when deleting a rule. To check rule IDs, run the **display acl** command. Before deleting an ACL rule, run the **display acl** command to check whether the ACL rule has been applied to other services. Delete the rule only when it is not applied to other services.




Example
-------

# Create an ARP-based ACL numbered 23000 and create a rule to match ARP reply messages with the destination MAC address 0-0-1 and source MAC address 0-0-2.
```
<HUAWEI> system-view
[~HUAWEI] acl number 23000
[*HUAWEI-acl-arp-23000] rule permit reply destination-mac 0-0-1 source-mac 0-0-2

```