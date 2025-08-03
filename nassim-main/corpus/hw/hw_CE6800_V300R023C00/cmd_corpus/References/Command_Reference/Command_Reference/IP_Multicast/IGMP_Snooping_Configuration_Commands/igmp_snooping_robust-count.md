igmp snooping robust-count
==========================

igmp snooping robust-count

Function
--------



The **igmp snooping robust-count** command sets a robustness variable that determines the number of times a querier sends group-specific query messages.

The **undo igmp snooping robust-count** command restores the default setting.



By default, the robustness variable is 2.


Format
------

**igmp snooping robust-count** *robust-count-value*

**undo igmp snooping robust-count**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *robust-count-value* | Specifies the IGMP robustness variable. | The value is an integer that ranges from 2 to 5. |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

This command has the following functions:

* Defines the number of times a querier sends group-specific query messages, preventing packet loss on a network. When a device receives an IGMP Leave message for a multicast group, it sends group-specific query messages for the number of times defined by robust-count to check whether there are any other members in this group. The interval at which group-specific query messages are sent is set using the **igmp snooping query last-member-interval** command.
* Changes the aging time of member ports. After receiving a Report message from a downstream device, a device sets the aging time of the corresponding member port based on the following formula: Aging time of a member port = Number of times group-specific query messages are sent x Interval at which general query messages are sent + Maximum time for a downstream host to respond to a querier. The default aging time is 130 seconds. The interval at which general query messages are sent is set using the **igmp snooping query interval** command. The maximum time for a downstream host to respond to a querier is set using the igmp snooping query max-response-time command.After receiving an IGMP Leave message from a host, a device sets the aging time of the corresponding member port based on the following formula: Aging time of a member port = Interval at which group-specific query messages are sent x Number of times group-specific query messages are sent. By default, the aging time is re-set to 2 seconds. The igmp-snooping robust-count command is used to set the number of times group-specific query messages are sent in the preceding formula. The interval at which group-specific query messages are sent is set using the **igmp snooping query last-member-interval** command. If the querier receives a Report message for the multicast group from another host within the robust-value x lastmember-queryinterval period, it continues to maintain the memberships for the group. Otherwise, the querier considers that there is no member of the group on the network segment, and does not maintain the memberships for the group.

**Prerequisites**

IGMP snooping has been configured using the **igmp snooping enable** command.

**Configuration Impact**

If the igmp snooping robust-count command is run in the same view several times, the latest configuration overrides the previous one.

**Precautions**

When the igmp snooping robust-count command is used to set the aging time for member ports, the settings of parameters in this command must be consistent on a Layer 2 device and its upstream Layer 3 device. Otherwise, multicast data transmission between Layer 2 and Layer 3 networks will be interrupted.The number of times a querier sends group-specific query messages in a VLAN fails to be set in any of the following situations:

* A Dot1q termination sub-interface has been added to the VLAN.

Example
-------

# Set the number of times a querier sends group-specific query messages to 5 in VLAN 2.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] vlan 2
[*HUAWEI-vlan2] igmp snooping robust-count 5

```