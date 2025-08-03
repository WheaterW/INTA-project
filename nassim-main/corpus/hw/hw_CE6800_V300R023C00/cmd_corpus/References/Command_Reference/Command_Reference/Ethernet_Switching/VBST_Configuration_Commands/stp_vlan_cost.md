stp vlan cost
=============

stp vlan cost

Function
--------



The **stp vlan cost** command sets the path cost of a port in a spanning tree.

The **undo stp vlan cost** command restores the default path cost.



By default, the path cost of a port in a spanning tree is the path cost corresponding to the port rate.


Format
------

**stp vlan** *vlan-id* [ **to** *vlan-id* ] [ *vlan-id* [ **to** *vlan-id* ] ] &<1-9> **cost** *cost*

**undo stp vlan** *vlan-id* [ **to** *vlan-id* ] [ *vlan-id* [ **to** *vlan-id* ] ] &<1-9> **cost** [ *cost* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **to** *vlan-id* | Configures the cost of a spanning tree in VLANs. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| *cost* | Specifies the path cost of an interface. | According to different calculation standards, the value ranges are as follows:   * Huawei legacy standard: 1 to 200,000 * IEEE 802.1d-1998 standard: 1 to 65535 * IEEE 802.1t standard: 1 to 200,000,000 |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The path cost of a port is an important basis for calculating a spanning tree. Path costs determine root port selection. In a spanning tree, the port with the lowest path cost to the root bridge is selected as a root port.If you configure different path costs for the same port in different spanning tree instances on a VBST-enabled device, traffic of different VLANs can be forwarded along different physical links, implementing VLAN-based load balancing.When IEEE 802.1d-1998 is used to calculate the path cost:For a 10GE port in Full-Duplex mode, the default path cost is 2.For a 10GE port in Aggregated Link Ports mode, the default path cost is 1.For a 25GE port in Full-Duplex mode, the default path cost is 1.For a 25GE port in Aggregated Link Ports mode, the default path cost is 1.For a 50GE port in Full-Duplex mode, the default path cost is 1.For a 50GE port in Aggregated Link Ports mode, the default path cost is 1.For a 100GE port in Full-Duplex mode, the default path cost is 1.For a 100GE port in Aggregated Link Ports mode, the default path cost is 1.For a 200GE port in Full-Duplex mode, the default path cost is 1.For a 200GE port in Aggregated Link Ports mode, the default path cost is 1.For a 400GE port in Full-Duplex mode, the default path cost is 1.For a 400GE port in Aggregated Link Ports mode, the default path cost is 1.When IEEE 802.1t is used to calculate the path cost:For a 10GE port in Full-Duplex mode, the default path cost is 2000.For a 10GE port in Aggregated Link Ports mode, the default path cost is 500.For a 25GE port in Full-Duplex mode, the default path cost is 800.For a 25GE port in Aggregated Link Ports mode, the default path cost is 200.For a 50GE port in Full-Duplex mode, the default path cost is 500.For a 50GE port in Aggregated Link Ports mode, the default path cost is 125.For a 100GE port in Full-Duplex mode, the default path cost is 200.For a 100GE port in Aggregated Link Ports mode, the default path cost is 50.For a 200GE port in Full-Duplex mode, the default path cost is 100.For a 200GE port in Aggregated Link Ports mode, the default path cost is 25.For a 400GE port in Full-Duplex mode, the default path cost is 50.For a 400GE port in Aggregated Link Ports mode, the default path cost is 12.When Huawei's calculation method is used to calculate the path cost:For a 10GE port in Full-Duplex mode, the default path cost is 2.For a 10GE port in Aggregated Link Ports mode, the default path cost is 1.For a 25GE port in Full-Duplex mode, the default path cost is 1.For a 25GE port in Aggregated Link Ports mode, the default path cost is 1.For a 50GE port in Full-Duplex mode, the default path cost is 1.For a 50GE port in Aggregated Link Ports mode, the default path cost is 1.For a 100GE port in Full-Duplex mode, the default path cost is 1.For a 100GE port in Aggregated Link Ports mode, the default path cost is 1.For a 200GE port in Full-Duplex mode, the default path cost is 1.For a 200GE port in Aggregated Link Ports mode, the default path cost is 1.For a 400GE port in Full-Duplex mode, the default path cost is 1.For a 400GE port in Aggregated Link Ports mode, the default path cost is 1.



**Prerequisites**

A path cost calculation standard has been set using the **stp pathcost-standard** command.

**Configuration Impact**

If the path cost of a port, the spanning tree where the port resides needs to be recalculated.

**Precautions**

* If you run the **stp pathcost-standard** command to change the path cost calculation method, the path cost configured using this command is restored to the default value.
* After VBST is enabled on an Eth-Trunk, the cost of the Eth-Trunk is fixed at 1/4 of the cost of a single link by default to prevent packet loss caused by the cost change of the Eth-Trunk when a member interface goes up or down.
* In a VBST-based M-LAG scenario, if an Eth-Trunk interface is specified as an M-LAG member interface, the path cost of the Eth-Trunk interface is fixed at 2000.


Example
-------

# Set the path cost of the specified interface in VLAN 10 to 300 when VBST is running.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[~HUAWEI-100GE1/0/1] stp vlan 10 cost 300

```