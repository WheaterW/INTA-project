clear route loop-detect isis alarm-state
========================================

clear route loop-detect isis alarm-state

Function
--------



The **clear route loop-detect isis alarm-state** command exits the routing loop alarm state and clears the loop detection alarm.




Format
------

**clear route loop-detect isis alarm-state**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After detecting an IS-IS routing loop, a device reports an alarm. The device cannot automatically detect whether the loop is rectified. After detecting and rectifying the loop, you need to run this command to disable the device from advertising a large link cost for imported routes and manually clear the IS-IS loop alarm. If this command is executed when the routing loop problem is not resolved, the alarm is reported again.

**Precautions**

If the configuration that causes the loop is not corrected, the loop may occur again after this command is run.


Example
-------

# Exits the routing loop alarm-state and clear the loop-detect alarm.
```
<HUAWEI> system-view
[~HUAWEI] clear route loop-detect isis alarm-state

```