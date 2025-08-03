display ospf nexthop
====================

display ospf nexthop

Function
--------



The **display ospf nexthop** command displays OSPF next hop information.




Format
------

**display ospf** [ *process-id* ] **nexthop**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an OSPF process. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view information about all the OSPF next hops, run the display ospf nexthop command. The command output can help you troubleshoot OSPF faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display OSPF next hop information.
```
<HUAWEI> display ospf nexthop
OSPF Process 1 with Router ID 10.1.1.1
                  Routing Nexthop information

Next hops:
 Address        Type  Refcount   Intf Addr       Intf Name
--------------------------------------------------------------
 192.168.0.1    Local 1          192.168.0.1     LoopBack1
 10.10.1.1      Local 1          10.10.1.1       100GE1/0/2
 10.20.1.1      Local 1          10.20.1.1       100GE1/0/1

```

**Table 1** Description of the **display ospf nexthop** command output
| Item | Description |
| --- | --- |
| Next hops | Detailed information about the next hop. |
| Address | Next hop. |
| Type | Type of the route passing through the next hop. Local indicates that the route is destined for the local network segment. |
| Refcount | Number of OSPF routes that use the next hop. |
| Intf Addr | Interface address. |
| Intf Name | Interface name. |