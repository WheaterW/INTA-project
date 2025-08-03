timer other-querier-present
===========================

timer other-querier-present

Function
--------



The **timer other-querier-present** command sets a global keepalive period of other IGMP queriers.

The **undo timer other-querier-present** command restores the default value.



The formula used to calculate the keepalive period of other IGMP queriers is: Keepalive period of other IGMP queriers = Robustness variable x Interval for sending IGMP general query messages + 1/2 x Maximum response time of IGMP Query messages. By default, if the default values of the robustness variable, the interval for sending IGMP general query messages, and the maximum response time of IGMP Query messages are used, the keepalive period of other IGMP queriers is 125s.


Format
------

**timer other-querier-present** *interval*

**undo timer other-querier-present**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the keepalive period of other IGMP queriers. | The value is an integer ranging from 60 to 300, in seconds. |



Views
-----

IGMP view,VPN instance IGMP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The function of this command is the same as the function of the **igmp timer other-querier-present** command used in the interface view. The configuration in the IGMP view is effective for all interfaces, whereas the configuration in the interface view is effective only for the specified interface. The configuration in the interface view takes precedence over the configuration in the IGMP view. The configuration in the IGMP view is used only when the configuration in the interface view is not available.


Example
-------

# In the IGMP view, set the keepalive period of other IGMP queriers to 200 seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] igmp
[*HUAWEI-igmp] timer other-querier-present 200

```