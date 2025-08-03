display ospfv3 interface
========================

display ospfv3 interface

Function
--------



The **display ospfv3 interface** command displays an OSPFv3 interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ospfv3** [ *process-id* ] **interface** [ **area** { *area-id* | *area-idIpv4* } ] [ *interfaceType* *interfaceNum* | *interfaceName* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the OSPFv3 process ID. | The value is an integer ranging from 1 to 4294967295. |
| **area** *area-idIpv4* | Specifies the OSPF area ID. | The value is in dotted decimal notation. |
| **area** *area-id* | Specifies the OSPF area ID. | The value is an integer that ranges from 0 to 4294967295. |
| *interfaceType* | Specifies the type of an interface. If no interface is specified, information of all OSPFv3 interfaces is displayed. | - |
| *interfaceNum* | Specifies the number of an interface. If no interface is specified, information of all OSPFv3 interfaces is displayed. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The display ospfv3 interface command output displays the configuration and operating status of OSPFv3, which facilitates fault location and configuration verification.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the OSPFv3 100GE 1/0/1.
```
<HUAWEI> display ospfv3 interface 100ge 1/0/1
100GE1/0/1 is up, line protocol is up
  Interface ID 0x102
  IPv6 Prefixes
    FE80::2E0:FFF:FE4E:F101 (Link-Local Address)
    2001:DB8::1/64
  OSPFv3 Process (1), Area 0.0.0.1, Instance ID 0
    Router ID 1.1.1.1, Network Type BROADCAST, Cost: 1
    Effective cost : 1, enabled by OSPFv3 Protocol
    Transmit Delay is 1 sec, State Waiting, Priority 1
    No designated router on this link
    No backup designated router on this link
    Timer interval configured, Hello 10, Dead 40, Wait 40, Retransmit 5
       Hello due in 00:00:02
    Neighbor Count is 0, Adjacent neighbor count is 0
    Interface Physical BandwidthHigh 0, BandwidthLow 100000000
    Authentication : HMAC-SHA256
      Higher Order Sequence Number : 0
      Lower Order Sequence Number  : 58
    Suppress flapping peer: enable(flapping-count: 0, threshold: 20)

```

**Table 1** Description of the **display ospfv3 interface** command output
| Item | Description |
| --- | --- |
| line protocol | Link status. |
| Interface ID | Interface ID. |
| Interface Physical BandwidthHigh | Higher order interface bandwidth value. |
| IPv6 Prefixes | IPv6 Prefix. |
| OSPFv3 Process | OSPFv3 process ID. |
| Area | Area to which the interface belongs. |
| Instance ID | ID of the instance to which the interface belongs. |
| Router ID | Router ID. |
| Network Type | Network type of the interface: Point-to-Point or broadcast. |
| Effective cost | Valid cost value:   * OSPFv3 Protocol. * BGP-IGP. * Tunnel. * Suppress flapping peer. * Cost-fallback. * Peer hold-max-cost. * BFD DOWN COST. * Received-lsa overload. |
| Transmit Delay | Transmission delay. |
| State | State of the interface:   * Down: The status of the interface is Down. If an interface is Down, the interface is unavailable and cannot be used to transmit traffic. * Loopback: The interface connecting to the network on the device is in the Loopback state. The loopback interface cannot be used to transmit data but can collect interface information through ICMP ping operations or bit error detection. * Waiting: The device is determining the DR and BDR on the network. The DR or BDR election mechanism is not implemented until the waiting period ends. This prevents unnecessary changes in the DR and BDR roles. * P-2-P: The interface is connected to the P2P network or a virtual link. * DROther: The device itself is not elected as the BDR. Instead, another device connecting to the broadcast network or NBMA network is elected as the DR. The device starts to set up adjacency with the DR and BDR (if existing). * BDR: The device functions as the BDR on the network, and will turn into a DR when the current DR fails. The device sets up adjacency with other devices that access the network. * DR: The device functions as the DR on the network. The device sets up adjacency with other devices that access the network. |
| Priority | Priority of the interface. |
| Timer interval configured | Configured interval:   * Hello: Interval at which Hello packets are sent. * Dead: Interval of the Dead timer. * Wait: Interval of the Wait timer. * Retransmit: Retransmission interval. |
| Hello due in 00:00:02 | Hello packets are sent 2 seconds later. |
| Neighbor Count | Number of neighbors. |
| Adjacent neighbor count | Number of adjacencies. |
| BandwidthLow | Lower order bandwidth value. |
| Suppress flapping peer | Status of OSPFv3 neighbor relationship flapping suppression:   * enable: OSPFv3 neighbor relationship flapping suppression is enabled. * flapping-count: number of valid flapping\_events. If the interval between two successive neighbor status changes from Full to a non-Full state is shorter than detecting-interval, a valid flapping\_event is recorded, and the flapping\_count increases by 1. To change detecting-interval, run the ospfv3 suppress-flapping peer detecting-interval detecting-interval command. * threshold: flapping suppression threshold. When the flapping\_count reaches or exceeds threshold, flapping suppression takes effect. To configure the threshold, run the ospfv3 suppress-flapping peer threshold threshold command. * disable: OSPFv3 neighbor relationship flapping suppression is disabled. In this case, the following information is displayed, without flapping-count or threshold: Suppress flapping peer: disable. * hold-down: OSPFv3 neighbor relationship flapping suppression works in Hold-down mode. In this case, an example of the displayed information is as follows: Suppress flapping peer: hold-down(start: 2016-01-02 09:58:41, remain-interval: 476 sec). * start: time when the flapping suppression started. * remain-interval: remaining time of the flapping suppression. In the flapping suppression state, remain-interval is reset each time when the device detects a valid neighbor flapping event. * hold-max-cost: OSPFv3 neighbor relationship flapping suppression works in Hold-max-cost mode. In this case, an example of the displayed information is as follows: Suppress flapping peer: hold-max-cost(start: 2016-01-02 09:58:41, remain-interval: 476 sec). |
| No designated router on this link | No designated router (DR) is on the link. |
| No backup designated router on this link | No backup designated router (BDR) is on the link. |
| Authentication | HMAC-SHA256 authentication which can be configured using the ospf authentication-mode command. |
| Higher Order Sequence Number | Higher order 32-bit of the sequence number of the sent packet. |
| Lower Order Sequence Number | Lower order 32-bit of the sequence number of the sent packet. |
| Cost | Cost of the interface. |