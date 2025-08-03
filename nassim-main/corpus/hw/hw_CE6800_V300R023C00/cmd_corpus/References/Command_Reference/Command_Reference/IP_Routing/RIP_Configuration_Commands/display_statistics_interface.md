display statistics interface
============================

display statistics interface

Function
--------



The **display rip statistics interface** command displays statistics on a RIP interface, including the statistics of packets sent and received by the interface.

The **display ripng statistics interface** command displays statistics about a RIPng interface, including the number of packets sent or received by the interface.




Format
------

**display rip** *process-id* **statistics** **interface** **all**

**display ripng** *process-id* **statistics** **interface** **all**

**display rip** *process-id* **statistics** **interface** { *interface-name* | *interface-type* *interface-number* } [ **neighbor** *neighbor-address* | **verbose** ]

**display ripng** *process-id* **statistics** **interface** { *interface-name* | *interface-type* *interface-number* } [ **neighbor** *neighbor-ipv6-address* | **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies a process ID. | The value is an integer ranging from 1 to 4294967295. |
| **all** | Displays statistics on all RIP interfaces. | - |
| *interface-type* | Specifies an interface type. | The value is in dotted decimal notation. |
| *interface-number* | Specifies an interface number. | - |
| **neighbor** *neighbor-address* | Specifies the IP address of a neighbor. | - |
| **verbose** | Displays detailed statistics of RIP packets sent and received by an interface. | - |
| *neighbor-ipv6-address* | Specifies the IPv6 address of the neighbor. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check RIP packet exchange statistics, run the **display rip statistics** command.The **display ripng statistics interface** command output helps you check the configuration and operating status of RIPng, locate faults, and verify the configuration.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about 100GE 1/0/1 in RIP process 1.
```
<HUAWEI> display rip 1 statistics interface 100GE1/0/1
100GE1/0/1(10.0.0.11)
Statistical information           Last min        Last 5 min     Total
-----------------------------------------------------------------------
Periodic updates sent             2               7              6960
Triggered updates sent            0               0              2
Response packets sent             2               7              6961
Response packets received         1               3              6572
Response packets ignored          0               0              0
Request packets sent              0               0              1
Request packets received          0               0              1
Request packets ignored           0               0              0
Bad packets received              0               0              0
Routes received                   2               6              13149
Routes sent                       4               14             14334
Bad routes received               0               0              0
Packet authentication failed      0               0              0
Packet send failed                0               0              0

```

**Table 1** Description of the **display statistics interface** command output
| Item | Description |
| --- | --- |
| Statistical information | Packet type. |
| Last min | Statistics within the last 1 minute. |
| Last 5 min | Statistics within the last 5 minutes. |
| Total | Total number of packets. |
| Periodic updates sent | Number of periodic Update packets that are sent. |
| Triggered updates sent | Number of triggered Update packets that are sent. |
| Bad packets received | Number of received packets that cannot be parsed correctly. |
| Bad routes received | Number of received routes that cannot be parsed correctly. |
| Routes sent | Number of routes that are sent by the interface. |
| Routes received | Number of routes received by the interface. |
| Packet authentication failed | Number of RIP packets that fail to be authenticated. |
| Packet send failed | Number of RIP packets that fail to be sent. |