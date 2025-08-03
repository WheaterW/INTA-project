ping ipv6
=========

ping ipv6

Function
--------

The **ping ipv6** command checks whether an IPv6 host is reachable.



Format
------

**ping ipv6** { [ **-a** *source-ipv6-address* | **-c** *echo-number* | { **-s** *byte-number* | **-range** [ [ **min** *min-value* | **max** *max-value* | **step** *step-value* ] \* ] } | **-t** *timeout* | { **-tc** *traffic-class-value* | **-dscp** *dscp* } | **vpn-instance** *vpn-instance-name* | **-m** *wait-time* | **-name** | **-h** *hoplimit* | { **-brief** | [ **-system-time** | **-ri** | **-detail** ] \* } | **-nexthop** *nextHopAddr* | **-p** *pattern* | **ignore-mtu** ] \* *destination-ipv6-address* [ **-i** { *interface-name* | *interface-type* *interface-number* } ] [ **ipv6-forwarding** ] }



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **-a** *source-ipv6-address* | Specifies a source IPv6 address for the ICMPv6 Echo Request messages to be sent.  If no source IPv6 address is specified, the IPv6 address of the outbound interface of the route is used as the source address of ICMPv6 Echo Request messages. For example, in a VPN scenario, an IPv6 address in the VPN is preferentially used as the source address. | The value is a 32-digit hexadecimal number in format X:X:X:X:X:X:X:X. |
| **-c** *echo-number* | Specifies the maximum number of times for sending ICMPv6 echo request packets.  In the case of a poor network quality, increase the value to check network quality based on the packet loss ratio. | The value is an integer ranging from 1 to 4294967295. The default value is 5. |
| **-s** *byte-number* | Specifies the length of an ICMPv6 echo request packet (excluding IP and ICMPv6 headers). | The value is an integer that ranges from 20 to 9600, in bytes. The default value is 56, in bytes. |
| **-range** | Enables the device to send ICMPv6 echo request messages with variable payload lengths. | * If -range is not specified, the length of sent packets is specified by -s byte-number. The default value is 56, in bytes. * If -range is specified, the length of the first sent packet is specified by min min-value, and the length of subsequent packets increases by a value specified by step step-value until the packet length reaches the maximum value (specified by max max-value).   By default, the length ranges from 56 to 9600, and the step is 1.   * During the execution, you can press Ctrl+C to terminate the execution. * You can adjust the values of min min-value and max max-value to control the number of packets to be sent. The value of min min-value must be smaller than that of max max-value. * -range and -c echo-number can be used together. In this case, after packets of the same length are sent for the number of times specified by echo-number, the packet length increases by a step until the next packet length is reached. |
| **min** *min-value* | Specifies the minimum payload length of an ICMPv6 echo request message. | The value is an integer that ranges from 20 to 9600, in bytes. The default value is 56, in bytes. |
| **max** *max-value* | Specifies the maximum payload length of an ICMPv6 echo request message. | The value is an integer ranging from 20 to 9600, in bytes. The default value is 9600. |
| **step** *step-value* | Specifies the step length of an ICMPv6 echo request message. | The value is an integer ranging from 1 to 1000, in bytes. The default value is 1. |
| **-t** *timeout* | Specifies the timeout period for waiting for an ICMPv6 Echo Reply packet after an ICMPv6 Echo Request Packet is sent.  After the ping command is run, the source sends an ICMPv6 Echo Request packet to a specific address and waits for a reply. If the destination sends an ICMPv6 Echo Reply packet to the source within the time specified by timeout, the destination is reachable. If the destination does not send any reply within the timeout period, the source displays "Request time out".  Normally, the source will receive an ICMPv6 Echo Reply packet within 1 to 10 seconds after an ICMPv6 Echo Request packet is sent. If the network transmission rate is low, increase the timeout period. | The value is an integer ranging from 0 to 65535, in milliseconds. The default value is 2000. |
| **-tc** *traffic-class-value* | Specifies the traffic class for ICMPv6 echo request packets.  You can specify traffic-class-value to control ICMPv6 traffic. | The value is an integer ranging from 0 to 255. The default value is 0. |
| **-dscp** *dscp* | Specifies the DSCP value of an ICMPv6 echo request packet to be sent. | The value is an integer ranging from 0 to 63. The default value is <b>0</b>. |
| **vpn-instance** *vpn-instance-name* | Specifies the VPN instance to which the IPv6 address belongs. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name cannot be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **-m** *wait-time* | Specifies the interval at which ICMPv6 echo request packets are sent.  After the ping command is run, the device sends an ICMPv6 echo request packet. If the device fails to receive a reply within 500 ms, it sends the next ICMPv6 echo request packet. You can use this parameter to set the packet sending interval as required. Do not set this parameter to less than 2000 ms on an unstable network. | The value is an integer ranging from 1 to 10000, in milliseconds. The default value is 500. |
| **-name** | Displays the host name of the destination address. | - |
| **-nexthop** *nextHopAddr* | Specifies an IPv6 address for the next hop.  If you have specified this parameter, the device no longer searches the routing table before sending ICMPv6 Echo Response packets. This process prevents ping failures caused by incorrect routing entries. | The value is a 32-digit hexadecimal number, in the format X:X:X:X:X:X:X:X.   * The specified next hop address must be the next hop address of a directly connected physical interface. * When specifying the next hop address, you can configure -i interface-type interface-number to specify the outbound interface. The following conditions must be met to ensure a successful test: * The specified next hop address matches the outbound interface. * The specified outbound interface cannot be a member interface of a logical interface. * When you specify the next hop address, you cannot specify a VPN. |
| **-h** *hoplimit* | Specifies the hop limit value for ICMPv6 Echo Request packet to be sent. | The value is an integer ranging from 1 to 255. |
| **-brief** | Displays brief information about packet loss. | - |
| **-system-time** | Specifies the system time when an ICMP echo request packet is sent. | - |
| **-ri** | Indicates that the source interface of echo response packet is displayed. | - |
| **-detail** | Displays detailed information about packet loss. | - |
| **-p** *pattern* | Specifies the padding byte of ICMPv6 Echo Request packets.  The padding byte allows the system to identify a specific packet among a large number of received ICMPv6 Echo Reply packets. | The value is a hexadecimal number ranging from 0 to FFFFFFFF. By default, the padding starts from 0x00. |
| **ignore-mtu** | Indicates that the system does not check the interface MTU when a packet is sent. | - |
| *destination-ipv6-address* | Specifies the source IPv6 address of an ICMPv6 echo request packet to be sent. | The value is a 32-digit hexadecimal number in format X:X:X:X:X:X:X:X. |
| **-i** *interface-name* | Specifies the name of an outbound interface through which ICMPv6 Echo Request packets are sent.  If the specified destination IPv6 address is a link-local address, specify the outbound interface for ICMPv6 Echo Request packets. | - |
| *interface-type* | Specifies the type of an outbound interface through which ICMPv6 Echo Request packets are sent.  If the specified destination IPv6 address is a link-local address, specify the outbound interface for ICMPv6 Echo Request packets. | - |
| *interface-number* | Specifies the number of an outbound interface through which ICMP Echo Request packets are sent.  If the specified destination IPv6 address is a link-local address, specify the outbound interface for ICMP Echo Request packets. | - |
| **ipv6-forwarding** | Indicates that the ping packets are forcibly forwarded through IPv6 on the first node. | - |




