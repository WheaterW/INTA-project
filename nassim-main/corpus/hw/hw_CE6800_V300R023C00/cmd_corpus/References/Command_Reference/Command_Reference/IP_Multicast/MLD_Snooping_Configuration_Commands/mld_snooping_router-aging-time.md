mld snooping router-aging-time
==============================

mld snooping router-aging-time

Function
--------



The **mld snooping router-aging-time** command sets the aging time of dynamic router interfaces.

The **undo mld snooping router-aging-time** command restores the default value.



By default, the aging time of dynamic router interfaces is 180s or equals the Holdtime value contained in a Protocol Independent Multicast (PIM) Hello message.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping router-aging-time** *router-aging-time*

**undo mld snooping router-aging-time**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **router-aging-time** *router-aging-time* | Specifies the aging time of dynamic router interfaces. | The value is an integer ranging from 1 to 1000, in seconds. |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Network congestion may delay the transmission of a Query message from an MLD Querier. If a dynamic router interface does not receive any MLD Query message with source IP addresses other than 0::0 or PIM hello message within the aging time, it becomes a non-router interface. The device will then not send Report or Done messages to the interface. This may lead to multicast data transmission interruption. Therefore, if a network is unstable, run the mld snooping router-aging-time command to set larger aging time for dynamic router interfaces. The device resets the aging time of a dynamic router interface when the interface receives an MLD Query or PIM Hello message from the interface.


Example
-------

# Set the aging time of dynamic router interfaces in VLAN 100 to 500s.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[*HUAWEI] vlan 100
[*HUAWEI-vlan100] mld snooping router-aging-time 500

```