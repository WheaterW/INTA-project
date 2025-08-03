display rip interface
=====================

display rip interface

Function
--------



The **display rip interface** command displays information about a RIP-capable interface.

The **display ripng interface** command displays information about RIPng interfaces.




Format
------

**display rip** *process-id* **interface** [ { *interface-name* | *interface-type* *interface-number* } ] [ **verbose** ]

**display ripng** *process-id* **interface** [ { *interface-name* | *interface-type* *interface-number* } ] [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of a process. | The value is an integer ranging from 1 to 4294967295. |
| **interface** *interface-type* *interface-number* | Specifies the type and number of an interface. | - |
| **verbose** | Displays detailed information about a RIPng interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check information about a RIP-capable interface, run the **display rip interface** command. The command output helps verify the configurations and diagnose faults.The interface information displayed using the display ripng interface command includes the name, IP address, and link status of the interface. If verbose is specified, in addition to the preceding interface information, the metric that is added to the route carried in a sent RIPng packet, metric that is added to the route carried in a received RIPng packet, and whether poison reverse or split horizon is enabled on the interface can be displayed.The display ripng interface command displays the operating status and configurations of RIPng, which facilitates fault location and configuration verification.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about 100GE 1/0/1.
```
<HUAWEI> display rip 1 interface 100GE 1/0/1 verbose
100GE1/0/1 (10.1.1.1)
State    : UP             MTU: 500
Metricin(with ACL/ip-prefix) : 7
Metricin(default) : 0
Metricout: 1
Input    : Enabled     Output: Enabled
Protocol : RIPv2 Multicast
Send     : RIPv2 Multicast Packets
Receive  : RIPv2 Multicast Packets
Poison-reverse               : Disabled
Split-Horizon                : Enabled
Authentication type          : None
Replay Protection            : Disabled
BFD                          : Enabled (Dynamic)
Transmit-Interval            : 1000 ms
Receive-Interval             : 1000 ms
Detect-Multiplier            : 3
Max Packet Length            : 512
Summary Address(es) :      192.168.0.0/16

```

# Display information about 100GE 1/0/1.
```
<HUAWEI> display rip 1 interface 100GE 1/0/1
-------------------------------------------------------------------------------
Interface                IP Address        State       Protocol            MTU
--------------------------------------------------------------------------------
100GE 1/0/1              10.1.1.2            UP         RIPv2 Compatible    500

```

# Display information about RIPng on 100GE 1/0/1.
```
<HUAWEI> display ripng 1 interface 100GE 1/0/1
100GE 1/0/1
FE80::A0A:200:1
State : UP, Protocol : RIPNG, MTU : 1440

```

**Table 1** Description of the **display rip interface** command output
| Item | Description |
| --- | --- |
| State | Status of the interface:   * Up. * Down. |
| Metricin(with ACL/ip-prefix) | Metric that an interface adds to the route that matches the ACL or IP prefix list when the interface receives RIP packets. |
| Metricin(default) | Metric that an interface adds to the route when the interface receives RIP packets. |
| Input | Whether the interface can receive packets. |
| Protocol | Version of RIP running on the interface:   * RIPv1 Compatible. * RIPv2 Compatible.   Protocol running on the interface:   * RIPv1. * RIPv2 Multicast. * RIPv2 Broadcast. |
| Send | Type of packets sent by the interface:   * RIPv1. * RIPv2 Broadcast. * RIPv2 Multicast. * None: RIP updates are not advertised. |
| Receive | Type of packets received by the interface:   * RIPv1. * RIPv2 Broadcast. * RIPv2 Multicast. * None: Application will not process the received packet. |
| Poison-reverse | Whether poison reverse is enabled on the interface. |
| Split-Horizon | Whether split horizon is enabled on the interface. |
| Authentication | Authentication mode configured on the interface. |
| Authentication type | Authentication type configured on the interface. |
| Replay Protection | Specifies whether replay protection is configured on the interface. |
| BFD | Whether BFD is enabled on the interface:   * Enabled (Static): indicates static BFD is enabled on the interface. * Enabled (Dynamic): indicates dynamic BFD is enabled on the interface. * Blocked: indicates BFD is disabled on the interface. |
| Transmit-Interval | Interval at which BFD packets are sent by the interface to the neighbor. |
| Receive-Interval | Interval at which the interface receives BFD packets from the neighbor. |
| Detect-Multiplier | BFD multiplier value configured on the interface. |
| Max Packet Length | Maximum packet length. |
| Summary Address(es) | Summary address configured on the interface. |
| Interface | RIP-capable interface. |
| IP Address | IP addresses of the interfaces. |
| MTU | Link MTU. |
| Metricin | Metric that is added to the route carried in a received RIPng packet. |
| Metricout | Metric that an interface adds to the route when the interface sends RIP packets. |
| Output | Whether the interface can send packets. |