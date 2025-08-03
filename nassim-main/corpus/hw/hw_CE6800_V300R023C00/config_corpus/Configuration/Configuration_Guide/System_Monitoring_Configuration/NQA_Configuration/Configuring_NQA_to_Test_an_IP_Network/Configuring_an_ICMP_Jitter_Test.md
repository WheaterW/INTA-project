Configuring an ICMP Jitter Test
===============================

Configuring an ICMP Jitter Test

#### Context

An ICMP jitter test calculates the delay, jitter, and packet loss rate using timestamps carried in ICMP messages. Jitter is calculated by subtracting the interval for sending two consecutive messages from the interval for receiving these two messages. In an ICMP jitter test, you can also set the number of messages to be sent consecutively in a single test instance to simulate a certain type of traffic.

[Figure 1](#EN-US_TASK_0000001176661829__fig_dc_vrp_network-monitor_feature_000601) shows a network on which an ICMP jitter test is performed. The ICMP jitter test process is as follows:

1. DeviceA (source) adds timestamp t1 to an ICMP message and sends it to DeviceB (destination).
2. DeviceB receives the message and adds timestamp t1' to the message.
3. DeviceB adds timestamp t2' to an ICMP response message and sends it to DeviceA.
4. DeviceA receives the message and adds timestamp t2 to the message. Timestamps t3, t3', t4, and t4' are added in a similar way.
5. DeviceA calculates the following values based on the timestamps in received messages:
   * Maximum, minimum, and average jitters of the messages exchanged between the source and destination.
   * Maximum one-way delay of the messages that are sent from the source to the destination or from the destination to the source.

**Figure 1** ICMP jitter test networking  
![](figure/en-us_image_0000001130622304.png)
An ICMP jitter test can measure jitters in two directions:

* Source-to-destination jitter = (t3' â t1') â (t3 â t1)
  
  A larger absolute jitter value indicates poorer link quality, no matter whether the jitter value is positive or negative.
* Destination-to-source jitter = (t4 â t2) â (t4' â t2')
  
  A larger absolute jitter value indicates poorer link quality, no matter whether the jitter value is positive or negative.

In addition, the following delay and packet loss rate information can be obtained:

* Maximum one-way delay (OWD): The maximum OWD is obtained by comparing the transmission delay of each message.
* RTT = (t2 â t1) â (t2' â t1')
* Packet loss: If the RTT of packets is longer than the configured packet transmission timeout interval, the network is congested and the packets will be counted as lost packets.
  + Packet loss rate = Number of lost packets/Number of sent packets x 100% (Number of lost packets = Number of sent packets â Number of received packets)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an NQA test instance and set the test instance type to ICMP jitter.
   1. Create an NQA test instance and enter the view of the test instance.
      
      
      ```
      [nqa](cmdqueryname=nqa) test-instance admin-name test-name
      ```
   2. Set the test instance type to ICMP jitter.
      
      
      ```
      [test-type](cmdqueryname=test-type) icmpjitter
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
   2. Set the mode for an ICMP jitter test.
      
      
      ```
      [icmp-jitter-mode](cmdqueryname=icmp-jitter-mode) { icmp-echo | icmp-timestamp }
      ```
   3. Configure padding characters in test packets.
      
      
      ```
      [datafill](cmdqueryname=datafill) fill-string
      ```
   4. Set the packet payload size for the NQA test instance.
      
      
      ```
      [datasize](cmdqueryname=datasize) datasizeValue
      ```
      
      This parameter is configurable only when **icmp-jitter-mode** is set to **icmp-echo**.
   5. Set the number of packets sent in a probe.
      
      
      ```
      [jitter-packetnum](cmdqueryname=jitter-packetnum) packetNum
      ```
   6. Set the number of probes in a test.
      
      
      ```
      [probe-count](cmdqueryname=probe-count) number
      ```
   7. Set the interval at which test packets are sent.
      
      
      ```
      [interval](cmdqueryname=interval) { milliseconds interval | seconds interval }
      ```
   8. Configure the source IP address for test packets.
      
      
      ```
      [source-address](cmdqueryname=source-address) { ipv4 srcAddress | ipv6 srcAddress6 }
      ```
   9. Set the source interface for test packets.
      
      
      ```
      [source-interface](cmdqueryname=source-interface) { ifName | ifType ifNum }
      ```
   10. Set the ToS value of test packets.
       
       
       ```
       [tos](cmdqueryname=tos) tos-value
       ```
   11. Set the TTL value of test packets.
       
       
       ```
       [ttl](cmdqueryname=ttl) ttlValue
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
7. (Optional) Configure the VPN instance name for the NQA test instance.
   
   
   ```
   [vpn-instance](cmdqueryname=vpn-instance) vpn-instance-name
   ```
8. (Optional) Configure the device to send traps.
   1. Configure the NQA client to send a trap to the NMS when the number of consecutive test failures reaches a specified value.
      
      
      ```
      [test-failtimes](cmdqueryname=test-failtimes) failTimes
      ```
   2. Set the thresholds for the RTD, OWD, and one-way jitter.
      
      
      ```
      [threshold](cmdqueryname=threshold) { owd-ds thresholdOwdDS | owd-sd thresholdOwdSD | rtd thresholdRtd | jitter-ds thresholdJitDS | jitter-sd thresholdJitSD }
      ```
   3. Configure the condition for sending a trap.
      
      
      ```
      [send-trap](cmdqueryname=send-trap) { all | { rtd | testfailure | testcomplete | owd-sd | owd-ds | jitter-sd | jitter-ds | testresult-change } * }
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