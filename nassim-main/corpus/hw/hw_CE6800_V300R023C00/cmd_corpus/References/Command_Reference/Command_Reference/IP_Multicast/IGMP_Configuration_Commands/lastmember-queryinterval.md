lastmember-queryinterval
========================

lastmember-queryinterval

Function
--------



The **lastmember-queryinterval** command sets a global interval for sending IGMP group-specific query messages after the IGMP querier receives an IGMP Leave message from a host.

The **undo lastmember-queryinterval** command restores the default value.



By default, the interval for sending IGMP group-specific query messages is one second.


Format
------

**lastmember-queryinterval** *interval*

**undo lastmember-queryinterval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the interval for sending IGMP group-specific query messages. | The value is an integer ranging from 1 to 5, in seconds. |



Views
-----

IGMP view,VPN instance IGMP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In IGMPv3, the lastmember-queryinterval command can also be used to set the interval at which an IGMP querier sends group/source-specific messages after receiving a Report message about the change of the relationship between the multicast group and its source list.The function of this command is the same as the function of the **igmp lastmember-queryinterval** command in the interface view. The configuration in the IGMP view is effective for all interfaces, whereas the configuration in the interface view is effective only for the specified interface. The configuration in the interface view takes precedence over the configuration in the IGMP view. The configuration in the IGMP view is used only when the configuration in the interface view is not available.


Example
-------

# In the IGMP view, set the interval at which an IGMP querier sends IGMP group-specific messages to 3 seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] igmp
[*HUAWEI-igmp] lastmember-queryinterval 3

```