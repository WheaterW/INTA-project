Using Ping to Test IPv4 or IPv6 Network Connectivity
====================================================

Using Ping to Test IPv4 or IPv6 Network Connectivity

#### Context

The number of ICMP Echo Request messages sent in a ping operation is configurable, which is 5 by default. The packet sequence number starts at 1. Each time an ICMP Echo Request message is sent, the packet sequence number is incremented by 1. If the destination is reachable, it sends ICMP Echo Reply messages with the same sequence number as the ICMP Echo Request messages that cause the reply.


#### Procedure

* Configure ping to test IPv4 network connectivity.
  
  You can perform either of the following operations to display details or brief information as required.
  + Run the following command to display detailed information:
    ```
    [ping](cmdqueryname=ping) [ ip ] { [ -c count | -i { interface-name | interface-type interface-number } | -nexthop nexthop-address | { -range [ min min-value | max max-value | step step-value ] * | -s packetsize } | -t timeout | -m time | -a source-ip-address [ -ignore-vpn | -response-vpn respVrfName ] | -h ttl-value | -p pattern | { -tos tos-value | -dscp dscp-value } | { -f | ignore-mtu } | -q | -r | -vpn-instance vpn-instance-name | -v | -name | -system-time | -ri | -8021p 8021p-value | -detail ] * host [ ip-forwarding ] }
    ```
  + Run the following command to display brief information:
    ```
    [ping](cmdqueryname=ping) [ ip ] { [ -c count | -i { interface-name | interface-type interface-number } | -nexthop nexthop-address | { -range [ min min-value | max max-value | step step-value ] * | -s packetsize } | -t timeout | -m time | -a source-ip-address | -h ttl-value | -p pattern | { -tos tos-value | -dscp dscp-value } | { -f | ignore-mtu } | -vpn-instance vpn-instance-name | -name | -8021p 8021p-value | -brief ] * host [ ip-forwarding ] }
    ```
* Configure ping to test IPv6 network connectivity.
  
  
  ```
  [ping ipv6](cmdqueryname=ping+ipv6) { [ -a source-ipv6-address | -c echo-number | { -s byte-number | -range [ [ min min-value | max max-value | step step-value ] * ] } | -t timeout | { -tc traffic-class-value | -dscp dscp } | vpn-instance vpn-instance-name | -m wait-time | -name | -nexthop nextHopAddr | -h hoplimit | { -brief | [ -system-time | -ri | -detail ] * } | -p pattern | ignore-mtu ] * destination-ipv6-address [ -i { interface-name | interface-type interface-number } ] [ ipv6-forwarding ] }
  ```

#### Example

* Perform a ping operation to test IPv4 network connectivity.
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
  
  The command output contains the following information:
  
  + Response to each test packet: If no ICMP Echo Reply message is received before the timer on the source expires, the message "Request time out" is displayed. If an ICMP Echo Reply message is received, information such as the number of bytes in the payload, packet sequence number, TTL, and response time is displayed.
  + Ping statistics: include the numbers of sent and received packets, the packet loss rate, and the minimum, maximum, and average response time durations.
* Perform a ping operation to test IPv6 network connectivity.
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
  ---2001:DB8::1 ping statistics---
      5 packet(s) transmitted
      5 packet(s) received
      0.00% packet loss
      round-trip min/avg/max=1/23/115 ms
  ```
  
  The command output contains the following information:
  
  + Response to each test packet: If no ICMP Echo Reply message is received before the timer on the source expires, the message "Request time out" is displayed. If an ICMP Echo Reply message is received, information such as the number of bytes in the payload, packet sequence number, hop limit, and response time is displayed.
  + Ping statistics: include the numbers of sent and received packets, the packet loss rate, and the minimum, maximum, and average response time durations.