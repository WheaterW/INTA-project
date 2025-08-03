ospfv3 router-id auto-recover disable
=====================================

ospfv3 router-id auto-recover disable

Function
--------



The **ospfv3 router-id auto-recover disable** command disables automatic recovery after a router ID conflict is detected.

The **undo ospfv3 router-id auto-recover disable** command enables automatic router ID recovery after a router ID conflict is detected.



By default, automatic router ID recovery takes effect after a router detects a router ID conflict.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3 router-id auto-recover disable**

**undo ospfv3 router-id auto-recover disable**


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

If a router ID conflict occurs in an OSPFv3 area, the system selects a new router ID, which prevents route flapping and reduces route calculation operations. Other protocols will not go Down when the CPU usage is controlled.NOTE:

* If the automatic recovery function is enabled and a router ID conflict occurs between indirectly connected routers in one OSPFv3 area, the system replaces the conflicted router ID with a newly calculated one. The automatic recovery function takes effect on both configured and automatically generated router IDs.
* The system can replace a router ID in a maximum of three attempts in case the router ID conflict persists.

Example
-------

# Disable automatic recovery after a router ID conflict is detected.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 router-id auto-recover disable

```