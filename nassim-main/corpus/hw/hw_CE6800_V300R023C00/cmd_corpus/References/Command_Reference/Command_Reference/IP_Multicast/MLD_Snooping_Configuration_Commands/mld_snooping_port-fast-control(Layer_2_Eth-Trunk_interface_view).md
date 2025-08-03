mld snooping port-fast-control(Layer 2 Eth-Trunk interface view)
================================================================

mld snooping port-fast-control(Layer 2 Eth-Trunk interface view)

Function
--------



The **mld snooping port-fast-control** command enables a device to ignore the Up/Down state of an interface so that Layer 2 multicast services can be quickly restored.

The **undo mld snooping port-fast-control** command disables the device from ignoring the Up/Down state of an interface so that the device can detect the Up/Down state of the interface.



By default, the device detects the Up/Down state of an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping port-fast-control**

**undo mld snooping port-fast-control**


Parameters
----------

None

Views
-----

Layer 2 Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

This command is used when the multicast switching performance on the M-LAG or port-group interface does not meet requirements, the entry switching time is long, and a large number of packets are lost. After this function is configured, the device ignores the Up/Down state of an interface. When the interface goes Down, the device does not delete the Layer 2 multicast entries of the interface. In this way, Layer 2 multicast services can be quickly restored after the interface goes Up.


Example
-------

# Enable the function of ignoring the Up/Down state of an interface.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[*HUAWEI] interface Eth-Trunk 1
[*HUAWEI-Eth-Trunk1] mld snooping port-fast-control

```