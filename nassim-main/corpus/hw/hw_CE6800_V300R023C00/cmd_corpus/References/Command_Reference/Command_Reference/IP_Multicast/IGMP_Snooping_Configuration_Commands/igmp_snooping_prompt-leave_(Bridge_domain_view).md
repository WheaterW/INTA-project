igmp snooping prompt-leave (Bridge domain view)
===============================================

igmp snooping prompt-leave (Bridge domain view)

Function
--------



The **igmp snooping prompt-leave** command enables member ports to promptly leave related multicast groups.

The **undo igmp snooping prompt-leave** command restores the default configuration.



By default, a member port is not allowed to promptly leave a multicast group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**igmp snooping prompt-leave** [ **group-policy** { *acl-number* | **acl-name** *acl-name* } ]

**undo igmp snooping prompt-leave**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **group-policy** | Specifies a multicast group policy for prompt leave. The policy specifies the multicast groups that member ports can promptly leave. | - |
| *acl-number* | Specifies the number of a basic ACL. | The value is an integer ranging from 2000 to 3999. |
| **acl-name** *acl-name* | Specifies the name of a named ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |



Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After receiving an IGMP Leave message for a multicast group from a host, a device enabled with prompt leave directly deletes the forwarding entry of the multicast group, without sending group-specific query messages. When an interface is connected to only one host, the prompt leave mechanism can be used to shorten the response delay and release bandwidth resources in a timely manner.If group-policy or group-policy acl-name is not set in the igmp snooping prompt-leave command, prompt leave will take effect for all multicast groups.If group-policy or group-policy acl-name is set in this command, the configured ACL will be used to filter Leave messages received in the BD.

* When a member port of a device receives a Leave message and the group address of the Leave message is within the range allowed by the ACL, the device will immediately delete the member port and notify the upstream device of the Leave event.
* When a member port of a device receives a Leave message and the group address of the Leave message is beyond the range allowed by the ACL, the device will send a group-specific query message.

**Prerequisites**

IGMP snooping is enabled globally and in a BD.Rules have been configured for a specified basic ACL. By default, the ACL rule in which the action is permit is applicable to all multicast groups. To enable prompt leave for a multicast group, you also need to run the rule (basic ACL view) deny source any or rule (advanced ACL view) deny source any command.

**Configuration Impact**

Do not enable the prompt leave function on an interface connected to multiple users. If a user leaves a multicast group, the other users in the multicast group cannot receive multicast data.If this command is run more than once, the latest configuration overrides the previous one.


Example
-------

# Allow member ports in BD 10 to promptly leave multicast group 225.1.1.123.
```
<HUAWEI> system-view
[~HUAWEI] acl number 2008
[*HUAWEI-acl-basic-2008] rule permit source 225.1.1.123 0
[*HUAWEI-acl-basic-2008] quit
[*HUAWEI] igmp snooping enable
[*HUAWEI] bridge-domain 10
[*HUAWEI-bd10] igmp snooping prompt-leave group-policy 2008

```