display rip ecmp-group
======================

display rip ecmp-group

Function
--------



The **display rip ecmp-group** command displays information about Equal Cost Multiple Path (ECMP) groups of a RIP process.

The **display ripng ecmp-group** command displays the information about Equal Cost Multiple Path (ECMP) groups of a RIPng process.




Format
------

**display rip** [ *process-id* ] **ecmp-group**

**display ripng** [ *process-id* ] **ecmp-group**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Displays information about the ABR or ASBR of an OSPF route in a specified OSPF process. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check information about ECMP groups of a RIP process, run this command. On a network with redundant links, if a route switchover occurs due to a link failure, this command can be used to check whether the route switchover is correctly performed.To check the information about ECMP groups of a RIPng process, run this command.On a network with redundant links, if a route switchover occurs due to a link failure, this command can be used to check whether the route switchover is correctly performed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the ECMP groups of all RIP processes.
```
<HUAWEI> display rip ecmp-group

  RIP(1) ECMP Group Information
------------------------------------------------------------------
 ECMPGroupId Flag RefCnt  NextHop
------------------------------------------------------------------
 3992977482      D     1  10.18.1.1
 3992977483    URT     1  10.18.1.2
                          10.19.1.2
 3992977485      D     1  10.19.1.1
------------------------------------------------------------------

 Flags: D-Direct, URT
 Used ECMP Group Number: 3

```

**Table 1** Description of the **display rip ecmp-group** command output
| Item | Description |
| --- | --- |
| ECMPGroupId | ID of the equal-cost route group. |
| RefCnt | Number of routes using the ECMP group ID. |
| NextHop | Next hop information. |
| Used ECMP Group Number | Number of ECMP groups in use. |
| Flags | Route attribute:   * D: Direct route. * URT: Unicast route. |