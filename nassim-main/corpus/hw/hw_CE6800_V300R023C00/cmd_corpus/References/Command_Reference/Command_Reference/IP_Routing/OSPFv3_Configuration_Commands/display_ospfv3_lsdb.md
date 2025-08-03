display ospfv3 lsdb
===================

display ospfv3 lsdb

Function
--------



The **display ospfv3 lsdb** command displays the OSPFv3 LSDB.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ospfv3** [ *process-id* ] **lsdb** [ **area** { *area-id* | *area-id* } ] [ [ **originate-router** *advertising-router-id* | **hostname** *hostnamestr* ] | **self-originate** ] [ { **router** | **network** | **inter-prefix** | **inter-router** | **link** | **intra-prefix** | **grace** | **router-information** | **nssa** | **e-router** } [ *link-state-id* ] ] [ **age** { **min-value** *min-age-value* | **max-value** *max-age-value* } \* ]

**display ospfv3** [ *process-id* ] **lsdb** [ [ **originate-router** *advertising-router-id* | **hostname** *hostnamestr* ] | **self-originate** ] { **external** | **e-as-external** } [ *link-state-id* ] [ **age** { **min-value** *min-age-value* | **max-value** *max-age-value* } \* ]

**display ospfv3** [ *process-id* ] **lsdb** [ **area** { *area-id* | *area-id* } ] [ **originate-router** *advertising-router-id* | **self-originate** ] [ { **router** | **network** | **inter-prefix** | **inter-router** | **link** | **intra-prefix** | **grace** | **router-information** | **e-router** } [ *link-state-id* ] ] [ **age** { **min-value** *min-age-value* | **max-value** *max-age-value* } \* ] **resolve-hostname**

**display ospfv3** [ *process-id* ] **lsdb** [ **originate-router** *advertising-router-id* | **self-originate** ] { **external** | **e-as-external** } [ *link-state-id* ] [ **age** { **min-value** *min-age-value* | **max-value** *max-age-value* } \* ] **resolve-hostname**

