display ospf lsdb
=================

display ospf lsdb

Function
--------



The **display ospf lsdb** command displays the OSPF Link-State Database (LSDB).




Format
------

**display ospf** [ *process-id* ] **lsdb** [ { [ { **router** | **network** | **summary** | **asbr** | **ase** | **opaque-as** [ **origin** ] | **opaque-area** [ **origin** ] | **opaque-link** [ **origin** ] | **nssa** } [ *link-state-id* ] ] [ **originate-router** [ *advertising-router-id* ] | **hostname** *hostname* | **self-originate** ] } ] [ **age** { **min-value** *min-age-value* | **max-value** *max-age-value* } \* ]

**display ospf** [ *process-id* ] **lsdb** [ { [ { **router** | **network** | **summary** | **asbr** | **ase** | **opaque-as** [ **origin** ] | **opaque-area** [ **origin** ] | **opaque-link** [ **origin** ] | **nssa** } [ *link-state-id* ] ] [ **originate-router** [ *advertising-router-id* ] | **self-originate** ] } ] [ **age** { **min-value** *min-age-value* | **max-value** *max-age-value* } \* ] **resolve-hostname**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | process-id. | The value is an integer ranging from 1 to 4294967295. |
| **router** | Displays historical information about Router LSAs. | - |
| **network** | Displays historical information about Network LSAs. | - |
| **summary** | Displays information about the network summary LSA. | - |
| **asbr** | Displays historical information about ASBR-summary LSAs. | - |
| **ase** | Displays information about the AS external LSA. | - |
| **opaque-as** | Displays information about the opaque AS LSA. | - |
| **origin** | Display the original content of the LSA. | - |
| **opaque-area** | Displays information about the opaque area LSA. | - |
| **opaque-link** | Displays information about the opaque link LSA. | - |
| **nssa** | Displays information about the status of external links in the NSSA. | - |
| *link-state-id* | Specifies the LSID of an LSA. | The value is in dotted decimal notation. |
| **originate-router** | Displays the LSA of the advertising router. | - |
| *advertising-router-id* | Specifies the router ID of the LSA advertising device. | The value is in dotted decimal notation. |
| **hostname** *hostname* | Displays information about the LSDB of a host. | The value is a string of 1 to 255 case-insensitive characters, spaces not supported. |
| **self-originate** | Displays the status of self-generated links. | - |
| **age** | Displays the LSAs that age in the scope. | - |
| **min-value** *min-age-value* | Displays the LSAs that age equal or more than min-age-value. | The value is an integer ranging from 0 to 3600. |
| **max-value** *max-age-value* | Displays the LSAs that age equal or less than max-age-value. | The value is an integer ranging from 0 to 3600. |
| **resolve-hostname** | Displays the hostname resolved from a router ID. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display ospf lsdb** command displays information about the LSDB in various modes, including:

* Brief information about the LSDB
* LSAs of a specified type
* LSAs of the originating device
* Locally originated LSAsThe command output can help you troubleshoot OSPF faults.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about network LSAs in the OSPF LSDB.
```
<HUAWEI> display ospf 1 lsdb network 10.1.1.2

          OSPF Process 1 with Router ID 1.1.1.1
                          Area: 0.0.0.0
                  Link State Database


  Type      : Network
  Ls id     : 10.1.1.2
  Adv rtr   : 2.2.2.2
  Ls age    : 571
  Len       : 32
  Options   :  E
  seq#      : 80000004
  chksum    : 0x2f08
  Net mask  : 255.255.255.0
     Attached Router: 1.1.1.1
     Attached Router: 2.2.2.2

```

# Display information about the opaque-as LSAs in the LSDB.
```
<HUAWEI> display ospf 1 lsdb opaque-as

          OSPF Process 1 with Router ID 10.2.2.1
                  Link State Database

  Type      : Opq-As
  Ls id     : 10.0.0.0
  Adv rtr   : 10.1.1.1
  Ls age    : 551
  Len       : 48
  Options   :  E
  seq#      : 8000003d
  chksum    : 0xa1ac
  Opaque Type: 7
  Opaque Id: 0
  OSPFv2 Extended Prefix Opaque LSA TLV information:
    OSPFv2 Extended Prefix TLV:
      Route Type: AS-External
      AF: IPv4-Unicast
      Flags: 0xc0 (A|N|-|-|-|-|-|-)
      Prefix: 10.1.1.0/24
      Redistribute-list Sub-TLV:
        Flags    : --
        RouterId : 0x1010101-1,0x0-0

```

# Display information about router LSAs in the OSPF LSDB.
```
<HUAWEI> display ospf 1 lsdb router 1.1.1.1

          OSPF Process 1 with Router ID 1.1.1.1
                          Area: 0.0.0.0
                  Link State Database


  Type      : Router
  Ls id     : 1.1.1.1
  Adv rtr   : 1.1.1.1
  Ls age    : 430
  Len       : 48
  Options   :  ABR  E
  seq#      : 80000014
  chksum    : 0xf615
  Link count: 2
     Link ID: 10.1.1.2
     Data   : 10.1.1.1
     Link Type: TransNet
     Metric : 1
     Link ID: 1.1.1.1
     Data   : 255.255.255.255
     Link Type: StubNet
     Metric : 0

```

