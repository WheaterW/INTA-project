display traffic-analysis tcp statistics
=======================================

display traffic-analysis tcp statistics

Function
--------



The **display traffic-analysis tcp statistics** command displays statistics about TCP flows involved in the intelligent traffic analysis function.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display traffic-analysis tcp statistics** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | The available slot. | The value is a string of 1 to 15 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to query statistics about TCP flows involved in the intelligent traffic analysis function. The statistics include the last time when TCP flow statistics are cleared, the number of TCP packets received by the TAP, and the number of TCP packets (in different types of TCP flows) sent to the TDA.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display TCP flow statistics on the switch.
```
<HUAWEI> display traffic-analysis tcp statistics slot 1
Slot: 1
Last time when statistics were cleared: --
---------------------------------------------------------------------------------------------------------------
Received packets: 261696740
---------------------------------------------------------------------------------------------------------------
Type                Current                 Aged              Created             Exported             Exported
                  (Streams)            (Streams)            (Streams)            (Streams)            (Packets)
---------------------------------------------------------------------------------------------------------------
TCP                       1                    0                    1                   69                   69
---------------------------------------------------------------------------------------------------------------
TCP one-way              --                   --                   --  9223372036854775807                 3677
---------------------------------------------------------------------------------------------------------------
TCP IPv6                  0                    0                    0                    0                    0
---------------------------------------------------------------------------------------------------------------
TCP IPv6 one-way         --                   --                   --                    0                    0
---------------------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display traffic-analysis tcp statistics** command output
| Item | Description |
| --- | --- |
| Last time when statistics were cleared | Last time when statistics were cleared. |
| Received packets | Number of TCP packets received by the TAP. |
| Type | TCP flow type.  -TCP: indicates TCP flows in a bidirectional flow table.  -TCP one-way: indicates TCP flows in a unidirectional flow table. |
| Current | Number of active flows. |
| Aged | Number of aged flows. |
| Created | Number of created flows. |
| Exported (packets) | Number of TCP packets sent to the TDA. |
| Slot | Slot ID of the switch. |
| Exported(streams) | Number of flows sent to the TDA. |