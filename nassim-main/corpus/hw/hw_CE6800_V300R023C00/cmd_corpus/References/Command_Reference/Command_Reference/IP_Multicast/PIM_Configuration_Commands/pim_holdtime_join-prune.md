pim holdtime join-prune
=======================

pim holdtime join-prune

Function
--------



The **pim holdtime join-prune** command sets the holdtime for Join/Prune messages sent by a PIM interface.

The **undo pim holdtime join-prune** command restores the default value.



By default, the holdtime value in Join/Prune messages sent by a PIM interface is 210 seconds.


Format
------

**pim holdtime join-prune** *interval*

**undo pim holdtime join-prune**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the value of holdtime in Join/Prune messages sent by a PIM interface. | The value is an integer ranging from 1 to 18000, in seconds. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After receiving a Join/Prune message from a downstream interface, an upstream Router determines the time period for keeping the join or prune state of a downstream interface based on the holdtime field carried in the Join/Prune message. To set a value for the holdtime field of Join/Prune messages sent by a specified PIM interface, run the pim holdtime join-prune command on the interface.Generally, the holdtime is 3.5 times the interval (specified using the **timer join-prune** command) at which Join/Prune messages are sent.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

If the pim holdtime join-prune command is run more than once, the latest configuration overrides the previous one.

**Precautions**



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# Set the holdtime in a Join/Prune message sent by VLANIF 1 to 280 seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] pim holdtime join-prune 280

```