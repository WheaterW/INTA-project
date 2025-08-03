pim timer join-prune
====================

pim timer join-prune

Function
--------



The **pim timer join-prune** command sets an interval at which a PIM interface sends Join/Prune messages upstream.

The **undo pim timer join-prune** command restores the default setting.



By default, a PIM interface sends Join/Prune messages upstream at an interval of 60 seconds.


Format
------

**pim timer join-prune** *interval*

**undo pim timer join-prune**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the value of timer in Join/Prune messages sent by a PIM interface. | The value is an integer ranging from 1 to 18000, in seconds. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set the interval at which a PIM interface sends Join/Prune messages upstream, run the pim timer join-prune command. The interval at which a PIM interface sends Join/Prune messages upstream must be shorter than the holdtime of Join/Prune messages.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

If the pim timer join-prune command is run more than once, the latest configuration overrides the previous one.

**Precautions**



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# Set the interval for sending Join/Prune messages to 80 seconds on vlanif 1.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] pim timer join-prune 80

```