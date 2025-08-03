ping
====

ping

Function
--------

The **ping** command checks the connectivity of an IP network and reachability of a host.



Format
------

**ping** [ **ip** ] { [ **-c** *count* | **-i** { *interface-name* | *interface-type* *interface-number* } | **-nexthop** *nexthop-address* | { **-range** [ **min** *min-value* | **max** *max-value* | **step** *step-value* ] \* | **-s** *packetsize* } | **-t** *timeout* | **-m** *time* | **-a** *source-ip-address* [ **-ignore-vpn** | **-response-vpn** *respVrfName* ] | **-h** *ttl-value* | **-p** *pattern* | { **-tos** *tos-value* | **-dscp** *dscp-value* } | { **-f** | **ignore-mtu** } | **-q** | **-r** | **-vpn-instance** *vpn-instance-name* | **-v** | **-name** | **-system-time** | **-ri** | **-8021p** *8021p-value* | **-detail** ] \* *host* [ **ip-forwarding** ] }

**ping** [ **ip** ] { [ **-c** *count* | **-i** { *interface-name* | *interface-type* *interface-number* } | **-nexthop** *nexthop-address* | { **-range** [ **min** *min-value* | **max** *max-value* | **step** *step-value* ] \* | **-s** *packetsize* } | **-t** *timeout* | **-m** *time* | **-a** *source-ip-address* | **-h** *ttl-value* | **-p** *pattern* | { **-tos** *tos-value* | **-dscp** *dscp-value* } | { **-f** | **ignore-mtu** } | **-vpn-instance** *vpn-instance-name* | **-name** | **-8021p** *8021p-value* | **-brief** ] \* *host* [ **ip-forwarding** ] }



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip** | Specifies the IPv4 protocol. | The default value is IPv4. |
| **-c** *count* | Specifies the maximum number of times for sending ICMP echo request packets.  After you run the ping command, the sequence number of an ICMP echo request packet starts from 1 and is incremented by 1 each time an ICMP echo request packet is sent. By default, five ICMP echo request packets are sent. You can use count to specify the number of ICMP echo request packets to be sent. If the peer is reachable, it sends five ICMP Echo Response packets with the same sequence numbers as those of the ICMP echo request packets.  In the case of a poor network quality, increase the count value and monitor network quality based on the packet loss ratio. | The value is an integer ranging from 1 to 4294967295. The default value is 5. |
| **-i** *interface-name* | Specifies the interface through which ICMP echo request packets are sent.  For broadcast links (on the Ethernet), the specified destination address functions as the next hop address. | The value is a string of 1 to 63 characters. |
| *interface-type* | Specifies the type of an interface through which ICMP echo request packets are sent.  For broadcast links (on the Ethernet), the specified destination address functions as the next hop address. | - |
| *interface-number* | Specifies the number of an interface through which ICMP echo request packets are sent.  For broadcast links (on the Ethernet), the specified destination address functions as the next hop address. | - |
| **-nexthop** *nexthop-address* | Specifies an IP address for the next hop.  If you have specified this parameter, the device no longer searches the routing table before sending ICMP Echo Response packets. This process prevents ping failures caused by incorrect routing entries. | The value is in dotted decimal notation.   * The specified next hop address must be the next hop address of a directly connected physical interface. * When specifying the next hop address, you can configure -i interface-type interface-number to specify the outbound interface. The following conditions must be met to ensure a test success:   1. The specified next hop address must match the outbound interface.   2. The specified outbound interface cannot be a logical interface's member interface. * When you specify the next hop address, you cannot specify a VPN. |
| **-s** *packetsize* | Specifies the length of an ICMP echo request packet (excluding the IP header and ICMP header). | The value is an integer ranging from 10 to 9600, in bytes. The default value is 56. |
| **-range** | Enables the device to send ICMP echo request messages with variable payload lengths. | * If -range is not specified, the length of the sent packet is -s packetsize. The default value is 56. * If -range is specified, the length of the first sent packet is min min-value, and the lengths of subsequent packets increase by step step-value until the packet length reaches max max-value.   By default, the payload length ranges from 56 to 9600, and the step is 1.   * During the execution, you can press Ctrl+C to terminate the execution. * You can adjust the values of min min-value and max max-value to control the number of packets to be sent. The value of min min-value must be smaller than that of max max-value. * If both the -range and -c count parameters are specified, the device sends ICMP Echo Request messages of the same payload length for the number of times specified by the -c count parameter. |
| **min** *min-value* | Specifies the minimum payload length of an ICMP echo request message. | The value is an integer that ranges from 20 to 9600, in bytes. The default value is 56, in bytes. |
| **max** *max-value* | Specifies the minimum payload length of an ICMP Echo Request message. | The value is an integer that ranges from 20 to 9600, in bytes. The default value is 9600. |
| **step** *step-value* | Specifies the step length of an ICMP echo request message. | The value is an integer that ranges from 1 to 1000. The default value is 1. |
| **-t** *timeout* | Specifies the timeout period for waiting for an ICMP Echo Reply packet after an ICMP Echo Request Packet is sent.  After the ping command is run, the source sends an ICMP Echo Request packet to a specific address and waits for a reply. If the destination sends an ICMP Echo Reply packet to the source within the time specified by timeout, the destination is reachable. If the destination does not send any reply within the timeout period, the source displays a timeout message.  Normally, the source will receive an ICMP Echo Reply packet within 1 to 10 seconds after an ICMP Echo Request packet is sent. If the network transmission rate is low, increase the timeout period. | The value is an integer ranging from 0 to 65535, in milliseconds. The default value is 2000. |
| **-m** *time* | Specifies the interval at which ICMP echo request packets are sent.  After you run the ping command, the device sends an ICMP echo request packet. If the device fails to receive a reply within 500 ms, it sends the next ICMP echo request packet. You can use the time parameter to set the interval at which ICMP echo request packets are sent. Do not set this parameter to less than 2000 ms on an unstable network. | The value is an integer ranging from 1 to 10000, in milliseconds. The default value is 500. |
| **-a** *source-ip-address* | Specifies a source IP address for the ICMP Echo Request messages to be sent.  If no source IP address is specified, the IP address of the outbound interface of the route is used as the source address of ICMP Echo Request messages. For example, in a VPN scenario, an IP address in the VPN is preferentially used as the source address. | The value is in dotted decimal notation. |
| **-ignore-vpn** | Indicates that the VPN instance is ignored in response packets. | - |
| **-response-vpn** *respVrfName* | Specifies the VPN instance name of response packets. | The value is a string of 1 to 31 case-sensitive characters, which do not contain spaces. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **-h** *ttl-value* | Specifies the TTL value.  If the TTL value in a packet is reduced to 0 during forwarding, the device that receives the packet sends an ICMP timeout packet to the source, indicating that the destination is unreachable. | The value is an integer ranging from 1 to 255. The default value is 255. |
| **-p** *pattern* | Specifies the padding byte of ICMP echo request packets.  The padding byte allows the system to identify a specific packet among a great number of received ICMP Echo Response packets. | The value is in hexadecimal notation and ranges from 0 to FFFFFFFF. By default, the padding starts from 0x00 in ascending order. |
| **-tos** *tos-value* | Specifies the ToS value of an ICMP echo request packet.  The priority of an ICMP packet is determined by the ToS value. | The value is an integer ranging from 0 to 255. The default value is 0. |
| **-dscp** *dscp-value* | Specifies the DSCP value of an Echo Request packet to be sent. | The value is an integer ranging from 0 to 63. The default value is <b>0</b>. |
| **-f** | Indicates that packets are not fragmented during transmission. | By default, packets will be fragmented during transmission. |
| **ignore-mtu** | Indicates that the system does not check the interface MTU when a packet is sent. | - |
| **-q** | Indicates that only statistics are displayed. By default, all information is displayed.  If -q is specified in the ping command, the system displays only statistics about sent and received packets, packet loss ratio, and minimum, average, and maximum RTTs. | By default, the system displays all information. |
| **-r** | Records routes.  If -r is configured, the IP address of each device that the IP packet passes along the packet transmission path is recorded in the Options field. When the IP packet reaches the destination, all IP addresses recorded in the Options field are copied to an ICMP Echo Response packet. In addition, the IP address of each device that the ICMP Echo Response packet passes through is recorded. When the ping program receives the reply, IP addresses of the passed devices are displayed. | By default, no route is recorded. |
| **-vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters without spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **-v** | Enables the device to display ICMP echo reply packets that are received by but not for this device. For example, a packet times out, or the sequence number of a packet is incorrect.   * If -v is not configured, the system displays only the ICMP Echo Response packets received by the local user.If -v is configured, the system displays all received ICMP Echo Response packets. * If the sequence number of a received ICMP Echo Response packet is incorrect or the packet delay is longer than the timeout period, the system displays a detailed message. | By default, non-user ICMP Echo Reply messages are not displayed. |
| **-system-time** | Specifies the system time when an ICMP echo request packet is sent. | - |
| **-ri** | Indicates that the source interface of echo response packet is displayed. | - |
| **-8021p** *8021p-value* | Specifies the 802.1p value of an echo request packet to be sent. | The value is an integer ranging from 0 to 7. The default value is 0. |
| **-name** | Displays the host name of the destination address. | - |
| **-detail** | Displays detailed information about packet loss. | - |
| *host* | Specifies the IP address or host name of a remote system. | The value is a string of case-sensitive characters. It cannot contain spaces. |
| **ip-forwarding** | Indicates that the ping packets are forcibly forwarded through IP on the first node. | - |
| **-brief** | Displays brief information about packet loss. | - |




