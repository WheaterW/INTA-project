tracert
=======

tracert

Function
--------

The **tracert** command enables the system to trace the gateways that packets pass through from the source to the destination.



Format
------

**tracert** [ **-a** *source-ip-address* [ **-response-public** | **-ignore-vpn** | **-response-vpn** *respVrfName* ] | **-f** *initTtl* | **-m** *maxTtl* | **-p** *destPort* | **-q** *nqueries* | **-vpn-instance** *vpn-instance-name* | **-w** *timeout* | **-name** | **-s** *size* | { **-tos** *tos-value* | **-dscp** *dscp* } | **-pipe** ] \* *host*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **-a** *source-ip-address* | Specifies a source IP address for the request packets to be sent.  If no source IP address is specified, the IP address of the outbound interface of the route is used as the source address of the request packets. For example, in a VPN scenario, an IP address in the VPN is preferentially used as the source address. | The value is in dotted decimal notation. |
| **-response-public** | Indicates that response packets are received from the public network. | - |
| **-ignore-vpn** | Indicates that the VPN instance is ignored in response packets. | - |
| **-response-vpn** *respVrfName* | Specifies the VPN instance name of response packets. | The value is a string of 1 to 31 case-sensitive characters without spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **-f** *initTtl* | Specifies the initial time to live (TTL).  Carried in the IP header, the TTL field indicates the lifetime of the IP packet and specifies the maximum number of devices that the packet can pass through. The TTL value is set on the source and reduced by 1 each time the packet passes through one device. When the TTL value is reduced to 0, the packet is discarded. At the same time, an ICMP Timeout packet is sent to the source.  If initTtl is specified and the number of hops is smaller than the specified value, the TTL value will be greater than 0 after the packet passes through all the nodes. Therefore, no ICMP timeout packet is sent to the source.If maxTtl is specified, the value of initTtl must be smaller than or equal to the value of maxTtl. | The value is an integer that ranges from 1 to 255. The default value is 1. |
| **-m** *maxTtl* | Specifies the maximum TTL.  Generally, the maximum TTL is set to the number of hops the packet passes through. You need to use this parameter to change the TTL. If initTtl is specified, the value of maxTtl must be greater than or equal to the value of initTtl. | The value is an integer that ranges from 1 to 255. The default value is 64. |
| **-p** *destPort* | Specifies the UDP port number of the destination.   * If no UDP port number is specified, when you run the tracert command, a port with the port number greater than 32768 is randomly chosen for the destination to receive trace packets. * Before specifying the UDP port number for the destination, ensure that the port is not in use; otherwise, the trace test fails. | The value is an integer ranging from 0 to 65535. The default value is 33434. |
| **-q** *nqueries* | Specifies the number of test packets sent in a trace test.  In the case of poor network qualities, you can set this parameter to a comparatively larger value to ensure that a test packet can reach the destination. | The value is an integer ranging from 1 to 65535. The default value is 3. |
| **-vpn-instance** *vpn-instance-name* | Specifies the name of the VPN instance to which the destination address belongs. | The value is a string of 1 to 31 case-sensitive characters without spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **-w** *timeout* | Specifies the period of time for waiting for a response.  If a test packet reaches a gateway and times out, "\*" is displayed.  In the case of poor network qualities and a low network transmission rate, you are advised to prolong the timeout period. | The value is an integer ranging from 0 to 3600000, in milliseconds. The default value is 5000. |
| **-s** *size* | Specifies a packet size. | It is an integer ranging from 12 to 9600. |
| **-pipe** | Specifies the pipe mode. | - |
| **-name** | Displays the host name of the destination address. | - |
| **-tos** *tos-value* | Specifies the ToS value of packets sent. By specifying this parameter, you can set the DSCP value and IP priority for packets. | The value is an integer ranging from 0 to 255. The default value is 0. |
| **-dscp** *dscp* | Specifies a DSCP value for the request packets to be sent. | The value is an integer ranging from 0 to 63. The default value is <b>0</b>. |
| *host* | Specifies the name or the IP address of the destination host. | The value is a string of 1 to 255 characters.  If the parameter value is an IP address, set the format of the parameter to dotted decimal notation. |




Views
-----

All views



Default Level
-------------

0: Visit level



Usage Guidelines
----------------

**Usage Scenario**

The **ping** command is used to check the connectivity of the network, and the **tracert** command is used to locate the faulty node.

In different test scenarios, parameters specified in the
**tracert** command are different:

* To view information about nodes between the source and the destination, run the **tracert host** command.
* To view information about nodes between the source and the destination on a network of poor qualities, run the **tracert -q nqueries -w timeout host** command. In the case of an unreliable network, you are advised to set -q and -w to larger values so as to obtain accurate information.
* To detect the nodes along a certain segment of a path, run the **tracert -f initTtl -m maxTtl host** command with the specified initial TTL and the maximum TTL.

**Prerequisites**

* Ensure that the UDP module of each node works properly. Otherwise, the tracert test fails.
* Ensure that the VPN module works properly if vpn-instance is specified.
* Ensure that the ICMP module of each node works properly; otherwise, \*\*\* is returned, indicating that the test times out.

**Implementation Procedure**

The process of the **tracert** command is as follows:

* The source sends a data packet with the TTL being 1. After the TTL times out, the first hop sends an ICMP Error message to the source, indicating that the data packet cannot be forwarded.
* The source sends a data packet with the TTL being 2. After the TTL times out, the second hop sends an ICMP Error message to the source, indicating that the data packet cannot be forwarded.
* The source sends a data packet with the TTL being 3. After the TTL times out, the third hop sends an ICMP Error message to the source, indicating that the data packet cannot be forwarded.
* The preceding process repeats until a packet reaches the destination.When receiving an IPv4 packet, the destination device of each hop searches for the port specified in the packet. If no such a port is found, the destination device sends back an ICMP Port Unreachable message, indicating that the destination port is unreachable and the tracert test ends. Based on the ICMP Port Unreachable message sent from each hop, you can obtain the path from the source to the destination.

