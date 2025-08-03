display ospfv3 next-hop
=======================

display ospfv3 next-hop

Function
--------



The **display ospfv3 next-hop** command displays the OSPFv3 next-hop routing table.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ospfv3** [ *process-id* ] **next-hop**


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

The display ospfv3 next-hop command output can display information about all the OSPFv3 next hops, which helps you troubleshoot OSPFv3 faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about next hops in the routing table of OSPFv3 process 1.
```
<HUAWEI> display ospfv3 1 next-hop
OSPFv3 Process (1)
Neighbor-Id     Next-Hop                                Interface   RefCount
10.3.3.9         FE80::2E0:FCFF:FE01:814F                100GE1/0/1  1

```

**Table 1** Description of the **display ospfv3 next-hop** command output
| Item | Description |
| --- | --- |
| Neighbor-Id | ID of the neighbor. |
| Next-Hop | Next hop. |
| Interface | Outbound interface name. |
| RefCount | Number of routes using the next hop. |