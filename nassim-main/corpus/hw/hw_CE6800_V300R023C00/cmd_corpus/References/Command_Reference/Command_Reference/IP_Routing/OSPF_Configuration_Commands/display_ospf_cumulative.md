display ospf cumulative
=======================

display ospf cumulative

Function
--------



The **display ospf cumulative** command displays OSPF statistics.




Format
------

**display ospf** [ *process-id* ] **cumulative**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an OSPF process.  If no OSPF process ID is specified, statistics of all the OSPF processes are displayed. | The value is an integer that ranges from 1 to 4294967295. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view OSPF statistics, run the display ospf cumulative command. The command output can help you troubleshoot OSPF faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display OSPF statistics.
```
<HUAWEI> display ospf cumulative

          OSPF Process 1 with Router ID 1.1.1.1
                  Cumulations

  IO Statistics
               Type        Input     Output
              Hello        17591      17701
     DB Description            9         12
     Link-State Req            4          4
  Link-State Update          209        109
     Link-State Ack          100        202

  ASE: (Disabled)
  LSAs originated by this router
  Router: 1
  Network: 2
  Sum-Net: 0
  Sum-Asbr: 0
  External: 0
  NSSA: 0
  Opq-Link: 0
  Opq-Area: 0
  Opq-As: 0
  LSAs Originated: 3  LSAs Received: 206

  Routing Table:
    Intra Area: 1  Inter Area: 0  ASE: 0

  Up Interface Cumulate: 1
      Interface Cumulate:
  =======================================================

     Interface cumulative data. (Process 1)
  -------------------------------------------------------
  Down:        0 Loopback:     0 Waiting:     0 P-2-P:    0
  DR:          0 BDR:          1 DROTHER:     0

      Neighbor Cumulate:
  =======================================================

     Neighbor cumulative data. (Process 1)
  -------------------------------------------------------
  Down:        0 Init:         0 Attempt:     0 2-Way:    0
  Exstart:     0 Exchange:     0 Loading:     0 Full:     1
  Retransmit Count: 0

      Interface cumulative data. (Total)
  -------------------------------------------------------
  Down:     0 Loopback:     0 Waiting:     0 P-2-P:    0
  DR:       0 BDR:          1 DROTHER:     0


      Neighbor cumulative data. (Total)
  -------------------------------------------------------
  Down:        0 Init:         0 Attempt:     0 2-Way:    0
  Exstart:     0 Exchange:     0 Loading:     0 Full:     1
  Retransmit Count: 0

```

**Table 1** Description of the **display ospf cumulative** command output
| Item | Description |
| --- | --- |
| Router | Router LSA. |
| IO Statistics | Statistics of the transmitted packets and LSAs. |
| Type | OSPF packet type. |
| Input | Number of packets received. |
| Output | Number of sent packets. |
| Hello | OSPF Hello packet. |
| DB Description | OSPF Database Description packet. |
| Link-State Ack | OSPF Link State Acknowledgement packet. |
| Link-State Req | OSPF Link State Request packet. |
| Link-State Update | OSPF Link State Update packet. |
| LSAs originated by this router | Detailed statistics of the transmitted LSAs. |
| LSAs Originated | Generated LSAs. |
| LSAs Received | Received LSAs. |
| Routing Table | Routing table. |
| Intra Area | Number of intra-area routes. |
| Inter Area | Number of inter-area routes. |
| Up Interface Cumulate | Statistics of interfaces that are Up. |
| Interface cumulative data | Detailed statistics of interfaces:   * Down. * Loopback. * Waiting. * P-2-P. * DR. * BDR. * DROTHER. |
| Interface Cumulate | Interface status statistics. |
| Neighbor Cumulate | Statistics of neighbors. |
| Neighbor cumulative data | Detailed statistics of neighbors:   * Down. * Init. * Attempt. * 2-Way. * Exstart. * Exchange. * Loading. * Full. |
| Retransmit Count | Total number of nodes in the retransmission list. |
| ASE | Number of ASE routes (when there are no ASE routes, Disabled is displayed). |
| Network | Network LSA. |
| Sum-Net | Type-3 summary LSA. |
| Sum-Asbr | Type 4 summary LSA. |
| External | AS external LSA. |
| NSSA | NSSA. |
| Opq-Link | Number of Type 9 Opque LSAs. |
| Opq-Area | Number of Type 10 Opque LSAs. |
| Opq-As | Number of Type 11 Opque LSAs. |