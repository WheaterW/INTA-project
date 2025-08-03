display ospf spf-statistics
===========================

display ospf spf-statistics

Function
--------



The **display ospf spf-statistics** command displays route calculation statistics in OSPF processes.




Format
------

**display ospf** [ *process-id* ] **spf-statistics** [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an OSPF process.  If no process ID is specified, this command displays brief information about route calculation statistics in all processes. | The value is an integer that ranges from 1 to 4294967295. |
| **verbose** | Displays the detailed statistics. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display ospf spf-statistics** command displays route calculation statistics in OSPF processes, including the time when route calculation occurs, cause of route calculation, and number of changed routes.When identifying the cause of OSPF route flapping, you can run this command to obtain OSPF route calculation statistics, and then identify the cause according to the command output.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about route calculation statistics in OSPF process 1.
```
<HUAWEI> display ospf 1 spf-statistics verbose
OSPF Process 1 with Router ID 2.2.2.2

Routing table change statistics:

Index: 1   This spf calculation is External increment calculation
           Time     : 2008-11-29,17:36:59
           Intra    : 0 Added,0 Deleted
           Inter    : 0 Added,0 Deleted
           External : 10 Added,0 Deleted
           The reason of calculation is:LSA
           NO.     Type          LS ID             Adv Router
           1       External      10.1.5.0          1.1.1.1
           2       External      10.1.3.0          1.1.1.1
           3       External      10.1.9.0          1.1.1.1
           4       External      10.1.4.0          1.1.1.1
           5       External      10.1.2.0          1.1.1.1
           6       External      10.1.8.0          1.1.1.1
           7       External      10.1.7.0          1.1.1.1
           8       External      10.1.6.0          1.1.1.1
           9       External      10.1.10.0         1.1.1.1
           10      External      10.1.1.0          1.1.1.1

```

# Display brief information about route calculation statistics in OSPF process 1.
```
<HUAWEI> display ospf 1 spf-statistics
OSPF Process 1 with Router ID 2.2.2.2

Routing table change statistics:

Date          Time            Intra       Inter    External    Reason
2008-08-14    10:17:16        17          17       17          LSA
2008-08-14    09:16:47        77          62       127         Other
2008-08-14    08:16:37        0           0        0           LSA
2008-08-14    07:04:40        24          230      108         LSA
2008-08-14    06:03:15        204         230      18          Other
2008-08-14    05:02:55        34          236      128         LSA
2008-08-14    04:01:49        54          130      158         LSA
2008-08-14    03:01:48        44          220      138         LSA
2008-08-14    02:01:43        22          233      158         LSA
2008-08-14    01:00:53        977         897      907         LSA

```

**Table 1** Description of the **display ospf spf-statistics** command output
| Item | Description |
| --- | --- |
| Routing table change statistics | Statistics about routing table changes. |
| External | External route. |
| Time | Time when the route calculation was triggered. |
| Intra | Intra-area route. |
| Inter | Number of inter-area routes in the routing table which are changed because of route calculation. |
| The reason of calculation is | Possible causes of route calculation are as follows:   * LSA: indicates that route calculation is triggered by LSAs. * Topo: The fault is caused by a topology change. * Other: indicates that the fault is caused by other reasons, for example, the configuration changes or the interface goes Down. |
| NO. | Sequence number of the LSA that causes route calculation, which ranges from 1 to 10. |
| Type | Type of the LSA that causes route calculation, including Router, Network, Sum-Net, External, and NSSA. |
| LS ID | Link state ID of the LSA that causes route calculation. |
| Adv Router | Router ID of the device that generates the LSA that causes route calculation. |
| Date | Date when route calculation occurs. |
| Reason | Possible causes of route calculation are as follows:   * LSA: indicates that route calculation is triggered by LSAs. * Topo: The fault is caused by a topology change. * Other: indicates that the fault is caused by other reasons, for example, the configuration changes or the interface goes Down. |
| Index | Index of statistics. |