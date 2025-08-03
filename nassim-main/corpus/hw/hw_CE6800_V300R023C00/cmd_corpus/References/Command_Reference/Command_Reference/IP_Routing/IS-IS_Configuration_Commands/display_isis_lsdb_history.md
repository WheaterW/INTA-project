display isis lsdb history
=========================

display isis lsdb history

Function
--------



The **display isis lsdb history** command displays information about a backup LSDB.




Format
------

**display isis** [ *process-id* ] **lsdb** [ { **level-1** | **level-2** } | **verbose** [ **no-name** ] ] \* **history** *history-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an IS-IS process. | The value is an integer ranging from 1 to 4294967295. |
| **level-1** | Displays information about a backup Level-1 LSDB. | - |
| **level-2** | Displays information about a backup Level-2 LSDB.  If no level is specified, information about Level-1 and Level-2 LSDBs is displayed. | - |
| **verbose** | Displays detailed information about a backup LSDB. | - |
| **no-name** | Displays detailed information about the LSDB, without the alias information. | - |
| **history** *history-id* | Specifies the number of times an LSDB is backed up. | The value is 1 or 2. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

If IS-IS LSPs are purged, you can run the display isis lsdb history command to assist troubleshooting.

* If IS-IS LSPs are purged, the current LSDB may be incomplete. In this case, you can run the display isis lsdb history command to check information about a backup LSDB. The command output helps with troubleshooting.
* All local LSPs are backed up, and the LSPs received from other devices that have neighbors are also backed up.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about a backup LSDB.
```
<HUAWEI> display isis lsdb verbose history 1
Backup Time : 2016-09-24 07:57:32                         
                        Database information for ISIS(1)
                        -----------------------------------
                        Level-1 Link State Database
LSPID                  Seq Num    Checksum   HoldTime       Length   ATT/P/OL
-----------------------------------------------------------------------------
0000.0000.0001.00-00*  0x00000019 0x5bb7     920            87       0/0/0
  SOURCE       router1wwwww.00
  HOST NAME    router1wwwww
  NLPID        IPV4
  NLPID        IPV6
  AREA ADDR    01
  INTF ADDR    1.1.1.1
  Topology     Standard
  NBR  ID      0000.0000.0002.01  COST: 10
  IP-Internal  1.1.1.0         255.255.255.0    COST: 10

0000.0000.0002.00-00   0x00000019 0xc561     922            89       0/0/0
  SOURCE       0000.0000.0002.00
  NLPID        IPV4
  NLPID        IPV6
  AREA ADDR    01
  INTF ADDR    1.1.1.2
  INTF ADDR    2.2.2.2
  Topology     Standard
  NBR  ID      0000.0000.0002.01  COST: 10
  IP-Internal  1.1.1.0         255.255.255.0    COST: 10
  IP-Internal  2.2.2.0         255.255.255.0    COST: 10

0000.0000.0002.01-00   0x00000016 0x6580     922            56       0/0/0
  SOURCE       0000.0000.0002.01
  NLPID        IPV4
  NLPID        IPV6
  NBR  ID      0000.0000.0002.00  COST: 0
  NBR  ID      router1wwwww.00  COST: 0

Total LSP(s): 3
    *(In TLV)-Leaking Route, *(By LSPID)-Self LSP, +-Self LSP(Extended),
           ATT-Attached, P-Partition, OL-Overload

```

# Display information about a backup LSDB.
```
<HUAWEI> display isis lsdb history 1
Backup Time : 2016-09-24 07:57:32                         
                        Database information for ISIS(1)                        
-------------------------------------------------------------------------------
                          Level-1 Link State Database
LSPID                 Seq Num      Checksum      HoldTime      Length  ATT/P/OL
-------------------------------------------------------------------------------
router1wwwww.00-00*   0x00000019   0x5bb7        920           87      0/0/0   
0000.0000.0002.00-00  0x00000019   0xc561        922           89      0/0/0   
0000.0000.0002.01-00  0x00000016   0x6580        922           56      0/0/0   
Total LSP(s): 3    *(In TLV)-Leaking Route, *(By LSPID)-Self LSP, +-Self LSP(Extended),
           ATT-Attached, P-Partition, OL-Overload

```

**Table 1** Description of the **display isis lsdb history** command output
| Item | Description |
| --- | --- |
| Backup Time | Backup time. |
| LSPID | ID of an LSP. |
| Seq Num | Sequence number of an LSP. |
| Checksum | Checksum of an LSP. |
| HoldTime | Hold time of an LSP. |
| Length | LSP length. |
| ATT/P/OL | * Attach bit (ATT). * Partition bit (P). * Overload bit (OL). |
| SOURCE | System ID of the source node. |
| HOST NAME | Dynamic hostname. |
| NLPID | Network protocol supported. |
| AREA ADDR | Area address. |
| INTF ADDR | IPv4 address of an interface. |
| Topology | Topology type. |
| NBR ID | System ID of a neighbor. |
| IP-Internal | Intra-area IPv4 route information. |
| Total LSP(s) | Total number of LSPs. |
| \*(In TLV) | leaked route. |
| \*(By LSPID) | Local LSP. |
| Len | Authentication password length. |
| COST | Cost. |