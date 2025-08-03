dcb pfc deadlock-recovery timer
===============================

dcb pfc deadlock-recovery timer

Function
--------



The **dcb pfc deadlock-recovery timer** command sets the recovery period for hardware-based deadlock detection.

The **undo dcb pfc deadlock-recovery timer** command restores the default recovery period for hardware-based deadlock detection.



By default, the recovery period for hardware-based deadlock detection is 100 ms.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**dcb pfc deadlock-recovery timer** *recovery-time*

**undo dcb pfc deadlock-recovery** [ **timer** *recovery-time* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *recovery-time* | Specifies the recovery period for hardware-based deadlock detection. | The value is an integer that ranges from 10 to 1500 ms. The default value is 100 ms. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A PFC deadlock may occur on a ring network. You can run the **dcb pfc deadlock-recovery timer** command to configure the recovery period for hardware-based deadlock detection. During PFC deadlock recovery, PFC frames received by the interface are ignored. The internal scheduler resumes traffic sending or discards traffic in the specified priority queue. After the recovery period expires, the normal flow control mechanism of PFC resumes. If the system still determines that a deadlock occurs in the next deadlock detection period, the deadlock recovery process starts again.

**Prerequisites**

A PFC profile has been applied to an interface and the PFC working mode has been set to forcible mode using the **dcb pfc enable** command in the interface view.


Example
-------

# Set the recovery period for hardware-based deadlock detection to 1000 ms.
```
<HUAWEI> system-view
[~HUAWEI] dcb pfc deadlock-recovery timer 1000

```