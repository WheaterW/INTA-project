igmp snooping query last-member-interval
========================================

igmp snooping query last-member-interval

Function
--------



The **igmp snooping query last-member-interval** command sets the interval at which a querier sends group-specific query messages or source/group-specific query messages.

The **undo igmp snooping query last-member-interval** command restores the default setting.



By default, a querier sends group-specific query messages or source/group-specific query messages at an interval of 1s.


Format
------

**igmp snooping query last-member-interval** *LastMemQIValue*

**undo igmp snooping query last-member-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *LastMemQIValue* | Specifies the interval at which a querier sends group-specific query messages or source/group-specific query messages. | The value ranges from 1 to 5, in seconds. |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The igmp snooping query last-member-interval command has the following functions:

* Sets the interval at which a querier sends group-specific query messages or source/group-specific query messages.If the querier function is enabled, this command is used to set the interval at which the querier sends group-specific messages or source/group-specific query messages. When memberships change frequently on the network, this command can be used to reduce the interval at which the querier sends group-specific query messages or source/group-specific query messages. This ensures that IGMP group-specific query messages or source/group-specific query messages can be rapidly responded to.
* Changes the aging time of member ports.After receiving an IGMP Leave message from a host, a device sets the aging time of the corresponding member port based on the following formula: Aging time of a member port = Interval at which group-specific query messages or source/group-specific query messages are sent x Number of times group-specific query messages or source/group-specific query messages are sent. By default, the aging time is re-set to 2s. The interval at which group-specific query messages or source/group-specific query messages are sent in the formula is set using the igmp snooping query last-member-interval command. The number of times group-specific group query messages or source/group-specific query messages are sent is set using the **igmp snooping robust-count** command.If the querier receives a Report message for the multicast group from another host within the robust-value x lastmember-queryinterval period, it continues to maintain the memberships for the group. Otherwise, the querier considers that there is no member of the group on the network segment, and does not maintain the memberships for the group.

**Prerequisites**

IGMP snooping has been configured globally and in a VLAN.

**Configuration Impact**

If the igmp snooping query last-member-interval command is run in the same VLANview several times, the latest configuration overrides the previous one.

**Precautions**

When the igmp snooping query last-member-interval command is used to set the aging time of member ports, the settings of parameters in this command must be consistent on a Layer 2 device and its upstream Layer 3 device; otherwise, multicast data transmission between Layer 2 and Layer 3 networks will be interrupted.The interval at which a querier sends group-specific query messages or source/group-specific query messages in a VLAN fails to be set in the following situation:

* A dot1q termination sub-interface has been added to the VLAN.

Example
-------

# Set the interval at which a querier sends group-specific query messages or source/group-specific query messages to 2s in VLAN 2.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] vlan 2
[*HUAWEI-vlan2] igmp snooping enable
[*HUAWEI-vlan2] igmp snooping query last-member-interval 2

```