Views
-----

All views



Default Level
-------------

0: Visit level



Usage Guidelines
----------------

**Usage Scenario**

Ping is a common debugging tool used to test the network connectivity. It uses ICMP packets to check the following items:

* Whether the remote device is available.
* Round-trip delay of packets transmitted between the local and remote devices.
* Whether packet loss occurs and what is the packet loss ratio.You can use the **ping** command to check network connectivity or line quality in the following scenarios:
* Check the protocol stack on the local device. The ping loopback-address command checks whether the TCP/IP protocol suite works properly on the local device.
* Check whether the destination host is reachable on an IP network. You can run the ping host command to send an ICMP echo request packet to the destination host. If a reply is received, it means that the destination host is reachable.
* Check whether the peer is reachable on an L3VPN. On an L3VPN, devices may lack routing information about each other, and run the **ping -vpn-instance vpn-instance-name host** command, not the ping host command, to check whether the peer is reachable. If the VPN instance name is specified, an ICMP echo request packet can reach the peer. If a reply is received, the peer is reachable.
* On an unstable network, run the **ping -c count-t timeout host** command to roughly determine the network quality between the local device and the peer host. The command output contains the packet loss rate and average delay for you to evaluate the network quality. If the network quality is poor, setting greater values for the count and timeout parameters is recommended to obtain more accurate testing results.
* Check the path. You can run the **ping -r host** command to obtain information about nodes along the path from the local device to the peer.
* Check the path MTU. You can run the ping { -f | ignore-mtu } -s packetsize host command to prevent ICMP packet fragmentation, or the system does not check the interface MTU when a packet is sent, and set the length of an ICMP packet so as to obtain the path MTU after multiple probes.
* If system resources are insufficient, error information is displayed.
* To display brief information about packet loss, set the -brief parameter.

