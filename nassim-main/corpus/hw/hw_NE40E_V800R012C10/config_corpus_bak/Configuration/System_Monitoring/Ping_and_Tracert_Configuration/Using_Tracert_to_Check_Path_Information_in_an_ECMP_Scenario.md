Using Tracert to Check Path Information in an ECMP Scenario
===========================================================

After ECMP tracert is configured, you can check path information of all reachable links from the source host to the destination in an ECMP scenario.

#### Context

By traversing a specified port number range, ECMP tracert can detect the quality of all possible equal-cost load balancing links. If a link fails, ECMP tracert can quickly switch traffic to another link, ensuring service continuity and stability.


#### Procedure

1. Run either of the following commands based on the service scenario:
   
   
   * To check links that carry IPv4 services in ECMP scenarios, run the [**tracert multipath**](cmdqueryname=tracert+multipath)[ **-vpn-instance***vrfName* ] *destAddress* [ **-a***sourceAddress* | **-f***initTtl* | **-m***maxTtl* | **-w***timeout* | **-s***pktSize* | **-q***count* | **-no-fragment** | { **-tos***tos* | **-dscp***dscp* } | **-detail** |**destination-port***begin-port* [ *end-port* ] | **-si** { *sourceIfName* | *sourceIfType**sourceIfNum* } ] \* command. The following is an example:
     ```
     <HUAWEI> tracert multipath 10.1.3.1 -detail destination-port 12345 12348 -si GigabitEthernet 0/1/1 
      traceroute to 10.1.3.1, max hops: 64, packet length: 40, press CTRL_C to break
       destination-port: 12345
        1 10.1.1.2 3 ms 
        2 10.1.3.1 3 ms 
       destination-port: 12346
        1 10.2.1.2 3 ms 
        2 10.1.3.1 2 ms 
       destination-port: 12347
        1 10.1.1.2 1 ms 
        2 10.1.3.1 2 ms 
       destination-port: 12348
        1 10.2.1.2 2 ms 
        2 10.1.3.1 2 ms 
     
       --- summary of all paths ---
       path 1 found
       destination-port: 12347
        1  10.1.1.2  1 ms
        2  10.1.3.1  2 ms
       path 2 found
       destination-port: 12348
        1  10.2.1.2  2 ms
        2  10.1.3.1  2 ms
     ```
   * To check links that carry IPv6 services in ECMP scenarios, run the [**tracert multipath ipv6**](cmdqueryname=tracert+multipath+ipv6)[ **-vpn-instance***vrfName* ] *destAddress* [ **-a***sourceAddress* | **-f***initTtl* | **-m***maxTtl* | **-w***timeout* | **-s***pktSize* | **-q***count* | { **-tc***tc* | **-dscp***dscp* } | **-detail** |**destination-port***begin-port* [ *end-port* ] | **-si** { *sourceIfName* | *sourceIfType**sourceIfNum* } ] \* command. The following is an example.
     ```
     <HUAWEI> tracert multipath ipv6 -vpn-instance vpna 2001:DB8:22::2 -detail destination-port 12345 12348 -si GigabitEthernet 0/1/1 
       traceroute to vpna 2001:DB8:22::2  64 hops max,60 bytes packet
       destination-port: 12345
        1 2001:DB8:40::1 2 ms 
        2 2001:DB8:22::2 1 ms 
       destination-port: 12346
        1 2001:DB8:20::1 2 ms 
        2 2001:DB8:22::2 2 ms 
       destination-port: 12347
        1 2001:DB8:40::1 2 ms 
        2 2001:DB8:22::2 2 ms 
       destination-port: 12348
        1 2001:DB8:20::1 3 ms 
        2 2001:DB8:22::2 3 ms 
     
       --- summary of all paths ---
       path 1 found
       destination-port: 12345
        1  2001:DB8:40::1  2 ms
        2  2001:DB8:22::2  1 ms
       path 2 found
       destination-port: 12346
        1  2001:DB8:20::1  2 ms
        2  2001:DB8:22::2  2 ms
     ```