pim ipv6 holdtime assert
========================

pim ipv6 holdtime assert

Function
--------



The **pim ipv6 holdtime assert** command sets the timeout period during which a PIM interface waits to receive Assert messages from the forwarder.

The **undo pim ipv6 holdtime assert** command restores the default timeout period.



By default, the timeout period of an interface is 180 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**pim ipv6 holdtime assert** *interval*

**undo pim ipv6 holdtime assert**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies a timeout period during which a PIM interface waits to receive Assert messages from the forwarder. | The value is an integer ranging from 7 to 65535, in seconds. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To prevent redundant traffic, a shared network segment should have only one forwarder. Therefore, each router sends an Assert message immediately after its forwarding interface receives the same multicast packet on a shared network segment, which indicates that more than one forwarder exists. Then, the routers elect a unique forwarder, called the assert winner. The assert winner periodically sends Assert messages to maintain its winner state. The router that fails in the election disable its downstream interfaces from forwarding multicast data within a specified timeout period, but restore the pruned interfaces to forward packets if they do not receive any Assert messages from the assert winner after the timeout period expires. To set such a timeout period, run the undo pim ipv6 holdtime assert command.

**Prerequisites**

The **multicast ipv6 routing-enable** command is run in the public network instance view.

**Configuration Impact**

If the pim ipv6 holdtime assert command is run more than once, the latest configuration overrides the previous one.


Example
-------

# Set the timeout period during which 100GE1/0/1 keeps the Assert state to 100 seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] pim ipv6 holdtime assert 100

```