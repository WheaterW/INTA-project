Using Tracert to Test a Forwarding Path on an IPv4 or IPv6 Network
==================================================================

Using Tracert to Test a Forwarding Path on an IPv4 or IPv6 Network

#### Context

The tracert function is used to test the reachability of each hop on the path from the source to the destination.

You can perform a tracert operation on the source by sending three UDP packets at a time. The TTL value of the first batch of UDP packets is 1, and the TTL value of each further batch is incremented by 1.

If the source receives response packets within a specified period after sending packets, the address and RTT of the response node are displayed on the source. If no response packet is received, a response timeout prompt is displayed on the source. If a response timeout prompt is displayed after the source sends a UDP packet with the maximum TTL value, the destination cannot be reached and the test fails.

To prevent malicious users from forging ICMP Port Unreachable or Time Exceeded messages in order to detect the IPv4 or IPv6 address of a device, you can specify the source IPv4 or IPv6 address of ICMP Port Unreachable or Time Exceeded messages in the loopback interface view. After this configuration, if you run the [**tracert**](cmdqueryname=tracert)/[**tracert ipv6**](cmdqueryname=tracert+ipv6) command to test the reachability of each hop, each hop uses the loopback interface address as the source address in ICMP Port Unreachable or Time Exceeded messages.


#### Procedure

* Configure tracert to test an IPv4 network.
  1. (Optional) Configure the IP address of the loopback interface as the source IP address of ICMP Port Unreachable or Time Exceeded messages.
     
     
     1. Enter the system view.
        
        ```
        [system-view](cmdqueryname=system-view)
        ```
     2. Create a loopback interface and enter the loopback interface view.
        
        ```
        [interface loopback](cmdqueryname=interface+loopback) loopback-number
        ```
     3. (Optional) Bind the loopback interface with a VPN instance.
        
        ```
        [ip binding vpn-instance](cmdqueryname=ip+binding+vpn-instance) vpn-instance-name
        ```
        
        By default, an interface functions as a public network interface that is not bound to any VPN instance.
     4. On each hop between the source and destination, configure the IP address of the loopback interface as the source IP address in the ICMP Time Exceeded messages. On the destination, configure the IP address of the loopback interface as the source IP address in the ICMP Port Unreachable messages.
        
        ```
        [ip icmp](cmdqueryname=ip+icmp) { ttl-exceeded | port-unreachable } source-address
        ```
     5. Commit the configuration.
        ```
        [commit](cmdqueryname=commit)
        ```
  2. Test the fault position.
     
     
     ```
     [tracert](cmdqueryname=tracert) [ -a source-ip-address [ -response-public | -ignore-vpn | -response-vpn respVrfName ] | -f initTtl | -m maxTtl | -p destPort | -q nqueries | -vpn-instance vpn-instance-name | -w timeout | -s size| -name | { -tos tos-value | -dscp dscp } | -pipe ] * host
     ```
* Configure tracert to test an IPv6 network.
  
  
  
  Test the fault position.
  
  ```
  [tracert ipv6](cmdqueryname=tracert+ipv6) [ -f first-hop-limit | -m max-hop-limit | -p port-number | -q probes | -w timeout | vpn-instance vpn-instance-name | -s size | -name | { -nexthop nextHopAddr | -passroute | -pipe }* | -a source-ipv6-address | { -tc tc | -dscp dscp } ] * host-name  [ -i { ifName | ifType ifNum } ]
  ```

#### Example

* Perform a tracert operation to test an IPv4 network.
  ```
  <HUAWEI> tracert -m 10 10.1.1.1
  traceroute to 10.1.1.1 (10.1.1.1), max hops: 10 ,packet length: 40,press CTRL_C to break
  1  172.16.112.1   19 ms   19 ms   1 ms
  2  172.16.216.1   39 ms   39 ms   19 ms
  3  172.16.136.23   39 ms   40 ms   39 ms
  4  172.16.168.22   39 ms   39 ms   39 ms
  5  172.16.197.4   40 ms   59 ms   59 ms
  6  172.16.221.5   59 ms   59 ms   59 ms
  7  172.31.70.13   99 ms   99 ms   80 ms
  8  172.31.71.6   139 ms   239 ms   319 ms
  9  172.31.81.7   220 ms   199 ms   199 ms
  10 10.1.1.1   239 ms   239 ms   239 ms
  ```
  
  If a loopback interface address is configured as the source IP address of ICMP Port Unreachable or Time Exceeded messages on the second hop (with the loopback interface address 10.2.2.9), the following information is displayed when a tracert operation is performed to check the IPv4 network:
  
  ```
  <HUAWEI> tracert -m 10 10.1.1.1
  traceroute to 10.1.1.1 (10.1.1.1), max hops: 10 ,packet length: 40,press CTRL_C to break
  1  172.16.112.1   19 ms   19 ms   1 ms
  2  10.2.2.9   39 ms   39 ms   19 ms
  3  172.16.136.23   39 ms   40 ms   39 ms
  4  172.16.168.22   39 ms   39 ms   39 ms
  5  172.16.197.4   40 ms   59 ms   59 ms
  6  172.16.221.5   59 ms   59 ms   59 ms
  7  172.31.70.13   99 ms   99 ms   80 ms
  8  172.31.71.6   139 ms   239 ms   319 ms
  9  172.31.81.7   220 ms   199 ms   199 ms
  10 10.1.1.1   239 ms   239 ms   239 ms
  ```
  
  The situation is similar on an IPv6 network.
* Perform a tracert operation to test an IPv6 network.
  ```
  <HUAWEI> tracert ipv6 -q 5 -w 8000 2001:DB8:100::3
  traceroute to 2001:DB8:100::3 30 hops max,60 bytes packet
  1 2001:DB8:200::2 26 ms 23 ms 26 ms 30 ms 29 ms 
  2 2001:DB8:100::3 3020 ms 3024 ms 4040 ms 6820 ms 5584 ms
  ```