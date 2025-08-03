mld snooping query interval
===========================

mld snooping query interval

Function
--------



The **mld snooping query interval** command sets an interval at which the querier sends general Query messages.

The **undo mld snooping query interval** command restores the interval.



The default interval is 125s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping query interval** *query-interval*

**undo mld snooping query interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *query-interval* | Sets an interval at which the querier sends general Query messages. | The value is an integer ranging from 1 to 65535, in seconds. |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The mld snooping query interval command provides the following functions:

* Sets an interval at which the querier sends general Query messages.After the querier function is enabled and an interval is set using the mld snooping query interval command, the querier sends general Query messages at the configured interval to maintain group member information. The shorter the interval is, the more sensitive the device is and the more bandwidth and system resources are occupied.The interval for the querier to send general Query messages must be greater than the maximum time for the querier to wait for responses from hosts. Otherwise, multicast group members may be deleted incorrectly.
* Adjusts the aging time of member interfaces.After receiving a Report message from a downstream host, the device sets the aging time of the member interface using the following formula: Member interface aging time = Number of group-specific Query messages to be sent x Interval at which general Query messages are sent + Maximum time for the querier to wait for responses from downstream hosts. By default, the device sets the aging time to 130s. Run the mld snooping query interval command to set an interval at which general Query messages are sent, run the **mld snooping robust-count** command to set the number of group-specific Query messages to be sent, and run the **mld snooping query max-response-time** command to set the maximum time that the querier waits for responses from downstream hosts.

Example
-------

# Configure the querier in VLAN 100 to send general Query messages at an interval of 100s.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[*HUAWEI] vlan 100
[*HUAWEI-vlan 100] mld snooping query interval 100

```