**Prerequisites**

* Before running the **ping** command, the ICMP module is working properly.
* If -vpn-instance is configured, the VPN module is working properly.

**Configuration Impact**

* If the destination host is unreachable, you cannot run the **ping** command to check network connectivity or locate a line fault. In this case, the system displays "Request time out", indicating that the ICMP Echo Request packet times out.
* If an intermediate device is disabled from responding to ICMP packets, detection on this node fails.

**Precautions**

If an exception occurs during the ping operation, you can press Ctrl+C to stop the ping operation.

The
**ping** command does not allow users to send ping packets to a broadcast address, such as XX.XX.XX.255/24.If both -c and -range are configured, -c indicates the number of times packets are sent at each step.If the IPv4 address of the destination host corresponds to a local address and the inbound interface of the response packet is specified, the inbound interface of the response packet cannot be displayed.

Example
-------

# Check whether the host with IP address 10.1.1.2 is reachable. Set the length of an ICMP echo request packet to 300 bytes, the time for waiting for the next ICMP echo request packet to 3000 ms, and the VPN instance name to vpna.
```
<HUAWEI> ping -m 3000 -s 300 -vpn-instance vpna 10.1.1.2
  PING 10.1.1.2: 300 data bytes, press CTRL_C to break 
    Reply from 10.1.1.2: bytes=300 Sequence=1 ttl=255 time=31 ms 
    Reply from 10.1.1.2: bytes=300 Sequence=2 ttl=255 time=31 ms 
    Reply from 10.1.1.2: bytes=300 Sequence=3 ttl=255 time=31 ms 
    Reply from 10.1.1.2: bytes=300 Sequence=4 ttl=255 time=31 ms 
    Reply from 10.1.1.2: bytes=300 Sequence=5 ttl=255 time=31 ms 

  --- 10.1.1.2 ping statistics --- 
    5 packet(s) transmitted 
    5 packet(s) received 
    0.00% packet loss 
    round-trip min/avg/max = 31/31/31 ms

```

