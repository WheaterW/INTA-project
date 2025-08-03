clock source-lost holdoff-time
==============================

clock source-lost holdoff-time

Function
--------



The **clock source-lost holdoff-time** command configures the hold time of a clock source after its signals become invalid.



By default, the hold time of a clock source after its signals become invalid is 1000 ms.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**clock source-lost holdoff-time** *holdoff-time-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *holdoff-time-value* | Specifies the hold time of a clock source after its signals become invalid. | The value is an integer ranging from 300 to 1800, in milliseconds. The default value is 1000. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When clock source signals are lost, the device reports status changes only after a hold time to instruct the clock source selection algorithm to reselect a clock source. This processing mechanism prevents the clock source selection algorithm from frequently reselecting a clock source when clock source signals are lost for a short time.You can configure an appropriate hold time based on the following rules:

* If the current clock source becomes invalid and the device needs to immediately switch to another clock source, configure a small hold time.
* To prevent frequent clock source reselections caused by the short invalidity of the current clock source, configure a large hold time.

Example
-------

# Set the hold time after clock source signals are lost to 500 milliseconds.
```
<HUAWEI> system-view
[~HUAWEI] clock source-lost holdoff-time 500

```