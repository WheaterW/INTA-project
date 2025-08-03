display qos headroom-usage
==========================

display qos headroom-usage

Function
--------



The **display qos headroom-usage** command displays the headroom buffer usage.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display qos headroom-usage** [ **slot** *slot-id* | **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of 1 to 31 case-sensitive characters without spaces. |
| **interface** | - | - |
| *interface-name* | Specifies an interface name. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| *interface-type* | Specifies an interface type. | - |
| *interface-number* | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to view the headroom buffer usage globally or on an interface. The command output helps you optimize the buffer space based on the actual traffic volume.If no parameter is specified, you can run this command to view the global headroom buffer usage.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the headroom buffer usage of the device.
```
<HUAWEI> display qos headroom-usage
Headroom Buffer Usage on lossless slot: (KBytes)
--------------------------------------------------------------------
Slot    Chip    Core       Total     Current        Peak     Average
--------------------------------------------------------------------
   1       0       0           0           0           0           0
--------------------------------------------------------------------

```

# Display the headroom buffer usage on 100GE1/0/1.
```
<HUAWEI> display qos headroom-usage interface 100GE 1/0/1
Headroom Buffer Usage on lossless queue: (KBytes)
Core: 0
--------------------------------------------------
Queue         Current         Peak         Average
--------------------------------------------------
    0               0            0               0
    1               0            0               0
    2               0            0               0
    3               0            0               0
    4               0            0               0
    5               0            0               0
    6               0            0               0
    7               0            0               0
--------------------------------------------------

```

**Table 1** Description of the **display qos headroom-usage** command output
| Item | Description |
| --- | --- |
| Headroom Buffer Usage on lossless queue: (KBytes) | Headroom buffer usage of a queue. |
| Headroom Buffer Usage on lossless slot: (KBytes) | Headroom buffer usage of a slot. |
| Slot | Slot ID. |
| Chip | Chip ID. |
| Core | Channel ID. |
| Total | Total buffer. |
| Current | Used buffer. |
| Peak | Peak value of the used buffer. |
| Average | Average buffer usage. |
| Queue | Queue ID. |