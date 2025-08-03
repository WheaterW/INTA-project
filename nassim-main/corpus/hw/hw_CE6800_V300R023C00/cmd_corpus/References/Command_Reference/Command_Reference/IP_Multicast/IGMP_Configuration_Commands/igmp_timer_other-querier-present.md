igmp timer other-querier-present
================================

igmp timer other-querier-present

Function
--------



The **igmp timer other-querier-present** command sets the keepalive period for other IGMP queriers on an interface.

The **undo igmp timer other-querier-present** command restores the default setting.



By default, if the default values of the robustness variable, the interval for sending IGMP general query messages, and the maximum response time of IGMP Query messages are used, the keepalive period of other IGMP queriers is 125s. The formula used to calculate the keepalive period of other IGMP queriers is: Keepalive period of other IGMP queriers = Robustness variable x Interval for sending IGMP general query messages + 1/2 x Maximum response time of IGMP Query messages.


Format
------

**igmp timer other-querier-present** *interval*

**undo igmp timer other-querier-present**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the keepalive period of other IGMP queriers. | The value is an integer ranging from 60 to 300, in seconds. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When multiple multicast Routers are connected to a network segment where user hosts reside, one of these multicast Router is elected as the querier that is responsible for periodically sending Query messages to the network segment. If the non-queriers do not receive any Query message from the querier within the keepalive period of other IGMP queriers, they consider the querier invalid and automatically trigger a new round of querier election. To set the keepalive period of other IGMP queriers, run the igmp **timer other-querier-present** command.In IGMPv1, the querier is determined by PIM; in IGMPv2, the Router that has the lowest IP address functions as the querier on a shared network segment.

**Precautions**

The igmp **timer other-querier-present** command applies only to IGMPv2 and IGMPv3.Note:If the keepalive period of other IGMP queriers is shorter than the interval for sending IGMP general query messages, the querier election is performed frequently.The function of the igmp **timer other-querier-present** command is the same as the function of the **timer other-querier-present** command in the IGMP view. The configuration in the IGMP view is effective for all interfaces, whereas the configuration in the interface view is effective only for the specified interface. The configuration in the interface view takes precedence over the configuration in the IGMP view. The configuration in the IGMP view is used only when the configuration in the interface view is not available.



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# On vlanif 1, set the other-querier-present timer to 200 seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] igmp timer other-querier-present 200

```