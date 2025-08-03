clear route loop-detect ospf alarm-state
========================================

clear route loop-detect ospf alarm-state

Function
--------



The **clear route loop-detect ospf alarm-state** command exits the routing loop alarm-state and clears loop detection alarms.




Format
------

**clear route loop-detect ospf alarm-state**


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

After detecting an OSPF routing loop, the device reports an alarm. The device cannot automatically detect whether the loop is rectified. Therefore, you need to run this command to disable the device from advertising a large link cost for imported routes and manually clear the OSPF loop alarm after detecting and rectifying the loop. If this command is executed when the routing loop problem is not resolved, the alarm is reported again.

**Precautions**

If this command is executed when the routing loop problem is not resolved, the alarm is reported again.


Example
-------

# Exits the routing loop alarm-state and clear the loop-detect alarm.
```
<HUAWEI> system-view
[~HUAWEI] clear route loop-detect ospf alarm-state

```