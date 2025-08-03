display any-flow flow-cache statistics
======================================

display any-flow flow-cache statistics

Function
--------



The **display any-flow flow-cache statistics** command displays the built-in CPU flow table for AnyFlow.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display any-flow flow-cache statistics** [ **slot** *slot-id* ]


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

You can run this command to view details about the built-in CPU flow table for AnyFlow in real time.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics on built-in CPU flow table for AnyFlow.
```
<HUAWEI> display any-flow flow-cache statistics slot 1
Slot: 1
------------------------------------------------------------------------------------------------
Type             Current           Aged           Created         Exported         Exported
                (Streams)        (Streams)       (Streams)        (Streams)        (Packets)
------------------------------------------------------------------------------------------------
Origin V4               8           124517          124525                0                0
------------------------------------------------------------------------------------------------
Origin V6               0                0               0                0                0
------------------------------------------------------------------------------------------------
Aggregate V4            0                9               9                0                0
------------------------------------------------------------------------------------------------
Aggregate V6            0                0               0                0                0
------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display any-flow flow-cache statistics** command output
| Item | Description |
| --- | --- |
| Type | Flow type. |
| Current | Number of active flows. |
| Aged | Number of aged flows. |
| Created | Number of created flows. |
| Exported (Packets) | Number of packets sent to the TDA. |
| Origin V4 | IPv4 original flow. |
| Origin V6 | IPv6 original flow. |
| Aggregate V4 | IPv4 aggregation flow. |
| Aggregate V6 | IPv6 aggregation flow. |
| Slot | slot-id. |
| Exported(Streams) | Number of flows sent to the TDA. |