# Enable the device to send ICMP echo request messages with variable payload lengths.
```
<HUAWEI> ping -range min 56 max 60 192.168.1.9
  PING 192.168.1.9: 56-60  data bytes, press CTRL_C to break
    Reply from 192.168.1.9: bytes=56 Sequence=1 ttl=255 time=80 ms
    Reply from 192.168.1.9: bytes=57 Sequence=2 ttl=255 time=60 ms
    Reply from 192.168.1.9: bytes=58 Sequence=3 ttl=255 time=80 ms
    Reply from 192.168.1.9: bytes=59 Sequence=4 ttl=255 time=80 ms
    Reply from 192.168.1.9: bytes=60 Sequence=5 ttl=255 time=50 ms

  --- 192.168.1.9 ping statistics ---
    5 packet(s) transmitted
    5 packet(s) received
    0.00% packet loss
    round-trip min/avg/max = 50/70/80 ms

```

# Check whether the host with IP address 10.1.1.3 is reachable and display detailed information.
```
<HUAWEI> ping -detail 10.1.1.3
  PING 10.1.1.3: 56 data bytes, press CTRL_C to break
    Request time out (unroutable)
    Request time out (unroutable)
    Request time out (unroutable)
    Request time out (unroutable)
    Request time out (unroutable)

  --- 10.1.1.3 ping statistics ---
    5 packet(s) transmitted
    0 packet(s) received
    100.00% packet loss

```

# Perform forward domain name parsing to convert the domain name into an IP address.
```
<HUAWEI> ping www.huawei.com
  PING www.huawei.com (192.168.10.2): 56  data bytes, press CTRL_C to break
    Reply from 192.168.10.2: bytes=56 Sequence=1 ttl=255 time=7 ms
    Reply from 192.168.10.2: bytes=56 Sequence=2 ttl=255 time=10 ms
    Reply from 192.168.10.2: bytes=56 Sequence=3 ttl=255 time=7 ms
    Reply from 192.168.10.2: bytes=56 Sequence=4 ttl=255 time=11 ms
    Reply from 192.168.10.2: bytes=56 Sequence=5 ttl=255 time=11 ms

  --- www.huawei.com ping statistics ---
    5 packet(s) transmitted
    5 packet(s) received
    0.00% packet loss
    round-trip min/avg/max = 7/9/11 ms

```

# Check whether the host with IP address 10.1.1.2 is reachable. Set the source address to 1.1.1.1 and the number of ICMP echo request packets to be sent to 8.
```
<HUAWEI> ping -a 1.1.1.1 -c 8 10.1.1.2
  PING 10.1.1.2: 56 data bytes, press CTRL_C to break 
    Reply from 10.1.1.2: bytes=56 Sequence=1 ttl=255 time=32 ms 
    Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=255 time=32 ms 
    Reply from 10.1.1.2: bytes=56 Sequence=3 ttl=255 time=32 ms 
    Reply from 10.1.1.2: bytes=56 Sequence=4 ttl=255 time=32 ms 
    Reply from 10.1.1.2: bytes=56 Sequence=5 ttl=255 time=32 ms 
    Reply from 10.1.1.2: bytes=56 Sequence=6 ttl=255 time=32 ms 
    Reply from 10.1.1.2: bytes=56 Sequence=7 ttl=255 time=32 ms 
    Reply from 10.1.1.2: bytes=56 Sequence=8 ttl=255 time=32 ms 

  --- 10.1.1.2 ping statistics --- 
    8 packet(s) transmitted 
    8 packet(s) received 
    0.00% packet loss 
    round-trip min/avg/max = 32/32/32 ms

```

# Check whether the host with IP address 10.1.1.2 is reachable.
```
<HUAWEI> ping 10.1.1.2
  PING 10.1.1.2 : 56 data bytes , press CTRL_C to break 
    Reply from 10.1.1.2 : bytes=56 sequence=1 ttl=255 time = 1ms 
    Reply from 10.1.1.2 : bytes=56 sequence=2 ttl=255 time = 2ms 
    Reply from 10.1.1.2 : bytes=56 sequence=3 ttl=255 time = 1ms 
    Reply from 10.1.1.2 : bytes=56 sequence=4 ttl=255 time = 3ms 
    Reply from 10.1.1.2 : bytes=56 sequence=5 ttl=255 time = 2ms 

  --10.1.1.2 ping statistics-- 
    5 packet(s) transmitted 
    5 packet(s) received 
    0.00% packet loss 
    round-trip min/avg/max = 1/2/3 ms

```

