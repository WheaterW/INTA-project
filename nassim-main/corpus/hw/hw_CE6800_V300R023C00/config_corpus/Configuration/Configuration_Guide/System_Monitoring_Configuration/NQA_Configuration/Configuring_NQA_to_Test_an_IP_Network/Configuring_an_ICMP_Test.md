Configuring an ICMP Test
========================

Configuring an ICMP Test

#### Context

An ICMP test checks whether there are reachable routes between a source and a destination. The ICMP test functions similarly to the [**ping**](cmdqueryname=ping) command, but it provides more output information, including:

* Results of the last several tests. By default, the results of last five tests are saved.
* Average delay, packet loss rate, and the time when the last ICMP Echo Reply message is received.

[Figure 1](#EN-US_TASK_0000001176661839__fig_dc_vrp_network-monitor_feature_001701) shows a network on which an ICMP test is performed. The ICMP test process is as follows:

1. DeviceA (source) sends an ICMP Echo Request message to DeviceB (destination) and records the timestamp t1 when the message is sent.
2. DeviceB receives the ICMP Echo Request message and responds with an ICMP Echo Reply message.
3. DeviceA receives the ICMP Echo Reply message within a specified period, records the timestamp t2 when the message is received, and obtains the delay in its communication with DeviceB by calculating the difference between t1 and t2.
   
   If DeviceA does not receive the ICMP Echo Reply message within the specified period, DeviceA considers the sent ICMP Echo Reply message as discarded and calculates the packet loss rate (Number of discarded ICMP Echo Request messages/Number of sent ICMP Echo Request messages). You can determine the network status based on the packet loss rate. If packet loss occurs, the network status is unstable. If the packet loss rate is 100%, the destination is unreachable.

**Figure 1** ICMP test networking  
![](figure/en-us_image_0000001176741763.png)

![](../public_sys-resources/note_3.0-en-us.png) 

ICMP tests are mainly used to check reachability, but cannot accurately reflect the link delay. To test the link delay, use ICMP jitter or UDP jitter tests.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an NQA test instance and set the test instance type to ICMP.
   1. Create an NQA test instance and enter the view of the test instance.
      
      
      ```
      [nqa](cmdqueryname=nqa) test-instance admin-name test-name
      ```
   2. Set the test instance type to ICMP.
      
      
      ```
      [test-type](cmdqueryname=test-type) icmp
      ```
   3. (Optional) Configure a description for the test instance.
      
      
      ```
      [description](cmdqueryname=description) description
      ```
3. Set the destination IP address for test packets, that is, the IP address of the NQA server. 
   
   
   ```
   [destination-address](cmdqueryname=destination-address) { ipv4 destAddress | ipv6 destAddress6 }
   ```
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
   4. Set the number of probes in a test.
      
      
      ```
      [probe-count](cmdqueryname=probe-count) number
      ```
   5. Set the interval at which test packets are sent.
      
      
      ```
      [interval](cmdqueryname=interval) seconds interval
      ```
   6. Configure the NQA client to send packets without searching the routing table.
      
      
      ```
      [sendpacket passroute](cmdqueryname=sendpacket+passroute)
      ```
   7. Configure the source IP address for test packets.
      
      
      ```
      [source-address](cmdqueryname=source-address) { ipv4 srcAddress | ipv6 srcAddr6 }
      ```
   8. Set the source interface for test packets.
      
      
      ```
      [source-interface](cmdqueryname=source-interface) { ifName | ifType ifNum }
      ```
   9. Set the ToS value of test packets.
      
      
      ```
      [tos](cmdqueryname=tos) tos-value [ dscp ]
      ```
   10. Set the TTL value of test packets.
       
       
       ```
       [ttl](cmdqueryname=ttl) ttlValue
       ```
   11. Set the next-hop IP address.
       
       
       ```
       [nexthop](cmdqueryname=nexthop) { ipv4 ipv4Address | ipv6 ipv6Address }
       ```
5. (Optional) Configure test failure conditions.
   1. Set the response timeout interval.
      
      
      ```
      [timeout](cmdqueryname=timeout) time
      ```
   2. Set the failure percentage for the NQA test instance.
      
      
      ```
      [fail-percent](cmdqueryname=fail-percent) percent
      ```
6. (Optional) Set the maximum number of historical test records and the maximum number of test results that can be saved for the NQA test instance.
   
   
   ```
   [records](cmdqueryname=records) { history history-number | result result-number }
   ```
7. (Optional) Configure the device to send traps.
   1. Configure the NQA client to send a trap to the NMS when the number of consecutive probe failures reaches a specified value.
      
      
      ```
      [probe-failtimes](cmdqueryname=probe-failtimes) failTimes
      ```
   2. Configure the NQA client to send a trap to the NMS when the number of consecutive test failures reaches a specified value.
      
      
      ```
      [test-failtimes](cmdqueryname=test-failtimes) failTimes
      ```
   3. Set the RTD threshold.
      
      
      ```
      [threshold](cmdqueryname=threshold) rtd thresholdRtd
      ```
   4. Configure the condition for sending a trap.
      
      
      ```
      [send-trap](cmdqueryname=send-trap) { all | { rtd | testfailure | probefailure | testcomplete | testresult-change } * }
      ```
8. (Optional) Configure the VPN instance name for the NQA test instance.
   
   
   ```
   [vpn-instance](cmdqueryname=vpn-instance) vpn-instance-name
   ```
9. Schedule the NQA test instance.
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
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```