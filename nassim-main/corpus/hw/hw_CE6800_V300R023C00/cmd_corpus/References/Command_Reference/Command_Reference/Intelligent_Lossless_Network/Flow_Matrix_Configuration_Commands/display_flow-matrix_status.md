display flow-matrix status
==========================

display flow-matrix status

Function
--------



The **display flow-matrix status** command displays Flow Matrix configuration and status.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display flow-matrix status** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to view Flow Matrix configuration and status.

**Precautions**

If no slot ID is specified, you can run this command to view Flow Matrix configuration and status in all slots.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display Flow Matrix configuration and status.
```
<HUAWEI> display flow-matrix status
Slot : 1  Chip : 0
-------------------------------------------------------------
Source            Destination       Flow-Rail       Status
-------------------------------------------------------------
10.1.1.2          10.1.2.1          100GE1/0/1      Normal
10.1.1.3          10.1.2.1          100GE1/0/1      Normal
10.1.1.4          10.1.2.1          100GE1/0/2      Abnormal
-------------------------------------------------------------

```

**Table 1** Description of the **display flow-matrix status** command output
| Item | Description |
| --- | --- |
| Slot | Slot ID. |
| Chip | Chip ID. |
| Source | Source IP address. |
| Destination | Destination IP address. |
| Flow-Rail | Flow rail. |
| Status | Effective status of a flow path planning rule in the Flow Matrix.   * Normal: The path planning rule takes effect normally. * Abnormal: The Flow Matrix function is abnormal and the path planning rule cannot take effect. |