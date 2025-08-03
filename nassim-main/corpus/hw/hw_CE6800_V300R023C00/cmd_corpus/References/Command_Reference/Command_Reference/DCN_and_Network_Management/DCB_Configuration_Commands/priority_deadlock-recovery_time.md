priority deadlock-recovery time
===============================

priority deadlock-recovery time

Function
--------



The **priority deadlock-recovery time** command sets the recovery period for hardware-based deadlock detection.

The **undo priority deadlock-recovery time** command restores the default recovery period for hardware-based deadlock detection.



By default, the recovery period for hardware-based deadlock detection is 100 ms.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**priority** *priority* **deadlock-recovery** **time** *time*

**undo priority** *priority* **deadlock-recovery** [ **time** *time* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *priority* | Specifies the priority. | The value is an integer ranging from 0 to 7. |
| *time* | Specifies the recovery period for hardware-based deadlock detection. | The value is an integer that ranges from 0 to 31. The default value is 10.  The unit is determined by the dcb pfc deadlock-detect interval command. The default unit is 10 ms. The actual effective time is the product of the period accuracy parameter <interval-value> and the specified period <time>. |



Views
-----

DCB PFC view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A PFC deadlock may occur on a ring network. You can run the **priority deadlock-recovery time** command to configure the recovery time for hardware-based deadlock detection. During PFC deadlock recovery, PFC frames received by the interface are ignored. The internal scheduler resumes traffic sending or discards traffic in the specified priority queue. After the recovery period expires, the normal flow control mechanism of PFC resumes. If the system still determines that a deadlock occurs in the next deadlock detection period, the deadlock recovery process starts again.

**Prerequisites**

The priority queue for which PFC is enabled has been specified using the **priority** command.A PFC profile has been applied to an interface using the **dcb pfc enable** command in the interface view, and the PFC profile works in forcible mode.

**Precautions**

If the value of <time> is 0, the device does not perform PFC deadlock recovery when a PFC deadlock occurs. Instead, the device performs a new round of deadlock detection.


Example
-------

# Set the recovery period for hardware-based deadlock detection of priority queue 4 to 1 second.
```
<HUAWEI> system-view
[~HUAWEI] dcb pfc deadlock-detect interval 100
[~HUAWEI] dcb pfc
[~HUAWEI-dcb-pfc-default] priority 4
[*HUAWEI-dcb-pfc-default] priority 4 deadlock-recovery time 10

```