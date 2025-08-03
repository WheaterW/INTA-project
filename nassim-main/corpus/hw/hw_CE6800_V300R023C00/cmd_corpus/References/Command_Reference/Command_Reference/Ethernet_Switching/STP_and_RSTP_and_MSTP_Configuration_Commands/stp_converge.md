stp converge
============

stp converge

Function
--------



The **stp converge** command sets a convergence mode for a spanning tree protocol.

The **undo stp converge** command restores the default mode.



By default, the convergence mode is normal.


Format
------

**stp converge** { **fast** | **normal** }

**undo stp converge**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **fast** | Directly deletes ARP entries. | - |
| **normal** | Ages ARP entries quickly. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a Layer 2 network running STP, if the topology of a spanning tree instance changes, the forwarding paths of VLANs that are mapped to this instance change. As a result, ARP entries related to these VLANs need to be updated. Two methods are available:

* fast: Entries that need to be updated in an ARP table are directly deleted.
* normal: Entries that need to be updated in an ARP table are quickly aged out. The lifetime of these ARP entries is set to 0. If the number of aging detection times is greater than 0, the device sends ARP probe packets before aging them.To set a convergence mode based on the method for processing ARP entries, run the stp converge command.

**Configuration Impact**



If the stp converge fast command is run and the topology of a spanning tree instance changes, ARP entries that need to be updated are directly deleted from the ARP table.If the stp converge normal command is run and the topology of a spanning tree instance changes, ARP entries that need to be updated are aged out in the ARP table.



**Precautions**



Setting the convergence mode to normal is recommended. If the fast mode is used, frequent ARP entry deletion will affect services and even may cause the CPU usage of device to reach 100%. As a result, packet processing times out, causing network flapping.In either fast or normal mode, MAC address entries that need to be updated are deleted.




Example
-------

# Set the converging mode of a spanning tree protocol as normal.
```
<HUAWEI> system-view
[~HUAWEI] stp converge normal

```