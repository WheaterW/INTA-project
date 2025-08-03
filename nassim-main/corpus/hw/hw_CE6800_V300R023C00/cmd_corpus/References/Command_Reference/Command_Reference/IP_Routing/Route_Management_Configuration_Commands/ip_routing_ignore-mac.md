ip routing ignore-mac
=====================

ip routing ignore-mac

Function
--------



The **ip routing ignore-mac** command configures the device to ignore the destination MAC address of packets. This configuration allows the device to forward the packets whose destination MAC address is not the local Layer 3 interface's MAC address according to routes.

The **undo ip routing ignore-mac** command restores the default configuration.



By default, the device is not configured to ignore the destination MAC address of packets.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ip routing ignore-mac**

**undo ip routing ignore-mac**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

During network maintenance, traffic is often redirected to a specific device for analysis. In most cases, a device forwards only packets whose destination MAC address is the local Layer 3 interface's MAC address according to routes, and forwards other packets at Layer 2 or discards other packets. If necessary, the device can also forward other packets at Layer 3 after it is configured to ignore the destination MAC address of packets.

**Precautions**

After the **ip routing ignore-mac** command is executed to ignore packet destination MAC addresses, the switch still performs Layer 3 forwarding even if the destination MAC address of a received packet is not the MAC address of the local Layer 3 interface, but the switch does not perform URPF check.This function is often used in traffic mirroring scenarios and is not recommended in other scenarios.


Example
-------

# Configure the device to ignore the destination MAC address of packets.
```
<HUAWEI> system-view
[~HUAWEI] ip routing ignore-mac

```