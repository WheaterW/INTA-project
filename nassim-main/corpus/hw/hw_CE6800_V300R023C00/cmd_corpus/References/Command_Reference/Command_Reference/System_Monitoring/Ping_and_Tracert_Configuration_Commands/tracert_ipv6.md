tracert ipv6
============

tracert ipv6

Function
--------

The **tracert ipv6** command enables the system to trace gateways that packets pass through from the source to the destination with an IPv6 address.



Format
------

**tracert ipv6** [ **-f** *first-hop-limit* | **-m** *max-hop-limit* | **-p** *port-number* | **-q** *probes* | **-w** *timeout* | **vpn-instance** *vpn-instance-name* | **-s** *size* | **-name** | **-a** *source-ipv6-address* | **-nexthop** *nextHopAddr* | **-passroute** | { **-tc** *tc* | **-dscp** *dscp* } | **-pipe** ] \* *host-name* [ **-i** { *ifName* | *ifType* *ifNum* } ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **-f** *first-hop-limit* | Specifies the initial hop-limit.  Carried in the IPv6 header, the hop-limit field indicates the lifetime of the IPv6 packet and specifies the maximum number of devices through which the packet can pass. The hop-limit field in IPv6 packets is similar to the TTL field in IPv4 packets. The hop-limit value is set on the source and reduced by 1 each time the packet passes through one device. When the hop-limit value is reduced to 0, the packet is discarded. At the same time, an ICMPv6 Timeout packet is sent to the source.  If first-hop-limit is specified and the number of hops is less than the specified value, the hop-limit value will be greater than 0 after the packet passes through all the nodes. Therefore, no ICMPv6 Timeout packet is sent to the source.  If max-hop-limit is specified, the value of first-hop-limit must be smaller than the value of max-hop-limit. | The value is an integer that ranges from 1 to 255. The default value is 1. |
| **-m** *max-hop-limit* | Specifies the maximum hop-limit.  Usually, the maximum hop-limit is set to the number of hops through which packets passes. Use this parameter to change hop-limit.  If first-hop-limit is specified, max-hop-limit must be greater than first-hop-limit. | The value is an integer that ranges from 1 to 255. The default value is 64. |
| **-p** *port-number* | Specifies the UDP port number of the destination.   * If no UDP port number is specified for the destination, when you run the tracert ipv6 command, a port with the port number greater than 32768 is randomly selected for the destination to receive trace packets. * The UDP port number to be specified must not in use. If a used UDP number is specified, the trace test fails. | The value is an integer ranging from 1 to 65535. The default value is 33434. |
| **-q** *probes* | Specifies the number of trace packets to be sent in a traceroute test.  If the network quality is poor, you can increase the number of probe packets to ensure that the probe packets can reach the destination node. | The value is an integer ranging from 1 to 65535. The default value is 3. |
| **-w** *timeout* | Specifies the timeout period for waiting for a response packet.  If a tracert packet times out when reaching a gateway, an asterisk (\*) is displayed.  If network quality is poor and the transmission rate is low, you can increase the parameter value to prolong the timeout period. | The value is an integer ranging from 1 to 65535, in milliseconds. The default value is 5000. |
| **vpn-instance** *vpn-instance-name* | Specifies the VPN instance name. | The value is a string of 1 to 31 case-sensitive characters. |
| **-s** *size* | Specifies a packet size. | The value is an integer that ranges from 20 to 9600. |
| **-name** | Displays the host name of the destination address. | - |
| **-nexthop** *nextHopAddr* | Specifies an IPv6 address for the next hop.  If you have specified this parameter, the device no longer searches the routing table before sending UDP packets. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X.   * The specified next hop address must be the next hop address of a directly connected physical interface. * When specifying the next hop address, you can configure -i interface-type interface-number to specify the outbound interface. The following conditions must be met to ensure a test success: * The specified next hop address matches the outbound interface. * The specified outbound interface cannot be a member interface of a logical interface. * When you specify the next hop address, you cannot specify a VPN. |
| **-passroute** | Sends UDP packets without searching for the routing table. | - |
| **-pipe** | Specifies the pipe mode. | - |
| **-a** *source-ipv6-address* | Specifies a source IPv6 address for the request packets to be sent.  If no source IPv6 address is specified, the IPv6 address of the outbound interface of the route is used as the source address of request packets. For example, in a VPN scenario, an IPv6 address in the VPN is preferentially used as the source address. | The value is a 32-digit hexadecimal number in format X:X:X:X:X:X:X:X. |
| **-tc** *tc* | Specifies the traffic class for echo request packets.  You can specify traffic-class-value to control echo request traffic. | The value is an integer ranging from 0 to 255. The default value is 0. |
| **-dscp** *dscp* | Specifies a DSCP value for the request packets to be sent. | The value is an integer ranging from 0 to 63. The default value is <b>0</b>. |
| *host-name* | Specifies the name or the IPv6 address of a destination host. | The value is a string of 1 to 255 characters.  If the IPv6 address of a destination is specified, the value is in the format of X:X:X:X:X:X:X:X. |
| **-i** *ifName* | Sets the interface name for sending UDP messages. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *ifType* | Sets the interface type for sending UDP messages. | - |
| *ifNum* | Sets the interface number for sending UDP messages. | The value is a string of 1 to 63 case-insensitive characters. It cannot contain spaces. |




Views
-----

All views



Default Level
-------------

0: Visit level



Usage Guidelines
----------------

**Usage Scenario**

You can run the **ping ipv6** command to check the connectivity of the network and then run the **tracert ipv6** command to locate the faulty node.

You can specify different parameters in the
**tracert ipv6** command in various test scenarios:

* To view information about nodes between the source and destination, run the **tracert ipv6 host** command.
* To view information about nodes between the source and destination on an L3VPN, run the tracert ipv6 vpn-instance vpn-instance-name host command. On an L3VPN, devices may not have each other's routing information, and you cannot use the **tracert ipv6 host** command to check whether the peer is reachable. Instead, you can run the tracert ipv6 vpn-instance vpn-instance-name host command to view information about nodes between the source and destination in a specified VPN instance.
* To view information about nodes between the source and destination on a network of poor qualities, run the **tracert ipv6 -q probes -w timeout host** command. On an unreliable network, increase -q and -w values to obtain more information.
* To check the nodes along a specified segment of a path, run the **tracert ipv6 -f first-hop-limit -m max-hop-limit host** command with the specified initial hop-limit and the maximum hop-limit.
* To display the label information of a tracert path, run the **tracert ipv6 -v** command.

**Prerequisites**

* Ensure that the UDP module of each node works properly. Otherwise, the tracert IPv6 test fails.
* Ensure that the VPN module works properly if vpn-instance is specified.
* Ensure that the ICMPv6 module of each node works properly. Otherwise, \* \* \* is returned, indicating that the test times out.

**Implementation Procedure**

The process of the **tracert ipv6** command is as follows:

* The source sends a packet with the hop-limit of 1. After the hop-limit times out, the first hop sends an ICMPv6 Error packet to the source, indicating that the packet cannot be forwarded.
* The source sends a packet with the hop-limit of 2. After the hop-limit times out, the second hop sends an ICMPv6 Error packet to the source, indicating that the packet cannot be forwarded.
* The source sends a packet with the hop-limit of 3. After the hop-limit times out, the third hop sends an ICMPv6 Error packet to the source, indicating that the packet cannot be forwarded.
* The preceding process proceeds until a packet reaches the destination.When receiving a test IPv6 packet, the destination hop attempts to find the port specified in the IPv6 packet. If no such a port is found, the destination hop sends back an ICMP Port Unreachable packet, indicating that the destination port is unreachable. The trace test then ends. Based on the ICMP Port Unreachable packet sent from each hop, you can obtain information about the path from the source to the destination.

**Precautions**

* By default, the ICMPv6 module is automatically enabled after the IPv6 module is enabled.
* In load balancing scenarios, when multiple packets are sent, different device addresses are displayed for the same hop.



Example
-------

# Perform forward domain name parsing to convert the domain name into an IPv6 address.
```
<HUAWEI> tracert ipv6 -name -f 1 -m 3 -p 65535 -q 2 www.huawei.com
 Resolved Host ( www.huawei.com -> 2001:DB8::1 )
 traceroute to www.huawei.com (2001:DB8::1)  3 hops max,60 bytes packet
 1 2001:DB8::1 66 ms  22 ms

```

# Trace the gateways along a specified segment of a path between the source host and the destination host at 2001:db8:100::3. Set the initial hop-limit and maximum hop-limit.
```
<HUAWEI> tracert ipv6 -f 2 -m 64 2001:db8:100::3
traceroute to vpn_out 2001:DB8:100::3 64 hops max,60 bytes packet
 1 2001:DB8:200::2 26 ms  23 ms  26 ms
 2 2001:DB8:300::1 47 ms 32 ms 33 ms
 3 2001:DB8:400::2 63 ms 46 ms 47 ms
 4 2001:DB8:100::3 78 ms 79 ms 62 ms

```

# Trace the gateways from the source to the destination at 2001:db8:100::3 on a specified L3VPN.
```
<HUAWEI> tracert ipv6 vpn-instance vsi6 2001:db8:100::3
traceroute to 2001:DB8:100::3  64 hops max,60 bytes packet
 1 2001:DB8:200::2 26 ms  23 ms  26 ms
 2 2001:DB8:100::2 3020 ms  !H 3024 ms  !H 4040 ms  !H

```

# Trace the gateways from the source to the destination at 2001:db8:100::3. Configure the test packets to be sent for 5 times and the timeout period to 8000 ms.
```
<HUAWEI> tracert ipv6 -q 5 -w 8000 2001:db8:100::3
traceroute to 2001:DB8:100::3 64 hops max,60 bytes packet
1 2001:DB8:200::2 26 ms 23 ms 26 ms 30 ms 29 ms 
2 2001:DB8:100::3 3020 ms 3024 ms 4040 ms 6820 ms 5584 ms

```

# Perform reverse domain name parsing to convert the IPv6 address into a domain name.
```
<HUAWEI> tracert ipv6 -name -f 1 -m 3 -p 65535 -q 2 2001:db8::1
 traceroute to 2001:DB8::1 (www.huawei.com) 3 hops max,60 bytes packet
 1 2001:DB8::1 67 ms  14

```


**Table 1** Description of the
**tracert ipv6** command output

| Item | Description |
| --- | --- |
| 1 | Sequence number of the received ICMPv6 Echo Response packet. |
| traceroute to HH:HH::HH:H | Destination IPv6 address. |
| x hops max | Maximum hop-limit. |
| x bytes packet | Size of a test packet. |
| HH:HH::HH:H | Address of a reply. |
| x ms x ms x ms | Round-trip time (RTT), in milliseconds. |