# Check whether the host with IP address 10.1.1.2 is reachable and display brief information.
```
<HUAWEI> ping -brief 10.1.1.2
  PING 10.1.1.2: 56  data bytes, press CTRL_C to break
    !!!!!

  --- 10.1.1.2 ping statistics ---
    5 packet(s) transmitted
    5 packet(s) received
    0.00% packet loss
    round-trip min/avg/max = 1/1/1 ms

```

# Perform reverse domain name parsing to convert the IP address into a domain name.
```
<HUAWEI> ping -c 2 -a 192.168.10.2 -name 192.168.10.2
  PING 192.168.10.2 (www.huawei.com): 56  data bytes, press CTRL_C to break
    Reply from 192.168.10.2: bytes=56 Sequence=1 ttl=255 time=18 ms
    Reply from 192.168.10.2: bytes=56 Sequence=2 ttl=255 time=8 ms

  --- 192.168.10.2 ping statistics ---
    2 packet(s) transmitted
    2 packet(s) received
    0.00% packet loss
    round-trip min/avg/max = 8/13/18 ms

```

# Enable the device to display ICMP echo reply packets that are received by but not for this device. The sequence numbers of the packets are incorrect, and the packet delay is longer than the timeout period.
```
<HUAWEI> ping -v -m 300 -t 300 10.0.0.1
  PING 10.0.0.1: 56  data bytes, press CTRL_C to break
    Request time out
    Reply from 10.0.0.1: bytes=56 Sequence=2 ttl=255 time=259 ms
    Error: Sequence number = 1 is less than the correct = 3!
    Request time out
    Error: Trip time = 320 ms is longer than wait time = 300 ms!
    Reply from 10.0.0.1: bytes=56 Sequence=4 ttl=255 time=280ms
    Reply from 10.0.0.1: bytes=56 Sequence=5 ttl=255 time=256 ms

  --- 10.0.0.1 ping statistics ---
    5 packet(s) transmitted
    3 packet(s) received
    40.00% packet loss
    round-trip min/avg/max = 256/265/280 ms

```

# Check whether the host with IP address 192.168.1.2 is reachable in an inter-VPN scenario.
```
<HUAWEI> ping -a 192.168.2.1 -response-vpn vpnb -vpn-instance vpna 192.168.1.2
Warning: The specified source address is not a local address, the ping command will not check the network connection.
  PING 30.1.1.2: 56  data bytes, press CTRL_C to break
    Reply from 192.168.1.2 response-vpn vpnb: bytes=56 Sequence=1 ttl=255 time=4 ms
    Reply from 192.168.1.2 response-vpn vpnb: bytes=56 Sequence=2 ttl=255 time=3 ms
    Reply from 192.168.1.2 response-vpn vpnb: bytes=56 Sequence=3 ttl=255 time=3 ms
    Reply from 192.168.1.2 response-vpn vpnb: bytes=56 Sequence=4 ttl=255 time=3 ms
    Reply from 192.168.1.2 response-vpn vpnb: bytes=56 Sequence=5 ttl=255 time=3 ms

  --- 192.168.1.2 ping statistics ---
    5 packet(s) transmitted
    5 packet(s) received
    0.00% packet loss
    round-trip min/avg/max = 3/3/4 ms

```


**Table 1** Description of the
**ping** command output

| Item | Description |
| --- | --- |
| PING x.x.x.x | IP address of the destination host. |
| press CTRL\_C to break | Press Ctrl+C to stop the ongoing ping test. |
| Reply from x.x.x.x | Response of the destination host to each Echo Request packet, including:   * bytes: length of the ICMP Echo Reply message. * sequence: sequence number of the response packet. * ttl: TTL of the ICMP Echo Reply packet. * time: response time, in ms. If no response packet is received after the timeout period, the message "Request time out" is displayed. |
| Request time out(xxxx) | Request times out. The timeout cause is displayed, which can be:   * unroutable: The route is not reachable. * no ARP: There are no ARP entries. * outgoing interface down: The outbound interface is Down. * icmp\_id is xxxx not xxxx: The ICMP ID is incorrect. * sequence is xxxx not xxxx: The sequence is incorrect. * ttl iquals 0 during transit: The TTL times out, causing an error.   Other causes of packet loss are not displayed. |
| x data bytes | Length of the Echo Request packet to be sent. |
| x.x.x.x ping statistics | Statistics collected in the ping test on the destination host. The statistics include the following information:   * packets transmitted: number of sent echo request packets. * packets received: number of received echo reply packets. * % packet loss: percentage of unresponded packets to total sent packets. * round-trip min/avg/max: minimum, average, and maximum time of responses. |