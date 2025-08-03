Configuring a TCP Test
======================

Configuring a TCP Test

#### Context

An NQA TCP test uses a three-way handshake to measure the time taken to set up a TCP connection between a source and a destination. [Figure 1](#EN-US_TASK_0000001130782074__fig_dc_vrp_network-monitor_feature_001301) shows a network on which a TCP test is performed. The TCP test process is as follows:

1. DeviceA (source) sends a TCP SYN packet to DeviceB (destination) to set up a TCP connection.
2. DeviceB receives the TCP SYN packet, accepts the request, and responds with a TCP SYN ACK packet.
3. DeviceA receives the TCP SYN ACK packet and sends an ACK packet to DeviceB. Then a TCP connection is successfully set up between DeviceA and DeviceB.
4. DeviceA calculates the time difference between sending a TCP SYN packet and receiving a TCP SYN ACK packet and between receiving a TCP SYN ACK and sending an ACK packet to obtain the time used to set up a TCP connection with DeviceB through the three-way handshake. The time can reflect the performance of the TCP protocol on the network.

**Figure 1** TCP test networking  
![](figure/en-us_image_0000001176661849.png)

#### Procedure

* Configure the destination for the TCP test.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Specify the listening IP address and listening port for TCP services on the NQA server.
     
     
     ```
     [nqa server tcpconnect](cmdqueryname=nqa+server+tcpconnect) [ vpn-instance vpn-instance-name ] ip-address port-number
     ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure the source for the TCP test.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create an NQA test instance and set the test instance type to TCP.
     
     
     1. Create an NQA test instance and enter its view.
        ```
        [nqa test-instance](cmdqueryname=nqa+test-instance) admin-name test-name
        ```
     2. Set the test instance type to TCP.
        ```
        [test-type](cmdqueryname=test-type) tcp
        ```
     3. (Optional) Configure a description for the test instance.
        ```
        [description](cmdqueryname=description) description
        ```
  3. Configure the destination IP address and destination port number for the test instance.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     The destination IP address and destination port number specified in this step must be the same as *ip-address* and *port-number* specified in Step 2 for the destination (NQA server).
     
     1. Set the destination IP address for test packets, that is, the IP address of the NQA server.
        ```
        [destination-address](cmdqueryname=destination-address) ipv4 destAddress
        ```
     2. (Optional) Set the destination port number for test packets.
        ```
        [destination-port](cmdqueryname=destination-port) port-number
        ```
  4. (Optional) Set optional parameters for the test instance to simulate packet transmission.
     
     
     1. Set the number of probes in a test.
        
        ```
        [probe-count](cmdqueryname=probe-count) number
        ```
     2. Set the interval at which test packets are sent.
        
        ```
        [interval seconds](cmdqueryname=interval+seconds) interval
        ```
     3. Configure the NQA client to send packets without searching the routing table.
        
        ```
        [sendpacket passroute](cmdqueryname=sendpacket+passroute)
        ```
     4. Configure the source IP address for test packets.
        
        ```
        [source-address](cmdqueryname=source-address) ipv4 srcAddress
        ```
     5. Set the source port number for the NQA test instance.
        
        ```
        [source-port](cmdqueryname=source-port) portValue
        ```
     6. Set the ToS value of test packets.
        
        ```
        [tos](cmdqueryname=tos) tos-value
        ```
     7. Set the TTL value of test packets.
        
        ```
        [ttl](cmdqueryname=ttl) ttlValue
        ```
  5. (Optional) Configure test failure conditions.
     
     
     + Set the response timeout interval.
       
       ```
       [timeout](cmdqueryname=timeout) time
       ```
       
       If no response packets are received within the timeout interval, the probe fails.
     + Set the failure percentage for the NQA test instance.
       
       ```
       [fail-percent](cmdqueryname=fail-percent) percent
       ```
       
       If the percentage of failed probes to total probes is greater than or equal to the configured failure percentage, the test is considered as a failure.
  6. (Optional) Set the maximum numbers of historical test records and test results that can be saved for the NQA test instance.
     
     
     ```
     [records](cmdqueryname=records) { history history-number | result result-number }
     ```
  7. (Optional) Configure the NQA client to send traps.
     
     
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
        [threshold rtd](cmdqueryname=threshold+rtd) thresholdRtd
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
        
        + Start the test instance immediately.
          
          ```
          [start](cmdqueryname=start) now [ end { at [ yyyy/mm/dd ] hh:mm:ss | delay { seconds second | hh:mm:ss } | lifetime { seconds second | hh:mm:ss } } ]
          ```
        + Start the test instance at a specified time.
          
          ```
          [start](cmdqueryname=start) at [ yyyy/mm/dd ] hh:mm:ss [ end { at [ yyyy/mm/dd ] hh:mm:ss | delay { seconds second | hh:mm:ss } | lifetime { seconds second | hh:mm:ss } } ]
          ```
        + Start the test instance after a specified delay.
          
          ```
          [start](cmdqueryname=start) delay { seconds second | hh:mm:ss } [ end { at [ yyyy/mm/dd ] hh:mm:ss | delay { seconds second | hh:mm:ss } | lifetime { seconds second | hh:mm:ss } } ]
          ```
        + Start the test instance at a specified time every day.
          
          ```
          [start](cmdqueryname=start) daily hh:mm:ss to hh:mm:ss [ begin yyyy/mm/dd ] [ end yyyy/mm/dd ]
          ```
  10. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```