stp max-hops
============

stp max-hops

Function
--------



The **stp max-hops** command sets the maximum hops of a spanning tree in an MST region.

The **undo stp max-hops** command restores the default maximum hops of a spanning tree.



By default, the maximum hops are 20 in an MST region.


Format
------

**stp max-hops** *hop*

**undo stp max-hops**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *hop* | Specifies the maximum number of hops of a spanning tree in an MST region. | The value is an integer ranging from 1 to 40. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The devices on a Layer 2 network running MSTP communicate with each other by exchanging MST BPDUs.

* An MST BPDU has a field that indicates the number of remaining hops.
* The number of remaining hops in a BPDU sent by the root device is the maximum number of hops.
* The number of remaining hops in a BPDU sent by a non-root device equals the maximum number of hops minus the number of hops from the non-root device to the root device.
* If a device receives a BPDU in which the number of remaining hops is 0, the device discards the BPDU.The maximum number of hops of a spanning tree in an MST region determines the network scale. To set the maximum number of hops in an MST domain, run the **stp max-hops** command to control the network scale of a spanning tree.

**Precautions**



In an MST region, the maximum number of hops set on the root device in a Common and Internal Spanning Tree (CIST) or an MSTI is the maximum number of hops in the CIST or Multiple Spanning Tree instance (MSTI).




Example
-------

# Set the maximum hops in an MST region to 35.
```
<HUAWEI> system-view
[~HUAWEI] stp max-hops 35

```