**display ospfv3** [ *process-id* ] **lsdb** [ **area** { *area-id* | *area-id* } ] [ [ **hostname** *hostnamestr* ] | **self-originate** ] **intra-prefix** [ *link-state-id* ] **originate-router** *advertising-router-id* [ **age** { **min-value** *min-age-value* | **max-value** *max-age-value* } \* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the OSPFv3 process ID. | The value is an integer ranging from 1 to 4294967295. |
| **area** *area-id* | Specifies the area ID. | The value can be a decimal integer or an IP address. When the value is an integer, the value ranges from 0 to 4294967295. |
| **originate-router** *advertising-router-id* | Displays OSPFv3 LSDB information on the LSA advertiser with a specified router ID. | The value is in dotted decimal notation. |
| **hostname** *hostnamestr* | Displays the OSPFv3 LSDB of the device with a specified OSPFv3 hostname. | The value is a string of 1 to 255 case-sensitive characters. It cannot contain spaces. |
| **self-originate** | Displays the status of self-generated links. | - |
| **router** | Displays the Router-LSA in the LSDB. | - |
| **network** | Displays the Network-LSA in the LSDB. | - |
| **inter-prefix** | Displays the Inter-area-prefix LSA in the LSDB. | - |
| **inter-router** | Displays the Inter-area-router LSA in the LSDB. | - |
| **link** | Displays the Link-local LSAs in the LSDB. | - |
| **intra-prefix** | Displays the Intra-area-prefix LSA in the LSDB. | - |
| **grace** | Displays the Grace-LSA in the LSDB. | - |
| **router-information** | Displays router LSA information in the LSDB. | - |
| **nssa** | Displays the NSSA-LSA in the LSDB. | - |
| **e-router** | Display the E-router-LSAs in the LSDB. | - |
| *link-state-id* | Specifies a link state ID. | The value is an IPv4 address in dotted decimal notation (X.X.X.X), for example, 10.1.1.1. |
| **age** | Displays the LSA in the age scope. | - |
| **min-value** *min-age-value* | Displays the LSAs with age greater than or equal to min-age-value. | The value is an integer ranging from 0 to 3600. |
| **max-value** *max-age-value* | Displays information about the LSAs with the age less than or equal to max-age-value. | The value is an integer ranging from 0 to 3600. |
| **external** | Displays the AS-external LSAs in the LSDB. | - |
| **e-as-external** | Displays the E-AS-External-LSA information in the database. | - |
| **resolve-hostname** | Displays information about resolved dynamic hostnames. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The display ospfv3 lsdb command displays the following information about the LSDB:

* Brief information about the LSDB
* LSAs of a specified type
* LSAs of the originating router
* Locally originated LSAsThe command output helps you troubleshoot OSPFv3 faults.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display OSPFv3 LSDB information.
```
<HUAWEI> display ospfv3 lsdb
OSPFv3 Router with ID (1.1.1.1) (Process 1)

               Link-LSA (Interface 100GE1/0/1)

Link State ID   Origin Router    Age   Seq#       CkSum      Prefix
0.0.0.4         1.1.1.1          1707  0x800000bd 0xd284          1
0.0.0.4         2.2.2.2          618   0x800000bd 0x4b20          1

               Router-Information-LSA (Interface 100GE1/0/1)

Link State ID   Origin Router    Age   Seq#       CkSum
0.0.0.0        1.1.1.1           103   0x80000001 0xa28c
0.0.0.0        2.2.2.2           733   0x80000001 0xbacb

               Router-LSA (Area 0.0.0.0)

Link State ID   Origin Router    Age   Seq#       CkSum    Link
0.0.0.1         1.1.1.1          1657  0x800000c3 0xe65d      1
0.0.0.1         2.2.2.2          1653  0x800000c1 0xcc75      1


               Network-LSA (Area 0.0.0.0)

Link State ID   Origin Router    Age   Seq#       CkSum 
0.0.0.4         2.2.2.2          1653  0x80000062 0x8f20


               Inter-Area-Prefix-LSA (Area 0.0.0.0)

Link State ID   Origin Router    Age   Seq#       CkSum 
0.0.0.2         1.1.1.1          1707  0x8000009b 0x8388
0.0.0.2         2.2.2.2          733   0x8000009b 0x65a2

               Inter-Area-Router-LSA (Area 0.0.0.0)

Link State ID   Origin Router    Age   Seq#       CkSum 
2.2.2.2         1.1.1.1          1614  0x80000062 0x456b
1.1.1.1         2.2.2.2          1614  0x80000062 0x2391

               Intra-Area-Prefix-LSA (Area 0.0.0.0)

Link State ID   Origin Router    Age   Seq#       CkSum   Prefix Reference
0.0.0.1         2.2.2.2          1653  0x80000062 0x7fce       1 Network-LSA

               Router-Information-LSA (Area 0.0.0.1)

Link State ID   Origin Router    Age   Seq#       CkSum
0.0.0.0         2.2.2.2          103   0x80000002 0x8bc0

               Router-LSA (Area 0.0.0.1)

Link State ID   Origin Router    Age   Seq#       CkSum    Link
0.0.0.1         1.1.1.1          1614  0x800000a1 0x741       1
0.0.0.1         2.2.2.2          1615  0x8000009f 0xec59      1

               AS-External-LSA

Link State ID   Origin Router    Age   Seq#       CkSum  Type
0.0.0.1         10.10.10.10      6     80000001   0x9943 E2

               E-AS-External-LSA
Link State ID   Origin Router    Age   Seq#       CkSum
0.0.0.0         1.1.1.1          1401  0x80000005 0xef48

```

# Display the NSSA-LSAs in the LSDB.
```
<HUAWEI> display ospfv3 lsdb nssa
           OSPFv3 Router with ID (3.3.3.3) (Process 1)

               NSSA-external-LSA (Area 0.0.0.1)

  LS Age: 118
  LS Type: NSSA-external-LSA
  Link State ID: 0.0.0.1
  Originating Router: 1.1.1.1
  LS Seq Number: 0x80000008
  Retransmit Count: 0
  Checksum: 0x499
  Length: 48
  Flags: (E|F|T)
   Metric Type: 2 (Larger than any link state path)
      Metric: 1
   Prefix: 2001:DB8:6::1/128
    Prefix Options: 8 (-|P|-|-|-)
    Forwarding Address: 2001:DB8::9
    Tag: 1

  LS Age: 1273
  LS Type: NSSA-external-LSA
  Link State ID: 0.0.0.0
  Originating Router: 2.2.2.2
  LS Seq Number: 0x8000000d
  Retransmit Count: 0
  Checksum: 0x38e4
  Length: 32    
  Flags: (E|F|T)
   Metric Type: 2 (Larger than any link state path)
      Metric: 1 
   Prefix: ::/0 
    Prefix Options: 0 (-|-|-|-|-)
    Forwarding Address: 2001:DB8::9
    Tag: 0      
                
  LS Age: 1521  
  LS Type: NSSA-external-LSA
  Link State ID: 0.0.0.0
  Originating Router: 3.3.3.3
  LS Seq Number: 0x80000009
  Retransmit Count: 0
  Checksum: 0x22fa
  Length: 32    
  Flags: (E|F|T)
   Metric Type: 2 (Larger than any link state path)
      Metric: 1 
   Prefix: ::/0 
    Prefix Options: 0 (-|-|-|-|-)
    Forwarding Address: 2001:DB8::9
    Tag: 0

```

# Display the E-router-LSAs in the LSDB.
```
<HUAWEI> display ospfv3 lsdb e-router

           OSPFv3 Router with ID (1.1.1.1) (Process 1)

               E-Router-LSA (Area 0.0.0.0)

  LS Age: 1269
  LS Type: E-Router-LSA
  Link State ID: 0.0.0.1
  Originating Router: 1.1.1.1
  LS Seq Number: 0x8000001c
  Retransmit Count: 0
  Checksum: 0xdc1
  Length: 64
  Flags: 0x03 (-|-|-|E|B)
  Options: 0x000013 (-|R|-|-|E|V6)

    E-Router-LSA TLV information:
    Router-Link TLV:
      Link Type: Transit Network
      Metric: 1
      Interface ID: 0x8
      Neighbor Interface ID: 0x8
      Neighbor Router ID: 1.1.1.1
      End.X SID Sub-TLV:
        Behavior: End.X with NO-PSP
        Flags: 0x00 (-|-|-|-|-|-|-|-)
        Algorithm: SPF
        Weight: 0
        SID: 2001:db8:2::1
      End.X SID Sub-TLV:
        Behavior: End.X with PSP
        Flags: 0x00 (-|-|-|-|-|-|-|-)
        Algorithm: SPF
        Weight: 0
        SID: 2001:db8:2::2
      Local Interface IPv6 Address Sub-TLV:
        2001:db8:1::1

```

# Display the Link-local LSAs in the LSDB.
```
<HUAWEI> display ospfv3 lsdb link
OSPFv3 Router with ID (2.2.2.2) (Process 1)

                Link-LSA (Interface 100GE1/0/1)
  LS Age: 11
  LS Type: Link-LSA
  Link State ID: 0.0.2.6
  Originating Router: 2.2.2.2
  LS Seq Number: 0x80000002
  Retransmit Count: 0
  Checksum: 0xEFFA
  Length: 56
  Priority: 1
  Options: 0x000013 (-|R|-|-|E|V6)
  Link-Local Address: FE80::1441:0:E213:1
  Number of Prefixes: 1
    Prefix: 2001:DB8:1::/64
Prefix Options: 0 (-|-|-|-)

```

# Display information about hostnames resolved from router IDs in the LSDB.
```
<HUAWEI> display ospfv3 lsdb resolve-hostname
OSPFv3 Router with ID (1.1.1.1) (Process 1)

               Link-LSA (Interface 100GE1/0/1)
Link State ID   Origin Router    Age   Seq#       CkSum      Prefix
0.0.0.4         RTR_BLR          263   80000005   0xD804          1
0.0.0.4         RTR_BJI          1     80000005   0xD804          1

               Router-LSA (Area 0.0.0.1)
Link State ID   Origin Router    Age   Seq#       CkSum    Link
0.0.0.1         2.2.2.2          222   80000006   0xB458      1
0.0.0.1         RTR_BLR          222   80000006   0xB458      1

               Network-LSA (Area 0.0.0.1)
Link State ID   Origin Router    Age   Seq#       CkSum 
0.0.0.4         RTR_BLR          223   80000005   0x22FA

               Intra-Area-Prefix-LSA (Area 0.0.0.1)
Link State ID   Origin Router    Age   Seq#       CkSum   Prefix Reference      
0.0.0.1         RTR_BLR          223   80000005   0x9AD1       1 Network-LSA

```

# Display information about hostnames resolved from router IDs in the Link-local LSA of the LSDB.
```
<HUAWEI> display ospfv3 lsdb link resolve-hostname
OSPFv3 Router with ID (1.1.1.1) (Process 1)

               Link-LSA (Interface 100GE1/0/1)

  LS Age: 332
  LS Type: Link-LSA
  Link State ID: 0.0.0.4
  Originating Router: 1.1.1.1
  Hostname: RTR_BLR
  LS Seq Number: 0x80000005
  Retransmit Count: 0
  Checksum: 0x249C
  Length: 64
  Priority: 1
  Options: 0x000013 (-|R|-|-|E|V6)
  Link-Local Address: FE80::3A00:10FF:FE03:0
  Number of Prefixes: 1
   Prefix: 2001:DB8::/120
    Prefix Options: 0x0 (-|-|-|-|-)

```

# Display E-AS-External-LSA information.
```
<HUAWEI> display ospfv3 1 lsdb e-as-external

           OSPFv3 Router with ID (1.1.1.1) (Process 1)

  LS Age: 463
  LS Type: E-AS-External-LSA
  Link State ID: 0.0.0.5
  Originating Router: 1.1.1.1
  LS Seq Number: 0x80000003
  Retransmit Count: 0
  Checksum: 0xe38c
  Length: 72
    External-Prefix TLV:
      Flags: (E|-|-)
       Metric Type: 2 (Larger than any link state path)
      Metric: 10223715
      Prefix: 2001:db8:1::2/128
      Prefix Options: 0 (-|-|-|-|-)
      Redistribute-list Sub-TLV:
        Flags          : --
        RedistributeId : 0x0101010100000001,0x1616161600000002

```

# Displays the Intra-area-prefix LSA in the LSDB.
```
<HUAWEI> display ospfv3 1 lsdb intra-prefix 0.0.0.1 originate-router 10.4.4.4

           OSPFv3 Router with ID (1.1.1.1) (Process 1)

               Intra-Area-Prefix-LSA (Area 0.0.0.1)

  LS Age: 180
  LS Type: Intra-Area-Prefix-LSA
  Link State ID: 0.0.0.1
  Originating Router: 10.4.4.4
  LS Seq Number: 0x80000001
  Retransmit Count: 0
  Checksum: 0xfc74
  Length: 48
  Number of Prefixes: 1
  Referenced LS Type: 0x2002
  Referenced Link State ID: 0.0.0.8
  Referenced Originating Router: 10.4.4.4
   Prefix: 2001:DB8:4::/96
    Prefix Options: 0 (-|-|-|-|-)
      Metric: 0

```

# Display Router-LSA information in the LSDB.
```
<HUAWEI> display ospfv3 lsdb router-information
OSPFv3 Router with ID (1.1.1.1) (Process 1)

               Router-Information-LSA (Interface 100GE1/0/1.1001)
  LS Age: 5
  LS Type: Router-Information-LSA
  Link State ID: 0.0.0.0
  Originating Router: 10.13.1.1
  LS Seq Number: 0x80000001
  Retransmit Count: 0
  Checksum: 0x7E3A
  Length: 100
    Hostname: abcdefghaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb

               Router-Information-LSA (Area 0.0.0.1)
  LS Age: 5
  LS Type: Router-information
  Link State ID: 0.0.0.0
  Originating Router: 10.13.1.1
  LS Seq Number: 0x80000001
  Retransmit Count: 0
  Checksum: 0x7E3A
  Length: 100
    Hostname: abcdefghasdfasdfasfdasfdasdfasdfasfdasfasdfasdfadfdfdfdfasdfasdfaaasdfassss

```

**Table 1** Description of the **display ospfv3 lsdb** command output
| Item | Description |
| --- | --- |
| Link-LSA | Description of the Link-LSA. |
| Link State ID | Link state ID in LSA header. |
| Link | Number of links in router LSAs. |
| Link Type | Link type. |
| Origin Router | Route generation device. |
| Age | Aging time of an LSA. |
| Seq# | Sequence number in the LSA header. |
| CkSum | LSA checksum. |
| Prefix | IPv6 Prefix. |
| Prefix Options | Protocol option carried in the prefix. |
| Router-Information-LSA | Description of the routes in the LSDB. |
| Router-LSA | Description of the Router-LSA. |
| Network-LSA | Description of the Network-LSA. |
| Inter-Area-Prefix-LSA | Description of the Inter-Area-Prefix-LSA. |
| Inter-Area-Router-LSA | Description of the Inter-Area-Router-LSA. |
| Intra-Area-Prefix-LSA | Description of the Intra-Area-Prefix-LSA. |
| Reference | Type of imported LSAs, including Router-LSAs and Network-LSAs. |
| AS-External-LSA | Description of the AS-external-LSA. |
| LS Age | Aging time of an LSA. |
| LS Type | LSA type:   * Router-LSAs. * Network-LSAs. * Inter-Area-Prefix-LSAs. * Inter-Area-Router-LSAs. * AS-external-LSAs. * Link-LSAs. * Intra-Area-Prefix-LSAs. |
| LS Seq Number | Sequence number in the LSA header. |
| Originating Router | Router that generated the route. |
| Retransmit Count | LSA retransmission count. |
| Metric | LSA cost. |
| Metric Type | Metric type used during calculation, which can be the IGP metric, the minimum unidirectional link-delay, or TE metric. |
| Forwarding Address | Forwarding address (ASE/NSSA LSA). |
| E-Router-LSA | Description of the E-router-LSA. |
| Interface ID | Interface ID. |
| Neighbor Interface ID | Interface ID of a neighbor. |
| Neighbor Router ID | System ID of a neighbor. |
| SID | Segment ID, which uniquely identifies a segment. |
| Local Interface IPv6 Address Sub-TLV | Local IPv6 address. |
| Link-Local Address | Link local address. |
| Number of Prefixes | Number of IPv6 prefixes in the LSA. |
| External-Prefix TLV | Description of the External-Prefix TLV. |
| Redistribute-list Sub-TLV | Description of the sub-TLV for loop detection capability re-advertisement. |
| Flags | An LSA identifier;  Flags in the Redistribute-list Sub-TLV indicates the loop detection capability. |
| RedistributeId | Flag of the loop detection capability redistribution sub-TLV. |
| Referenced LS Type | Router-LSA or network-LSA associated with the IPv6 address prefix.   * If the Referenced LS Type field is 0x2001, the IPv6 prefix address is associated with a router-LSA. * If the Referenced LS Type field is 0x2002, the IPv6 prefix address is associated with a network-LSA. |
| Referenced Link State ID | Referenced LS ID.   * If Referenced LS Type is 0x2001, Referenced Link State ID should be 0. * If Referenced LS Type is 0x2002, Referenced Link State ID should be the DR's interface ID. |
| Referenced Originating Router | ID of the associated release device. |
| Length | Length of the LSA. |
| Priority | Priority of the interface that corresponds to the link. |
| Options | OSPFv3 protocol option, special processing flag for LSA communication:   * R indicates that traffic can be forwarded. * E indicates that the device can learn external routes. * V6 indicates that IPv6 packets can be forwarded. |
| Hostname | Name of the host that advertises the route. |
| Area | Area whose LSDB information is displayed. |
| Checksum | Metric value. |
| Weight | Weight. |
| Tag | Tag value of a route. |
| Behavior | Name of a traffic behavior. |
| Algorithm | Algorithm of the prefix label. |