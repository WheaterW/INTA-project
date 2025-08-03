stp pathcost-standard (MSTP process view)
=========================================

stp pathcost-standard (MSTP process view)

Function
--------



The **stp pathcost-standard** command sets a standard for calculating the path cost in MSTP process.

The **undo stp pathcost-standard** command restores the default standard for calculating the path cost in MSTP process.



By default, IEEE 802.1T is used to calculate the path cost.


Format
------

**stp pathcost-standard** { **dot1d-1998** | **dot1t** | **legacy** }

**undo stp pathcost-standard**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **dot1d-1998** | Indicates that IEEE 802.1d-1998 is used to calculate the path cost. | - |
| **dot1t** | Indicates that IEEE 802.1T is used to calculate the path cost. | - |
| **legacy** | Indicates that the Huawei legacy standard is used to calculate the path cost. | - |



Views
-----

MSTP process view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Path costs are used as a reference for a spanning tree protocol to select stable links, block redundant paths, and trim a network into a loop-free network. Path costs vary with path cost calculation standards. To set a standard for calculating the path cost, run the stp pathcost-standard command.



**Configuration Impact**



If the path cost calculation standard is changed on a port, the path cost of the port is restored to the default value. To set a path cost for a port, run the **stp cost** command.



**Precautions**

* Generally, all devices on the same network should use the same path cost calculation standard.
* After STP is enabled on a PW interface, the cost of the PW interface is fixed: dot1d-1998=3, dot1t=4657, and legacy=13.


Example
-------

# Use IEEE 802.1D to calculate the MSTP process 1's path cost.
```
<HUAWEI> system-view
[~HUAWEI] stp process 1
[*HUAWEI-mst-process-1] stp pathcost-standard dot1d-1998

```