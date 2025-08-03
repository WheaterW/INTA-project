pim ipv6 holdtime join-prune
============================

pim ipv6 holdtime join-prune

Function
--------



The **pim ipv6 holdtime join-prune** command sets the holdtime for Join/Prune messages sent by a PIM interface.

The **undo pim ipv6 holdtime join-prune** command restores the default value.



By default, the holdtime value in Join/Prune messages sent by a PIM interface is 210 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**pim ipv6 holdtime join-prune** *interval*

**undo pim ipv6 holdtime join-prune**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies an interval at which a PIM interface sends Join/Prune messages upstream. | The value is an integer ranging from 1 to 65535, in seconds. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After receiving a Join/Prune message from a downstream interface, an upstream Router determines the time period for keeping the join or prune state of a downstream interface based on the holdtime field carried in the Join/Prune message. To set a value for the holdtime field of Join/Prune messages sent by a specified PIM interface, run the pim ipv6 holdtime join-prune command on the interface.Generally, the holdtime is 3.5 times the interval (specified using the **timer join-prune** command) at which Join/Prune messages are sent.


Example
-------

# Set the holdtime in Join/Prune messages sent by 100GE1/0/1 to 280 seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] pim ipv6 holdtime join-prune 280

```