display flex-buffer state
=========================

display flex-buffer state

Function
--------



The **display flex-buffer state** command displays the status of the TCP FlexBuffer function.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display flex-buffer state** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* | Specifies an interface name. | - |
| **interface** *interface-type* *interface-number* | Specifies the type and number of an interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to check the parameter adjustment status of the TCP FlexBuffer function.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the status of TCP FlexBuffer. (CE6820H, CE6820S, CE6820H-K, CE6863H, CE6863H-K, CE6881H, and CE6881H-K)
```
<HUAWEI> display flex-buffer state
Low-Limit: Lower threshold of packets of all colors. The unit is Bytes.
High-Limit: Upper threshold of packets of all colors. The unit is Bytes.
Discard-Percentage: Drop probability of packets of all colors. The unit is %.
-----------------------------------------------------------------------------------------
Interface       Queue   Low-Limit   High-Limit   Discard-Percentage      Last Adjust Time
-----------------------------------------------------------------------------------------
100GE1/0/1          1      153600       512000                    1   2021-11-24 15:48:02
-----------------------------------------------------------------------------------------
100GE1/0/2          1      153600       512000                    1   2021-11-24 15:48:03
-----------------------------------------------------------------------------------------

```

# Display the status of TCP FlexBuffer. (CE6866, CE6866K, CE6860-SAN, CE6860-HAM, CE8851-32CQ8DQ-P, CE8851K, CE8850-SAN, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, and CE6863E-48S8CQ)
```
<HUAWEI> display flex-buffer state
Low-Limit: Lower threshold of packets of all colors. The unit is Bytes.
High-Limit: Upper threshold of packets of all colors. The unit is Bytes.
Discard-Percentage: Drop probability of packets of all colors. The unit is %.
Dynamic: Dynamic queue-level queue service buffer size of a mice-flow queue.
---------------------------------------------------------------------------------------------------
Current Mice-flow Packet Number: 1024
Interface       Queue   Low-Limit   High-Limit   Discard-Percentage   Dynamic      Last Adjust Time
---------------------------------------------------------------------------------------------------
100GE1/0/1          1      153600       512000                    1         6   2021-11-24 15:48:02
---------------------------------------------------------------------------------------------------
100GE1/0/2          1      153600       512000                    1         6   2021-11-24 15:48:03
---------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display flex-buffer state** command output
| Item | Description |
| --- | --- |
| Interface | Name of an interface. |
| Queue | Queue for which differentiated flow scheduling is enabled. |
| Low-Limit | Lower threshold for packets of all colors, in bytes. |
| High-Limit | Upper threshold for packets of all colors, in bytes. |
| Discard-Percentage | Drop probability of packets of all colors, in percentage. |
| Last Adjust Time | For the CE6866, CE6866K, CE6860-SAN, CE6860-HAM, CE8851-32CQ8DQ-P, CE8851K, CE8850-SAN, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, and CE6863E-48S8CQ: last time when the buffer configuration for elephant- and mice-flow queues on an interface is adjusted.  For the CE6820H, CE6820S, CE6820H-K, CE6863H, CE6863H-K, CE6881H, and CE6881H-K: last time when the buffer configuration for an elephant-flow queue on an interface is adjusted. |
| Dynamic | Dynamic buffer size of the queue-level queue service of the mice-flow queue. |
| Current Mice-flow Packet Number | Number of mice-flow packets for which the function takes effect. |