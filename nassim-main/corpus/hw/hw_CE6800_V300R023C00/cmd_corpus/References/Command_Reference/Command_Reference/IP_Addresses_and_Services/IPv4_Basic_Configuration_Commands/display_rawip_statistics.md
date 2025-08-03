display rawip statistics
========================

display rawip statistics

Function
--------



The **display rawip statistics** command displays statistics about IPv4 RawIP packets.

The **display rawip ipv6 statistics** command displays statistics about IPv6 RawIP packets.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display rawip statistics**

**display rawip statistics verbose**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display rawip ipv6 statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **verbose** | Indicates detailed information. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To check statistics about RawIP packets, including the number of sent and received RawIP packets, run the display rawip statistics command.RSVP, OSPF, and ICMP packets are encapsulated into RawIP packets during transmission. During ping operations, for example, run the display rawip statistics command to check the number of RawIP packets sent by the local device to see if the network abnormality is caused by abnormal sending and receiving of RawIP packets.If you want to diagnose problems and monitor information of specific applications, configure verbose in the display rawip statistics command so that application-specific RawIP packet statistics are displayed. The applications can be ICMP, OSPF, RSVP, or others.

**Precautions**

The number of packets received by the Router includes the number of forwarded packets, packets sent to the upper layer, and discarded packets.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display RawIP packet statistics.
```
<HUAWEI> display rawip statistics
------------------------ Display Rawip Statistics ---------------------  
Received packets:
    Total: 6
    Input packets missing pcb cache: 0
Sent packets:
    Total: 3
-----------------------------------------------------------------------

```

# Display RawIP traffic statistics by application.
```
<HUAWEI> display rawip statistics verbose
Received packets:
------------------------------------------------------------------
Application    Overflow         No Matching
------------------------------------------------------------------
ICMP                  0                  0
OSPF                  0                  0
RSVP                  0                  0
Others                0                  0
------------------------------------------------------------------
 
Sent packets:
------------------------------------------------------------------
Application    Dropped Packets
------------------------------------------------------------------        
ICMP                         0
OSPF                         0
RSVP                         0
Others                       0
------------------------------------------------------------------

```

# Display statistics about IPv6 RawIP packets.
```
<HUAWEI> display rawip ipv6 statistics
------------------------ Display Rawip Statistics -------------------
Received packets:
    Total: 0
    Input packets missing pcb cache: 0
Sent packets:
    Total: 0
-----------------------------------------------------------------------

```

**Table 1** Description of the **display rawip statistics** command output
| Item | Description |
| --- | --- |
| Received packets | Received packet statistics. |
| Input packets missing pcb cache | Number of packets discarded because no corresponding Protocol Control Block (PCB) exists. |
| Sent packets | Number of sending packets. |
| Application | Application categorization. |
| Overflow | Number of RawIP packets discarded due to a socket buffer overflow. |
| No Matching | Number of RawIP packets discarded due to a socket mismatch on the receive end. |
| ICMP | ICMP packet statistics. |
| OSPF | OSPF packet statistics. |
| RSVP | RSVP packet statistics. |
| Others | Number of other types of packets. |
| Dropped Packets | Number of discarded packets. |
| Total | Total number of received/sent packets. |