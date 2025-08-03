spf-schedule-interval(OSPFv3 view)
==================================

spf-schedule-interval(OSPFv3 view)

Function
--------



The **spf-schedule-interval** command sets the interval for OSPFv3 to calculate routes through an intelligent SPF timer.

The **undo spf-schedule-interval** command restores the default setting.



By default, the maximum interval for SPF calculation is 5000 ms, the initial interval is 50 ms, and the Holdtime interval is 200 ms.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**spf-schedule-interval intelligent-timer** *max-interval* *start-interval* *hold-interval*

**spf-schedule-interval millisecond** *interval2*

**spf-schedule-interval** *delay-interval* *spftimer-hold-interval*

**undo spf-schedule-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *max-interval* | Specifies the maximum interval for performing the OSPFv3 SPF calculation. | The value is an integer ranging from 1 to 120000, in milliseconds. |
| *start-interval* | Specifies the initial interval for performing the OSPFv3 SPF calculation. | The value is an integer ranging from 1 to 60000 in milliseconds. |
| *hold-interval* | Specifies the holding interval for performing the OSPFv3 SPF calculation. | The value is an integer ranging from 1 to 60000 in milliseconds. |
| **millisecond** *interval2* | Specifies the interval for performing the OSPFv3 SPF calculation. | The value is an integer that ranges from 1 to 10000, in milliseconds. |
| *delay-interval* | Specifies the interval between the route change detection and the SPF calculation. | The value is an integer ranging from 0 to 65535, in seconds. The default value is 5. |
| *spftimer-hold-interval* | Specifies the holding interval between two consecutive SPF calculations. | The value is an integer ranging from 0 to 65535, in seconds. The default value is 10. |
| **intelligent-timer** | Sets the SPF calculation interval through an intelligent timer. | - |



Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Based on the LSDB, the device that runs OSPFv3 can calculate the Shortest Path Tree (SPT) with itself as the root based on the SPF algorithm, and determine the next hop to the destination network according to the SPT. When the OSPFv3 LSDB changes, the shortest path needs to be recalculated. Frequent network changes and SPF calculation consume many system resources and affect router performance. You can configure an intelligent timer and set a proper interval for the SPF calculation to prevent excessive router memory and bandwidth resources from being consumed.If fast route convergence is required, you can set a millisecond-level interval to speed up route calculation. In other networking environments, the default value is recommended.

**Configuration Impact**

The interval of the SPF intelligent timer is calculated as follows:

* The initial interval for SPF calculation is specified by start-interval.
* The interval for the SPF calculation for the nth (nâ¥2) time is equal to hold-interval x 2^(n-2).
* When the interval specified by hold-interval x 2^(n-2) reaches the maximum interval specified by max-interval, OSPFv3 keeps performing SPF calculation at the maximum interval.
* If no flapping occurs within the period specified by max-interval after the last SPF calculation, the intelligent timer exits.
* If route flapping does not occur within the last SPF calculation interval but occurs within the current SPF calculation interval, the SPF calculation is delayed by start-interval. The current SPF calculation interval is used after the SPF calculation is complete.


Example
-------

# Set the maximum interval for performing the SPF calculation to 10000 ms, the initial interval to 700 ms, and the hold interval to 4000 ms.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] spf-schedule-interval intelligent-timer 10000 700 4000

```

# Set the interval at which OSPFv3 route calculation is performed to 5s and the hold interval at which OSPFv3 route calculation is performed to 6s.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] spf-schedule-interval 5 6

```