display qos buffer-monitoring result history
============================================

display qos buffer-monitoring result history

Function
--------



The **display qos buffer-monitoring result history** command displays historical congestion monitoring information about queues.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display qos buffer-monitoring result history interface** { *interface-type* *interface-number* | *interface-name* } [ **queue** *queue-index* ] [ **record-number** *number-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies an interface type. | - |
| *interface-number* | Specifies an interface number. | The value is a string case-sensitive characters. It cannot contain spaces. |
| **queue** *queue-index* | Specifies the index of a queue to be queried. | The value is an integer ranging from 0 to 7. |
| **record-number** *number-value* | Specifies the number of records to be queried. | The value is an integer ranging from 1 to 100. The default value is 10. |
| **interface** *interface-name* | Specifies an interface name. | The value is a string case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

When the buffer usage of a queue enabled with congestion monitoring reaches the upper buffer threshold and then falls below the lower buffer threshold, you can run this command to check historical congestion monitoring information about each queue on an interface.

**Precautions**

* A maximum of 100 pieces of historical congestion monitoring information can be saved for each queue.
* The time precision between two pieces of historical congestion monitoring information for the same queue is within 2 ms.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display historical congestion monitoring information about queues on 100GE1/0/1.
```
<HUAWEI> display qos buffer-monitoring result history interface 100GE 1/0/1
Queue Time                         BufferUsage(Bytes)    Percent(%) 
-------------------------------------------------------------------- 
    0 2015-11-11 14:36:27.691                 1602016           100 
      2015-11-11 14:36:27.690                 1599728           100 
      2015-11-11 14:36:27.689                 1599728           100 
      2015-11-11 14:36:27.688                 1599728           100 
      2015-11-11 14:36:27.687                 1599728           100 
      2015-11-11 14:36:27.686                 1600976           100 
      2015-11-11 14:36:27.685                 1602016           100 
      2015-11-11 14:36:27.684                 1602016           100 
      2015-11-11 14:36:27.683                 1602016           100 
      2015-11-11 14:36:27.682                 1599728           100 
--------------------------------------------------------------------

```

**Table 1** Description of the **display qos buffer-monitoring result history** command output
| Item | Description |
| --- | --- |
| Queue | Queue index. |
| Time | Time when historical congestion monitoring information was recorded. |
| BufferUsage(Bytes) | Historical queue buffer value, in bytes. |
| Percent(%) | Historical queue buffer usage, in percentage. |