display udp statistics
======================

display udp statistics

Function
--------



The **display udp statistics** command displays UDP packet statistics.

The **display udp ipv6 statistics** command displays IPv6 UDP packet statistics.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display udp statistics**

**display udp statistics verbose**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display udp ipv6 statistics**

**display udp ipv6 statistics verbose**


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

UDP is a communications protocol used for packet exchanging on the Internet. It uses the simplest transmission model to send messages from one user application to another. To view IPv6 UDP packet statistics, run the **display udp ipv6 statistics** command. The following information will be displayed:

* Number of received and sent packets
* Number of discarded packets
* Number of redirected packets

**Precautions**

The number of packets received by a device includes the number of packets forwarded to another device, the number of packets sent to the upper layer on the device, and the number of packets discarded by the device.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display application-based IPv6 UDP traffic statistics.
```
<HUAWEI> display udp ipv6 statistics verbose
Received packets:                                                               
--------------------------------------------------------------------------------
Application       Format Errors     Checksum Errors   No Port 
--------------------------------------------------------------------------------
LDP               0                 0                 0        
DHCP              0                 0                 0         
BFD               0                 0                 0         
RIP               0                 0                 0         
SNMP              0                 0                 0         
Others            0                 0                 0
--------------------------------------------------------------------------------

Sent packets:                                                                   
--------------------------------------------------------------------------------
Application       Dropped Packets                                               
--------------------------------------------------------------------------------
LDP               0                                                            
DHCP              0                                                             
BFD               0                                                             
RIP               0                                                            
SNMP              0                                                             
Others            0          
--------------------------------------------------------------------------------

```

# Display UDP packet statistics by application.
```
<HUAWEI> display udp statistics verbose
Received packets:                                                               
--------------------------------------------------------------------------------
Application       Format Errors     Checksum Errors   No Port 
--------------------------------------------------------------------------------
LDP               0                 0                 0        
DHCP              0                 0                 0         
BFD               0                 0                 0         
RIP               0                 0                 0         
SNMP              0                 0                 0         
Others            0                 0                 0
--------------------------------------------------------------------------------

Sent packets:                                                                   
--------------------------------------------------------------------------------
Application       Dropped Packets                                               
--------------------------------------------------------------------------------
LDP               0                                                            
DHCP              0                                                             
BFD               0                                                             
RIP               0                                                            
SNMP              0                                                             
Others            0          
--------------------------------------------------------------------------------

```

# Display UDP packet statistics.
```
<HUAWEI> display udp statistics
Received packets:
    Total packets: 0
    Checksum error: 0
    Shorter than header: 0
    Data length larger than packets: 0
    No socket on port: 0
    Broadcast: 0
    Not delivered, input socket full: 0
    Input packets missing pcb cache: 0
Sent packets:
    Total packets: 0

```

# Display IPv6 UDP packet statistics.
```
<HUAWEI> display udp ipv6 statistics
Received packets:
    Total packets: 0
    Checksum error: 0
    Shorter than header: 0
    Data length larger than packets: 0
    No socket on port: 0
    Broadcast: 0
    Not delivered, input socket full: 0
    Input packets missing pcb cache: 0
Sent packets:
    Total packets: 0

```

**Table 1** Description of the **display udp statistics** command output
| Item | Description |
| --- | --- |
| Received packets | Statistics of received packets. |
| Application | Application categorization. |
| Format Errors | Number of packets with incorrect formats. |
| Checksum error | Number of packets with checksum errors. |
| Checksum Errors | Number of packets with CRC errors. |
| No socket on port | Number of packets whose port numbers are not used by any socket. |
| No Port | Number of packets for which no socket can be found. |
| LDP | Number of LDP packets. |
| DHCP | Number of DHCP packets. |
| BFD | Number of BFD packets. |
| RIP | Number of RIP packets. |
| SNMP | Number of SNMP packets. |
| Others | Other packet statistics. |
| Sent packets | Statistics about sent packets. |
| Dropped Packets | Number of dropped packets. |
| Total packets | Number of received UDP packets. |
| Shorter than header | Number of packets whose length is shorter than the header. |
| Data length larger than packets | Number of packets whose data length is greater than the packet length. |
| Not delivered, input socket full | Number of packets that are not sent out because the socket buffer is full. |
| Input packets missing pcb cache | Number of sent packets that are not found in the PCB cache. |
| Broadcast | Number of broadcast or multicast packets. |