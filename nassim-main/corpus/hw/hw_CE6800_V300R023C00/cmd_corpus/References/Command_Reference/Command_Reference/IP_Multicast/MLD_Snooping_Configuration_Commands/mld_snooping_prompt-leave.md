mld snooping prompt-leave
=========================

mld snooping prompt-leave

Function
--------



The **mld snooping prompt-leave** command enables prompt leave.

The **undo mld snooping prompt-leave** command disables prompt leave.



By default, prompt leave is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping prompt-leave** [ **group-policy** { *acl6-number* | **acl6-name** *acl6-name* } ]

**undo mld snooping prompt-leave**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **group-policy** | Configures a group policy to enable prompt leave for member interfaces of a specified or all multicast groups. | - |
| *acl6-number* | Specifies the number of an ACL6. | The value is an integer ranging from 2000 to 3999. |
| **acl6-name** *acl6-name* | Specifies the name of a named ACL6. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After receiving an MLD Done message for a multicast group from a host, a device enabled with prompt leave directly deletes the forwarding entry of the multicast group, without sending group-specific Query messages. If an interface is connected to only one host, the prompt leave mechanism can be used to shorten the response delay and release bandwidth resources in a timely manner.If group-policy is not set, prompt leave will take effect for all multicast groups.If group-policy is set, prompt leave will take effect for groups of which the MLD Done messages meet the permit clause of the ACL6.

* If a multicast group meets the permit clause of the specified ACL6, the device deletes the member interface of the group immediately after receiving an MLD Done message of this group and notifies the upstream device of the user leave event.
* If a multicast group does not meet the permit clause of the specified ACL6, the device notifies the upstream device of a user leave event after receiving an MLD Done message of a group. The upstream device can then send a group-specific Query message to learn whether members exist in the group.

**Prerequisites**

MLD snooping has been enabled globally and in the VLAN view.Rules have been configured in the specified ACL6. By default, the ACL6 rule in which the action is permit applies to all multicast groups. To enable prompt leave for a multicast group, you need to run the rule (ACL6 view) deny source any command.


Example
-------

# Enable prompt leave for VLAN 2 member interfaces of the multicast group FF18::1.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 2008
[*HUAWEI-acl6-basic-2008] rule permit source ff18::1 64
[*HUAWEI-acl6-basic-2008] quit
[*HUAWEI] mld snooping enable
[*HUAWEI] vlan 2
[*HUAWEI-vlan2] mld snooping prompt-leave group-policy 2008

```