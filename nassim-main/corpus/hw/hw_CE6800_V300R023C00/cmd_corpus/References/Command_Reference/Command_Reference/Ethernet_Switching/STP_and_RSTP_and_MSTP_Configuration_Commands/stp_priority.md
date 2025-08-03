stp priority
============

stp priority

Function
--------



The **stp priority** command sets a priority for a device on a spanning tree.

The **undo stp priority** command restores the default priority.



By default, the priority of a device on a spanning tree is 32768.


Format
------

**stp** [ **instance** *instance-id* ] **priority** *priority*

**undo stp** [ **instance** *instance-id* ] **priority**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-id* | Specifies the ID of a spanning tree instance.  If this parameter is not specified, the configuration takes effect on a Common and Internal Spanning Tree (CIST) instance. | The value is an integer ranging from 0 to 4094, Value 0 indicates CIST. |
| *priority* | Specifies the priority of a device.  A smaller value indicates a higher priority. | The value is an integer ranging from 0 to 61440, with a step of 4096. That is, there are a maximum of 16 priorities, such as 0, 4096, or 8192. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

* Priorities of devices are an important factor to calculate a spanning tree and determine root bridge selection.
* On a network running STP/RSTP/MSTP, each spanning tree has only one root bridge responsible for sending Bridge Protocol Data Units (BPDUs). Because the root bridge is of great importance, it is hoped that a device with high performance and network hierarchy can be chosen as the root bridge. However, this cannot be achieved if the device has a low priority. To set a priority for the device, run the stp priority command.
* You can also run the stp priority command to set a low priority for devices with low performance and network hierarchy so that these devices are not selected as the root bridge.
* On an MSTP network, each device can be set with a unique priority in each spanning tree instance.

**Configuration Impact**



A smaller priority value indicates a higher possibility to be selected as the root bridge.



**Precautions**

* If a device has been configured as the primary or secondary root bridge, before changing the priority of the device, run the undo stp root command to disable the root bridge function.
* After the **stp root primary** command is run to configure a device as the primary root bridge, the priority value of the device is 0.
* After the **stp root secondary** command is run to configure a device as the secondary root bridge, the priority value of the device is 4096.


Example
-------

# Set the priority of the device in spanning tree instance 1 to 4096.
```
<HUAWEI> system-view
[~HUAWEI] stp instance 1 priority 4096

```