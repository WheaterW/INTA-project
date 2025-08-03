display isis spf-log
====================

display isis spf-log

Function
--------



The **display isis spf-log** command displays the SPF calculation log of IS-IS.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display isis** *process-id* **spf-log** **spf** [ **ipv6** | [ **level-1** | **level-2** ] ] \*

**display isis spf-log** [ *process-id* | **vpn-instance** *vpn-instance-name* ] **spf** [ **ipv6** | [ **level-1** | **level-2** ] ] \*

**display isis** *process-id* **spf-log** **frr** [ **ipv6** | [ **level-1** | **level-2** ] ] \*

**display isis spf-log** [ *process-id* | **vpn-instance** *vpn-instance-name* ] **frr** [ **ipv6** | [ **level-1** | **level-2** ] ] \*

**display isis** *process-id* **spf-log** **prc** [ **ipv6** ] \*

**display isis spf-log** [ *process-id* | **vpn-instance** *vpn-instance-name* ] **prc** [ **ipv6** ]

**display isis** [ *process-id* ] **spf-log** [ **spf** | **prc** | **frr** | **ipv6** ]

For CE6885-LL (low latency mode):

**display isis** *process-id* **spf-log** **spf** [ **level-1** | **level-2** ]

**display isis spf-log** [ *process-id* | **vpn-instance** *vpn-instance-name* ] **spf** [ **level-1** | **level-2** ]

**display isis** *process-id* **spf-log** **frr** [ **level-1** | **level-2** ]

**display isis spf-log** [ *process-id* | **vpn-instance** *vpn-instance-name* ] **frr** [ **level-1** | **level-2** ]

**display isis** *process-id* **spf-log** **prc**

**display isis spf-log** [ *process-id* | **vpn-instance** *vpn-instance-name* ] **prc**

**display isis** [ *process-id* ] **spf-log** [ **spf** | **prc** | **frr** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an IS-IS process ID. | The value is an integer ranging from 1 to 4294967295. |
| **spf** | Indicates the SPF calculation log. | - |
| **ipv6** | Indicates the SPF calculation log in the IPv6 topology.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **level-1** | Indicates the SPF calculation log in a Level-1 area. | - |
| **level-2** | Indicates the SPF calculation log in a Level-2 area. | - |
| **prc** | Indicates the PRC calculation log. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **frr** | Indicates the FRR calculation log. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When an error occurs in the IS-IS SPF calculation, run the **display isis spf-log** command to diagnose the fault. The command can be used to view the SPF calculation log of IS-IS, such as the start time, duration, number of nodes, and events that trigger the SPF calculation. You can check which event causes the error of the SPF calculation by the start time.Check the StartTime field first. If the SPF calculation is performed repeatedly at short intervals, flapping may have occurred. Then check the Last Trigger LSP and Trigger Event fields for further analysis.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the SPF calculation log of IS-IS.
```
<HUAWEI> display isis spf-log
                        SPF Log information for ISIS(1)
                        -------------------------------
                            ISIS(1) Level-1 SPF Log
                            -----------------------
 StartTime  Duration  Nodes  Count  Last Trigger LSP      Trigger Event
--------------------------------------------------------------------------------
 15:11:28   0         0      1      NULL                  ISPF_ADJ_STATE_CHG
 15:11:6    0         2      2      NULL                  ISPF_CIRC_DR_CHANGE
 15:9:30    0         0      4      1111.1111.1111.00-00  TUNNEL_ADJ_UP
 15:9:20    0         2      3      NULL                  ISPF_LINK_ADD
 15:3:36    0         0      1      NULL                  ISPF_ADJ_STATE_CHG
 15:3:15    0         2      2      NULL                  ISPF_CIRC_DR_CHANGE
 15:2:30    0         2      3      NULL                  ISPF_LINK_ADD
 15:1:40    0         0      1      NULL                  ISPF_ADJ_STATE_CHG
 15:1:30    0         2      2      NULL                  ISPF_CIRC_DR_CHANGE
 14:2:39    0         1      5      1111.1111.1111.00-00  ISPF_LINK_DEL
 13:5:49    0         1      2      NULL                  ISPF_LINK_ADD
 13:5:39    0         2      5      NULL                  ISPF_ADJ_PROT_CHG
 13:5:17    0         2      2      NULL                  ISPF_CIRC_DR_CHANGE
 11:12:19   0         0      3      NULL                  ISPF_2WAY_CHECK
 10:27:32   0         0      3      NULL                  ISPF_2WAY_CHECK
 9:54:12    0         2      8      NULL                  ISPF_LINK_ADD
 9:54:2     0         2      2      NULL                  ISPF_CIRC_DR_CHANGE
 9:38:33    0         0      4      1111.1111.1111.00-00  TUNNEL_ADJ_UP
 9:38:12    0         0      1      NULL                  ISPF_ADJ_NEXTHOP_CHG
 9:38:2     0         2      3      NULL                  ADJDOWN

```

**Table 1** Description of the **display isis spf-log** command output
| Item | Description |
| --- | --- |
| StartTime | Start time for SPF calculation. |
| Duration | Time taken for SPF calculation, the value rounds down the actual duration, in milliseconds. In most cases, the value is less than 1 ms. Therefore, it is displayed as 0. |
| Nodes | Number of nodes calculated by SPF. |
| Count | Number of events that trigger the SPF calculation. |
| Last Trigger LSP | LSP that triggers the last SPF calculation. |
| Trigger Event | Event that triggers the last SPF calculation. |