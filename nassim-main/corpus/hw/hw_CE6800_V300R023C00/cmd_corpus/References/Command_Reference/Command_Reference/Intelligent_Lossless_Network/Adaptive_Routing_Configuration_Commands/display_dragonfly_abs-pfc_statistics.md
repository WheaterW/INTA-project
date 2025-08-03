display dragonfly abs-pfc statistics
====================================

display dragonfly abs-pfc statistics

Function
--------



The **display dragonfly abs-pfc statistics** command displays the statistics on PFC frames in dragonfly antilocking PFC.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display dragonfly abs-pfc statistics** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* | Specifies the name of an interface. | - |
| **interface** *interface-type* *interface-number* | Specifies the type and number of an interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to view statistics on PFC frames in dragonfly antilocking PFC.

**Precautions**

The PFC frame rate in the command output is the average rate within a period of time, but not the real-time statistics. The number of PFC frames and the number of PFC deadlocks are real-time statistics. Therefore, the PFC frame rate and the number of PFC frames do not correspond to each other in real time.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics on PFC frames in dragonfly antilocking PFC on an interface.
```
<HUAWEI> display dragonfly abs-pfc statistics interface 100GE 1/0/1
-----------------------------------------------------------------------------------------
Interface         Queue         Received(Frames)        ReceivedRate(pps)     DeadlockNum
                             Transmitted(Frames)     TransmittedRate(pps)     RecoveryNum
-----------------------------------------------------------------------------------------
100GE1/0/1            3                118789880                    43517               0
                                               0                        0               0
-----------------------------------------------------------------------------------------

```

**Table 1** Description of the **display dragonfly abs-pfc statistics** command output
| Item | Description |
| --- | --- |
| Interface | Name of the interface on which dragonfly antilocking PFC is enabled. |
| Queue | Index of a queue for which dragonfly antilocking PFC is enabled. |
| Received(Frames) | Number of PFC frames received in a queue.  This number is the sum of the PFC frames received when antilocking PFC is enabled and those when PFC is enabled for the queue. |
| ReceivedRate(pps) | Rate of PFC frames received in a queue. The value is the average rate within a period of time, not the real-time statistics value. |
| DeadlockNum | Number of PFC deadlocks in a queue. |
| Transmitted(Frames) | Number of PFC frames sent from a queue.  This number is the sum of the PFC frames sent when antilocking PFC is enabled and those when PFC is enabled for the queue. |
| TransmittedRate(pps) | Rate of PFC frames sent from a queue. The value is the average rate within a period of time, not the real-time statistics value. |
| RecoveryNum | Number of recovery times after a PFC deadlock occurs in a queue. |