igmp robust-count
=================

igmp robust-count

Function
--------



The **igmp robust-count** command sets a robustness variable for an IGMP querier on an interface.

The **undo igmp robust-count** command restores the default setting.



By default, the robustness variable of an IGMP querier is 2.


Format
------

**igmp robust-count** *robust-value*

**undo igmp robust-count**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *robust-value* | Specifies the robustness variable for an IGMP querier. It is the number of attempts to retransmit messages to compensate for packet loss. | The value is an integer ranging from 2 to 5. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a shared network segment where user hosts reside, the querier is responsible for maintaining IGMP group memberships. The robustness variable affects the timeout period of group memberships. The timeout period of a group membership is calculated by using the formula: Timeout period of a group membership = Interval for sending general IGMP query messages x Robustness variable + Maximum response time. The robustness variable defines the following values:

* Number of times for sending general query messages when the querier startsWhen the querier starts, it sends general query messages for the number of "robustness variable" times to query the multicast groups that have members on the attached network segment. The sending interval is 1/4 of the interval for sending general query messages. The interval for sending general query messages can be set by using the **igmp timer query** command or the timer query command.
* Number of times for sending IGMPv2 or IGMPv3 group-specific query messages when the querier receives a Leave messageAfter receiving a Leave message for a group, the querier sends group-specific query messages continuously for the number of "robustness variable" times to check whether any other member of this group exists. The interval for sending group-specific query messages can be set by using the **igmp lastmember-queryinterval** command or the lastmember-queryinterval command.
* Number of times for a querier to send group/source-specific query messages after receiving an IGMPv3 (S, G) Report messageAfter receiving a Report message for a multicast group corresponding to a source list, the querier sends group/source-specific query messages for the "robustness variable" times. The interval for sending group/source-specific query messages can be set by using the **igmp lastmember-queryinterval** command or the lastmember-queryinterval command.The function of the igmp **robust-count** command is the same as the function of the **robust-count** command in the IGMP view. The configuration in the IGMP view is effective for all interfaces, whereas the configuration in the interface view is effective only for the specified interface. The configuration in the interface view takes precedence over the configuration in the IGMP view. The configuration in the IGMP view is used only when the configuration in the interface view is not available.

**Precautions**



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# Set the robustness variable of the querier to 3 on VLANIF 1.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] igmp robust-count 3

```