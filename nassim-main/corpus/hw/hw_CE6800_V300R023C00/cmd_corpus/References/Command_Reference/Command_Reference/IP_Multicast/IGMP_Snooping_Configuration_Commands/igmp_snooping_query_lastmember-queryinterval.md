igmp snooping query lastmember-queryinterval
============================================

igmp snooping query lastmember-queryinterval

Function
--------



The **igmp snooping query lastmember-queryinterval** command sets the interval at which a querier sends Group-Specific Query messages or Source- and Group-Specific Query messages.

The **undo igmp snooping query lastmember-queryinterval** command restores the interval at which a querier sends Group-Specific Query messages or Source- and Group-Specific Query messages to 1 second.



By default, a querier sends group-specific query messages or source/group-specific query messages at an interval of 1s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**igmp snooping query lastmember-queryinterval** *LastMemQIValue*

**undo igmp snooping query lastmember-queryinterval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *LastMemQIValue* | Specifies the interval at which a querier sends group-specific query messages or source/group-specific query messages. | The value ranges from 1 to 5, in seconds. |



Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The igmp snooping query last-member-interval command has the following functions:

* Sets the interval at which a querier sends group-specific query messages or source/group-specific query messages. If the querier function is enabled, this command is used to set the interval at which the querier sends group-specific messages or source/group-specific query messages. When memberships change frequently on the network, this command can be used to reduce the interval at which the querier sends group-specific query messages or source/group-specific query messages. This ensures that IGMP group-specific query messages or source/group-specific query messages can be rapidly responded to.
* Changes the aging time of member ports. After receiving an IGMP Leave message from a host, a device sets the aging time of the corresponding member port based on the following formula: Aging time of a member port = Interval at which group-specific query messages or source/group-specific query messages are sent x Number of times group-specific query messages or source/group-specific query messages are sent. By default, the aging time is re-set to 2s. The interval at which group-specific query messages or source/group-specific query messages are sent in the formula is set using the igmp snooping query last-member-interval command. The number of times group-specific group query messages or source/group-specific query messages are sent is set using the **igmp snooping robust-count** command. If the querier receives a Report message for the multicast group from another host within the robust-value x lastmember-queryinterval period, it continues to maintain the memberships for the group. Otherwise, the querier considers that there is no member of the group on the network segment, and does not maintain the memberships for the group.

**Prerequisites**

IGMP snooping has been configured globally and in a BD.

**Configuration Impact**

If the igmp snooping query last-member-interval command is run in the same BD view several times, the latest configuration overrides the previous one.

**Precautions**

The aging time configured on a Layer 2 device must be the same as that on its upstream Layer 3 device. Otherwise, multicast data transmission between Layer 2 and Layer 3 networks will be affected.


Example
-------

# Set the interval at which a querier sends group-specific query messages or source/group-specific query messages to 4s in BD 10.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] bridge-domain 10
[*HUAWEI-bd10] igmp snooping query lastmember-queryinterval 4

```