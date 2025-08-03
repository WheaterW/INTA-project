pim ipv6 hello-option lan-delay
===============================

pim ipv6 hello-option lan-delay

Function
--------



The **pim ipv6 hello-option lan-delay** command sets the time in which a PIM interface delays sending Prune messages on a shared network segment.

The **undo pim ipv6 hello-option lan-delay** command restores the default value.



By default, a PIM interface delays sending Prune messages on a shared network segment for 500 milliseconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**pim ipv6 hello-option lan-delay** *interval*

**undo pim ipv6 hello-option lan-delay**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the time in which a PIM interface delays sending Prune messages on a shared network segment. | The value is an integer ranging from 1 to 32767, in milliseconds. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Hello messages sent by the Router carry lan-delay and override-interval parameters. lan-delay indicates the delay in sending Prune messages in a LAN. When the values of lan-delay on all Routers on the same link are different, the maximum value among these values is used after negotiation.If one Router receives a Prune message from an upstream interface, it indicates that other downstream Routers still exist in the LAN. If the Router still needs to receive multicast data, it must send a Join message to the upstream interface to override the prune action within the set override-interval.When receiving a Prune message from a downstream interface, the Router does not perform the prune action immediately until the Prune-Pending Timer (PPT) times out. The PPT equals the value of the lan-delay plus the override-interval. If the Router receives a Join message from its downstream device before the PPT expires, the Router cancels the prune action.To prevent redundant traffic, a shared network segment should have only one forwarder. Therefore, each Router sends an Assert message immediately after its forwarding interface receives the same multicast packet on a shared network segment, which indicates that more than one forwarder exists. Then, the Routers elect a unique forwarder, called the assert winner. The assert winner periodically sends Assert messages to maintain its winner state. The Router that fails in the election disable its downstream interfaces from forwarding multicast data within a specified timeout period, but restore the pruned interfaces to forward packets if they do not receive any Assert messages from the assert winner after the timeout period expires. To set such a timeout period, run the undo pim ipv6 holdtime assert command.


Example
-------

# Set the delay for 100GE1/0/1 to transmit Prune messages on the shared network to 200 ms.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] pim ipv6 hello-option lan-delay 200

```