spf timers
==========

spf timers

Function
--------



The **spf timers** command uses a common Shortest Path First (SPT) timer to calculate the interval at which OSPFv3 routes are calculated.

The **undo spf timers** command restores the default setting.



By default, delay-interval is 5 seconds, hold-interval is 10 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**spf timers** *delay-interval* *hold-interval*

**undo spf timers**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *delay-interval* | Specifies the interval between the network change detection and the SPF calculation. | An integer ranging from 0 to 65535, in seconds. |
| *hold-interval* | Specifies the holding interval between two consecutive SPF calculations. | An integer ranging from 0 to 65535, in seconds. |



Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Based on the local LSDB, an OSPFv3 device uses the SPF algorithm to calculate the SPT with itself as the root and determines the next hop to the destination network according to the SPT. By adjusting the SPF calculation interval, you can prevent excessive consumption of bandwidth and device resources caused by frequent network changes.

**Precautions**

The SPF common timer and SPF intelligent timer are mutually exclusive.


Example
-------

# Set both the OSPFv3 route calculation interval and the hold interval to 6 seconds.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] spf timers 6 6

```