Views
-----

All views



Default Level
-------------

0: Visit level



Usage Guidelines
----------------

**Usage Scenario**

To check network connectivity, run the **ping ipv6** command. It uses ICMPv6 messages to monitor the following items:

* Whether the remote device is available.
* Round-trip delay of packets transmitted between the local and remote devices.
* Whether packet loss occurs and what is the packet loss ratio.You can use the **ping ipv6** command to check network connectivity or line quality in the following scenarios:
* Scenario 1: Check the protocol stack on the local device.You can run the **ping ipv6** command to check whether the TCP/IP protocol suite works properly on the local device.
* Scenario 2: Check whether the destination IPv6 host is reachable on an IPv6 network.You can run the ping ipv6 destination-ipv6-address command to send an ICMPv6 Echo Request message to the destination host. If a reply is received, the destination host is reachable.
* Scenario 3: Check whether the peer is reachable on an L3VPN.On an L3VPN, devices may lack routing information about each other. Run the ping ipv6 vpn-instance vpna destination-ipv6-address command, not the ping ipv6 destination-ipv6-address command, to check whether the peer is reachable. If the VPN instance name is specified, an ICMPv6 Echo Request message can reach the peer. If a reply is received, the peer is reachable.
* Scenario 4: Check network quality by analyzing the packet loss rate and average delay in the command output.For example, you can run the ping ipv6 -c 20 -t 5000 2001:db8:c01f:700:1::**3** command to check the quality of the line connecting the local device to the peer at 2001:db8:c01f:700:1::3. In the case of an unreliable network, increase -c and -t values to obtain information more accurately.
* Scenario 5: Check brief information about packet loss by specifying the -brief parameter in the **ping ipv6** command.

