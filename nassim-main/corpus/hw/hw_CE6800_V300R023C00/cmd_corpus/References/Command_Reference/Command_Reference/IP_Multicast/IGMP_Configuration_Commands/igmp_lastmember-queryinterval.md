igmp lastmember-queryinterval
=============================

igmp lastmember-queryinterval

Function
--------



The **igmp lastmember-queryinterval** command sets the interval at which an IGMP querier sends IGMP last-member query messages after it receives an IGMP Leave message from a host.

The **undo igmp lastmember-queryinterval** command restores the default setting.



By default, an IGMP querier sends IGMP last-member query messages at an interval of 1s.


Format
------

**igmp lastmember-queryinterval** *interval*

**undo igmp lastmember-queryinterval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies an interval at which an IGMP querier sends IGMP last-member query messages. | The value is an integer ranging from 1 to 5, in seconds. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If multiple multicast devices are connected to a shared network segment where user hosts reside, these multicast devices automatically elect a unique querier. The querier maintains IGMP group memberships by sending IGMP query messages. To set the interval at which IGMP last-member query messages are sent, run the igmp **lastmember-queryinterval** command.The igmp **lastmember-queryinterval** command is valid only when the querier runs IGMPv2 or IGMPv3. A last-member query is also known as a group-specific query. IGMPv3 also supports source/group-specific queries.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

After receiving a Leave message for a group, the querier sends group-specific query messages constantly to check whether there is a member of the group. The interval at which the querier sends group-specific query messages is specified by interval, and the number of times for sending group-specific query messages is specified by robust-value in the **igmp robust-count** command or the robust-count command.If there is a member of a group on the network segment, the member must send a Report message within the maximum response time. The maximum response time can be set by using the igmp max-response-time command or the max-response-time command.If the querier receives a Report message within the period obtained by the value of robust-value multiplied by the value of interval, it continues to maintain the memberships for the group. Otherwise, the querier considers that there is no member of the group on the network segment, and therefore does not maintain the memberships for the group.

**Precautions**

The function of the igmp **lastmember-queryinterval** command is the same as the function of the **lastmember-queryinterval** command in the IGMP view. The configuration in the IGMP view is effective for all interfaces, whereas the configuration in the interface view is effective only for the specified interface. The configuration in the interface view takes precedence over the configuration in the IGMP view. The configuration in the IGMP view is used only when the configuration in the interface view is not available.



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# On vlanif 1, set the interval at which a querier sends last-member query messages (group-specific query messages) to 3 seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] igmp lastmember-queryinterval 3

```