Using Tracert to Check a Path on an IPv4 or IPv6 Network
========================================================

A tracert operation is used to check network connectivity and locate network faults.

#### Context

The [**tracert**](cmdqueryname=tracert) and [**tracert ipv6**](cmdqueryname=tracert+ipv6) commands are used to trace the gateways through which a packet passes from the source to the destination. The maximum TTL value that can be set for packets using the [**tracert**](cmdqueryname=tracert) or [**tracert ipv6**](cmdqueryname=tracert+ipv6) command is 255. Each time the source does not receive a reply after the configured period of time elapses, it displays timeout information and sends another packet with the TTL value incremented by 1. If timeout information is still displayed when the TTL value is 255, the source considers that the destination is unreachable and the test fails.

To prevent malicious users from forging ICMP Port Unreachable or Time Exceeded messages in order to detect the IPv4 or IPv6 addresses of device interfaces, you can specify the source IPv4 or IPv6 address of Port Unreachable or Time Exceeded messages in the loopback interface view. If the [**tracert**](cmdqueryname=tracert) or [**tracert ipv6**](cmdqueryname=tracert+ipv6) command is run to detect a remote address, the device uses the address of the loopback interface as the source address of Port Unreachable or Time Exceeded messages.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The command format is for reference only. For details about the formats of the [**tracert**](cmdqueryname=tracert) or [**tracert ipv6**](cmdqueryname=tracert+ipv6) commands, see *Command Reference*.



#### Procedure

* On an IPv4 network:
  
  
  1. (Optional) Configure the address of a loopback interface as the source IP address of ICMP Port Unreachable or Time Exceeded messages.
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**interface loopback**](cmdqueryname=interface+loopback) *loopback-number*
        
        A loopback interface is created, and its view is displayed.
     3. (Optional) Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
        
        The interface is bound to a VPN instance.
     4. Run [**ip icmp**](cmdqueryname=ip+icmp) { **ttl-exceeded** | **port-unreachable** } **source-address**
        
        The address of the loopback interface is configured as the source IP address of ICMP Port Unreachable or Time Exceeded messages.
     5. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
  2. Run [**tracert**](cmdqueryname=tracert) [ **-a** *source-ip-address* | **-f** *initTtl* | **-m** *maxTtl* | **-p** *destPort* | **-q** *nqueries* | { **-vpn-instance** *vpn-instance-name* [ **peer** *peerIpv6* ] | **-as** } | **-w** *timeout* | **-v** | **-s** *size* | { { **-i** { *interface-name* | *interface-type* *interface-number* } | **-nexthop** *nexthop-address* | **-passroute** | **-service-class***classValue* | **-pipe** } \* | **-si** { *source-interface-name* | *source-interface-type**source-interface-number* } } | **-te-class** *teClassValue* | **-name** | { **-tos** *tos-value* | **-dscp** *dscp* } ] \* *host*
     
     The fault is located.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the **-as** keyword is configured, the AS number of each hop is obtained by querying the local routing table based on the destination address. The AS number is displayed only when the corresponding routing entry is learned through BGP and the BGP route carries the AS number.
     
     The following example uses the [**tracert**](cmdqueryname=tracert) command to analyze the network.
     
     ```
     <HUAWEI> tracert -m 10 10.1.1.1
     ```
     ```
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
     If a loopback interface address is configured as the source IP address of ICMP Port Unreachable or Time Exceeded messages on a transit device (the loopback interface address 10.2.2.9 of the second hop is used as an example), the following information is displayed when a tracert operation is performed to check the IPv4 network:
     ```
     <HUAWEI> tracert -m 10 10.1.1.1
     ```
     ```
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
* On an IPv6 network:
  
  
  1. (Optional) Configure the address of a loopback interface as the source IPv6 address of ICMPv6 Port Unreachable or Time Exceeded messages.
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**interface loopback**](cmdqueryname=interface+loopback) *loopback-number*
        
        A loopback interface is created, and its view is displayed.
     3. (Optional) Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
        
        The interface is bound to a VPN instance.
     4. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
        
        IPv6 is enabled on the interface.
     5. Run [**ipv6 icmp**](cmdqueryname=ipv6+icmp) { **hop-limit-exceeded** | **port-unreachable** } **source-address**
        
        The address of the loopback interface is configured as the source IPv6 address of ICMPv6 Port Unreachable or Time Exceeded messages.
     6. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
  2. Run [**tracert ipv6**](cmdqueryname=tracert+ipv6) [ **-f** *first-hop-limit* | **-m** *max-hop-limit* | **-p** *port-number* | **-fixedPort** | **-q** *probes* | **-w** *timeout* | { **vpn-instance** *vpn-instance-name* [ **peer** *peerIpv6* ] } | **-s** *size* | **-name** | { { **-nexthop** *nextHopAddr* | **-passroute** | **-service-class** *classValue* | **-pipe** } \* | **-si** { *source-interface-name* | *source-interface-type**source-interface-number* } } | **-a** *source-ipv6-address* | **-v** | { **-tc***tc* | **-dscp***dscp* } | **-te-class** *teClassValue* | **ignore-mtu** ] \* *host-name* [ **-i** { *ifName* | *ifType* *ifNum* } ]
     
     The fault is located.
     
     The following example uses the [**tracert ipv6**](cmdqueryname=tracert+ipv6) command to analyze the network.
     
     ```
     <HUAWEI> tracert ipv6 -q 5 -w 8000 2001:DB8:100::3
     ```
     ```
     traceroute to 2001:DB8:100::3 30 hops max,60 bytes packet
     1 2001:DB8:200::2 26 ms 23 ms 26 ms 30 ms 29 ms 
     2 2001:DB8:100::3 3020 ms 3024 ms 4040 ms 6820 ms 5584 ms
     ```
     Note that on a network that carries APN6 services, you need to run the **[**tracert ipv6**](cmdqueryname=tracert+ipv6)** **-apn-id-ipv6****instance***instName* [ **-f** *first-hop-limit* | **-m** *max-hop-limit* | **-p** *port-number* | **-fixedPort** | **-q** *probes* | **-w** *timeout* | **vpn-instance** *vpn-instance-name* | **-s** *size* | **-name** | **-a** *source-ipv6-address* | **-v** | **-si** { *source-interface-name* | *source-interface-type**source-interface-number* } | { **-tc** *tc* | **-dscp** *dscp* } ] \* *host-name* command to check whether the network connection is normal. The following is an example:
     ```
     <HUAWEI> tracert ipv6 -apn-id-ipv6 instance inst1 vpn-instance vpna -si Gigabitethernet 0/1/0 2001:DB8:22::1
     ```
     ```
       traceroute to vpna 2001:DB8:22::1  30 hops max,60 bytes packet
      1 2001:DB8:10::2 2 ms  3 ms  2 ms 
      2 2001:DB8:22::1 2 ms  1 ms  2 ms
     ```