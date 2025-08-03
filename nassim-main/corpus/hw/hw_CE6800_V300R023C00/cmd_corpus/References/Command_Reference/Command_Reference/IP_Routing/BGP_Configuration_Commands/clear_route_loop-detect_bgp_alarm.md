clear route loop-detect bgp alarm
=================================

clear route loop-detect bgp alarm

Function
--------



The **clear route loop-detect bgp alarm** command clears BGP loop alarms reported to the NMS.




Format
------

**clear route loop-detect bgp alarm**


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

After a BGP routing loop is detected, the device reports a hwBgpRouteLoopDetected alarm. The device cannot automatically detect whether the loop is removed. Therefore, you need to run this command to manually clear the BGP loop alarm after the routing loop is removed.

**Precautions**

After the **clear route loop-detect bgp alarm** command is run, the loop breaking process is triggered again. If a loop has occurred, the loop will not be broken.


Example
-------

# Clear BGP loop alarms.
```
<HUAWEI> system-view
[~HUAWEI] clear route loop-detect bgp alarm

```