pim ipv6 timer join-prune
=========================

pim ipv6 timer join-prune

Function
--------



The **pim ipv6 timer join-prune** command sets an interval at which a PIM interface sends Join/Prune messages upstream.

The **undo pim ipv6 timer join-prune** command restores the default setting.



By default, a PIM interface sends Join/Prune messages upstream at an interval of 60 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**pim ipv6 timer join-prune** *interval*

**undo pim ipv6 timer join-prune**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies an interval at which a PIM interface sends Join/Prune messages upstream. | The value is an integer ranging from 1 to 18000, in seconds. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set the interval at which a PIM interface sends Join/Prune messages upstream, run the pim ipv6 timer join-prune command. The interval at which a PIM interface sends Join/Prune messages upstream must be shorter than the holdtime of Join/Prune messages configured using the **pim ipv6 holdtime join-prune** command.

**Prerequisites**

The multicast routing function has been enabled using the **multicast ipv6 routing-enable** command in the public network instance view.

**Configuration Impact**

If the pim ipv6 timer join-prune command is run more than once, the latest configuration overrides the previous one.


Example
-------

# Set the interval at which 100GE1/0/1 sends Join/Prune messages to 80 seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] pim ipv6 timer join-prune 80

```