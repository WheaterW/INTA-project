display traffic-analysis udp statistics
=======================================

display traffic-analysis udp statistics

Function
--------



The **display traffic-analysis udp statistics** command displays statistics about UDP flows involved in the intelligent traffic analysis function.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display traffic-analysis udp statistics** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | ID of an available slot. | The value is a string of 1 to 15 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to query statistics about UDP flows involved in the intelligent traffic analysis function. The statistics include the last time when TCP flow statistics are cleared, the number of TCP packets received by the TAP, and the number of TCP packets (in different types of TCP flows) sent to the TDA.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display UDP flow statistics on a switch.
```
<HUAWEI> display traffic-analysis udp statistics slot 1
Slot: 1
PTP time lock success : yes
Last time when statistics were cleared: --
-------------------------------------------------------------------------------------------------------------------
Received packets: 261696740                                                                                        
-------------------------------------------------------------------------------------------------------------------
Type      Direction     Current                 Aged              Created             Exported             Exported
                      (Streams)            (Streams)            (Streams)            (Streams)            (Packets)
-------------------------------------------------------------------------------------------------------------------
UDP       Inbound             1                    0                    1                   69                   69
UDP       Outbound            1                    0                    1                   69                   69
-------------------------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display traffic-analysis udp statistics** command output
| Item | Description |
| --- | --- |
| PTP time lock success | PTP clock synchronization status.  The value is no in either of the following cases:   * PTP is disabled. * PTP is enabled, but the clock source is an external clock source and the clock is not locked.   The value is yes in either of the following cases:   * PTP is enabled and the clock source is the local clock source. * PTP is enabled, the clock source is an external clock source, and the clock is locked. |
| Last time when statistics were cleared | Last time when statistics were cleared. |
| Received packets | Number of UDP packets received by the TAP. |
| Type | UDP Flow type. The value is UDP. |
| Direction | Flow direction.   * Inbound. * Outbound. |
| Current | Number of active flows. |
| Aged | Number of aged flows. |
| Created | Number of created flows. |
| Exported (packets) | Number of UDP packets sent to the TDA. |
| Slot | Slot ID of the switch. |
| Exported(streams) | Number of flows sent to the TDA. |