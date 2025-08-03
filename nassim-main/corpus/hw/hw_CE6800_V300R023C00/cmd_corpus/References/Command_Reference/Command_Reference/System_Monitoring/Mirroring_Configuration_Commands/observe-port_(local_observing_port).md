observe-port (local observing port)
===================================

observe-port (local observing port)

Function
--------



The **observe-port** command configures a local observing port.

The **undo observe-port** command deletes a local observing port.



By default, no local observing port is configured.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**undo observe-port** *observe-port-index*

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**observe-port** [ *observe-port-index* ] **interface** { *interface-type* *interface-number* | *interface-name* } [ **cir** *cir-value* [ **gbps** | **kbps** | **mbps** ] ]

For CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**observe-port** [ *observe-port-index* ] **interface** { *interface-type* *interface-number* | *interface-name* } [ **cir** *cir-value* [ **gbps** | **kbps** | **mbps** ] ] [ **truncate** **packet** *packet-length* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *observe-port-index* | Specifies the index of the observing port. | The value is an integer that ranges from 1 to 8. |
| **interface** *interface-type* *interface-number* | Specifies the type and number of the interface.   * interface-type indicates the type of the interface. * interface-number indicates the number of the interface. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The interface type can be Ethernet or Eth-Trunk interface.  For the CE6885-LL (low latency mode):The interface type can be Ethernet interface. |
| *interface-name* | Specifies an interface name. | The interface type can be Ethernet or Eth-Trunk interface. |
| **cir** *cir-value* | Specifies the committed information rate (CIR), which is the average rate of traffic that can pass through an interface. | The value is an integer in the range from 24 to 400000000. |
| **gbps** | Indicates that the rate unit is Gbit/s. | - |
| **kbps** | Specifies the rate unit as kbit/s. | - |
| **mbps** | Specifies the rate unit as Mbit/s. | - |
| **packet** *packet-length* | Configures packet truncation on the observing port.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer that ranges from 64 to 256 and must be a multiple of 32. The unit is byte. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When configuring local mirroring, you must specify the ports that are directly connected to monitoring devices as local observing ports.If traffic of mirrored ports is copied to observing ports and exceeds the bandwidth of observing ports, congestion will occur or a large number of packets will be dropped, affecting the device forwarding performance. You can limit the rate at which interfaces send data to so that interfaces can send packets evenly.

**Precautions**



If the observe-port-index parameter is not specified when multiple observing ports are configured, by default, the observing port indexes ranging from 1 to 8 start from 1 and increase by 1 each time you run this command. These indexes cannot conflict with the existing configured indexes.If the traffic rate limit is configured on an observing port, this limit applies to all the traffic copied to this observing port, including incoming and outgoing traffic.To prevent service conflicts, it is recommended that no other services be configured on observing ports.




Example
-------

# Configure 100GE1/0/1 as the observing port, set the CIR to 20000 kbit/s, and set the port index to 1.
```
<HUAWEI> system-view
[~HUAWEI] observe-port 1 interface 100GE 1/0/1 cir 20000 kbps

```