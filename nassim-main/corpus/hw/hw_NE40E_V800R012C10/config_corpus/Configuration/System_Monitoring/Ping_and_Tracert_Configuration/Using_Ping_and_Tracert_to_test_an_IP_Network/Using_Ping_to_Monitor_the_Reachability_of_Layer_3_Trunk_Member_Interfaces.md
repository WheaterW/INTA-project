Using Ping to Monitor the Reachability of Layer 3 Trunk Member Interfaces
=========================================================================

A ping operation can be performed to test the reachability of trunk member interfaces, helping you learn a physical link's status and locate faulty links.

#### Context

Multiple physical interfaces can be bundled into a logical trunk interface, and these physical interfaces are trunk member interfaces. A specific transmission path is used by each member interface. Path-specific service parameters, such as the delay, jitter, and packet loss rate, are also different. Therefore, you cannot determine which member interface is faulty when the quality of services on a trunk interface deteriorates. To resolve this problem, perform a ping test to monitor each physical link to help locate the faulty link.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The ping test applies when two devices are directly connected through trunk interfaces or Eth-Trunk sub-interfaces.



#### Procedure

1. Enable the receive end to monitor Layer 3 trunk member interfaces.
   1. Run the [**system-view**](cmdqueryname=system-view) to enter the system view.
   2. Run the [**trunk member-port-inspect**](cmdqueryname=trunk+member-port-inspect) command to enable the receive end to monitor Layer 3 trunk member interfaces.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      This command takes effect on all Layer 3 trunk interfaces in a virtual system (VS). Therefore, if you only need to test the connectivity of trunk links, disable this function after the monitoring process is complete. Otherwise, the system keeps monitoring the trunk member interfaces, consuming a lot of system resources.
   3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
2. Ping a Layer 3 trunk member interface from the source.
   1. Generally, to check the connectivity of a Layer 3 trunk member interface, run the [**ping**](cmdqueryname=ping) [ **ip** ] { [ **-a** *source-ip-address* | **-c** *count* | **-d** | { **-f** | **ignore-mtu** } | **-h** *ttl-value* | { { **-i** *interface-type* *interface-number* | **-nexthop** *nexthop-address* } \* | **-si** *source-interface-type* *source-interface-number* } | **-m** *time* | **-p** *pattern* | **-q** | **-r** | { **-s** *packetsize* | **-range** [ [ **min** *min-size* | **max** *max-size* | **step** *step-size* ] \* ] } | **-system-time** | **-t** *timeout* | { **-tos** *tos-value* | **-dscp** *dscp-value* } | **-v** | **-vpn-instance** *vpn-instance-name* | **-ri** | **-8021p** *8021p-value* | **-detail** ] \* *host* [ **ip-forwarding** ] } command.
   2. To perform a trunk member interface-based fast reply test, run the [**ping**](cmdqueryname=ping) [ **ip** ] { [ **-c** *count* | { [ **-i** { *interface-name* | *interface-type* *interface-number* } **-fri** } | { **-s** *packetsize* | **-range** [ [ **min** *min-value* | **max** *max-value* | **step** *step-value* ] \* ] } | **-t** *timeout* | **-m** *time* | **-a** *source-ip-address* | **-h** *ttl-value* | **-p** *pattern* | { **-tos** *tos-value* | **-dscp** *dscp-value* } | { **-f** | **ignore-mtu** } | **-vpn-instance** *vpn-instance-name* | **-8021p** *8021p-value* | **-name** | { **-brief** | [ **-q** | **-detail** | **-v** | **-d** | **-system-time** | **-ri** ] \* } ] \* *host* [ **ip-forwarding** ] } command.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The fast reply function is not supported when packets are fragmented. In this case, the trunk member interface-based fast reply test configure by specifying the **-fri** keyword does not take effect.
   
   
   
   The command output contains the following information:
   
   * Response to each ping packet: If no response packet is received after the timeout period expires, the message "Request time out" is displayed. If a response packet is received, the number of bytes in the response packet, packet sequence number, and response time are displayed.
   * Final statistics: include the number of sent packets, number of received packets, percentage of sent packets with failed responses, and minimum, maximum, and average response times.
   ```
   <HUAWEI> ping -a 192.168.1.1 -i Eth-Trunk 1 10.1.1.2
   ```
   ```
    PING 10.1.1.2: 56 data bytes, press CTRL_C to break
       Reply from 10.1.1.2: bytes=56 Sequence=1 ttl=255 time=170 ms
       Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=255 time=30 ms
       Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=255 time=30 ms
       Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=255 time=50 ms
       Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=255 time=50 ms    
   
     --- 10.1.1.2 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 30/66/170 ms 
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   On an IPv6 network, you need to run the [**ping ipv6**](cmdqueryname=ping+ipv6) command.