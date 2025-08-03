stp root (MSTP process view)
============================

stp root (MSTP process view)

Function
--------



The **stp root** primary command sets a device as the root or the secondary bridge of a spanning tree.

The **undo stp root** command cancels the configuration.



By default, the device does not act as the root or secondary root bridge of any spanning tree.


Format
------

**stp** [ **instance** *instance-id* ] **root** { **primary** | **secondary** }

**undo stp** [ **instance** *instance-id* ] **root**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-id* | Specifies the ID of a spanning tree instance.  If this parameter is not specified, the configuration takes effect on a Common and Internal Spanning Tree (CIST) instance. | The value is an integer ranging from 0 to 4094, Value 0 indicates CIST. |
| **primary** | Specifies a device as the root bridge of a spanning tree. | - |
| **secondary** | Specifies a device as the secondary root bridge of a spanning tree. | - |



Views
-----

MSTP process view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



On an STP/RSTP/MSTP network, each spanning tree has only one root bridge responsible for sending Bridge Protocol Data Units (BPDUs). To configure a device with high performance and network hierarchy as the root bridge, run the stp root primary command. To ensure uninterrupted traffic forwarding, run the stp root secondary command to set a secondary root bridge. When the primary root bridge becomes faulty or is powered off, the secondary root bridge becomes the primary root bridge after the spanning tree calculation is complete.After the stp root primary command is run to configure a device as the primary root bridge, the priority value of the device is 0 on the spanning tree. The secondary root bridge specified using the stp root secondary command has the priority value 4096.



**Precautions**

* A spanning tree has only one root bridge.
* A device on a spanning tree cannot function as both the primary and secondary root bridges.
* If multiple secondary root bridges are set on a spanning tree, the one with the smallest MAC address functions as the secondary root bridge of the spanning tree.


Example
-------

# Set the MSTP process 1 as the secondary root bridge of spanning tree instance 4.
```
<HUAWEI> system-view
[~HUAWEI] stp process 1
[*HUAWEI-mst-process-1] stp instance 4 root secondary

```