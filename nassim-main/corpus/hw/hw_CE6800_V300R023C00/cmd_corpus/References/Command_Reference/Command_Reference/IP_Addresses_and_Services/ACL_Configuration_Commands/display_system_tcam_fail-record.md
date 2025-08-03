display system tcam fail-record
===============================

display system tcam fail-record

Function
--------



The **display system tcam fail-record** command displays TCAM delivery failures.




Format
------

**display system tcam fail-record** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



When services fail to be delivered, the TCAM resource management module records delivery failures, including modules that deliver services, delivery time, and cause. You can run this command to view the causes of TCAM delivery failures.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the causes of TCAM delivery failures in slot 1.
```
<HUAWEI> display system tcam fail-record slot 1
--------------------------------------------------------------------------------
Slot  Chip Time                Service                  ErrInfo
--------------------------------------------------------------------------------
1     0    2020-12-16 14:23:01 CPCAR CP                 No entry resource
--------------------------------------------------------------------------------
Total: 1

```

**Table 1** Description of the **display system tcam fail-record** command output
| Item | Description |
| --- | --- |
| Slot | ID of the slot that delivers TCAM. |
| Chip | ID of the chip that delivers TCAM. |
| Time | TCAM delivery time. |
| Service | TCAM delivery services. |
| ErrInfo | Cause of a TCAM delivery failure. |
| Total | Total number of TCAM delivery times. |