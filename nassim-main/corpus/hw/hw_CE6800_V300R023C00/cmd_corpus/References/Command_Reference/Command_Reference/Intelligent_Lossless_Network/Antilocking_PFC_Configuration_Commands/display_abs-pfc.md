display abs-pfc
===============

display abs-pfc

Function
--------



The **display abs-pfc** command displays the statistics on PFC frames for antilocking PFC.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6885-SAN and CE8850-SAN.



Format
------

**display abs-pfc** [ **interface** { *interface-name* | *interface-type* *interface-num* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-num* | Specifies the type and number of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| **interface** *interface-name* | Specifies an interface name. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to view the statistics on PFC frames for antilocking PFC.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the statistics on PFC frames for antilocking PFC on an interface.
```
<HUAWEI> display abs-pfc interface 100GE 1/0/1
-----------------------------------------------------------------------------------------
Interface         Queue         Received(Frames)        ReceivedRate(pps)     DeadlockNum
                             Transmitted(Frames)     TransmittedRate(pps)     RecoveryNum
-----------------------------------------------------------------------------------------
100GE1/0/1            3                118789880                    43517               0
                                               0                        0               0
-----------------------------------------------------------------------------------------

```

**Table 1** Description of the **display abs-pfc** command output
| Item | Description |
| --- | --- |
| Interface | Name of the interface on which antilocking PFC is enabled. |
| Queue | Index of the queue for which antilocking PFC is enabled. |
| Received(Frames) | Number of PFC frames received in a queue.  This number is the total number of PFC frames received when antilocking PFC and PFC are enabled for the queue. |
| ReceivedRate(pps) | Rate of PFC frames received in a queue. |
| DeadlockNum | Number of PFC deadlocks in a queue. |
| Transmitted(Frames) | Number of PFC frames sent from a queue.  This number is the total number of PFC frames sent when antilocking PFC and PFC are enabled for the queue. |
| TransmittedRate(pps) | Rate of PFC frames sent from a queue. |
| RecoveryNum | Number of recovery times after a PFC deadlock occurs in a queue. |