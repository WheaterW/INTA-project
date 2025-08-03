mld snooping query last-member-interval
=======================================

mld snooping query last-member-interval

Function
--------



The **mld snooping query last-member-interval** command sets an interval at which a querier sends group-specific or source-and group-specific Query messages.

The **undo mld snooping query last-member-interval** command restores the default interval.



By default, a querier sends group-specific or source-and group-specific Query messages at an interval of 1s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping query last-member-interval** *lastmember-queryinterval*

**undo mld snooping query last-member-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *lastmember-queryinterval* | Sets an interval at which a querier sends group-specific or source-and group-specific Query messages. | The value is an integer ranging from 1 to 5, in seconds. |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The mld snooping query last-member-interval command provides the following functions:

* Sets an interval at which a querier sends group-specific or source-and group-specific multicast group Query messages.After the querier function is enabled, run this command to set a shorter interval if multicast group members change frequently. The device can then rapidly respond to users' requests.
* Adjusts the aging time of member interfaces.After receiving an MLD Snooping Done message from a host, a device sets the aging time of the corresponding member interface based on the following formula: Member interface aging time = Interval at which group-specific or source-and group-specific Query messages are sent x Number group-specific or source-and group-specific multicast group Query messages to be sent. By default, the device sets the aging time to 2s. To adjust the aging time, run the mld snooping query last-member-interval command to set the message sending interval, and run the **mld snooping robust-count** command to set the number of group-specific or source-and group-specific multicast group Query messages to be sent.If the querier receives a Report message for the multicast group from another host within the robust-count x lastmember-queryinterval period, it continues to maintain the member interface information for the group. Otherwise, the querier considers that there is no member of the group on the network segment, and does not maintain the member interface information for the group any more.

Example
-------

# Configure the querier in VLAN 2 to send group-specific or source-and group-specific Query messages at an interval of 2s.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[*HUAWEI] vlan 2
[*HUAWEI-vlan2] mld snooping query last-member-interval 2

```