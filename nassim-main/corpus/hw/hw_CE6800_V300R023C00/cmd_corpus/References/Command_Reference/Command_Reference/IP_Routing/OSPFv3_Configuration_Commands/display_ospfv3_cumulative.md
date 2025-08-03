display ospfv3 cumulative
=========================

display ospfv3 cumulative

Function
--------



The **display ospfv3 cumulative** command displays OSPFv3 statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ospfv3** [ *process-id* ] **cumulative**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an OSPFv3 process. If no OSPFv3 process ID is specified, statistics of all the OSPFv3 processes are displayed. | The value is an integer that ranges from 1 to 4294967295. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view OSPFv3 statistics, run the display ospfv3 cumulative command. The command output can help you troubleshoot OSPFv3 faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display OSPFv3 statistics.
```
<HUAWEI> display ospfv3 cumulative
OSPFv3 Process 1 with Router ID 1.1.1.1
                  Cumulations
  IO Statistics
  Type                    Input     Output
  Hello                    7282       7283
  DB Description              2          6
  Link State Request          1          1
  Link State Update         126         84
  Link State Ack             82        125

 ASE: Disabled

  LSAs originated by this router
  Router: 1
  Network: 0
  Inter Area Prefix Lsa: 0
  Inter Area Router Lsa: 0
  External: 0
  NSSA: 0
  Link Lsa: 1
  Intra Area Prefix Lsa: 0
  AS RI Lsa: 0
  Area RI Lsa: 0
  Link RI Lsa: 0
  E-Router Lsa: 0
  E-AS-External-LSA: 0
  Area Locator Lsa: 0
  Intra Area TE Lsa: 0
  LSAs Originated: 2  LSAs Received: 126

  Routing Table:
    Intra Area: 0  Inter Area: 0  ASE: 0

 Up Interface Cumulate: 1
 -------------------------------------------------------
 Neighbor cumulative data. (Process 1)
 -------------------------------------------------------
 Down:        0 Init:         0 Attempt:     0 2-Way:    0
 Exstart:     0 Exchange:     0 Loading:     0 Full:     1
 Retransmit Count: 0

 Neighbor cumulative data. (Total)
 -------------------------------------------------------
 Down:        0 Init:         0 Attempt:     0 2-Way:    0
 Exstart:     0 Exchange:     0 Loading:     0 Full:     1

```

**Table 1** Description of the **display ospfv3 cumulative** command output
| Item | Description |
| --- | --- |
| Router | Router LSA. |
| IO Statistics | Statistics of the transmitted packets and LSAs. |
| Type | OSPFv3 packet type. |
| Input | Number of packets received. |
| Output | Number of sent packets. |
| Hello | OSPFv3 Hello packets. |
| DB Description | OSPFv3 Database Description packet. |
| Link Lsa | Number of Link LSAs. |
| Link RI Lsa | Link scope of Router-Information LSAs. |
| LSAs originated by this router | Detailed statistics of the transmitted LSAs. |
| LSAs Originated | Generated LSAs. |
| LSAs Received | Received LSAs. |
| Inter Area Prefix Lsa | Number of Inter-area prefix LSAs. |
| Inter Area Router Lsa | Number of Inter-area router LSAs. |
| Inter Area | Number of inter-area routes. |
| Area RI Lsa | Area scope of Router-Information LSAs. |
| Area Locator Lsa | Number of Area Locator LSAs. |
| Intra Area Prefix Lsa | Number of Intra-area prefix LSAs. |
| Intra Area | Number of intra-area routes. |
| Intra Area TE Lsa | Number of intra-area TE LSAs. |
| AS RI Lsa | AS scope of Router-Information LSAs. |
| E-Router Lsa | Number of E-Router LSAs. |
| Routing Table | Routing table. |
| Up Interface Cumulate | Statistics of interfaces that are Up. |
| Neighbor cumulative data | Status of neighbors:   * Down. * Init. * Attempt. * 2-Way. * Exstart. * Exchange. * Loading. * Full. |
| Retransmit Count | Total number of nodes in the retransmission list. |
| ASE | Number of ASE routes (when there are no ASE routes, Disabled is displayed). |
| Network | Network LSA. |
| External | AS external LSA. |
| NSSA | NSSA. |
| E-AS-External-LSA | Number of E-AS-External-LSA. |