display ospfv3
==============

display ospfv3

Function
--------



The **display ospfv3** command displays brief information of OSPFv3.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ospfv3** [ *process-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an OSPFv3 process ID. If no process ID is specified, the brief information of all OSPFv3 processes is displayed in the ascending order of the process ID. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check brief OSPFv3 process information, run the **display ospfv3** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the brief information of OSPFv3.
```
<HUAWEI> display ospfv3
Routing Process "OSPFv3 (1)" with ID 0.0.0.0
 Route Tag: 0
 Multi-VPN-Instance is not enabled
 SPF Intelligent Timer[millisecs] Max: 10000, Start: 500, Hold: 1000
 For router-LSA and network-LSA:
  LSA Originate Intelligent Timer[millisecs] Max: 5000, Start: 500, Hold: 1000
 For other LSAs:
  LSA Originate Interval 5 seconds
  LSA Arrival Intelligent Timer[millisecs] Max: 1000, Start: 500, Hold: 500
 Default ASE parameters: Metric: 1 Tag: 1 Type: 2
 Stub router capability: enabled on-startup, timer 500 secs
 Number of AS-External LSA 0. AS-External LSA's Checksum Sum 0x0
 Number of AS-Scoped Unknown LSA 0. AS-Scoped Unknown LSA's Checksum Sum 0x0
 Number of FULL neighbors 0
 Number of Exchange and Loading neighbors 0
 Number of LSA originated 0
 Number of LSA received 0
 SPF Count          : 0
 Non Refresh LSA    : 0
 Non Full Nbr Count : 0

 Number of areas in this router is 1
 Authentication : HMAC-SHA256

```

**Table 1** Description of the **display ospfv3** command output
| Item | Description |
| --- | --- |
| Routing Process | Process ID and router ID. |
| Route Tag | Route distinguisher. |
| Multi-VPN-Instance | Whether Multi-VPN-Instance is enabled. |
| SPF Intelligent Timer[millisecs] | Intelligent timer for SPF calculation:   * Max: maximum interval for SPF calculation. * Start: initial interval for SPF calculation. * Hold: hold interval for SPF calculation. |
| SPF Count | Number of events triggered by SPF calculation. |
| LSA Originate Intelligent Timer[millisecs] | Intelligent timer for LSA regeneration:   * Max: maximum interval for generating the same LSA. * Start: initial interval for generating the same LSA. * Hold: hold interval for generating the same LSA. |
| LSA Originate Interval | Minimum interval for generating the same LSA. |
| LSA Arrival Intelligent Timer[millisecs] | Intelligent timer for LSA receiving:   * Max: maximum interval at which OSPF LSAs are received. * Start: initial interval at which OSPF LSAs are received. * Hold: hold interval at which OSPF LSAs are received. |
| Default ASE parameters | Default ASE parameters. |
| Stub router capability | Stub router capability. If on-startup is not specified when the stub-router command is run, information about this field is always displayed. If on-startup is specified when the stub-router command is run, information about this field is displayed only in the valid period during which the device keeps serving as a stub router after being restarted. |
| Number of AS-External LSA | Number of ASE LSAs. |
| Number of AS-Scoped Unknown LSA | Number of unknown LSAs in the entire AS, which is the flooding scope. |
| Number of FULL neighbors | Number of neighbors that are in the FULL state. |
| Number of Exchange and Loading neighbors | Number of neighbors in the Exchange state and the Loading state. |
| Number of LSA originated | Number of generated LSAs. |
| Number of LSA received | Number of received LSAs. |
| Number of areas in this router is | Number of areas on a device. |
| Checksum Sum | ASE LSA checksum. |
| Non Refresh LSA | Number of LSAs that are not updated in the retransmission list. |
| Non Full Nbr Count | Number of neighbors in the Exchange state and the Loading state during GR. |
| Authentication | HMAC-SHA256 authentication mode. |