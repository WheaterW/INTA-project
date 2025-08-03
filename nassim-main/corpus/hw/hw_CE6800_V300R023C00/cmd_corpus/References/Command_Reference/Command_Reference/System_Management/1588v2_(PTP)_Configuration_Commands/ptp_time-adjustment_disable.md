ptp time-adjustment disable
===========================

ptp time-adjustment disable

Function
--------



The **ptp time-adjustment disable** command disables the time adjustment function.

The **undo time-adjustment disable** command enables the time adjustment function.



By default, the time adjustment disable function is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ptp time-adjustment disable**

**undo ptp time-adjustment disable**


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

1. By default, the 1588 Layer 3 unicast negotiation function synchronizes the frequency and time. If the customer network does not need the time synchronization function, run this command to disable the time synchronization function.
2. After the time synchronization function is enabled, the device time is adjusted. Adjusting the device time affects frequency synchronization. When locating frequency synchronization exceptions, you can run this command to disable time adjustment to eliminate the impact of time adjustment on frequency synchronization.

Example
-------

# Configure time adjustment disable.
```
<HUAWEI> system-view
[~HUAWEI] ptp time-adjustment disable

```