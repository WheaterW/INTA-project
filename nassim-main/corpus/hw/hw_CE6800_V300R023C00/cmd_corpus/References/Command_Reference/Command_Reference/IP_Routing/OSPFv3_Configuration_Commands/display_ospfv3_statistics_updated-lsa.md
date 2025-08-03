display ospfv3 statistics updated-lsa
=====================================

display ospfv3 statistics updated-lsa

Function
--------



The **display ospfv3 statistics updated-lsa** command displays the frequent updates of the Link State Advertisements (LSAs) that the Link-state Database (LSDB) receives.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ospfv3** [ *process-id* ] **statistics** **updated-lsa** [ **originate-router** *adv-rtr-id* | **history** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an OSPFv3 process.  If no process ID is specified, this command displays brief information about the route calculation statistics in all processes. | The value is an integer that ranges from 1 to 4294967295. |
| **originate-router** *adv-rtr-id* | Specifies the router ID of an advertising device. | The value is in dotted decimal notation. |
| **history** | Displays the update records of all the received LSAs in the LSDB. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The **display ospf statistics updated-lsa** command is used to display the frequent updates of LSAs, facilitating routing flapping troubleshooting.

* If the history parameter is not configured, the **display ospf statistics updated-lsa** command only displays the updates of LSAs within the latest hour.
* If the history parameter is configured, the **display ospf statistics updated-lsa** command displays the change history of LSAs within the last 24 hours.

**Precautions**

* If you run the **reset ospfv3** command to restart the OSPFv3 process, the real-time and historical statistics on the process will be cleared.
* The **display ospfv3 statistics updated-lsa** command displays only the frequent updates of LSAs. The updated LSAs are compared with the LSAs in the local LSDB, and those with the age greater than 900 will not be displayed except those with the age of 3600.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the LSA updates within the last one hour.
```
<HUAWEI> display ospfv3 statistics updated-lsa

    OSPFv3 Process 1 with Router ID 1.1.1.1
        Statistics of Received LSAs

Begin time: 2021-11-01 02:01:08
AdvRouter            Total        Updated at:
2.2.2.2              3            2021-11-01 03:00:13
3.3.3.3              5            2021-11-01 03:00:23
4.4.4.4              5            2021-11-01 03:00:34
5.5.5.5              2            2021-11-01 03:00:47
6.6.6.6              3            2021-11-01 03:01:05
7.7.7.7              5            2021-11-01 03:01:17
8.8.8.8              6            2021-11-01 03:01:29

```

# Display the LSA updates of the specified advertising device.
```
<HUAWEI> display ospfv3 statistics updated-lsa originate-router 2.2.2.2

    OSPFv3 Process 1 with Router ID 1.1.1.1
        Statistics of Received LSAs

Begin time: 2021-11-01 02:01:08

AdvRouter: 2.2.2.2
Total               : 9            Updated at          : 2021-11-01 02:58:50
Router              : 3             Network             : 2
Inter-Area-Prefix   : 0             Inter-Area-Router   : 0
AS-external         : 0             NSSA-external       : 0
Link                : 1             Intra-Area-Prefix   : 0
Grace-LSA           : 0             AS-RI-LSA           : 0
Area-RI-LSA         : 2             Link-RI-LSA         : 0
E-Router-LSA        : 1             Area-Locator-LSA    : 0
Intra-Area-TE       : 1             E-AS-External-LSA   : 1 
Unknown-LSA         : 0

```

# Display the update records of LSAs.
```
<HUAWEI> display ospfv3 statistics updated-lsa history

        OSPFv3 Process 1 with Router ID 1.1.1.1
        History Information for Received LSAs

Record 1
Begin time  : 2021-11-01 01:01:07
End time    : 2021-11-01 02:01:08

AdvRouter           : 2.2.2.2              Total               : 1
Router              : 0                    Network             : 1
Inter-Area-Prefix   : 0                    Inter-Area-Router   : 0
AS-external         : 0                    NSSA-external       : 0
Link                : 0                    Intra-Area-Prefix   : 0
Grace-LSA           : 0                    AS-RI-LSA           : 0
Area-RI-LSA         : 0                    Link-RI-LSA         : 0
E-Router-LSA        : 1                    Area-Locator-LSA    : 0
Intra-Area-TE       : 1                    E-AS-External-LSA   : 0 
Unknown-LSA         : 0

Record 2
Begin time  : 2021-11-01 00:01:07
End time    : 2021-11-01 01:01:07

AdvRouter           : 2.2.2.2              Total               : 1
Router              : 0                    Network             : 1
Inter-Area-Prefix   : 0                    Inter-Area-Router   : 0
AS-external         : 0                    NSSA-external       : 0
Link                : 0                    Intra-Area-Prefix   : 0
Grace-LSA           : 0                    AS-RI-LSA           : 0
Area-RI-LSA         : 0                    Link-RI-LSA         : 0
E-Router-LSA        : 1                    Area-Locator-LSA    : 0
Intra-Area-TE       : 1                    E-AS-External-LSA   : 0 
Unknown-LSA         : 0

```

**Table 1** Description of the **display ospfv3 statistics updated-lsa** command output
| Item | Description |
| --- | --- |
| Router | Update times of Router LSAs. |
| Begin time | Start time of statistics collection. |
| AdvRouter | Advertising Device. |
| Total | Total update times of LSAs. |
| Updated at | Latest update time. |
| Network | Update times of Network LSAs. |
| Inter-Area-Prefix | Update times of Network Summary LSAs. |
| Inter-Area-Router | Update times of ASBR Summary LSAs. |
| AS-external | Update times of AS External LSAs. |
| NSSA-external | Update times of Type 7 LSAs. |
| Link | Update times of Type 8 LSAs. |
| Intra-Area-Prefix | Update times of Intra-Area-Prefix LSAs. |
| Grace-LSA | Update times of Type 10 LSAs. |
| AS-RI-LSA | Update times of the AS scope Router-Information-LSA. |
| Area-RI-LSA | Update times of the area scope Router-Information-LSA. |
| Link-RI-LSA | Update times of the link scope Router-Information-LSA. |
| E-Router-LSA | Update times of E-Router-LSAs. |
| Area-Locator-LSA | Update times of Area-Locator-LSA LSAs. |
| Intra-Area-TE | Number of intra-area-TE updates in an area. |
| E-AS-External-LSA | Update times of E-AS-External-LSA LSAs. |
| Unknown-LSA | Update times of Unknown-LSAs. |
| Record | Record number. |
| End time | End time of statistic collection. |