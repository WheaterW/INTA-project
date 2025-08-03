igmp snooping port-fast-control (Layer 2 Eth-Trunk interface view)
==================================================================

igmp snooping port-fast-control (Layer 2 Eth-Trunk interface view)

Function
--------



The **igmp snooping port-fast-control** command enables a device to ignore the Up/Down state of an interface so that Layer 2 multicast services can be quickly restored.

The **undo igmp snooping port-fast-control** command disables the function of ignoring the Up/Down state of an interface so that the device can detect the Up/Down state of the interface.



By default, the device detects the Up/Down state of an interface.


Format
------

**igmp snooping port-fast-control**

**undo igmp snooping port-fast-control**


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

**Usage Scenario**

This command is used when the multicast switching performance on the M-LAG or port-group interface does not meet requirements, the entry switching time is long, and a large number of packets are lost. After this function is configured, the device ignores the Up/Down state of an interface. When the interface goes Down, the device does not delete the Layer 2 multicast entries of the interface. In this way, Layer 2 multicast services can be quickly restored after the interface goes Up.

**Precautions**

This command and the igmp snooping static-group command are mutually exclusive.


Example
-------

# Enable the function of ignoring the Up/Down state of the interface.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] interface Eth-Trunk 1
[*HUAWEI-Eth-Trunk1] igmp snooping port-fast-control

```