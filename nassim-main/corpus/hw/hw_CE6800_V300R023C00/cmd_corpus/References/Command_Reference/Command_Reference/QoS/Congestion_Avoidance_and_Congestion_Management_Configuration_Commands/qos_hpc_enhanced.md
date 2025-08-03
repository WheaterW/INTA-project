qos hpc enhanced
================

qos hpc enhanced

Function
--------



The **qos hpc enhanced** command configures high-priority scheduling for queues 6 and 7 in an HPC scenario.

The **undo qos hpc enhanced** command restores the common scheduling mode.



By default, high-priority scheduling is not configured in an HPC scenario.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**qos hpc enhanced**

**undo qos hpc enhanced**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In the HPC scenario, if small packets are congested on multiple interfaces, packet loss may occur in queues 6 and 7. In this case, you can configure high-priority scheduling for queues 6 and 7.

**Precautions**

The **qos hpc enhanced** command is mutually exclusive with the qos {drr | lpq} command configured for queues 6 and 7.


Example
-------

# Configure high-priority scheduling for queues 6 and 7 in an HPC scenario.
```
<HUAWEI> system-view
[~HUAWEI] qos hpc enhanced

```