display ospf ecmp-group
=======================

display ospf ecmp-group

Function
--------



The **display ospf ecmp-group** command displays information about OSPF ECMP groups.




Format
------

**display ospf** [ *process-id* ] **ecmp-group**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | process-id Specifies the ID of an OSPF process. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When OSPF load balancing is implemented, the display ospf ecmp-group command can be used to check whether indirect next hop IDs are correctly assigned. This helps to implement a rapid route switchover.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about OSPF ECMP groups.
```
<HUAWEI> display ospf ecmp-group
OSPF Process 1 with Router ID 10.1.1.1
                 OSPF ECMP Group Information
-----------------------------------------------------------------------
 ECMPGroupId MtId Flag  RefCnt    NextHop
-----------------------------------------------------------------------
   0x1000048    0 D          1    10.1.1.1
-----------------------------------------------------------------------
Flags: D-Direct, URT-Unicast Routing Table
Used ECMP Group Number: 1

Total Used ECMP Group Number: 1
Unused ECMP Group Number: 7
Unused ECMP Group List:
0x1000049, 0x100004a, 0x100004b, 0x100004c, 0x100004d, 0x100004e, 0x100004f

```

**Table 1** Description of the **display ospf ecmp-group** command output
| Item | Description |
| --- | --- |
| OSPF ECMP Group Information | Information about an OSPF ECMP group. |
| ECMPGroupId | ID of an ECMP group. |
| MtId | Topology ID. |
| RefCnt | Number of times that an ECMP group is referenced. |
| NextHop | Routing information on the next hop. |
| Used ECMP Group Number | Number of used ECMP groups in a process. |
| Total Used ECMP Group Number | Total number of used ECMP groups. |
| Unused ECMP Group Number | Number of remaining ECMP groups. |
| Unused ECMP Group List | List of remaining ECMP groups. |
| Flags | Flag of an ECMP group:   * D: Direct route. * URT: Unicast route. |