# Display information about opaque-area LSAs in the OSPF LSDB.
```
<HUAWEI> display ospf 1 lsdb opaque-area
          OSPF Process 1 with Router ID 10.1.1.1
                          Area: 0.0.0.0
                  Link State Database

  Type      : Opq-Area
  Ls id     : 10.0.0.1
  Adv rtr   : 10.1.1.1
  Ls age    : 639
  Len       : 200
  Options   :  E
  seq#      : 80000001
  chksum    : 0x2175
  Opaque Type: 1
  Opaque Id: 1
  Opaque lsa information:

     00 02 00 b0 00 01 00 01 02 00 00 00 00 02 00 04
     0a 01 01 01 00 03 00 04 0a 01 01 01 00 04 00 04
     00 00 00 00 00 05 00 04 00 00 00 01 80 02 00 04
     00 00 00 01 00 06 00 04 00 00 00 00 00 07 00 04
     00 00 00 00 80 00 00 04 00 00 00 00 00 09 00 04
     00 00 00 00 00 08 00 20 00 00 00 00 00 00 00 00
     00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
     00 00 00 00 00 00 00 00 80 01 00 20 00 00 00 00
     00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
     00 00 00 00 00 00 00 00 00 00 00 00 00 0a 00 09
     00 00 00 00 00 00 00 00 00 00 00 00 00 0c 00 04
     00 01 00 01
 

  Type      : Opq-Area
  Ls id     : 10.0.0.4
  Adv rtr   : 10.1.1.1
  Ls age    : 940
  Len       : 32
  Options   :  E
  seq#      : 80000003
  chksum    : 0xbdb8
  Opaque Type: 4
  Opaque Id: 0
  Router-Information LSA TLV information:
    SR-Algorithm TLV:
      Algorithm: SPF
    SID/Label Range TLV:
      Range Size: 50001
      SID/Label Sub-TLV:
        Label: 200000
    Dynamic Hostname TLV:
      Hostname: mckck
    Node MSD TLV:
      MSD Type  : 1
      MSD Value : 10 


  Type      : Opq-Area
  Ls id     : 10.0.0.7
  Adv rtr   : 10.1.1.1
  Ls age    : 1158
  Len       : 44
  Options   :  E
  seq#      : 80000024
  chksum    : 0x58fc
  Opaque Type: 7
  Opaque Id: 0
  OSPFv2 Extended Prefix Opaque LSA TLV information:
    OSPFv2 Extended Prefix Range TLV:
      AF: IPv4-Unicast
      Flags: 0x00 (-|-|-|-|-|-|-|-)
      Prefix: 10.5.5.5/32
      Range: 1
      Prefix SID Sub-TLV:
        Flags: 0x60 (-|NP|M|-|-|-|-|-)
        MT ID: 0
        Algorithm: SPF
        Index: 1
                          Area: 0.0.0.1
                  Link State Database


  Type      : Opq-Area
  Ls id     : 10.0.0.8
  Adv rtr   : 10.1.1.1
  Ls age    : 13
  Len       : 56
  Options   :  E
  seq#      : 8000014a
  chksum    : 0x7ff8
  Opaque Type: 8
  Opaque Id: 0
  OSPFv2 Extended Link Opaque LSA TLV information:
    OSPFv2 Extended Link TLV:
      Link Type: P-2-P
      Link ID: 10.2.2.2
      Link Data: 10.0.0.12
      Remote IPv4 Address Sub-TLV:
        Remote Address: 10.0.0.2
      Local Remote Interface ID Sub-TLV:
        Local Interface ID: 9
        Remote Interface ID: 0

```

# Display original information about Opaque-area LSAs in the LSDB.
```
<HUAWEI> display ospf 1 lsdb opaque-area origin
          OSPF Process 1 with Router ID 10.1.1.1
                          Area: 0.0.0.0
                  Link State Database

  Type      : Opq-Area
  Ls id     : 10.0.0.4
  Adv rtr   : 10.1.1.1
  Ls age    : 4
  Len       : 64
  Options   :  E
  seq#      : 80000003
  chksum    : 0x71fd
  Opaque Type: 4
  Opaque Id: 0
  Opaque lsa information:

     00 08 00 01 00 00 00 00 00 09 00 0c 00 03 e9 00 
     00 01 00 03 00 3e 80 00 00 07 00 06 48 55 41 57 
     45 49 00 00 00 0c 00 02 01 0a 00 00

```

# Display information about the OSPF LSDB.
```
<HUAWEI> display ospf lsdb
          OSPF Process 1 with Router ID 10.1.1.1
                  Link State Database

                          Area: 0.0.0.0
 Type      LinkState ID    AdvRouter        Age  Len   Sequence       Metric
 Router    10.1.1.1         10.1.1.1           93  48    80000004            1
 Router    10.2.2.2         10.2.2.2           92  48    80000004            1
 Sum-Net   172.16.1.0      10.1.1.1         1287  28    80000002            2
 Sum-Net   192.168.1.0     10.1.1.1         1716  28    80000001            1
 Sum-Net   172.17.1.0      10.2.2.2         1336  28    80000001            2
 Sum-Net   192.168.2.0     10.2.2.2           87  28    80000002            1

```

