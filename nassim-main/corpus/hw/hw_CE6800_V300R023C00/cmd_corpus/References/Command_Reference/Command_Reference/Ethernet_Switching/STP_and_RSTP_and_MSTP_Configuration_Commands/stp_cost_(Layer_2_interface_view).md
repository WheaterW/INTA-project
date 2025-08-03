stp cost (Layer 2 interface view)
=================================

stp cost (Layer 2 interface view)

Function
--------



The **stp cost** command sets a path cost for a spanning tree port.

The **undo stp cost** command restores the default path cost.



By default, the path cost of a spanning tree port is the path cost corresponding to the port rate.


Format
------

**stp** [ **process** *process-id* ] [ **instance** *instance-id* ] **cost** *cost*

**undo stp** [ **process** *process-id* ] [ **instance** *instance-id* ] **cost**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **process** *process-id* | Specifies the ID of a Multiple Spanning Tree Protocol (MSTP) process. | The value is a decimal integer ranging from 1 to 256. |
| **instance** *instance-id* | Specifies the ID of a spanning tree instance.  If instance <instance-id> is not specified, the path cost of an interface in the Common and Internal Spanning Tree (CIST) is configured. | The value is an integer ranging from 0 to 4094, Value 0 indicates CIST. |
| *cost* | Specifies the path cost of an interface. | The value varies with path cost calculation standards:   * Huawei legacy standard: 1 to 200,000 * IEEE 802.1d-1998 standard: 1 to 65535 * IEEE 802.1t standard: 1 to 200,000,000 |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Port path costs are important basis for calculating a spanning tree. Path costs determine root port selection. On a spanning tree, the port with the lowest path cost to the root bridge is selected as a root port. To configure a port path cost, run the stp cost command.If different path costs are set for a port in different spanning tree instances, traffic of different VLANs will be forwarded along different physical links and VLAN-based load balancing can be performed.



**Prerequisites**



A path cost calculation standard has been set using the **stp pathcost-standard** command. By default, the IEEE 802.1T is used to calculate the path cost.



**Configuration Impact**



If the path cost of an interface changes, the spanning tree where the interface resides is recalculated.



**Precautions**



If the path cost calculation standard is changed using the **stp pathcost-standard** command, the path cost set using the stp cost command is restored to the default value.If an Eth-Trunk interface is specified as the member interface of an M-LAG configured in V-STP mode, the path cost of the Eth-Trunk interface is fixed at 2000.




Example
-------

# Set the path cost of 100GE1/0/1 in spanning tree instance 2 to 200.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[~HUAWEI-100GE1/0/1] stp instance 2 cost 200

```