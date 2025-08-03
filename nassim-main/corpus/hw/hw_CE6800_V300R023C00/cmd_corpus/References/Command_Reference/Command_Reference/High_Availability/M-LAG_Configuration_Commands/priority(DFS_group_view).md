priority(DFS group view)
========================

priority(DFS group view)

Function
--------



The **priority** command sets the priority of a DFS group.

The **undo priority** command restores the default priority of a DFS group.



By default, the priority of a DFS group is 100.


Format
------

**priority** *priorityvalue*

**undo priority** [ *priorityvalue* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **priority** *priorityvalue* | Specifies the priority of a DFS group. | The value is an integer that ranges from 1 to 254. |



Views
-----

DFS group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Two devices configured with M-LAG send negotiation packets to negotiate their master/backup status. M-LAG determines the master/backup status based on the priority and system MAC address. The device with a higher priority is the master. You can also run the **priority** command to set the M-LAG priority to determine the master/backup status of devices.

**Prerequisites**

A DFS group has been configured.

**Precautions**

If the priorities of the two devices are the same, the device with a smaller system MAC address is the master.If the priority and system MAC address are the same, M-LAG considers the two devices to be the master. You are advised to set different priorities for the two devices.


Example
-------

# Set the priority of a DFS group to 10.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] priority 10

```