**Table 1** Description of the **display ospf lsdb** command output
| Item | Description |
| --- | --- |
| Link Data | Link data. |
| Link Type | Link type of the OSPFv2 extended link TLV. |
| Link ID | For extended link TLVs, Link ID indicates the OSPFv2 link ID.  For router LSAs, link IDs have different meanings in different link types.   * If the link type is P2P, Link ID indicates the router ID of the neighbor. * If the link type is TransNet, Link ID indicates the IP address of the DR. * If the link type is Stub, Link ID indicates the IP address. * If the link type is Virtual Link, Link ID indicates the router ID of the neighbor. |
| Link count | Number of router LSA links. |
| Type | LSA type: Router, Network, Sum-Net, Sum-Asbr, NSSA, External, Opq-Link, Opq-Area, or Opq-As. |
| LinkState ID | Link State ID in the LSA header. |
| AdvRouter | Device that advertises or generates LSAs. |
| Age | Aging time of an LSA. |
| Len | LSA length. |
| Sequence | Sequence number in the LSA header. |
| Metric | Metric value. |
| Ls age | Aging time of the LSA. |
| Ls id | Link state ID of the LSA that causes route calculation. |
| Adv rtr | Router ID of the device that generates the LSA that causes route calculation. |
| Options | Capability options supported by the device:   * E: allows the flooding of AS-External-LSAs. * MC: forwards IP multicast packets. * N/P: indicates that Type 7 LSAs can be processed. * DC: processes on-demand links. * DN: prevents loops on a BGP/MPLS IP VPN. * O: indicates that the originating device supports Opaque LSAs (Type 9, Type 10, and Type 11). * V: If the device is an endpoint of one or more virtual links in the Full state, the V bit is set when the device advertises Router LSAs to the transit area of the virtual link. * ASBR: The device is an ASBR. * ABR: The device is an ABR.   The actual support depends on the device. |
| chksum | Check LSDB num. |
| Net mask | (Network LSA) network mask. |
| Attached Router | (Network LSA) router that connects to the network. |
| Opaque lsa information | Detailed Opaque LSA information. |
| Opaque Id | Used to distinguish different LSAs of the same application type. The Opaque Type and Opaque ID together form the link state ID in the LSA header. |
| Opaque Type | LSA application type.  Value 1 indicates traffic engineering; value 3 indicates OSPF graceful restart. |
| OSPFv2 Extended Prefix Range TLV | OSPFv2 Extended Prefix Range TLV information. |
| OSPFv2 Extended Prefix TLV | OSPFv2 extended prefix TLV information. |
| OSPFv2 Extended Link TLV | OSPFv2 Extended Link TLV information. |
| OSPFv2 Extended Prefix Opaque LSA TLV information | OSPFv2 extended prefix Opaque LSA TLV information. |
| OSPFv2 Extended Link Opaque LSA TLV information | OSPFv2 extended link Opaque LSA TLV information. |
| Prefix | Prefix information. |
| Prefix SID Sub-TLV | Information about the OSPFv2 prefix SID sub-TLV. |
| Route Type | Route type. |
| Flags | OSPFv2 extended prefix range TLV flag. |
| Flags | Flag of the flexible algorithm prefix metric sub-TLV. |
| Flags | Flexible algorithm definition flag. |
| RouterId | Router ID of the device. |
| Data | (Router LSA) Link Data:   * If the link type is P2P, TransNet, or Virtual Link, Data indicates the IP address. * If the link type is Stub, Link Data indicates the mask of the IP address. |
| Router-Information LSA TLV information | Router-information (RI) LSA TLV information. |
| SR-Algorithm TLV | SR-Algorithm TLV information. |
| SID/Label Range TLV | SID/Label Range TLV information. |
| SID/Label Sub-TLV | SID/Label Sub-TLV information. |
| Range Size | SID range. |
| Range | Prefix Range. |
| Dynamic Hostname TLV | Dynamic Hostname TLV information. |
| Hostname | Name of the host that advertised the route. |
| Node MSD TLV | Displays the maximum stack depth TLV information of a node. |
| MSD Type | Maximum stack depth type. |
| MSD Value | Maximum stack depth. |
| MT ID | Multi-topology ID of the OSPFv2 prefix SID sub-TLV. |
| Remote IPv4 Address Sub-TLV | Remote IPv4 Address Sub-TLV information. |
| Remote Address | Remote IPv4 address. |
| Remote Interface ID | Remote interface ID. |
| Local Remote Interface ID Sub-TLV | Local Remote Interface ID Sub-TLV information. |
| Local Interface ID | Local interface ID. |
| Area | Area whose LSDB information is displayed. |
| Label | Start SID of a range. |
| AF | Address family. |
| Algorithm | Algorithm of the OSPFv2 prefix SID sub-TLV:   * SPF. * Algorithm 128â255. |
| Index | Index of the OSPFv2 prefix SID sub-TLV. |