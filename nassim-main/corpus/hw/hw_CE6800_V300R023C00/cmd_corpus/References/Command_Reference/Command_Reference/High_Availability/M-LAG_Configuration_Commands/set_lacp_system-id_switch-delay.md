set lacp system-id switch-delay
===============================

set lacp system-id switch-delay

Function
--------



The **set lacp system-id switch-delay** command sets the delay in switching the LACP M-LAG system ID.

The **undo set lacp system-id switch-delay** command restores the default delay in switching the LACP M-LAG system ID.



By default, the delay in switching the LACP M-LAG system ID is 0, that is, the LACP M-LAG system ID is not switched.


Format
------

**set lacp system-id switch-delay** { *switch-delay-time* | **immediately** }

**undo set lacp system-id switch-delay** [ *switch-delay-time* | **immediately** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *switch-delay-time* | Specifies the delay in switching the LACP M-LAG system ID. | The value is an integer that ranges from 0 to 3600, in seconds. The default value is 0. |
| **immediately** | Indicates that the LACP M-LAG system ID is switched immediately. | - |



Views
-----

DFS group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When devices successfully pair into a DFS group, the master device synchronizes its LACP M-LAG system ID to the backup device. The M-LAG member interface on the backup device uses the synchronized LACP M-LAG system ID for LACP negotiation. However, when devices fail to pair into a DFS group, the M-LAG splits, and the devices do not join the M-LAG again within the delay specified by switch-delay-time, the backup device switches the synchronized LACP M-LAG system ID to its own LACP M-LAG system ID. If the backup device joins the M-LAG again within the time specified by switch-delay-time, the LACP M-LAG system ID is not switched.If the value of switch-delay-time is set to 0, the LACP M-LAG system ID is not switched.

**Precautions**

After an M-LAG master/backup switchover is performed, the LACP M-LAG system ID is not switched.


Example
-------

# Set the delay in switching the LACP M-LAG system ID to 1200 seconds.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] set lacp system-id switch-delay 1200

```