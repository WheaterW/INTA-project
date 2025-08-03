mld timer other-querier-present
===============================

mld timer other-querier-present

Function
--------



The **mld timer other-querier-present** command sets a global Keepalive period of other Multicast Listener Discovery (MLD) queriers.

The **undo mld timer other-querier-present** command restores the default value.



By default, if the robustness variable, the interval for sending MLD general query messages, and the maximum response time of MLD Query messages are all of default values, the Keepalive period of other MLD queriers is 255 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld timer other-querier-present** *interval*

**undo mld timer other-querier-present**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the Keepalive period of other MLD queriers. The formula used to calculate the Keepalive period of other MLD queriers is: Keepalive period of other MLD queriers = Robustness variable x Interval for sending MLD general query messages + 1/2 x maximum response time of MLD query messages. | The value is an integer ranging from 60 to 300, in seconds. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If multiple multicast Routers are connected to a network segment, one of the Routers is selected as the querier to periodically send Query messages to the network segment. If the non-queriers do not receive any Query message from the querier within the Keepalive period of other MLD queriers, they consider the querier invalid, and automatically trigger a new round of the querier election. After the election, the Router with the lowest IPv6 link-local address on the shared network segment acts as the querier.If the Keepalive period of other MLD queriers is shorter than the interval for sending MLD general query messages, the querier election is performed frequently.


Example
-------

# Set the timeout period of an MLD querier to 200 seconds on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] mld timer other-querier-present 200

```