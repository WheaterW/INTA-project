mld robust-count
================

mld robust-count

Function
--------



The **mld robust-count** command sets a robustness variable for a Multicast Listener Discovery (MLD) querier.

The **undo mld robust-count** command restores the default value.



By default, the robustness variable of an MLD querier is 2.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld robust-count** *robust-value*

**undo mld robust-count**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *robust-value* | Specifies the robustness variable of an MLD querier. | The value is an integer ranging from 2 to 5. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The robustness variable defines the following:

* Number of times for sending general query messages when the MLD querier starts
* Number of times the MLD querier sends group-specific query messages after receiving a Leave messageA host running MLD sends a Leave message when leaving a group. If the querier receives this message, it sends MLD last-listener query messages based on the robustness variable Robust\_Count at the interval specified by mld lastlistener-queryinterval. If the interval is not set, the default value 1 second is used.If another host receives an MLD Last Listener Query message from the MLD querier and wants to join the group, the host sends an MLD Membership Report message within the maximum response time specified in the message. If the MLD querier receives MLD Report messages from other hosts within the period of (Interval x Robust\_Count), the querier continues to maintain group memberships. If no, the device considers that the group times out and stops maintaining group members.If the robustness variable is set in both the interface view and the MLD view, the robustness variable set in the interface view takes precedence.

Example
-------

# Set the robustness variable of 100GE1/0/1 to 3.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] mld robust-count 3

```