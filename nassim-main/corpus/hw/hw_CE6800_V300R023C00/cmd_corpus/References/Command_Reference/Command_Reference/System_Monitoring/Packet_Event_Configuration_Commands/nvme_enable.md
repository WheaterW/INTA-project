nvme enable
===========

nvme enable

Function
--------



The **nvme enable** command enables the NVMe packet parsing function.

The **undo nvme enable** command disables the NVMe packet parsing function.



By default, NVMe packet parsing is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**nvme enable**

**undo nvme enable**


Parameters
----------

None

Views
-----

packet-event-monitor view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

This command is used to enable NVMe packet parsing to implement I/O-based abnormal flow analysis.


Example
-------

# Enable the NVMe packet parsing function.
```
<HUAWEI> system-view
[~HUAWEI] packet event monitor
[*HUAWEI-packet-event-monitor] nvme enable

```