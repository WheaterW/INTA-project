display ospf statistics updated-lsa
===================================

display ospf statistics updated-lsa

Function
--------



The **display ospf statistics updated-lsa** command displays the frequent updates of the LSAs that the LSDB receives.




Format
------

**display ospf** [ *process-id* ] **statistics** **updated-lsa** [ **originate-router** *adv-rtr-id* | **history** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an OSPF process.  If no process ID is specified, this command displays brief information about all processes. | The value is an integer ranging from 1 to 4294967295. |
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

* If you run the **reset ospf** command to restart the OSPF process, the real-time and historical statistics on the process are cleared.
* The **display ospf statistics updated-lsa** command is used only to display the frequent updates of LSAs. The updated LSAs are compared with the LSAs in the local LSDB, and those with the age greater than 900 (except those with the age of 3600) will not be displayed.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the LSA updates within the last one hour.
```
<HUAWEI> display ospf statistics updated-lsa
OSPF Process 1 with Router ID 1.1.1.1
               Statistics of Received LSAs

 Begin time: 11:37:32/2011/04/25

 AdvRouter           Total        Updated at
 1.1.1.1             18           11:37:40/2011/04/25
 2.2.2.2             5            11:37:40/2011/04/25
 3.3.3.3             5            11:37:41/2011/04/25
 4.4.4.4             5            11:37:41/2011/04/25
 5.5.5.5             2            11:37:40/2011/04/25
 6.6.6.6             3            11:37:40/2011/04/25
 7.7.7.7             5            11:37:40/2011/04/25
 8.8.8.8             6            11:37:41/2011/04/25

```

# Display the update records of LSAs.
```
<HUAWEI> display ospf statistics updated-lsa history
OSPF Process 1 with Router ID 1.1.1.1
          History Information for Received LSAs

 Record  1:
 Begin time: 11:39:32/2011/04/25
 End   time: 11:41:32/2011/04/25

 no Record

 Record  2:
 Begin time: 11:37:32/2011/04/25
 End   time: 11:39:32/2011/04/25

 AdvRouter      : 1.1.1.1           Total           : 18
 Router(1)      : 0                 Network(2)      : 0
 Summary-Net(3) : 0                 Summary-Asbr(4) : 18
 External(5)    : 0                 NSSA(7)         : 0
 Opaque-link(9) : 0                 Opaque-area(10) : 0
 Opaque-as(11)  : 0

 AdvRouter      : 2.2.2.2           Total           : 5
 Router(1)      : 3                 Network(2)      : 2
 Summary-Net(3) : 0                 Summary-Asbr(4) : 0
 External(5)    : 0                 NSSA(7)         : 0
 Opaque-link(9) : 0                 Opaque-area(10) : 0
 Opaque-as(11)  : 0

 AdvRouter      : 3.3.3.3           Total           : 5
 Router(1)      : 3                 Network(2)      : 2
 Summary-Net(3) : 0                 Summary-Asbr(4) : 0
 External(5)    : 0                 NSSA(7)         : 0
 Opaque-link(9) : 0                 Opaque-area(10) : 0
 Opaque-as(11)  : 0

 AdvRouter      : 4.4.4.4           Total           : 5
 Router(1)      : 2                 Network(2)      : 2
 Summary-Net(3) : 0                 Summary-Asbr(4) : 0
 External(5)    : 1                 NSSA(7)         : 0
 Opaque-link(9) : 0                 Opaque-area(10) : 0
 Opaque-as(11)  : 0

```

# Display the LSA updates of the specified advertising device.
```
<HUAWEI> display ospf statistics updated-lsa originate-router 1.1.1.1
OSPF Process 1 with Router ID 2.2.2.2
               Statistics of Received LSAs

 Begin time: 11:37:32/2011/04/25

 AdvRouter      : 1.1.1.1
 Total          : 6                 Updated at      : 11:37:41/2011/04/25
 Router(1)      : 3                 Network(2)      : 2
 Summary-Net(3) : 0                 Summary-Asbr(4) : 0
 External(5)    : 1                 NSSA(7)         : 0
 Opaque-link(9) : 0                 Opaque-area(10) : 0
 Opaque-as(11)  : 0

```

**Table 1** Description of the **display ospf statistics updated-lsa** command output
| Item | Description |
| --- | --- |
| Begin time | Start time of statistics collection. |
| AdvRouter | Advertising Device. |
| Total | Total update times of LSAs. |
| Updated at | Latest update time. |
| Record | Record number. |
| End time | End time of statistic collection. |
| Router(1) | Update times of Router LSAs. |
| Network(2) | Update times of Network LSAs. |
| Summary-Net(3) | Update times of Network Summary LSAs. |
| Summary-Asbr(4) | Update times of ASBR Summary LSAs. |
| External(5) | Update times of AS External LSAs. |
| NSSA(7) | Update times of Type 7 LSAs. |
| Opaque-link(9) | Update times of Type 9 LSAs. |
| Opaque-area(10) | Update times of Type 10 LSAs. |
| Opaque-as(11) | Update times of Type 11 LSAs. |