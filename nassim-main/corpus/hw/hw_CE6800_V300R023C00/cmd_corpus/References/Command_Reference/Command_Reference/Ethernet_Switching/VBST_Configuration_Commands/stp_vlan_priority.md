stp vlan priority
=================

stp vlan priority

Function
--------



The **stp vlan priority** command sets the priority of the switching device in a spanning tree.

The **undo stp vlan priority** command restores the default priority.



By default, the priority of the switching device in a spanning tree is 32768.


Format
------

**stp vlan** *vlan-id* [ **to** *vlan-id* ] [ *vlan-id* [ **to** *vlan-id* ] ] &<1-9> **priority** *priority-value*

**undo stp vlan** *vlan-id* [ **to** *vlan-id* ] [ *vlan-id* [ **to** *vlan-id* ] ] &<1-9> **priority** [ *priority-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **to** *vlan-id* | Configures the priority of a port in VLANs. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| *priority-value* | Specifies the priority of the device in a spanning tree.  The smaller the value is, the higher the device priority is. | The value is an integer that ranges from 0 to 61440 and is a multiple of 4096, such as 0, 4096, and 8192. The default value is 32768. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Priorities of switching devices are an important factor to calculate a spanning tree and determine the selection of the root bridge.On a VBST network, each spanning tree has only one root bridge, which is responsible for sending BPDUs. Owning to the importance of the root bridge, the switching device with high performance and network hierarchy is generally chosen as the root bridge. The priority of such a switching device, however, may not be that high. Therefore, setting a high priority for the switching device is necessary so that the device can function as a root bridge.Other devices with low performance and network hierarchy are not fit to be a root bridge. Therefore, set low priorities for these devices.On a VBST network, each switching device can be set with a priority for the spanning tree in each VLAN.

**Prerequisites**

If the device has been specified as the root bridge or secondary root bridge, run the **undo stp vlan root** command to disable the root bridge or secondary root bridge function before changing the device priority.


Example
-------

# Set the priority of the switch in VLAN 10 to 4096 when VBST is running.
```
<HUAWEI> system-view
[~HUAWEI] stp vlan 10 priority 4096

```