display isis lsdb
=================

display isis lsdb

Function
--------



The **display isis lsdb** command displays the LSDB information of IS-IS.




Format
------

**display isis lsdb** [ **verbose** [ **no-name** ] | { **level-1** | **level-2** } | { **local** | *lspid* | **is-name** *isname* } ] \* [ *process-id* | { **vpn-instance** *vpn-instance-name* } ]

**display isis** *process-id* **lsdb** [ { **level-1** | **level-2** } | **verbose** [ **no-name** ] | { **is-name** *isname* | **local** | *lspid* } ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **verbose** | Displays detailed LSDB information. | - |
| **no-name** | Displays detailed information about the LSDB, without the alias information. | - |
| **level-1** | Displays information about the Level-1 LSDB. | - |
| **level-2** | Displays information about the Level-2 LSDB. | - |
| **local** | Displays information about the local LSDB. | - |
| *lspid* | Specifies an LSP ID. | The value is in dotted decimal notation, ranging from 16 to 20 and in the format of ####.####.####.##-##, such as 0050.0500.5004.00-00. |
| **is-name** *isname* | Specifies a dynamic host name. | The value is a string and it has two values:   * symbolic-name: the length is from 1 to 64. * symbolic-name.XX-XX: the length is from 1 to 70.   When quotation marks are used around the string, spaces are allowed in the string. |
| *process-id* | Specifies an IS-IS process ID. | The value is an integer ranging from 1 to 4294967295. |
| **vpn-instance** *vpn-instance-name* | Displays mesh-group information about a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view the LSDB information of IS-IS, run the display isis lsdb command. If no level is specified, information about Level-1 and Level-2 LSDBs is displayed.If verbose is specified, you can view detailed information about the IS-IS LSDB, including the multi-topology (MT) ID, MT neighbor ID, and IPv6 prefix.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display extended prefix attributes in the IS-IS LSDB.
```
<HUAWEI> display isis lsdb verbose
                        Database information for ISIS(1)
                        -----------------------------------
                          
                          
                          Level-2 Link State Database

LSPID                  Seq Num    Checksum   HoldTime       Length   ATT/P/OL
-----------------------------------------------------------------------------
1111.1111.1111.00-00*  0x0000000c 0xe880     1193           365      0/0/0   
 SOURCE       1111.1111.1111.00 
 NLPID        IPV4
 NLPID        IPV6
 AREA ADDR    10
 INTF ADDR    10.1.1.1
 INTF ADDR    1.1.1.1
 INTF ADDR V6 2001:DB8:1::1
 INTF ADDR V6 2001:DB8:10::1
 Topology     Standard
+NBR  ID      2222.2222.2222.01  COST: 10
+NBR  ID      2222.2222.2222.01  COST: 10
   Lan-SRv6-X-Sid   2001:DB8:100::1:0:6  2222.2222.2222  B: 0  S: 0  P: 0  C: 0  Algorithm: 0  Weight: 0  
     Function: End.X      Flavor: NO-FLAVOR    
     Block-Len: --  NodeID-Len: --  Func-Len: --  Args-Len: --     
   Lan-SRv6-X-Sid   2001:DB8:100::1:0:7  2222.2222.2222  B: 0  S: 0  P: 0  C: 0  Algorithm: 0  Weight: 0  
     Function: End.X      Flavor: PSP     
     Block-Len: --  NodeID-Len: --  Func-Len: --  Args-Len: --     
+IP-Extended  10.1.1.0        255.255.255.0    COST: 10        
   Extended Reach Attr   Flag: X:0 R:0 N:0
+IP-Extended  1.1.1.1         255.255.255.255  COST: 0         
   Extended Reach Attr   Flag: X:0 R:0 N:1
+IP-Extended  2.2.2.2         255.255.255.255  COST: 10         
   Extended Reach Attr   Flag: X:0 R:1 N:1
 IPV6         2001:DB8:1::1/128                COST: 0          
   Extended Reach Attr   Flag: X:0 R:0 N:1
 IPV6         2001:DB8:10::/64                 COST: 10         
   Extended Reach Attr   Flag: X:0 R:0 N:0
 IPV6         2001:DB8:100::/64                COST: 0          
   Extended Reach Attr   Flag: X:0 R:0 N:0
 Router Cap   1.1.1.1          D: 0  S: 0
   Segment Routing IPv6 Cap   O: 0   C: 0
   Segment Routing MSD   Max-SL: 10   Max-End-Pop: 11   Max-H-Ins: 10   Max-H-Encap: 10   Max-End-D: 11
   Segment Routing IPv6 Router ID    2001:DB8:1::1
 SRv6 Locator 2001:DB8:100::/64                MT: 0 Metric: 0 D: 0 Algorithm: 0
   SRv6 End Sid   2001:DB8:100::1:0:3              C: 0
      Function: End         Flavor: NO-FLAVOR     
      Block-Len: --  NodeID-Len: --  Func-Len: --  Args-Len: --      
   SRv6 End Sid   2001:DB8:100::1:0:4              C: 0
      Function: End         Flavor: PSP      
      Block-Len: --  NodeID-Len: --  Func-Len: --  Args-Len: --      
   SRv6 End Sid   2001:DB8:100::1:0:5              C: 0
      Function: End         Flavor: PSP USP USD      
      Block-Len: --  NodeID-Len: --  Func-Len: --  Args-Len: --      
   Extended Reach Attr   Flag: X:0 R:0 N:0

```

# Display LSDB information of IS-IS.
```
<HUAWEI> display isis lsdb
Database information for ISIS(1)
-------------------------------------------------------------------------------------
Level-2 Link State Database
LSPID                 Seq Num      Checksum      Holdtime      Length  ATT/P/OL
-------------------------------------------------------------------------------
0000.0000.0001.00-00  0x0000017a   0xa21c             846          84  0/0/0
2222.2222.2222.00-00* 0x000001ce   0xbdcc             845         111  0/0/0
3333.3333.3333.00-00  0x00000013   0x8847            1004          84  0/0/0
3333.3333.3333.01-00  0x0000000b   0x95bc            1004          55  0/0/0
Total LSP(s): 4
*(In TLV)-Leaking Route, *(By LSPID)-Self LSP, +-Self LSP(Extended),
           ATT-Attached, P-Partition, OL-Overload

```

# Display redistList information of nodes in IS-IS LSDB.
```
<HUAWEI> display isis lsdb verbose 6501.0102.0000.00-01

                        Database information for ISIS(100)
                        -----------------------------------
                          
                          
                          Level-2 Link State Database

LSPID                  Seq Num    Checksum   HoldTime       Length   ATT/P/OL
-----------------------------------------------------------------------------
6501.0102.0000.00-01*  0x00000002 0x2290     1176           110      0/0/0   
 SOURCE       6501.0102.0000.00 
+IP-Extended  10.1.1.0       255.255.255.0    COST: 0         
   Redistribute List   6501.0102.0000 | 0x1e01010100000003
+IP-Extended  192.168.100.1         255.255.255.255  COST: 0         
   Redistribute List   6501.0102.0000 | 0x1e01010100000003
+IP-Extended  172.16.1.0       255.255.255.0    COST: 0         
   Redistribute List   6501.0102.0000 | 0x1e01010100000003
+IP-Extended  192.168.2.0        255.255.255.0    COST: 0         
   Redistribute List   6501.0102.0000

Total LSP(s): 1
    *(In TLV)-Leaking Route, *(By LSPID)-Self LSP, +-Self LSP(Extended),
           ATT-Attached, P-Partition, OL-Overload

```

**Table 1** Description of the **display isis lsdb** command output
| Item | Description |
| --- | --- |
| LSPID | ID of an LSP.  Take LSPID 0000.0000.0001.00-00 as an example. The asterisk (\*) indicates that the route is generated by the local router. 0000.0000.0001 indicates the source ID, which identifies the system ID of the router that generates the LSP. The two digits 00 behind the source ID indicate the pseudonode ID. If the two digits are not 0s, the router that generates the LSP is the DIS. The last two digits 00 indicate the fragment number. If the last two digits are 0s, it indicates that the packet is not fragmented. If the last two digits are not 0s, it indicates the fragment sequence. |
| Seq Num | LSP sequence number. |
| Checksum | LSP checksum. |
| Length | LSP length. |
| ATT/P/OL | * ATT: attach bit; * P: partition bit; * OL: indicates the overload bit. |
| SOURCE | Source node identifier. |
| +IP-Extended | Extended IPv4 routing information, which carries TE-related information. |
| Extended Reach Attr Flags | Extended prefix attribute flag. The meaning of each bit is as follows:  X: external prefix flag.  R: re-advertisement flag.  N: node flag. |
| Total LSP(s) | LSP quantity. |
| \*(In TLV) | Leaked route. |
| \*(By LSPID) | Self-LSP, which is generated by the local device. |
| Holdtime | Holdtime of an LSP. |
| Redistribute List | Redistribute list.  Redistribute List 6501.0102.0000 | 0x1e01010100000003.  The first ID is the system ID of the IS-IS that advertises the route.  The second ID is the ID carried by the imported route, which depends on the routing protocol that generates the route. If the routing protocol is OSPF, the ID is the router ID and process ID of OSPF. If the routing protocol is BGP, the ID is the instance ID of BGP and a four-byte random number. |
| COST | Route cost. |