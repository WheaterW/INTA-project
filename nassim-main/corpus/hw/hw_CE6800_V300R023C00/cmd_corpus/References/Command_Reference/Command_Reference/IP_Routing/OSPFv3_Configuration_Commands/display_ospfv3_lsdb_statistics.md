display ospfv3 lsdb statistics
==============================

display ospfv3 lsdb statistics

Function
--------



The **display ospfv3 lsdb statistics** command displays the OSPFv3 LSDB.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ospfv3** [ *process-id* ] **lsdb** **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the OSPFv3 process ID. | The value is an integer ranging from 1 to 4294967295. |
| **statistics** | Indicates the statistics of the LSDB. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check OSPFv3 LSDB statistics, run this command. The command output helps diagnose faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display OSPFv3 LSDB information.
```
<HUAWEI> display ospfv3 lsdb statistics

          OSPFv3 (Process 1) DATABASE STATISTICS

 Type Of LSA              Number
 Router-LSA               :   1
 Network-LSA              :   0
 Inter-Area-Prefix-LSA    :   0
 Inter-Area-Router-LSA    :   0
 AS-External-LSA          :   1
 NSSA-external-LSA        :   0
 Link-LSA                 :   0
 Intra-Area-Prefix-LSA    :   0
 Grace LSA                :   0
 AS-RI-LSA                :   0
 Area-RI-LSA              :   0
 Link-RI-LSA              :   0
 
 E-Router-LSA             :   2
 E-AS-External-LSA        :   5
 Area-Locator-LSA         :   1
 Intra-Area-TE-LSA        :   1

 Unknown-LSA              :   0

 Total Number Of LSAs     :   11

```

**Table 1** Description of the **display ospfv3 lsdb statistics** command output
| Item | Description |
| --- | --- |
| Type Of LSA | LSA type. |
| Router-LSA | Number of Router-LSAs. |
| Network-LSA | Number of Network-LSAs. |
| Inter-Area-Prefix-LSA | Number of Inter-Area-Prefix-LSAs. |
| Inter-Area-Router-LSA | Number of Inter-Area-Router-LSAs. |
| AS-External-LSA | Number of AS-external-LSAs. |
| NSSA-external-LSA | Number of NSSA-external-LSAs. |
| Link-LSA | Number of Link-LSAs. |
| Intra-Area-Prefix-LSA | Number of Intra-Area-Prefix-LSAs. |
| Grace LSA | Number of Grace LSAs. |
| AS-RI-LSA | Number of AS-RI-LSAs. |
| Area-RI-LSA | Number of Area-RI-LSAs. |
| Link-RI-LSA | Number of Link-RI-LSAs. |
| E-AS-External-LSA | Number of E-AS-External-LSA. |
| Unknown-LSA | Unknown LSA. |
| Total Number Of LSAs | Total number of LSAs. |
| E-Router-LSA | Number of E-Router-LSAs. |
| Area-Locator-LSA | Number of Area-Locator-LSAs. |
| Intra-Area-TE-LSA | Number of Intra-Area-TE-LSAs. |