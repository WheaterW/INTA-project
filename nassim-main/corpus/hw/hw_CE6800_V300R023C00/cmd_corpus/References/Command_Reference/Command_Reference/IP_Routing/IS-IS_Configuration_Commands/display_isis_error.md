display isis error
==================

display isis error

Function
--------



The **display isis error** command displays the statistics of the incorrect Link State PDUs (LSPDUs) and Hello packets received by an interface or a process.




Format
------

**display isis error** [ [ *process-id* | **vpn-instance** *vpn-instance-name* ] [ **interface** ] ]

**display isis error interface** { *interface-name* | *interface-type* *interface-number* }

**display isis error** *process-id* **interface** { *interface-name* | *interface-type* *interface-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an IS-IS process.  If no IS-IS process is specified, statistics about incorrect LSPs and Hello packets received by all local IS-IS processes are displayed. | The value is an integer ranging from 1 to 4294967295. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **interface** | Displays statistics about incorrect LSPs and Hello packets received by all interfaces. | - |
| **interface** *interface-name* | Specifies the name of an interface. | - |
| **interface** *interface-type* *interface-number* | Specifies the type and number of an interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When an IS-IS fault occurs, you can run this command to view various incorrect packets.You can run the **display isis error interface** command to view the number of each type of incorrect packets that are received on a specified interface.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the number of each type of incorrect packets received on all interfaces in IS-IS process 1.
```
<HUAWEI> display isis error 1
Statistics of error packets for ISIS(1)
----------------------------------------------------------------------------
LSP Packet Errors:
Longer LSP                 : 0           Smaller LSP                 : 0           
Mismatched Level           : 0           Invalid Sysid               : 0           
Zero Sequence Number       : 0           Illegal IS Type             : 0           
Zero Checksum              : 0           Incorrect Checksum          : 0           
Bad Authentication         : 0           Bad Auth Count              : 0           
More Protocol TLV          : 0           Bad Protocol TLV            : 0           
Bad NBR TLV                : 0           Bad Extended IS TLV         : 0           
Bad IF Addr TLV            : 0           Bad Reach TLV               : 0           
Bad Inter Domain TLV       : 0           Mismatched Area ID(L1)      : 0           
Bad TLV Length             : 0           Bad Alias TLV               : 0           
Bad Area TLV               : 0           Bad SRLG TLV                : 0           
Bad MT IS TLV              : 0           Bad MT ID TLV               : 0           
Bad MT IPv6 TLV            : 0           Bad IPv6 Reach TLV          : 0           
Unknown Adjacency          : 0           Bad Protocol ID             : 0           
Bad Version                : 0           Zero Lifetime               : 0           
Bad Ext Reach TLV          : 0           Bad TE Router ID TLV        : 0          
Bad TE Sub TLV             : 0           Bad Router Capability TLV   : 0           
Bad Adj SID Sub TLV        : 0           Bad Prefix SID Sub TLV      : 0           
LSP Lifetime less than 300s: 0           Bad IID TLV                 : 0
Ignored LSP Number         : 0

Hello Packet Errors:
Bad Packet Length          : 0           Reserved CircType           : 0         
Repeated System ID         : 0           Bad Circuit Type            : 0         
Longer Packet              : 0           More Area Addr              : 0          
Longer Area Addr           : 0           Bad Area Addr TLV           : 0         
More IF Addr               : 0           Bad Formatted IF TLV        : 0
More NBR SNPA(LAN)         : 0           Invalid Sysid               : 0         
Bad TLV Length             : 0           Zero HoldingTime            : 0
Unusable IP Addr           : 0           Repeated IPv4 Addr          : 0
Mismatched Area Addr(L1)   : 0           Mismatched Proto            : 0         
SNPA Conflicted(LAN)       : 0           Mismatched Level            : 0         
Mismatched Max Area Addr   : 0           Bad Authentication          : 0         
More Auth TLV              : 0           3-Way Option Error(P2P)     : 0          
No Area Addr TLV           : 0           Bad Protocol ID             : 0         
Bad Version                : 0           Invalid IPv6 Addr           : 0         
More IPv6 IF Addr          : 0           Duplicate IPv6 Addr         : 0         
More Optional Checksum     : 0           Bad Optional Checksum       : 0 ........
Bad IID TLV                : 0           No Common IID               : 0
--------------------------------------------------------------------

```

**Table 1** Description of the **display isis error** command output
| Item | Description |
| --- | --- |
| LSP packet errors | LSP errors exist. |
| LSP Lifetime less than 300s | Number of LSPs that are generated by another device and have a Remaining Lifetime value less than 300s. |
| Longer LSP | The LSP length is greater than the length that can be received. |
| Longer packet | The Hello packet length is greater than the larger value between the interface MTU and the length of the generated LSP. |
| Longer Area Addr | The area address is too long. |
| Smaller LSP | Number of LSPs with the header length shorter than the fixed length. |
| Mismatched Level | Number of LSPs with the level mismatching the local IS-IS level. |
| Mismatched Area Id(L1) | Number of Hello packets with mismatched Level-1 area ID. |
| Mismatched Area Addr(L1) | Number of LSPs with Level-1 area address mismatch. |
| Mismatched Proto | Protocol mismatch. |
| Mismatched Max Area Addr | Number of Hello packets with mismatched maximum area addresses. |
| Invalid Sysid | Invalid system ID. |
| Invalid IPv6 Addr | Number of Hello packets with invalid IPv6 addresses. |
| Zero Sequence Number | Number of LSPs with sequence number 0. |
| Zero Checksum | The checksum of an LSP is 0. |
| Zero Lifetime | Number of LSPs with remaining lifetime 0. |
| Zero HoldingTime | Number of Hello packets with the neighbor holding time being 0. |
| Illegal IS Type | The IS type is invalid. |
| Incorrect Checksum | The checksum of an LSP is incorrect. |
| Bad Authentication | Authentication failed. |
| Bad Auth Count | Number of LSPs carrying an incorrect number of authentication fields. |
| Bad Protocol TLV | Number of LSPs with incorrect protocol TLVs. |
| Bad Nbr TLV | Number of LSPs with incorrect neighbor TLVs. |
| Bad Extended IS TLV | The extended IS TLV is incorrect. |
| Bad IF Addr TLV | Number of LSPs with incorrect interface address TLVs. |
| Bad Reach TLV | Number of LSPs with incorrect Reach TLVs. |
| Bad Inter Domain TLV | Number of LSPs with incorrect inter-domain TLVs (not 0x83). |
| Bad TLV Length | Number of LSPs with incorrect TLV lengths. |
| Bad Alias TLV | Number of LSPs with incorrect Alias TLVs. |
| Bad Area TLV | Number of LSPs with incorrect area TLVs. |
| Bad SRLG TLV | Number of LSPs with incorrect SRLG TLVs. |
| Bad MT IS TLV | Number of LSPs with incorrect MT IS TLVs. |
| Bad MT ID TLV | Number of LSPs with incorrect MT ID TLVs. |
| Bad MT IPv6 TLV | Number of LSPs with incorrect MT IPv6 TLVs. |
| Bad IPv6 Reach TLV | Number of LSPs with incorrect IPv6 Reach TLVs. |
| Bad Protocol ID | Number of LSPs with incorrect protocol IDs. |
| Bad Version | Number of LSPs with incorrect protocol versions. |
| Bad Ext Reach TLV | Incorrect Ext Reach TLV. |
| Bad TE Router ID TLV | Number of LSPs with incorrect TE Router ID TLVs. |
| Bad TE Sub TLV | The TE sub-TLV is incorrect. |
| Bad Router Capability TLV | Number of LSPs with incorrect router capability TLVs. |
| Bad Adj SID Sub TLV | Number of LSPs with incorrect adjacency SID TLVs. |
| Bad Prefix SID Sub TLV | Number of LSPs with incorrect prefix SID TLVs. |
| Bad IID TLV | Number of LSPs or Hello packets with incorrect IID TLVs. |
| Bad Packet Length | Number of Hello packets with incorrect lengths. |
| Bad Circuit Type | Number of Hello packets with incorrect circuit types. |
| Bad Area Addr TLV | Number of Hello packets with incorrect area address TLVs. |
| Bad Formatted IF TLV | The format of the interface TLV is incorrect. |
| Bad Optional Checksum | Number of LSPs with error Optional Checksum TLV. |
| More Protocol TLV | The number of protocol TLVs in an LSP is greater than 1. |
| More Area Addr | Number of Hello packets with superfluous area addresses. |
| More IF Addr | Interface addresses are superfluous. |
| More Nbr SNPA(LAN) | Number of Hello packets with superfluous Sub-network Points of Attachments (SNPAs) of a neighbor in a broadcast network. |
| More Auth TLV | Number of LSPs with superfluous authentication TLVs. |
| More IPv6 IF Addr | A Hello packet carries more than 11 IPv6 addresses. |
| More Optional Checksum | Number of LSPs with more than one Optional Checksum TLV. |
| Unknown Adjacency | Number of LSPs sent by an unknown adjacency. |
| Ignored LSP Number | Number of ignored LSPs (the function of ignore-receive-lsp). |
| Hello packet errors | Number of incorrect Hello packets. |
| Reserved CircType | Number of Hello packets with incorrect reserved circuit type fields. |
| Repeated System ID | Number of Hello packets with repeated system IDs. |
| Repeated IPv4 Addr | The IPv4 address is repeated. |
| Unusable IP Addr | Number of Hello packets with the IP address in a different network segment from that of the peer. |
| SNPA Conflicted(LAN) | SNPA conflict on the broadcast network (the source MAC address of the packet conflicts with that of the local interface). |
| 3-Way Option Error(P2P) | 3-way information is incorrect. |
| No Area Addr TLV | Number of LSPs with no area address TLV. |
| No Common IID | The IID carried in the packet is different from the local IID. |
| Duplicate IPv6 Addr | Number of Hello packets with repeated IPv6 addresses. |