**Precautions**

* If the IPv6 address of the destination host corresponds to a local address, you need to specify the name of the local outbound interface that sends the Echo Request packet. Otherwise, the **ping ipv6** command times out.
* If an exception occurs during the execution of the **ping ipv6** command, you can press Ctrl+C to stop the execution.
* If the destination host is unreachable, you cannot run the **ping ipv6** command to check the network connection or network line fault. At the same time, the system displays the message "Request time out", indicating that the request times out.
* If a transit node is disabled from responding to ICMPv6 packets, detection on this node fails.
* If the IPv6 address of the destination host corresponds to a local address and the inbound interface of the response packet is specified, the interface bound to the local address is displayed.



Example
-------

# Perform forward domain name parsing to convert the domain name into an IPv6 address.
```
<HUAWEI> ping ipv6 -c 1 -name www.huawei.com
  Resolved Host ( www.huawei.com -> 2001:db8::1 )
  PING www.huawei.com (2001:db8::1) : 56  data bytes, press CTRL_C to break
    Reply from 2001:db8::1 
    bytes=56 Sequence=1 hop limit=64 time=5 ms
---2001:db8::1 ping statistics---
    1 packet(s) transmitted
    1 packet(s) received
    0.00% packet loss
    round-trip min/avg/max=5/5/5 ms

```

# Perform reverse domain name parsing to convert the IPv6 address into a domain name.
```
<HUAWEI> ping ipv6 -c 1 -name 2001:db8::1
  PING 2001:db8::1 (www.huawei.com): 56  data bytes, press CTRL_C to break
    Reply from 2001:db8::1 
    bytes=56 Sequence=1 hop limit=64 time=7 ms
---2001:db8::1 ping statistics---
    1 packet(s) transmitted
    1 packet(s) received
    0.00% packet loss
    round-trip min/avg/max=7/7/7 ms

```

# Ping an IPv6 address to check whether the host is reachable.
```
<HUAWEI> ping ipv6 2001:DB8::1
PING 2001:DB8::1 : 56  data bytes, press CTRL_C to break
    Reply from 2001:DB8::1
    bytes=56 Sequence=1 hop limit=64 time=115 ms
    Reply from 2001:DB8::1
    bytes=56 Sequence=2 hop limit=64 time=1 ms
    Reply from 2001:DB8::1
    bytes=56 Sequence=3 hop limit=64 time=1 ms
    Reply from 2001:DB8::1
    bytes=56 Sequence=4 hop limit=64 time=1 ms
    Reply from 2001:DB8::1
    bytes=56 Sequence=5 hop limit=64 time=1 ms
---2001:db8::1 ping statistics---
    5 packet(s) transmitted
    5 packet(s) received
    0.00% packet loss
    round-trip min/avg/max=1/23/115 ms

```

# Check whether the host with IPv6 address 2001:db8:1::1 is reachable and display brief information.
```
<HUAWEI> ping ipv6 -brief 2001:db8:1::1
  PING 2001:db8:1::1 : 56  data bytes, press CTRL_C to break
    !!!!!
--- 2001:db8:1::1 ping statistics---
    5 packet(s) transmitted
    5 packet(s) received
    0.00% packet loss
    round-trip min/avg/max=1/1/1 ms

```


**Table 1** Description of the
**ping ipv6** command output

| Item | Description |
| --- | --- |
| PING HH:HH::HH:HH | IPv6 address of the destination host. |
| press CTRL\_C to break | You can terminate the ongoing ping test by pressing Ctrl+C. |
| Reply from HH:HH::HH:HH | Information about an Echo Response packet in response to the ICMPv6 echo request packet:   * bytes: packet length. * sequence: sequence number of the packet. * hop limit: hop limit of the packet. * time: response time, in milliseconds.   If no ICMP echo reply packet is received within the timeout period, "Request time out" is displayed. |
| x data bytes | Length (in bytes) of a sent ICMPv6 echo request packet. |
| HH:HH::HH:HH ping statistics | Statistics collected in the ping test on the destination host. The statistics include the following information:   * packets transmitted: number of sent ICMP echo request packets. * packets received: number of received ICMP echo reply packets. * % packet loss: percentage of unresponded packets to total sent packets. * round-trip min/avg/max: minimum, average, and maximum time of responses. |