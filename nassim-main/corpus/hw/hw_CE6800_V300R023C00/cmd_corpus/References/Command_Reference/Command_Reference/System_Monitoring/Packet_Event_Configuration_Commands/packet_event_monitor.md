packet event monitor
====================

packet event monitor

Function
--------



The **packet event monitor** command displays the packet monitoring view.

The **undo packet event monitor** command deletes the packet monitoring view.



By default, the packet monitoring view is not displayed.


Format
------

**packet event monitor**

**undo packet event monitor**


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

To analyze traffic passing through a device, you can run the packet event monitor command to enter the packet monitoring view and enable the packet loss visualization or latency visualization function.

**Precautions**



The packet event service and the large MAC address table mode are mutually exclusive.




Example
-------

# Enter the packet monitoring view.
```
<HUAWEI> system-view
[~HUAWEI] packet event monitor

```