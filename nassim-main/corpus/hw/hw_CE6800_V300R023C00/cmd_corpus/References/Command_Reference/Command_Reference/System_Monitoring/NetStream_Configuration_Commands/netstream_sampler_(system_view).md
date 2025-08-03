netstream sampler (system view)
===============================

netstream sampler (system view)

Function
--------



The **netstream sampler** command configures packet sampling on interfaces.

The **undo netstream sampler** command restores the default setting.



By default, packet sampling is not configured on interfaces.


Format
------

**netstream sampler random-packets** *packet-number* { **inbound** | **outbound** }

**undo netstream sampler** [ **random-packets** *packet-number* ] { **inbound** | **outbound** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **inbound** | Samples incoming traffic on an interface. | - |
| **outbound** | Samples outgoing traffic on an interface. | - |
| **random-packets** *packet-number* | Specifies the number of packets between two sampled packets in packet-based random sampling mode. In this mode, one packet is randomly sampled out of packet-number packets. | The value is an integer in the range from 1 to 32768 and must be 2^n (n = 0, 1, 2...). |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After the NetStream function is enabled on an interface, the system stores the NetStream information in the corresponded interface information table. If every packet passing an interface is captured and counted, forwarding performance on the interface will deteriorate, especially on the interface with a high forwarding rate. To understand interface traffic attributes without compromising forwarding performance, configure packet sampling on the interface. A low sampling rate can significantly reduce impact of NetStream on device performance.

**Precautions**



The packet sampling function configured in the system view takes effect on all interfaces on the device. If the function is configured in both the interface view and system view, the configuration in the interface view has priority.After NetStream is configured in inbound or outbound direction and a sampling interval is configured, flow sampling will be performed based on the configuration.If you run the **netstream sampler** command multiple times in the same view, only the latest configuration takes effect.For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM, if the sampling rate is less than or equal to 64, packets are sampled at a fixed interval. If the sampling rate is greater than 64, packets are sampled at a random interval.




Example
-------

# Configure packet-based random sampling on an interface in the inbound direction and set the sampling rate to 8192.
```
<HUAWEI> system-view
[~HUAWEI] netstream sampler random-packets 8192 inbound

```

# Configure packet-based random sampling on an interface in the outbound direction and set the sampling rate to 8192.
```
<HUAWEI> system-view
[~HUAWEI] netstream sampler random-packets 8192 outbound

```