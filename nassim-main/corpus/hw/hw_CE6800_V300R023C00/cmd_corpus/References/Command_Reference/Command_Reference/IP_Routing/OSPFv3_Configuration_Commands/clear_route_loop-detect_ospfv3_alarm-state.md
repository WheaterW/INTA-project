clear route loop-detect ospfv3 alarm-state
==========================================

clear route loop-detect ospfv3 alarm-state

Function
--------



The **clear route loop-detect ospfv3 alarm-state** command exits OSPFv3 routing loop detection state and clears OSPFv3 loop detection alarms.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**clear route loop-detect ospfv3 alarm-state**


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

After detecting an OSPFv3 routing loop, the device reports an alarm. The device cannot automatically detect whether the loop is rectified. Therefore, you need to run this command to disable the device from advertising a large cost for imported routes and manually clear the OSPFv3 loop alarm after detecting and rectifying the loop. If this command is executed when the routing loop problem is not resolved, the alarm is reported again.


Example
-------

# Exit the OSPFv3 routing loop alarm state and clear the alarm.
```
<HUAWEI> system-view
[~HUAWEI] clear route loop-detect ospfv3 alarm-state

```