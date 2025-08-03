display interface counters errors
=================================

display interface counters errors

Function
--------



The **display interface counters errors** command displays error packet statistics of all service interfaces.




Format
------

**display interface counters errors** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Displays the services that use recycle resources in a specified slot. | The value is a string of 1 to 23 case-insensitive characters, spaces not supported.  The value must be set according to the device configuration. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **display interface** command to view detailed information about an interface, such as the interface status and received normal and error packets. If you only need to view statistics about error packets received by all interfaces, run this command.

**Precautions**

The displayed interfaces do not include offline interfaces, such as interfaces on pre-configured boards, management interfaces, or logical interfaces such as Eth-Trunk interfaces.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display error packet statistics of all service interfaces.
```
<HUAWEI> display interface counters errors slot 1

 interface 10GE1/0/1 Errors:
 CRC      :0                    Giants     :0
 Symbols  :0                    Alignments :0
 Runts    :0                    Jabbers    :0
 Fragments:0                    OutDiscards:0

 interface 10GE1/0/2 Errors:
 CRC      :0                    Giants     :0
 Symbols  :0                    Alignments :0
 Runts    :0                    Jabbers    :0
 Fragments:0                    OutDiscards:0

 interface 10GE1/0/3 Errors:
 CRC      :0                    Giants     :0
 Symbols  :0                    Alignments :0
 Runts    :0                    Jabbers    :0
 Fragments:0                    OutDiscards:0

 interface 10GE1/0/4 Errors:
 CRC      :0                    Giants     :0
 Symbols  :0                    Alignments :0
 Runts    :0                    Jabbers    :0
 Fragments:0                    OutDiscards:0

  ---- More ----

```

**Table 1** Description of the **display interface counters errors** command output
| Item | Description |
| --- | --- |
| CRC | Number of CRC error packets with lengths greater than or equal to 64 bytes and less than or equal to the maximum non-jumbo frame length. |
| Giants | Number of received packets with correct FCS values and with lengths greater than the maximum jumbo frame length. |
| Symbols | Number of received frames with coding errors. |
| Alignments | Number of received frames with alignment errors. |
| Runts | Number of undersized frames with correct FCS values received by the interface. Undersized frames are the frames that are shorter than 64 bytes and have the correct format and valid CRC field. |
| Jabbers | Number of received packets with incorrect FCS values and with lengths greater than the maximum non-jumbo frame length and less than or equal to the maximum jumbo frame length. |
| Fragments | Number of fragments received by on interface. Fragments are the received packets that are shorter than 64 bytes and have CRC errors. |
| OutDiscards | Number of packets discarded by the interface during physical layer detection due to queue congestion. |