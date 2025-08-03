rewrite no-action
=================

rewrite no-action

Function
--------



The **rewrite no-action** command configures a dot1q Layer 2 sub-interface to transparently transmit received packets, instead of removing VLAN tags from the packets.

The **undo rewrite no-action** command restores the default configuration.



By default, a dot1q Layer 2 sub-interface removes VLAN tags from received packets, instead of transparently transmitting them.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**rewrite no-action**

**undo rewrite no-action**


Parameters
----------

None

Views
-----

100GE Layer 2 sub-interface view,200GE Layer 2 sub-interface view,400GE Layer 2 sub-interface view,50GE Layer 2 sub-interface view,Eth-Trunk Layer 2 sub-interface view,Layer 2 sub-interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a service access point is configured in the EVC model, if a Layer 2 sub-interface is selected and the encapsulation mode of the Layer 2 sub-interface is Dot1q, the sub-interface removes VLAN tags from received packets by default. To enable a Layer 2 sub-interface to transparently transmit single-tagged data packets, run the **rewrite no-action** command.

**Prerequisites**

* The dot1q Layer 2 sub-interface has not been added to a BD.
* A VLAN ID or VLAN ID range of packets that the dot1q Layer 2 sub-interface permits has been configured using the **encapsulation dot1q vid** command.

**Precautions**



This command applies only to dot1q Layer 2 sub-interfaces.If a dot1q Layer 2 sub-interface is bound to a BD after the **rewrite no-action** command is run for the sub-interface, the BD does not support VBDIF interfaces and ARP broadcast packet suppression.




Example
-------

# Configure the Layer 2 sub-interface 100GE 1/0/1.1 to transparently transmit received packets.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1.1 mode l2
[*HUAWEI-100GE1/0/1.1] encapsulation dot1q vid 2
[*HUAWEI-100GE1/0/1.1] rewrite no-action

```