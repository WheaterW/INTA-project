spf-schedule-interval
=====================

spf-schedule-interval

Function
--------



The **spf-schedule-interval** command sets the interval for OSPF to calculate routes.

The **undo spf-schedule-interval** command restores the default setting.



By default, the intelligent timer is enabled. The maximum interval for the SPF calculation is 5000 ms, the initial interval is 50 ms, and the Holdtime interval is 200 ms.


Format
------

**spf-schedule-interval** *interval1*

**spf-schedule-interval intelligent-timer** *max-interval* *start-interval* *hold-interval* [ **conservative** ]

**spf-schedule-interval millisecond** *interval2*

**undo spf-schedule-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval1* | Specifies the interval for OSPF to perform the SPF calculation. | The value is an integer that ranges from 1 to 10, in seconds. |
| **intelligent-timer** | Sets the interval for the SPF calculation of OSPF through an intelligent timer. | - |
| *max-interval* | Specifies the maximum interval for OSPF to perform the SPF calculation. | The value ranges from 1 to 300000, in milliseconds. |
| *start-interval* | Specifies the initial interval for OSPF to perform the SPF calculation. | The value is an integer ranging from 1 to 60000, in milliseconds. |
| *hold-interval* | Specifies the Holdtime interval for OSPF to perform the SPF calculation. | The value is an integer ranging from 1 to 60000, in milliseconds. |
| **conservative** | Enables conservative mode for OSPF to perform the SPF calculation. | - |
| **millisecond** *interval2* | Specifies the interval for OSPF to perform the SPF calculation. | The value ranges from 1 to 10000, in milliseconds. |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Based on the LSDB, the device that runs OSPF calculates the SPT with itself as the root based on the SPF arithmetic, and determines the next hop to the destination network according to the SPT. By adjusting SPF calculation interval, you can reduce bandwidth and router resources that are consumed by the frequent change of the network.On a network where the convergence time of routes is required to be shorter, set millisecond as the unit of interval to increase the frequency of calculating routes. This increases route convergence. In other networking environments, the default value is recommended.When an OSPF LSDB changes, shortest paths must be recalculated. If a network changes frequently, the shortest path is calculated accordingly, resulting in excessive consumption of system resources, affecting device efficiency. You can configure an intelligent timer and set a proper interval for the SPF calculation to prevent the excessive consumption of device memory and bandwidth resources.If the intelligent timer is enabled using intelligent-timer, the interval for SPF calculation is as follows:

* The initial interval for SPF calculation is specified by the parameter start-interval.
* The interval for the SPF calculation for the nth (nâ¥2) time is equal to hold-interval x 2^(n-2).
* When the interval specified by hold-interval x 2^(n-2) reaches the maximum interval specified by max-interval, OSPF always uses the maximum interval for SPF calculation.
* If the interval between the last SPF calculation and the current SPF calculation exceeds max-interval and no flapping occurs within max-interval, the intelligent timer exits.
* If no flapping occurs in the previous SPF calculation but flapping occurs in the current SPF calculation, the SPF calculation is delayed by start-interval. After the SPF calculation is complete, the current interval is used.If a common timer is used, the interval for the SPF calculation is as follows:
* The interval for the first SPF calculation is 0. That is, the SPF calculation is performed immediately after the first route change is received.
* The interval for the SPF calculation for the nth (nâ¥2) time is specified by interval1 or millisecond interval2.

Example
-------

# Set the interval for OSPF to calculate routes to 6s.
```
<HUAWEI> system-view
[~HUAWEI] ospf 100
[*HUAWEI-ospf-100] spf-schedule-interval 6

```