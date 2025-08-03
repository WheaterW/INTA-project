Using Ping to Check Link Connectivity on an IPv4 or IPv6 Network
================================================================

Packet Internet Groper (ping) is used to check network connectivity and host reachability. In a ping operation, the source sends an Internet Control Message Protocol (ICMP) request message to the destination, which returns an ICMP reply message to the source.

#### Context

The [**ping**](cmdqueryname=ping) command is a most common debugging tool used for testing device accessibility. It uses ICMP Echo messages to determine the following:

* Whether the remote device is available.
* Round-trip delay in communication with a remote device.
* Whether packet loss occurs.

The [**ping**](cmdqueryname=ping) command labels each ICMP Echo message with a sequence ID that starts from 1 and is increased by 1. The number of ICMP Echo messages to be sent is determined by the device, and the default number is 5. You can also set the number of ICMP Echo messages to be sent using a command. If the destination is reachable, it sends five ICMP Echo Reply messages to the source, with their sequence numbers identical with those of ICMP Echo messages.

Perform the following steps in any view on the client:

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The command format is for reference only. For details about the formats of the [**ping**](cmdqueryname=ping) and [**ping ipv6**](cmdqueryname=ping+ipv6) commands, see *Command Reference*.



#### Procedure

1. Run the [**ping**](cmdqueryname=ping) command to check whether network connection is normal. You can run either command to view detailed or brief information.
   
   
   * To view detailed information, run the [**ping**](cmdqueryname=ping) [ **ip** ] { [ **-c** *count* | { [ **-i** { *interface-name* | *interface-type* *interface-number* } | **-nexthop** *nexthop-address* ] \* | **-si** { *source-interface-name* | *source-interface-type* *source-interface-number* } [ **-ei** { *evcSubIfName* | *evcSubIfType* *evcSubIfNum* } ] } | { **-s** *packetsize* | **-range** [ [ **min** *min-value* | **max** *max-value* | **step** *step-value* ] \* ] } | **-t** *timeout* | **-m** *time* | **-a** *source-ip-address* | **-h** *ttl-value* | **-p** *pattern* | { **-tos** *tos-value* | **-dscp** *dscp-value* } | { **-f** | **ignore-mtu** } | **-q** | **-r** | **-vpn-instance** *vpn-instance-name* [ **peer** *peerIpv6* ] | **-v** | **-system-time** | **-ri** | **-8021p** *8021p-value*| | **-name** | **-detail** | **-te-class** *teClassValue* | **-service-class***classValue* ] \* *host* [ **ip-forwarding** ] } or **[**ping**](cmdqueryname=ping)** [ **ip** ] { [ **-c** *count* | { **-s** *packetsize* | **-range** [ [ **min** *min-value* | **max** *max-value* | **step** *step-value* ] \* ] } | **-t** *timeout* | **-m** *time* | **-a** *source-ip-address* | **-h** *ttl-value* | **-p** *pattern* | { **-tos** *tos-value* | **-dscp** *dscp-value* } | { **-f** | **ignore-mtu** } | **-q** | **-r** | **-vpn-instance** *vpn-instance-name* | **-v** | **-system-time** | **-ri** | **-name** ] \* *host* [ **bypass** **-si** { *frrSrcIfName* | *frrSrcIfType* *frrSrcIfNum* } ] command.
   * To view brief information, run the [**ping**](cmdqueryname=ping) [ **ip** ] { [ **-c** *count* | { [ **-i** { *interface-name* | *interface-type* *interface-number* } | **-nexthop** *nexthop-address* ] \* | **-si** { *source-interface-name* | *source-interface-type* *source-interface-number* } [ **-ei** { *evcSubIfName* | *evcSubIfType* *evcSubIfNum* } ] } | { **-s** *packetsize* | **-range** [ [ **min** *min-value* | **max** *max-value* | **step** *step-value* ] \* ] } | **-t** *timeout* | **-m** *time* | **-a** *source-ip-address* | **-h** *ttl-value* | **-p** *pattern* | { **-tos** *tos-value* | **-dscp** *dscp-value* } | { **-f** | **ignore-mtu** } | **-vpn-instance** *vpn-instance-name* [ **peer** *peerIpv6* ] | **-ri** | **-8021p** *8021p-value* | | **-name** | **-brief** | **-te-class** *teClassValue* | **-service-class***classValue* ] \* *host* [ **ip-forwarding** ] } or [**ping**](cmdqueryname=ping) [ **ip** ] { [ **-c** *count* | { [ **-i** { *interface-name* | *interface-type* *interface-number* } [ **-fri** ] } | { **-s** *packetsize* | **-range** [ [ **min** *min-value* | **max** *max-value* | **step** *step-value* ] \* ] } | **-t** *timeout* | **-m** *time* | **-a** *source-ip-address* | **-h** *ttl-value* | **-p** *pattern* | { **-tos** *tos-value* | **-dscp** *dscp-value* } | { **-f** | **ignore-mtu** } | **-vpn-instance** *vpn-instance-name* | **-8021p** *8021p-value* | **-name** | { **-brief** | [ **-q** | **-detail** | **-v** | **-d** | **-system-time** | **-ri** ] \* } | **-service-class***classValue* ] \* *host* [ **ip-forwarding** ] } command.
   
   The command output includes the following:
   
   * Response to each ping packet: If no ICMP Echo Reply message is received within a specified period of time, the message reading "Request time out" is displayed. If a Reply message is received, the data bytes, packet sequence number, TTL value, and response time carried in the message are displayed.
   * Final statistics: The number of sent and received messages, percentage of messages that are not responded to, and the minimum, maximum, and average values of the response time are displayed.
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
   
   On an IPv6 network, you need to run the [**ping ipv6**](cmdqueryname=ping+ipv6) command. For details, see *Command Reference*.
   
   Note that on a network that carries APN6 services, you need to run the [**ping ipv6**](cmdqueryname=ping+ipv6) { **-apn-id-ipv6****instance***instName* [ **-a** *source-ipv6-address* | **-c** *echo-number* | { **-s** *byte-number* | **-range** [ [ **min** *min-value* | **max** *max-value* | **step** *step-value* ] \* ] } | **-t** *timeout* | { **-tc** *traffic-class-value* | **-dscp** *dscp* } | **vpn-instance** *vpn-instance-name* | **-m** *wait-time* | **-name** | **-si** { *source-interface-name* | *source-interface-type**source-interface-number* | **-h** *hoplimit* } | { **-brief** | [ **-system-time** | **-ri** | **-detail** ] \* } | **-p** *pattern* ] \* *destination-ipv6-address* } command to check whether the network connection is normal. The following is an example:
   ```
   <HUAWEI> ping ipv6 -apn-id-ipv6 instance inst1 vpn-instance vpna -si Gigabitethernet 0/1/0 2001:DB8:22::1
   ```
   ```
     PING 2001:DB8:22::1 : 56  data bytes, press CTRL_C to break
       Reply from 2001:DB8:22::1
       bytes=56 Sequence=1 hop limit=64 time=7 ms
       Reply from 2001:DB8:22::1
       bytes=56 Sequence=2 hop limit=64 time=2 ms
       Reply from 2001:DB8:22::1
       bytes=56 Sequence=3 hop limit=64 time=2 ms
       Reply from 2001:DB8:22::1
       bytes=56 Sequence=4 hop limit=64 time=2 ms
       Reply from 2001:DB8:22::1
       bytes=56 Sequence=5 hop limit=64 time=2 ms
   
     --- 2001:DB8:22::1 ping statistics---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max=2/3/7 ms
   ```
2. (Optional) Run the [**icmp-reply fast**](cmdqueryname=icmp-reply+fast) command to enable ICMP fast reply.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In VS mode, this command is supported only by the admin VS.
   
   
   
   1. Run the [**icmp-reply fast**](cmdqueryname=icmp-reply+fast) command in the system view to enable ICMP fast reply on the device.
   2. Run the [**icmp-reply fast**](cmdqueryname=icmp-reply+fast) command in the slot view to enable ICMP fast reply on a specified interface board.
   3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   
   Ping packets are prone to long delays and large jitters. This is because the ICMP messages used in ping operations need to be processed by the CPUs of devices and the processing produces long delays. The detailed reasons are as follows:
   * To minimize the impact of ping attacks on itself, the NE40E reduces the processing priority of ICMP messages to the lowest level.
   
   To resolve ping delay and jitter issues, devices provide the ICMP fast reply function. After this function is enabled, received ICMP request messages are not sent to the CPU for processing. Instead, the packet forwarding engine (PFE) of an interface board responds to clients with ICMP reply messages, greatly shortening the ping delay.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the [**undo icmp-reply fast**](cmdqueryname=undo+icmp-reply+fast) command is run in the system or slot view, ICMP fast reply is disabled on the interface board. After ICMP fast reply is disabled on an interface board, this function takes effect on the interface board only after the [**icmp-reply fast**](cmdqueryname=icmp-reply+fast) command is run in both the system and slot views.