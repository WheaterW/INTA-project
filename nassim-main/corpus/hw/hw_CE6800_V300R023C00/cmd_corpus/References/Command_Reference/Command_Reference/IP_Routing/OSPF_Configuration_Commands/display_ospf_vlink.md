display ospf vlink
==================

display ospf vlink

Function
--------



The **display ospf vlink** command displays OSPF virtual links.




Format
------

**display ospf** [ *process-id* ] **vlink**


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

After OSPF areas are defined, OSPF route updates between non-backbone areas are transmitted through a backbone area. Therefore, OSPF requires that all non-backbone areas maintain the connectivity with the backbone area and the backbone areas in different OSPF areas maintain the connectivity with each other. In real world situations, this requirement may not be met because of some restrictions. To resolve this problem, you can configure OSPF virtual links.The **display ospf vlink** command displays OSPF virtual link information, which can help you troubleshoot OSPF virtual link faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display OSPF virtual links.
```
<HUAWEI> display ospf vlink
OSPF Process 1 with Router ID 1.1.1.1
                  Virtual Links
 Virtual-link Neighbor-id  -> 2.2.2.2, Neighbor-State: Full
 Interface: 10.1.1.1 (100GE1/0/1)
 Cost: 1  State: P-2-P  Type: Virtual
 Transit Area: 0.0.0.1
 Timers: Hello 10 , Dead 40 , Retransmit 5 , Transmit Delay 1
 GR State: Normal

```

**Table 1** Description of the **display ospf vlink** command output
| Item | Description |
| --- | --- |
| Virtual-link Neighbor-id | ID of the neighboring router that is connected through the virtual link. |
| Transit Area | Transit area ID if the current interface is a virtual link. |
| GR State | GR status:   * Normal: indicates that no GR is performed. * Doing GR: indicates that the Router is performing GR. * Complete GR: indicates that the Router finishes GR. * Helper: indicates that the Router is Helper when the neighbor is performing GR. |
| Neighbor-State | Neighbor status, such as Down, Init, 2-Way, ExStart, Exchange, Loading, and Full. |
| Interface | Information about interfaces in the area is listed, including the IP address and name of the main interface. If the interface cannot be identified, Unknown is displayed. |
| Cost | Cost. |
| State | Interface state. |
| Type | Interface type. |
| Timers | Interval for sending Hello messages, Dead time, polling interval (NBMA), retransmission interval, and transmission delay on the interface. |