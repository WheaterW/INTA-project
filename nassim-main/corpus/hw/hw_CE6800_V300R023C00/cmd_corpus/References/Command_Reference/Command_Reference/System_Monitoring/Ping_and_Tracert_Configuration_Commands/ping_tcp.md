ping tcp
========

ping tcp

Function
--------



The **ping tcp** command tests whether the link between the client and TCP server is reachable and checks the speed of setting up a TCP connection through three-way handshake.




Format
------

**ping tcp** [ **-c** *count* | **-t** *timeout* | **-m** *interval* | **-h** *ttl* | **-vpn-instance** *vrfName* | **-passroute** | **-a** *srcAddress* ] \* *destAddress* [ *destPort* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **-c** *count* | Specifies the number of messages to be sent.  After you run the ping tcp command, the sequence number of an ICMP echo request message starts from 1 and is incremented by 1 for each subsequent message. By default, a device sends five ICMP echo request messages for a ping operation. You can configure the parameter -c to specify the number of ICMP echo request messages to be sent. If the peer is reachable, it sends five ICMP echo reply messages with the same sequence numbers as those of the ICMP echo request messages.  If the network quality is poor, you can increase the parameter value to determine the network quality based on the packet loss rate. | The value is an integer ranging from 1 to 4294967295. The default value is 5. |
| **-t** *timeout* | Specifies the length of time to wait for an ICMP echo reply message after an ICMP echo request message is sent. | The value is an integer ranging from 0 to 65535, in milliseconds. The default value is 2000. |
| **-m** *interval* | Specifies an interval at which ICMP echo request messages are sent.  Each time the source sends an ICMP echo request message, the source waits a period of time (500 ms by default) before sending the next ICMP echo request message. You can set the time to wait before sending the next ICMP echo request message. If network quality is poor, setting this parameter to a value greater than or equal to 2000 ms is recommended. | The value is an integer ranging from 1 to 10000, in milliseconds. The default value is 500. |
| **-h** *ttl* | Specifies the TTL value. | The value is an integer ranging from 1 to 255. The default value is 30. |
| **-vpn-instance** *vrfName* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **-passroute** | Sends packets without searching for the routing table. | - |
| **-a** *srcAddress* | Specifies the source IP address for echo request packets.  If no source IP address is specified, the IP address of the outbound interface is used. | Dotted decimal notation. |
| *destAddress* | Specifies the IP address or host name of a remote system. | * If the value is an IPv4 address, it is in dotted decimal notation. * If the value is a host name, it is a string of case-sensitive characters without spaces. |
| *destPort* | Specifies the TCP server port. | The value is an integer ranging from 1 to 65535. The default value is 7. |



Views
-----

All views


Default Level
-------------

0: Visit level


Usage Guidelines
----------------

**Usage Scenario**



To test whether the link between the client and TCP server is reachable and check the speed of setting up a TCP connection through three-way handshake, run the **ping tcp** command.The command output helps detect the performance indicators such as the network connectivity, packet loss rate, and delay.




Example
-------

# Test whether the TCP server with the IP address 10.1.1.1 and port number 3000 is reachable, and check the TCP connection setup speed and performance indicators.
```
<HUAWEI> ping tcp 10.1.1.1 3000
  PING TCP 10.1.1.1: 3000, press CTRL_C to break
    Reply from 10.1.1.1: Sequence=1 time=3 ms
    Reply from 10.1.1.1: Sequence=2 time=3 ms
    Reply from 10.1.1.1: Sequence=3 time=3 ms
    Reply from 10.1.1.1: Sequence=4 time=3 ms
    Reply from 10.1.1.1: Sequence=5 time=4 ms

  --- TCP ping statistics ---
    5 packet(s) transmitted
    5 packet(s) received
    0.00% packet loss
    round-trip min/avg/max = 3/3/4 ms

```

**Table 1** Description of the **ping tcp** command output
| Item | Description |
| --- | --- |
| PING TCP x.x.x.x | IP address of the destination host. |
| TCP ping statistics | Statistics collected in the tcp ping test on the destination host. The statistics include the following information:   * packets transmitted: number of sent ICMP echo request packets. * packets received: number of received ICMP echo reply packets. * % packet loss: percentage of unresponded packets to total sent packets. * round-trip min/avg/max: minimum, average, and maximum time of responses. |
| press CTRL\_C to break | You can terminate the ongoing tcp ping test by pressing Ctrl+C. |
| Reply from x.x.x.x | Destination host of an ICMP echo request packet. An ICMP Echo Response packet contains the following:   * sequence: sequence number of the packet. * time: timeout period, in milliseconds. If no ICMP Echo Response packet is received within the timeout period, the system displays "Request time out". |