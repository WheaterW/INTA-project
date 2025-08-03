display qos buffer-monitoring result
====================================

display qos buffer-monitoring result

Function
--------



The **display qos buffer-monitoring result** command displays real-time congestion monitoring information.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display qos buffer-monitoring result interface** { *interface-type* *interface-number* | *interface-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | The value is a string case-sensitive characters, spaces not supported. |
| **interface** *interface-name* | Specifies the name of an interface. | The value is a string case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After queue-based congestion monitoring is enabled, you can run this command to check real-time congestion monitoring information about each queue on an interface.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display real-time congestion monitoring information about queues on 100GE1/0/1.
```
<HUAWEI> display qos buffer-monitoring result interface 100GE 1/0/1
Queue Time           BufferUsage(Bytes) Percent(%)
----------------------------------------------------------------
  0 2015-11-11 14:36:15.208       1602016    100
  1 --                    --     --
  2 --                    --     --
  3 --                    --     --
  4 --                    --     --
  5 --                    --     --
  6 --                    --     --
  7 --                    --     --
----------------------------------------------------------------

```

**Table 1** Description of the **display qos buffer-monitoring result** command output
| Item | Description |
| --- | --- |
| Queue | Queue index. |
| Time | Time when real-time congestion monitoring information was recorded. |
| BufferUsage(Bytes) | Real-time queue buffer value, in bytes. |
| Percent(%) | Real-time queue buffer usage, in percentage. |