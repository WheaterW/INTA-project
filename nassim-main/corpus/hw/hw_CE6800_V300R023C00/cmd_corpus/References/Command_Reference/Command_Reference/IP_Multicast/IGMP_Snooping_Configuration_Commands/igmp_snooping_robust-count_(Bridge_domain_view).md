igmp snooping robust-count (Bridge domain view)
===============================================

igmp snooping robust-count (Bridge domain view)

Function
--------



The **igmp snooping robust-count** command sets a robustness variable that determines the number of times a querier sends group-specific query messages.

The **undo igmp snooping robust-count** command restores the default setting.



By default, the robustness variable is 2.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**igmp snooping robust-count** *robust-count-value*

**undo igmp snooping robust-count**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *robust-count-value* | Specifies the number of times a querier sends group-specific query messages. | The value ranges from 2 to 5. |



Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

This command has the following functions:

* Defines the number of times a querier sends group-specific query messages, preventing packet loss on a network. When a device receives an IGMP Leave message for a multicast group, it sends group-specific query messages for the number of times defined by robust-count to check whether there are any other members in this group. The interval at which group-specific query messages are sent is set using the **igmp snooping query last-member-interval** command.
* Changes the aging time of member ports. After receiving a Report message from a downstream device, a device sets the aging time of the corresponding member port based on the following formula: Aging time of a member port = Number of times group-specific query messages are sent x Interval at which general query messages are sent + Maximum time for a downstream host to respond to a querier. The default aging time is 130 seconds. The interval at which general query messages are sent is set using the **igmp snooping query interval** command. The maximum time for a downstream host to respond to a querier is set using the **igmp snooping query max-response-time** command. After receiving an IGMP Leave message from a host, a device sets the aging time of the corresponding member port based on the following formula: Aging time of a member port = Interval at which group-specific query messages are sent x Number of times group-specific query messages are sent. By default, the aging time is re-set to 2 seconds. The igmp snooping robust-count command is used to set the number of times group-specific query messages are sent in the preceding formula. The interval at which group-specific query messages are sent is set using the **igmp snooping query last-member-interval** command. If the querier receives a Report message for the multicast group from another host within the robust-value x lastmember-queryinterval period, it continues to maintain the memberships for the group. Otherwise, the querier considers that there is no member of the group on the network segment, and does not maintain the memberships for the group.

**Prerequisites**

IGMP snooping has been configured using the **igmp snooping enable** command.

**Configuration Impact**

If the igmp snooping robust-count command is run in the same view several times, the latest configuration overrides the previous one.

**Precautions**

When the parameter in this command is used as the dynamic aging time of members, the configuration on a Layer 2 device must be the same as that on its upstream Layer 3 device. Otherwise, multicast data transmission between Layer 2 and Layer 3 networks will be affected.


Example
-------

# Set the number of times a querier sends group-specific query messages to 5 in BD 10.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] bridge-domain 10
[*HUAWEI-bd10] igmp snooping robust-count 5

```