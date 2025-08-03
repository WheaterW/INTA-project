mld snooping query max-response-time
====================================

mld snooping query max-response-time

Function
--------



The **mld snooping query max-response-time** command sets the maximum time for a querier to wait for responses from downstream hosts.

The **undo mld snooping query max-response-time** restores the default value.



By default, the maximum time for a querier to wait for responses from downstream hosts is 10s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping query max-response-time** *max-response-time*

**undo mld snooping query max-response-time**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *max-response-time* | Sets the maximum time for a querier to wait for responses from downstream hosts. | The value is an integer ranging from 1 to 25, in seconds. |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The mld snooping query max-response-time command provides the following functions:

* Sets the maximum time for a querier to wait for responses from downstream hosts.After the querier function is enabled, if you want hosts to rapidly respond to the querier, set a smaller value for max-response-time; if you want to prevent traffic congestions caused by frequently sent response messages, set a larger value for max-response-time.Ensure that max-response-time is smaller than the interval at which general Query messages are sent; otherwise, multicast group member entries may be deleted incorrectly.
* Adjusts the aging time of member interfaces.After receiving an MLD Report message from a host, a device sets the aging time of the corresponding member interface based on the following formula: Member interface aging time = Number of group-specific Query messages to be sent x Interval at which general Query messages are sent + Maximum time for a querier to wait for responses from downstream hosts. By default, the device sets the aging time to 130s. To adjust the aging time, run the mld snooping query max-response-time command to set the maximum time for a querier to wait for responses from downstream hosts, run the **mld snooping robust-count** command to set the number of group-specific Query messages to be sent, and run the **mld snooping query interval** command to set the sending interval of general Query messages.

Example
-------

# Set the maximum time for a querier in VLAN 100 to wait for responses from downstream hosts to 20s.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[*HUAWEI] vlan 100
[*HUAWEI-vlan100] mld snooping query max-response-time 20

```