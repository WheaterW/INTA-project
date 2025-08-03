display ospfv3 bfd session
==========================

display ospfv3 bfd session

Function
--------



The **display ospfv3 bfd session** command displays BFD session information of an OSPFv3 process.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ospfv3** [ *process-id* ] **bfd** **session** [ *IntfName* | *interfaceType* *interfaceNum* ] [ *NbrRouterId* ] [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies a process ID of OSPFv3. | The value is an integer ranging from 1 to 4294967295. |
| *IntfName* | Specifies an interface name. | - |
| *interfaceType* | Specifies the type of an interface. | - |
| *interfaceNum* | Specifies the number of an interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| *NbrRouterId* | Specifies the neighbor router ID. | The value is in dotted decimal notation. |
| **verbose** | Displays detailed information of the neighbor. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

If no process ID is specified, the information about all OSPFv3 processes is displayed in an ascending order.If the type and number of an interface are not specified, the information about all OSPFv3 interfaces is displayed in an ascending order.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display BFD session information of all OSPFv3 processes.
```
<HUAWEI> display ospfv3 bfd session
OSPFv3 Process 1 with Router ID 2.2.2.2
* - STALE

 Neighbor-Id      Interface         BFD-Status
 2.2.2.2         100GE1/0/1             Up*

```

# Display the detailed BFD session information of process 1.
```
<HUAWEI> display ospfv3 1 bfd session verbose
* - STALE

        OSPFv3 Process 1 with Router ID 1.1.1.1

 Neighbor-Id: 3.3.3.3              BFD Status: Up
 Interface: 100GE1/0/1             Instance : 2
 IPv6-Local-Address: FE80::2E0:B1FF:FE49:8142
 IPv6-Remote-Address: FE80:23:22::

   Total UP/DOWN/UNKNOWN BFD Session Number : 0 / 0 / 1

```

**Table 1** Description of the **display ospfv3 bfd session** command output
| Item | Description |
| --- | --- |
| OSPFv3 Module preferred timer values | Recommended BFD sending and receiving time parameters for OSPFv3. |
| Router ID | Route ID. |
| \* - STALE | Stale BFD session. |
| Neighbor-Id | Neighbor ID. |
| Interface | Interface to which this session is bound. |
| BFD-Status | BFD session status:   * Up. * Down. |
| BFD Status | BFD session status:   * Up. * Down. |
| BFD Module preferred timer values | Recommended BFD receiving and sending time parameters. |
| Instance | OSPFv3 instance to which the OSPFv3 process belongs. |
| Total UP/DOWN/UNKNOWN BFD Session Number | Total number of BFD sessions in the Up, Down, or Unknown state. |
| IPv6-Local-Address | Local IPv6 address to which this session is bound. |
| IPv6-Remote-Address | Remote IPv6 address to which this session is bound. |
| Configured timer values | BFD sending and receiving time parameters. |