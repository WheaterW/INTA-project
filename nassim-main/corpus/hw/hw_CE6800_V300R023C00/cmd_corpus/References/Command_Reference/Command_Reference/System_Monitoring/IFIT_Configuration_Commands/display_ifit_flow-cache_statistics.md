display ifit flow-cache statistics
==================================

display ifit flow-cache statistics

Function
--------



The **display ifit flow-cache statistics** command displays statistics in IFIT flow tables.

The **display ifit forward flow-cache statistics** command displays statistics in IFIT hardware flow tables.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ifit flow-cache statistics slot** *slot-id*

**display ifit forward flow-cache statistics slot** *slot-id* [ **chip** *chip-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **forward** | Specifies the forwarding action. | - |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |
| **chip** *chip-id* | Specifies a chip ID. | The value is an integer. The default value is 0. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to view detailed statistics about the IFIT flow table on the device.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about the IFIT hardware flow table.
```
<HUAWEI> display ifit forward flow-cache statistics slot 1
Chip: 0
-------------------------------------------------------------------------------
FlowGroupId    PolicyName       Current            Created                 Aged    
-------------------------------------------------------------------------------
1              p1                     0                  0                    0
64             -                      0                  0                    0
Total                                 0                  0                    0
-------------------------------------------------------------------------------

```

# Display IFIT flow table statistics.
```
<HUAWEI> display ifit flow-cache statistics slot 1
-------------------------------------------------------------------------------
StreamType    Current         Aged        Created        Cleared       Exported
-------------------------------------------------------------------------------
IPv4              2              0              2              0              0
-------------------------------------------------------------------------------
IPv6              2              0              2              0              0
-------------------------------------------------------------------------------
Tunnel-IPv4       2              0              2              0              0
-------------------------------------------------------------------------------
Tunnel-IPv6       2              0              2              0              0
-------------------------------------------------------------------------------

```

**Table 1** Description of the **display ifit flow-cache statistics** command output
| Item | Description |
| --- | --- |
| FlowGroupId | Flow group ID. |
| PolicyName | Policy name. |
| Current | Number of active flow tables in the display ifit flow-cache statistics command output.  Number of created flow tables in the display ifit forward flow-cache statistics command output. |
| Created | Number of created flow tables. |
| Aged | Number of aged flow tables. |
| StreamType | Flow type. |
| Cleared | Number of cleared flow tables. |
| Exported | Number of exported flow tables. |
| Chip | Chip ID. |