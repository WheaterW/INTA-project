mld snooping robust-count
=========================

mld snooping robust-count

Function
--------



The **mld snooping robust-count** command configures the robustness variable. The robustness variable decides the number of group-specific Query messages to be sent by the querier.

The **undo mld snooping robust-count** command restores the default robustness variable.



By default, the robustness variable is 2.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping robust-count** *robust-count*

**undo mld snooping robust-count**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **robust-count** *robust-count* | Sets the number of group-specific Query messages to be sent by the querier. | The value is an integer ranging from 2 to 5. |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

This command provides the following functions:

* Adjusts the number of group-specific Query messages to be sent by a querier, preventing messages loss on a network.When receiving an MLD Done message of a multicast group, the device sends group-specific Query messages for robust-count times to check whether there are any other members in this group. Run the **mld snooping query last-member-interval** command to set the interval at which group-specific Query messages are sent.
* Changes the aging time of member interfaces.After receiving a Report messages from a downstream host, the device sets the aging time of the member interface using the following formula: Member interface aging time = Number of group-specific Query messages to be sent x Interval at which general Query messages are sent + Maximum time for the querier to wait for responses from downstream hosts. By default, the device sets the aging time to 130s. Run the **mld snooping query interval** command to set the interval at which general Query messages are sent, and run the **mld snooping query max-response-time** command to set the maximum time for the querier to wait for responses from downstream hosts.After receiving a Done message, the device sets the aging time of the member interface using the following formula: Member interface aging time = Interval at which group-specific Query messages are sent x Number of group-specific Query messages to be sent. By default, the device sets the aging time to 2s. Run the mld-snooping robust-count command to set the number of group-specific Query messages to be sent, and run the **mld snooping query last-member-interval** command to set the interval at which group-specific Query messages are sent.If the querier receives a Report message for the multicast group from another host within the robust-count x lastmember-queryinterval period, it continues to maintain the member interface information for the group. If the querier does not receive a Report message for the multicast group within this period, the querier considers that there is no member of the group on the network segment, and does not maintain the member interface information for the group.

Example
-------

# Configure the querier of VLAN 100 to send five group-specific Query messages.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[*HUAWEI] vlan 100
[*HUAWEI-vlan100] mld snooping robust-count 5

```