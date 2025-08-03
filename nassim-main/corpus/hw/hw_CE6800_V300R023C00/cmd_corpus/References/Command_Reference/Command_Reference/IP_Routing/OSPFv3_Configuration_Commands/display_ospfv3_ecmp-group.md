display ospfv3 ecmp-group
=========================

display ospfv3 ecmp-group

Function
--------



The **display ospfv3 ecmp-group** command displays information about OSPFv3 ECMP groups.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ospfv3** [ *process-id* ] **ecmp-group**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the OSPFv3 process ID. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When OSPFv3 load balancing is implemented, the display ospfv3 ecmp-group command can be used to check whether indirect next hop IDs are correctly assigned. This helps to implement a rapid route switchover.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about OSPFv3 ECMP groups.
```
<HUAWEI> display ospfv3 ecmp-group

         OSPFv3 Process 1 with Router ID 1.1.1.1
                 OSPFv3 ECMP Group Information
-----------------------------------------------------------------------
 ECMPGroupId MtId Flag  RefCnt    NextHop
-----------------------------------------------------------------------
   0x1000064    0 URT6       2    ::
   0x1000065    0 URT6       2    ::
   0x1000066    0 URT6       1    FE80::3A9C:80FF:FE21:300
   0x1000067    0 URT6       2    FE80::3A9C:80FF:FE21:300
-----------------------------------------------------------------------
Flags: D-Direct, URT6-Unicast Routing Table For IPv6
Used ECMP Group Number: 4

Total Used ECMP Group Number: 4
Unused ECMP Group Number: 56
Unused ECMP Group List:
0x1000068, 0x1000069, 0x100006a, 0x100006b, 0x100006c, 0x100006d, 0x100006e, 0x100006f, 0x1000070, 0x1000071, 0x1000072, 0x1000073, 0x1000074, 0x1000075, 0x1000076, 0x1000077, 0x1000078, 0x1000079, 0x100007a, 0x100007b, 0x100007c, 0x100007d, 0x100007e, 0x100007f, 0x1000080, 0x1000081, 0x1000082, 0x1000083, 0x1000084, 0x1000085, 0x1000086, 0x1000087, 0x1000088, 0x1000089, 0x100008a, 0x100008b, 0x100008c, 0x100008d, 0x100008e, 0x100008f, 0x1000090, 0x1000091, 0x1000092, 0x1000093, 0x1000094, 0x1000095, 0x1000096, 0x1000097, 0x1000098, 0x1000099, 0x100009a, 0x100009b, 0x100009c, 0x100009d, 0x100009e, 0x100009f

```

**Table 1** Description of the **display ospfv3 ecmp-group** command output
| Item | Description |
| --- | --- |
| OSPFv3 ECMP Group Information | Information about an OSPFv3 ECMP group. |
| ECMPGroupId | ID of an ECMP group. |
| MtId | Topology ID. |
| RefCnt | Number of times that an ECMP group is referenced. |
| NextHop | Routing information on the next hop. |
| Used ECMP Group Number | Number of used ECMP groups in a process. |
| Total Used ECMP Group Number | Total number of used ECMP groups. |
| Unused ECMP Group Number | Number of remaining ECMP groups. |
| Unused ECMP Group List | List of remaining ECMP groups. |
| Flags | Flag of an ECMP group. |