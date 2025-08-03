priority deadlock-detect time
=============================

priority deadlock-detect time

Function
--------



The **priority deadlock-detect time** command configures the detection period for hardware-based deadlock detection.

The **undo priority deadlock-detect time** command restores the default detection period for hardware-based deadlock detection.



By default, the detection period for hardware-based deadlock detection is 100 ms.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**priority** *priority* **deadlock-detect** **time** *time*

**undo priority** *priority* **deadlock-detect** [ **time** *time* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *priority* | Specifies the priority. | The value is an integer ranging from 0 to 7. |
| *time* | Specifies the detection period for hardware-based deadlock detection. | The value is an integer that ranges from 1 to 15. The default value is 10.  The unit is determined by the dcb pfc deadlock-detect interval command. The default unit is 10 ms. The actual effective time is the product of the period precision parameter <interval-value> and the specified period <time>. |



Views
-----

DCB PFC view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A PFC deadlock may occur on a ring network. You can run the **priority deadlock-detect time** command to configure the detection period for hardware-based deadlock detection. During the detection period, the system checks the PFC frames received by a queue. If the queue is in the PFC-XOFF (flow-controlled) state throughout the specified deadlock detection period, the system determines that a PFC deadlock occurs. In this case, the PFC deadlock recovery process needs to be performed.During PFC deadlock recovery, PFC frames received by the interface are ignored. The internal scheduler resumes traffic sending or discards traffic in the specified priority queue. After the recovery period expires, the normal flow control mechanism of PFC resumes. If the system still determines that a deadlock occurs in the next deadlock detection period, the deadlock recovery process starts again.

**Prerequisites**

The priority queue for which PFC is enabled has been specified using the **priority** command.A PFC profile has been applied to an interface using the **dcb pfc enable** command in the interface view, and the PFC profile works in forcible mode.


Example
-------

# Set the detection period for hardware-based deadlock detection of priority queue 4 to 1 second.
```
<HUAWEI> system-view
[~HUAWEI] dcb pfc deadlock-detect interval 100
[~HUAWEI] dcb pfc
[~HUAWEI-dcb-pfc-default] priority 4
[*HUAWEI-dcb-pfc-default] priority 4 deadlock-detect time 10

```