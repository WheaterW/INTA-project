dcb pfc deadlock-detect timer
=============================

dcb pfc deadlock-detect timer

Function
--------



The **dcb pfc deadlock-detect timer** command sets the detection period for hardware-based deadlock detection.

The **undo dcb pfc deadlock-detect timer** command restores the default detection period for hardware-based deadlock detection.



By default, the detection period for hardware-based deadlock detection is 100 ms.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**dcb pfc deadlock-detect timer** *detect-time*

**undo dcb pfc deadlock-detect** [ **timer** *detect-time* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *detect-time* | Specifies the detection period for deadlock detection. | The value is an integer that ranges from 10 to 1500 ms. The default value is 100 ms. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A PFC deadlock may occur on a ring network. You can run the **dcb pfc deadlock-detect timer** command to set the detection period for hardware-based deadlock detection. During the detection period, the system checks the PFC frames received by a queue. If the queue is in the PFC-XOFF (flow-controlled) state throughout the specified detection period, the system determines that a PFC deadlock has occurred and needs to be handled.During PFC deadlock recovery, PFC frames received by the interface are ignored. The internal scheduler resumes traffic sending or discards traffic in the specified priority queue. After the recovery period expires, the normal flow control mechanism of PFC resumes. If the system still determines that a deadlock occurs in the next deadlock detection period, the deadlock recovery process starts again.

**Prerequisites**

A PFC profile has been applied to an interface and the PFC working mode has been set to forcible mode using the **dcb pfc enable** command in the interface view.


Example
-------

# Set the detection period for hardware-based deadlock detection to 512 ms.
```
<HUAWEI> system-view
[~HUAWEI] dcb pfc deadlock-detect timer 512

```