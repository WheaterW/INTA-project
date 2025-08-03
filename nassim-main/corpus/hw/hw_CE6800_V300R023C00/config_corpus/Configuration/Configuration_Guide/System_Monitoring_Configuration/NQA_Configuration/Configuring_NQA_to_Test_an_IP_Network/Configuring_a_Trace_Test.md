Configuring a Trace Test
========================

Configuring a Trace Test

#### Context

A trace test monitors the forwarding path between a source and a destination and collects statistics such as delay about each hop on the forwarding path. The trace test functions similarly to the **tracert** command, but it provides more output information, including the average delay, packet loss rate, and time when the last packet is received for each hop. [Figure 1](#EN-US_TASK_0000001130622300__fig_dc_vrp_network-monitor_feature_001801) shows a network on which a trace test is performed. The trace test process is as follows:

1. DeviceA (source) sends a UDP packet with the time to live (TTL) value of 1 to DeviceB (destination).
2. DeviceC (first hop) receives the packet, discards the packet according to the TTL value, and sends an ICMP Time Exceeded message to DeviceA.
3. DeviceA receives the ICMP Time Exceeded message, records the first-hop IP address, and sends a UDP packet with the TTL value of 2.
4. DeviceD (second hop) receives the packet, discards the packet according to the TTL value, and sends an ICMP Time Exceeded message to DeviceA.
5. Similarly, a UDP packet will reach the destination DeviceB and DeviceB sends an ICMP Port Unreachable message to DeviceA.
6. Based on the ICMP message returned from each hop, DeviceA collects information about the forwarding path and statistics about each hop on the forwarding path.

**Figure 1** Trace test networking  
![](figure/en-us_image_0000001176661857.png)

In addition, a trace test can be used to detect the maximum transmission unit (MTU) of the path from the source to the destination.

When creating an NQA trace test instance, you can disable packet fragmentation and set the packet payload size. After the test instance is started, test packets are sent based on the specified size without being fragmented. If the test is successful, the packet payload size is smaller than the path MTU. Then, keep increasing the packet payload size until the test fails. The test failure indicates that the packet payload size is greater than the path MTU. The maximum size of the packet that can be sent without being fragmented is used as the path MTU.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an NQA test instance and set the test instance type to trace.
   1. Create an NQA test instance and enter the view of the test instance.
      
      
      ```
      [nqa](cmdqueryname=nqa) test-instance admin-name test-name
      ```
   2. Set the test instance type to trace.
      
      
      ```
      [test-type](cmdqueryname=test-type) trace
      ```
   3. (Optional) Configure a description for the test instance.
      
      
      ```
      [description](cmdqueryname=description) description
      ```
3. Configure the destination IP address and destination port number for the test instance.
   
   
   1. Set the destination IP address for test packets, that is, the IP address of the NQA server.
      ```
      [destination-address](cmdqueryname=destination-address) { ipv4 destAddress | ipv6 destAddress6 }
      ```
   2. (Optional) Specify the destination port number for test packets.
      ```
      [destination-port](cmdqueryname=destination-port) port-number
      ```
      
      By default, the destination port number for a test packet is 33434.
4. (Optional) Set optional parameters for the test instance to simulate packet transmission.
   1. Configure the aging time for the NQA test instance.
      
      
      ```
      [agetime](cmdqueryname=agetime) ageTimeValue
      ```
   2. Configure padding characters in test packets.
      
      
      ```
      [datafill](cmdqueryname=datafill) fill-string
      ```
   3. Set the packet payload size for the NQA test instance.
      
      
      ```
      [datasize](cmdqueryname=datasize) datasizeValue
      ```
   4. Set the number of probes for each hop in a test.
      
      
      ```
      [probe-count](cmdqueryname=probe-count) number
      ```
   5. Configure the NQA client to send packets without searching the routing table.
      
      
      ```
      [sendpacket passroute](cmdqueryname=sendpacket+passroute)
      ```
   6. Configure the source IP address for test packets.
      
      
      ```
      [source-address](cmdqueryname=source-address) { ipv4 srcAddress | ipv6 srcAddr6 }
      ```
   7. Set the source interface for test packets.
      
      
      ```
      [source-interface](cmdqueryname=source-interface) { ifName | ifType ifNum }
      ```
   8. Set the TTL of test packets.
      
      
      ```
      [tracert-livetime](cmdqueryname=tracert-livetime) first-ttl first-ttl max-ttl max-ttl
      ```
   9. Set the next-hop IP address.
      
      
      ```
      [nexthop](cmdqueryname=nexthop) { ipv4 ipv4Address | ipv6 ipv6Address }
      ```
   10. Set the ToS value of test packets.
       
       
       ```
       [tos](cmdqueryname=tos) tos-value [ dscp ]
       ```
5. (Optional) Disable packet fragmentation.
   
   
   ```
   [set-df](cmdqueryname=set-df)
   ```
6. (Optional) Configure test failure conditions.
   1. Set the response timeout interval.
      
      
      ```
      [timeout](cmdqueryname=timeout) time
      ```
   2. Set the maximum number of hop failures in a probe.
      
      
      ```
      [tracert-hopfailtimes](cmdqueryname=tracert-hopfailtimes) hopFailTimes
      ```
7. (Optional) Set the maximum number of historical test records and the maximum number of test results that can be saved for the NQA test instance.
   
   
   ```
   [records](cmdqueryname=records) { history history-number | result result-number }
   ```
8. (Optional) Configure the device to send traps.
   1. Configure the NQA client to send a trap to the NMS when the number of consecutive test failures reaches a specified value.
      
      
      ```
      [test-failtimes](cmdqueryname=test-failtimes) failTimes
      ```
   2. Set the RTD threshold.
      
      
      ```
      [threshold](cmdqueryname=threshold) rtd thresholdRtd
      ```
   3. Configure the condition for sending a trap.
      
      
      ```
      [send-trap](cmdqueryname=send-trap) { all | { rtd | testfailure | testcomplete | testresult-change } * }
      ```
9. (Optional) Configure the VPN instance name for the NQA test instance.
   
   
   ```
   [vpn-instance](cmdqueryname=vpn-instance) vpn-instance-name
   ```
10. Schedule the NQA test instance.
    1. (Optional) Set the interval for performing NQA tests.
       
       
       ```
       [frequency](cmdqueryname=frequency) frequencyValue
       ```
    2. Start the NQA test instance.
       
       
       
       You can start an NQA test instance immediately, at a specified time, after a delay, or periodically.
       
       * Start the test instance immediately.
         ```
         [start](cmdqueryname=start) now [ end { at [ yyyy/mm/dd ] hh:mm:ss | delay { seconds second | hh:mm:ss } | lifetime { seconds second | hh:mm:ss } } ]
         ```
       * Start the test instance at a specified time.
         ```
         [start](cmdqueryname=start) at [ yyyy/mm/dd ] hh:mm:ss [ end { at [ yyyy/mm/dd ] hh:mm:ss | delay { seconds second | hh:mm:ss } | lifetime { seconds second | hh:mm:ss } } ]
         ```
       * Start the test instance after a specified delay.
         
         ```
         [start](cmdqueryname=start) delay { seconds second | hh:mm:ss } [ end { at [ yyyy/mm/dd ] hh:mm:ss | delay { seconds second | hh:mm:ss } | lifetime { seconds second | hh:mm:ss } } ]
         ```
       * Start the test instance at a specified time every day.
         
         ```
         [start](cmdqueryname=start) daily hh:mm:ss to hh:mm:ss [ begin yyyy/mm/dd ] [ end yyyy/mm/dd ]
         ```
11. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```