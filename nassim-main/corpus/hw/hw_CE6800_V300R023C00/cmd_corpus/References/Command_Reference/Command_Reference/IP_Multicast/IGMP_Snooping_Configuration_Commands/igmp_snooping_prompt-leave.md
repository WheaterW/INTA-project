igmp snooping prompt-leave
==========================

igmp snooping prompt-leave

Function
--------



The **igmp snooping prompt-leave** command enables member ports to promptly leave related multicast groups.

The **undo igmp snooping prompt-leave** command restores the default configuration.



By default, a member port is not allowed to promptly leave a multicast group.


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

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After receiving an IGMP Leave message for a multicast group from a host, a device enabled with prompt leave directly deletes the forwarding entry of the multicast group, without sending group-specific query messages. When an interface is connected to only one host, the prompt leave mechanism can be used to shorten the response delay and release bandwidth resources in a timely manner.If group-policy or group-policy acl-name is not set in the igmp snooping prompt-leave command, prompt leave will take effect for all multicast groups.If group-policy or group-policy acl-name is set in this command, the configured ACL will be used to filter Leave messages received in the VLAN.

* When a member port of a device receives a Leave message and the group address of the Leave message is within the range allowed by the ACL, the device will immediately delete the member port and notify the upstream device of the Leave event.
* When a member port of a device receives a Leave message and the group address of the Leave message is beyond the range allowed by the ACL, the device will send a group-specific query message.

**Prerequisites**

IGMP snooping is enabled globally and in a VLAN.Rules have been configured for a specified basic ACL. By default, the ACL rule in which the action is permit is applicable to all multicast groups. To enable prompt leave for a multicast group, you also need to run the rule (basic ACL view) deny source any or rule (advanced ACL view) deny source any command.

**Configuration Impact**

Running the igmp snooping prompt-leave command on an interface connected to multiple user hosts is not recommended. If this command is run on the interface, the leave of one user host will cause other use hosts in the group to fail to receive multicast data.If the igmp snooping prompt-leave command is run several times, the latest configuration overrides the previous one.

**Precautions**

The querier function fails to be run in a VLAN in any of the following situations:

* A Dot1q termination sub-interface has been added to the VLAN.

Example
-------

# Allow member ports in VLAN 2 to promptly leave multicast group 225.1.1.123.
```
<HUAWEI> system-view
[~HUAWEI] acl number 2008
[*HUAWEI-acl-basic-2008] rule permit source 225.1.1.123 0
[*HUAWEI-acl-basic-2008] quit
[*HUAWEI] igmp snooping enable
[*HUAWEI] vlan 2
[*HUAWEI-vlan2] igmp snooping prompt-leave group-policy 2008

```