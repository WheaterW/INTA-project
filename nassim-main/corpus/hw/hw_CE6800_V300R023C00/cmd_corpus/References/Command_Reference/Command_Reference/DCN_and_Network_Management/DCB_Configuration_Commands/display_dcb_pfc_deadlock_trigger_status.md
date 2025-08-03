display dcb pfc deadlock trigger status
=======================================

display dcb pfc deadlock trigger status

Function
--------



The **display dcb pfc deadlock trigger status** command displays the PFC deadlock detection status on an interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display dcb pfc deadlock trigger status** [ **interface** { *interface-name* | *interface-type* *interface-num* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** | Indicates an interface. | - |
| *interface-name* | Specifies an interface name. | The value is a string of 1 to 63 case-insensitive characters. It cannot contain spaces. |
| *interface-type* | Specifies an interface type. | The value is a string of 1 to 63 case-insensitive characters. It cannot contain spaces. |
| *interface-num* | Indicates an interface number. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After PFC deadlock detection is configured on an interface, you can run this command to check the detection status on the interface.

**Precautions**

The update period of this command is 20 seconds.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the PFC deadlock detection status on an interface.
```
<HUAWEI> display dcb pfc deadlock trigger status
------------------------------------------------------
Interface      Queue  TriggerMode Threshold  Status  
------------------------------------------------------
100GE1/0/1         3  TurnOff           100  TurnOff
                   4  TurnOff           100  TurnOff
100GE1/0/2         5  TurnOff            30  LinkUp
100GE1/0/3         5  ErrorDown          30  LinkDown
------------------------------------------------------

```

**Table 1** Description of the **display dcb pfc deadlock trigger status** command output
| Item | Description |
| --- | --- |
| Interface | Name of an interface. |
| Queue | Queue where PFC is enabled. |
| TriggerMode | Action taken when the number of PFC deadlocks reaches the deadlock detection threshold. |
| Threshold | Deadlock detection threshold. |
| Status | Interface status, which can be:   * LinkUp. * LinkDown. * TurnOff. * ErrorDown. * ShutDown.   When the states are overlapped, the status is displayed according to the following priorities: TurnOff > LinkUp > ShutDown > ErrorDown > LinkDown. |