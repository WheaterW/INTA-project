dcb pfc deadlock-detect interval
================================

dcb pfc deadlock-detect interval

Function
--------



The **dcb pfc deadlock-detect interval** command sets the accuracy of the hardware-based PFC deadlock detection interval and recovery time.

The **undo dcb pfc deadlock-detect interval** command restores the default accuracy of the hardware-based PFC deadlock detection interval and recovery time.



By default, the accuracy of the hardware-based PFC deadlock detection interval and recovery time is 10 ms.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dcb pfc deadlock-detect interval** *interval-value*

**undo dcb pfc deadlock-detect interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval-value* | Specifies the accuracy of the hardware-based PFC deadlock detection interval and recovery time. | The value is 10, 100, 500, or 1000, in milliseconds. The default value is 10 ms. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

A PFC deadlock may occur on a ring network. You can run the **priority deadlock-detect time** command to configure the hardware-based deadlock detection interval and run the **priority deadlock-recovery time** command to set the hardware-based deadlock recovery time. By default, the accuracy of the hardware-based deadlock detection interval and recovery time is 10 ms. You can run the **dcb pfc deadlock-detect interval** command to configure the accuracy of the hardware-based deadlock detection interval and recovery time.The actual effective time is the product of the period accuracy parameter <interval-value> and the specified period <time>.


Example
-------

# Set the accuracy of the hardware-based PFC deadlock detection interval and recovery time to 100 ms.
```
<HUAWEI> system-view
[~HUAWEI] dcb pfc deadlock-detect interval 100

```