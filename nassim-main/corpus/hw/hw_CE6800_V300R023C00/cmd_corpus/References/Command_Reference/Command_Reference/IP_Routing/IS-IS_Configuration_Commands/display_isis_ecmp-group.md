display isis ecmp-group
=======================

display isis ecmp-group

Function
--------



The **display isis ecmp-group** command displays the information about ECMP groups of an IS-IS process.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display isis ecmp-group** [ *process-id* ] [ **ipv6** ]

For CE6885-LL (low latency mode):

**display isis ecmp-group** [ *process-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an IS-IS process. | The value is an integer ranging from 1 to 4294967295. |
| **ipv6** | Displays the information about IPv6 routes.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view information about ECMP groups of an IS-IS process, run the display isis ecmp-group command.On a network with redundant links, if a route switchover occurs due to a link failure, this command can be used to check whether the route switchover is correctly performed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the ECMP groups of all IS-IS processes.
```
<HUAWEI> display isis ecmp-group

ISIS(1) Ecmp Group Information
----------------------------------------------------------------------------
  ECMPGroupId MTId RefCnt Flag NextHop
----------------------------------------------------------------------------
    0x10000a3    0      1 D    192.168.1.2                            

---------------------------------------------------------------------------- 
Flags: D-Direct, URT-Unicast Routing Table, M-Migp Routing Table, MIX-IPv4 over IPv6

Used ECMP Group Number: 1
Unused ECMP Group Number: 63
Unused ECMP Group List:
0x10000a4, 0x10000a5, 0x10000a6, 0x10000a7, 0x10000a8, 0x10000a9, 0x10000aa, 0x10000ab, 0x10000ac, 0x10000ad, 0x10000ae, 0x10000af, 0x10000b0, 0x10000b1, 0x10000b2, 0x10000b3, 0x10000b4, 0x10000b5, 0x10000b6, 0x10000b7, 0x10000b8, 0x10000b9, 0x10000ba, 0x10000bb, 0x10000bc, 0x10000bd, 0x10000be, 0x10000bf, 0x10000c0, 0x10000c1, 0x10000c2, 0x10000c3, 0x10000c4, 0x10000c5, 0x10000c6, 0x10000c7, 0x10000c8, 0x10000c9, 0x10000ca, 0x10000cb, 0x10000cc, 0x10000cd, 0x10000ce, 0x10000cf, 0x10000d0, 0x10000d1, 0x10000d2, 0x10000d3, 0x10000d4, 0x10000d5, 0x10000d6, 0x10000d7, 0x10000d8, 0x10000d9, 0x10000da, 0x10000db, 0x10000dc, 0x10000dd, 0x10000de

```

**Table 1** Description of the **display isis ecmp-group** command output
| Item | Description |
| --- | --- |
| ECMPGroupId | ID of an ECMP group. |
| MTId | Multi-topology ID. |
| RefCnt | Number of routes using the ECMP group ID. |
| NextHop | Next hop. |
| Used ECMP Group Number | Number of ECMP groups in use. |
| Unused ECMP Group Number | Number of remaining available ECMP groups. |
| Unused ECMP Group List | Number of remaining available ECMP group lists. |
| Flags | Route attribute.   * D: Direct route. * URT: Unicast Routing Table. |