rule (User ACL group view)
==========================

rule (User ACL group view)

Function
--------



The **rule** command creates or modifies an ACL rule in the user-defined ACL view.

The **undo rule** command deletes an ACL rule in the user-defined ACL view.



By default, no user-defined ACL rule is created.


Format
------

**rule** [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ [ [ [ **l2-head** ] *rule1* *rulemask1* *offset1-l2* [ *rule2* *rulemask2* *offset2-l2* [ *rule3* *rulemask3* *offset3-l2* [ *rule4* *rulemask4* *offset4-l2* ] ] ] ] | [ **ipv4-head** *rule1* *rulemask1* *offset1-ipv4* [ *rule2* *rulemask2* *offset2-ipv4* [ *rule3* *rulemask3* *offset3-ipv4* [ *rule4* *rulemask4* *offset4-ipv4* ] ] ] ] | [ **l4-head** *rule1* *rulemask1* *offset1-l4* [ *rule2* *rulemask2* *offset2-l4* [ *rule3* *rulemask3* *offset3-l4* [ *rule4* *rulemask4* *offset4-l4* ] ] ] ] ] | [ **time-range** *time-name* ] ] \*

**undo rule** *rule-id* [ **to** *to-rule-id* ]

**undo rule** [ **name** *rule-name* ] { **deny** | **permit** } [ [ [ [ **l2-head** ] *rule1* *rulemask1* *offset1-l2* [ *rule2* *rulemask2* *offset2-l2* [ *rule3* *rulemask3* *offset3-l2* [ *rule4* *rulemask4* *offset4-l2* ] ] ] ] | [ **ipv4-head** *rule1* *rulemask1* *offset1-ipv4* [ *rule2* *rulemask2* *offset2-ipv4* [ *rule3* *rulemask3* *offset3-ipv4* [ *rule4* *rulemask4* *offset4-ipv4* ] ] ] ] | [ **l4-head** *rule1* *rulemask1* *offset1-l4* [ *rule2* *rulemask2* *offset2-l4* [ *rule3* *rulemask3* *offset3-l4* [ *rule4* *rulemask4* *offset4-l4* ] ] ] ] ] | [ **time-range** *time-name* ] ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rule-id* | Specifies the ID of an ACL rule. | The value is an integer ranging from 0 to 4294967294. |
| **name** *rule-name* | Specifies the name of an ACL rule. | The value is a string of 1 to 32 case-sensitive characters that cannot begin with an underscore (\_), spaces not supported. |
| **deny** | Denies packets that match conditions. | - |
| **permit** | Permits packets that match conditions. | - |
| **l2-head** | Indicates that the offset starts from the Layer 2 header. | - |
| *rule1* | Specifies a user-defined rule string. | The value must be a hexadecimal number and start with 0x. The length ranges from 3 to 10 digits. |
| *rulemask1* | Specifies the mask for a user-defined rule string. | The value must be a hexadecimal number and start with 0x. The length ranges from 3 to 10 digits. |
| *offset1-l2* | Specifies an offset that starts from the header. | The value is an integer, ranging from 2 to 114, in bytes. |
| *rule2* | Specifies a user-defined rule string. | The value must be a hexadecimal number and start with 0x. The length ranges from 3 to 10 digits. |
| *rulemask2* | Specifies the mask for a user-defined rule string. | The value must be a hexadecimal number and start with 0x. The length ranges from 3 to 10 digits. |
| *offset2-l2* | Specifies an offset that starts from the header. | The value is an integer, ranging from 2 to 114, in bytes. |
| *rule3* | Specifies a user-defined rule string. | The value must be a hexadecimal number and start with 0x. The length ranges from 3 to 10 digits. |
| *rulemask3* | Specifies the mask for a user-defined rule string. | The value must be a hexadecimal number and start with 0x. The length ranges from 3 to 10 digits. |
| *offset3-l2* | Specifies an offset that starts from the header. | The value is an integer, ranging from 2 to 114, in bytes. |
| *rule4* | Specifies a user-defined rule string. | The value must be a hexadecimal number and start with 0x. The length ranges from 3 to 10 digits. |
| *rulemask4* | Specifies the mask for a user-defined rule string. | The value must be a hexadecimal number and start with 0x. The length ranges from 3 to 10 digits. |
| *offset4-l2* | Specifies an offset that starts from the header. | The value is an integer, ranging from 2 to 114, in bytes. |
| **ipv4-head** | Indicates that the offset starts from the IPv4 header. | - |
| *offset1-ipv4* | Specifies an offset that starts from the header. | The value is an integer, ranging from 0 to 96, in bytes. |
| *offset2-ipv4* | Specifies an offset that starts from the header. | The value is an integer, ranging from 0 to 96, in bytes. |
| *offset3-ipv4* | Specifies an offset that starts from the header. | The value is an integer, ranging from 0 to 96, in bytes. |
| *offset4-ipv4* | Specifies an offset that starts from the header. | The value is an integer, ranging from 0 to 96, in bytes. |
| **l4-head** | Indicates that the offset starts from the Layer 4 header. | - |
| *offset1-l4* | Specifies an offset that starts from the header. | The value is an integer, ranging from 0 to 96, in bytes. |
| *offset2-l4* | Specifies an offset that starts from the header. | The value is an integer, ranging from 0 to 96, in bytes. |
| *offset3-l4* | Specifies an offset that starts from the header. | The value is an integer, ranging from 0 to 96, in bytes. |
| *offset4-l4* | Specifies an offset that starts from the header. | The value is an integer, ranging from 0 to 96, in bytes. |
| **time-range** *time-name* | Specifies a time range during which an ACL rule takes effect.  A time range is configured using the time-range command. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **undo** | Cancel current setting. | - |
| **to** *to-rule-id* | Specifies an end rule ID for user-defined ACL rules to be deleted in batches. to-rule-id must be greater than rule-id. | The value is an integer ranging from 0 to 4294967294. |



Views
-----

User ACL group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After an ACL is created, run the **rule** command to add rules to the ACL.



**Prerequisites**



A user-defined ACL has been created using the **acl** command in the system view.A time range has been configured using the **time-range** command in the system view if you want to specify a validity period when creating a user-defined ACL rule.



**Configuration Impact**

When specifying an ACL rule ID, note the following:

* If a rule with the specified rule ID exists and the new rule is different from the existing rule, the new rule overwrites the existing one.
* If no rule with the specified rule ID exists, a rule with the specified rule ID is created.When an ACL rule ID is not specified and a rule is added, the system automatically allocates an ID to this rule. ACL rules are arranged in ascending order of rule IDs, with the difference between two adjacent rules as an ACL increment.The rule IDs automatically generated by the system start from the ACL increment. For example, if the ACL increment is 5, the rule ID starts from 5; if the ACL increment is 2, the rule ID starts from 2. This allows you to add rules before the first rule.

**Precautions**



If rule-id is not specified when you run the **rule** command to create an ACL, the system automatically assigns an ID to the ACL rule. You can run the **display acl** command to check the rule ID automatically assigned to an ACL.If name rule-name is not specified when you run the **rule** command to create an ACL, the system automatically generates a name for the ACL in the format of "rule"+"\_"+rule ID. Rule ID is the ID of an ACL rule that can be specified using the rule-id parameter or automatically assigned by the system. You can check the automatically generated name of an ACL rule through the NMS.When a rule is being added to a user-defined ACL, by default, the offset starts from the Layer 2 header if you do not specify where an offset starts.The rule IDs automatically generated by the system start from the ACL increment. For example, if the ACL increment is 5, the rule ID starts from 5; if the ACL increment is 2, the rule ID starts from 2. This allows you to add rules before the first rule.




Example
-------

# Create a user-defined ACL numbered 5001. Add a rule to ACL 5001 to permit packets in which the four consecutive bytes starting from the fourteenth byte of the Layer 2 header is 0180C200.
```
<HUAWEI> system-view
[~HUAWEI] acl number 5001
[*HUAWEI-acl-user-5001] rule permit l2-head 0x0180C200 0xFFFFFFFF 14

```