**Precautions**

If tracert messages used to monitor IP network connectivity traverse a GRE tunnel, the **tracert** command output does not contain transit node information on the GRE tunnel.



Example
-------

# Trace the gateways from the source to the destination at 10.10.1.1.
```
<HUAWEI> tracert -name -f 2 -m 64 -s 100 10.10.1.1
traceroute to 10.10.1.1(tcore1.as1.net), hops max: 64, packet length: 100,press CTRL_C to break
1 10.1.1.1 (tcore1.as6.net) 19 ms 23 ms 20 ms
2 10.1.2.1 (tcore1.as6453.net) 19 ms 25 ms 30 ms
3 * * *
4 10.1.3.1 (tcore1.as63454.net) 259 ms 499 ms 279 ms
5 * * *
6 10.10.1.1 (tcore1.as1.net) 339 ms 279 ms 279 ms

```

# Perform reverse domain name parsing to convert the IP address into a domain name.
```
<HUAWEI> tracert -name 192.168.10.2
traceroute to 192.168.10.2(www.huawei.com), max hops: 64 ,packet length: 40,press CTRL_C to break
 1 192.168.10.2(www.huawei.com) 9 ms  1 ms  15 ms

```

# Display the gateways that packets with IP address 192.168.1.2 pass through in an inter-VPN scenario.
```
<HUAWEI> tracert -a 192.168.2.1 -response-vpn vpnb -vpn-instance vpna 192.168.1.2
Warning: The specified source address is not a local address, the tracert command will not check the network connection.
 traceroute to vpna 192.168.1.2(192.168.1.2), max hops: 64, packet length: 40, press CTRL_C to break
 1 192.168.1.2(response-vpn vpnb) 123 ms  5 ms  4 ms

```

# Trace the gateways from the source to the destination at 10.10.0.10. Set the number of trace packets to be sent to 5 and the timeout period to 8000 ms.
```
<HUAWEI> tracert -q 5 -w 8000 10.10.0.10
traceroute to 10.10.0.10 (10.10.0.10), hops max: 64, packet length: 40,press CTRL_C to break
1 10.3.112.1 (10.3.112.1) 17 ms 17 ms 27 ms 17ms 20ms
2 10.32.216.1 (10.32.216.1) 19 ms 19 ms 19 ms 19ms 18ms
3 10.32.216.1 (10.32.216.1) 39 ms 19 ms 19 ms 25ms 19ms
4 10.32.136.23 (10.32.136.23) 19 ms 39 ms 39 ms 21ms 28ms
5 10.32.168.22 (10.32.168.22) 20 ms 39 ms 39 ms 27ms 30ms
6 10.32.197.4 (10.32.197.4) 59 ms 119 ms 39 ms 60ms 57ms
7 10.119.2.5 (10.119.2.5) 59 ms 59 ms 39 ms 60ms 45ms
8 10.140.70.13 (10.140.70.13) 80 ms 79 ms 99 ms 90ms 87ms
9 10.140.71.6 (10.140.71.6) 139 ms 139 ms 159 ms 120ms 160ms
10 10.140.81.7 (10.140.81.7) 199 ms 180 ms 300 ms 200ms 150ms
11 10.140.72.17 (10.140.72.17) 300 ms 239 ms 239 ms 350ms 200ms
12 * * * * *
13 10.121.54.72 (10.121.54.72) 259 ms 499 ms 279 ms 500ms 550ms
14 * * * * *
15 * * * * *
16 * * * * *
17 * * * * *
18 10.10.0.10 (10.10.0.10) 339 ms 279 ms 279 ms 600ms 592ms

```

# Trace the gateways from the source to the destination at 192.168.5.115 on a specified L3VPN.
```
<HUAWEI> tracert -vpn-instance abc 192.168.5.115
traceroute to 192.168.5.115 (192.168.5.115), hops max: 64, packet length: 40,press CTRL_C to break
1 10.3.112.1 (10.3.112.1) 17 ms 17 ms 27 ms
2 10.32.216.1 (10.32.216.1) 19 ms 19 ms 19 ms
3 * * *
4 10.121.54.72 (10.121.54.72) 259 ms 499 ms 279 ms
5 * * *
6 192.168.5.115 (192.168.5.115) 339 ms 279 ms 279 ms

```

# Perform forward domain name parsing to convert the domain name into an IP address.
```
<HUAWEI> tracert www.huawei.com
traceroute to 192.168.10.2(www.huawei.com), max hops: 64 ,packet length: 40,press CTRL_C to break
 1 192.168.10.2 7 ms  2 ms  12 ms

```


**Table 1** Description of the
**tracert** command output

| Item | Description |
| --- | --- |
| traceroute to x.x.x.x | IP address of the destination host. |
| packet length: x | Size of a test packet. |
| 1 x.x.x.x a ms b ms c ms | The value 1 indicates the first-hop gateway. The sequence number increases by one each time a hop is added. By default, the maximum number of hops is 64.  x.x.x.x indicates the gateway address of the first hop. The IPv4 address following the sequence number of each hop is the gateway address of the hop.  a ms b ms c ms indicates the difference between the time when three UDP packets are sent and the time when ICMP Time Exceeded or ICMP Port Unreachable packets are received. By default, three UDP probe packets are sent for each hop. |
| hops max: x | Maximum TTL value for tracert. |
| \* | Test packet times out. |
| x | TTL value. |
| x.x.x.x | Address of a reply. |
| x ms | Round-trip time (RTT). |