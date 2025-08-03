display isis purge packet
=========================

display isis purge packet

Function
--------



The **display isis purge packet** command displays statistics about received IS-IS purge LSPs carrying the POI TLV.




Format
------

**display isis** *process-id* **purge** **packet** [ *packet-number* ]

**display isis purge packet** *process-id* [ *packet-number* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an IS-IS process ID. | The value is an integer ranging from 1 to 4294967295. |
| *packet-number* | Specifies the number of purge LSPs whose statistics are to be displayed. | The value is an integer ranging from 1 to 70. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check statistics about received IS-IS purge LSPs carrying the POI TLV, run the **display isis purge packet** command. You can specify packet-number in the command to check statistics about a specified number of purge LSPs.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about received IS-IS purge LSPs carrying the POI TLV.
```
<HUAWEI> display isis purge packet 1 10
Purge LSP packet for ISIS(1) 
------------------------------------------------------------ 
Packet information(Index 1): 
----------------------------------------------------- 
Received LSPID      :  0000.0000.0027.00-00* 
Source Interface    :  100GE1/0/1 
Time                :  2015-1-22 13:55:06 
Level               :  Level-2 
PDU Type            :  20(Level-2 LSP) 
PDU Length          :  55 
Sequence Number     :  0x00000015 
Checksum            :  0xc891 
POI NAME            :  0000.0000.0004 
POI NAME(Neighbor)  :  0000.0000.0005   
HOST NAME           :  RT4-Pro1 
Auth Type           :  **               
0010: 83 1b 01 06 12 01 00 03 00 43 00 00 00 00 00 00 
0020: 00 27 00 00 00 01 6a 6c bd ed 01 0d 07 01 00 00 
0030: 00 00 00 01 89 0a 52 54 31 2d 50 72 6f 2d 30 31 
0040: ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** 
0050: ** ** **                          
-----------------------------------------------------
    **-Authentication TLV, *(By LSPID)-Self LSP

```

**Table 1** Description of the **display isis purge packet** command output
| Item | Description |
| --- | --- |
| Packet information(Index 1) | Information about purge LSP packets. |
| Received LSPID | ID of a received purge LSP. |
| Source Interface | Source interface of a received purge LSP. |
| Time | Time when a purge LSP was received. |
| Level | Level of a received purge LSP. |
| PDU Type | Type of received purge LSP. |
| PDU Length | Length of a received purge LSP. |
| Sequence Number | Long sequence number (LSN) of a received purge LSP. |
| Checksum | Checksum of a received purge LSP. |
| POI NAME | POI TLV carried in a received purge LSP. |
| POI NAME(Neighbor) | Neighbor system ID in the POI TLV carried in a received purge LSP. |
| HOST NAME | Dynamic hostname carried in a received purge LSP. |
| Auth Type | Authentication information carried in a received purge LSP.  This is the first official release. |