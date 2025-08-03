priority deadlock-recovery time(Antilocking PFC profile view)
=============================================================

priority deadlock-recovery time(Antilocking PFC profile view)

Function
--------



The **priority deadlock-recovery time** command sets the recovery time for hardware-based deadlock detection.

The **undo priority deadlock-recovery time** command restores the default recovery time for hardware-based deadlock detection.



By default, the recovery time for hardware-based deadlock detection is 100 ms.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6885-SAN.



Format
------

**priority** *priority* **deadlock-recovery** **time** *time*

**undo priority** *priority* **deadlock-recovery** [ **time** *time* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *priority* | Specifies the priority. | The value is an integer ranging from 0 to 7. |
| *time* | Specifies the recovery time for hardware-based deadlock detection. | The value is an integer that ranges from 0 to 31. The default value is 10.  The unit is determined by the dcb pfc deadlock-detect interval command. The default unit is 10 ms. The actual effective time is the product of the period accuracy parameter <interval-value> and the specified period <time>. |



Views
-----

Antilocking PFC profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A PFC deadlock may occur on a ring network. You can run the **priority deadlock-recovery time** command to configure the recovery time for hardware-based deadlock detection. During PFC deadlock recovery, PFC frames received by the interface are ignored. The internal scheduler resumes traffic sending or discards traffic in the specified priority queue. After the recovery period expires, the normal flow control mechanism of PFC resumes. If the system still determines that a deadlock occurs in the next deadlock detection period, the deadlock recovery process starts again.

**Prerequisites**

The **priority** command has been run to specify the priority queue for which antilocking PFC is enabled.

**Precautions**

If the value of <time> is 0, the device does not perform PFC deadlock recovery when a PFC deadlock occurs. Instead, the device performs a new round of deadlock detection.


Example
-------

# Set the recovery time for hardware-based deadlock detection in priority queue 3 to 1.5 seconds.
```
<HUAWEI> system-view
[~HUAWEI] dcb pfc deadlock-detect interval 100
[~HUAWEI] abs-pfc profile myabspfc
[~HUAWEI-abs-pfc-myabspfc] priority 3
[*HUAWEI-abs-pfc-myabspfc] priority 3 deadlock-recovery time 15

```