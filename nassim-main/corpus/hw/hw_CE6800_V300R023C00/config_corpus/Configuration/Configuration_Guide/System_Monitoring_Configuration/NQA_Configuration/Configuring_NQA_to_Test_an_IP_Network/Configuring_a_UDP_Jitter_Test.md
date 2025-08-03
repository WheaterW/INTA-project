Configuring a UDP Jitter Test
=============================

Configuring a UDP Jitter Test

#### Context

A UDP jitter test calculates the delay, jitter, and packet loss rate using timestamps carried in UDP packets. Jitter is calculated by subtracting the interval for sending two consecutive packets from the interval for receiving these two packets. You can set the number of packets to be sent in a single UDP jitter test to simulate a type of traffic. For example, configure the source to send 3000 UDP packets at an interval of 20 ms to simulate G.711 traffic in a minute.

![](../public_sys-resources/note_3.0-en-us.png) 

The maximum number of packets sent in a UDP jitter test is equal to the configured *probe-count* value (number of probes in a test) multiplied by the *jitter-packetnum* value (number of packets sent in a probe).

[Figure 1](#EN-US_TASK_0000001130622288__fig_dc_vrp_network-monitor_feature_000501) shows a network on which a UDP jitter test is performed. The UDP jitter test process is as follows:

1. DeviceA (source) sends a data packet to DeviceB (destination). Timestamp t1 is added when the packet is sent.
2. DeviceB receives the packet and adds timestamp t1' to the packet.
3. DeviceB adds timestamp t2' to the packet and sends it to DeviceA.
4. DeviceA receives the packet and adds timestamp t2 to the packet. Timestamps t3, t3', t4, and t4' are added in a similar way.
5. DeviceA calculates the following values based on the timestamps in received packets:
   * Maximum, minimum, and average jitters of the packets exchanged between the source and destination.
   * Maximum one-way delay of the packets that are sent from the source to the destination or from the destination to the source.

**Figure 1** UDP jitter test networking  
![](figure/en-us_image_0000001130782090.png)
A UDP jitter test can measure jitters in two directions:

* Source-to-destination jitter = (t3' â t1') â (t3 â t1)
  
  A larger absolute jitter value indicates poorer link quality, no matter whether the jitter value is positive or negative.
* Destination-to-source jitter = (t4 â t2) â (t4' â t2')
  
  A larger absolute jitter value indicates poorer link quality, no matter whether the jitter value is positive or negative.

In addition, the following delay and packet loss rate information can be obtained:

* Maximum OWD: The maximum OWD is obtained by comparing the transmission delay of each message.
* RTT = (t2 â t1) â (t2' â t1')
* Packet loss: If the RTT of packets is longer than the configured packet transmission timeout interval, the network is congested and the packets will be counted as lost packets.
  + Number of packets lost during one-way transmission:
    - Number of packets lost during their transmission from the source to the destination = Number of packets sent by DeviceA â Number of packets received by DeviceB
    - Number of packets lost during their transmission from the destination to the source = Number of packets sent by DeviceB â Number of packets received by DeviceA
    - If DeviceA does not receive any response packet, it considers packet loss occurs and records the number of discarded packets in **Packet Loss Unknown**, which can be queried using the [**display nqa results**](cmdqueryname=display+nqa+results) command.
  + Packet loss rate = Number of lost packets/Number of sent packets x 100% (Number of lost packets = Number of sent packets â Number of received packets)

#### Procedure

* Configure the NQA server for the UDP jitter test.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Specify the listening IP address and listening port for UDP services on the NQA server.
     
     
     ```
     [nqa server udpecho](cmdqueryname=nqa+server+udpecho) [ vpn-instance vpn-instance-name ] { ip-address | ipv6 ipv6-address } port-number
     ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure the NQA client for the UDP jitter test.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. (Optional) Configure the packet version for a UDP jitter test instance.
     
     
     ```
     [nqa jitter tag-version](cmdqueryname=nqa+jitter+tag-version) version-number
     ```
     
     By default, the packet version in a jitter test instance is 1.
     
     Packet version 2 is recommended because packet statistics collected in this version is more accurate than those in version 1.
  3. Create an NQA test instance and set the test instance type to UDP jitter.
     
     
     1. Create an NQA test instance and enter the view of the test instance.
        ```
        [nqa test-instance](cmdqueryname=nqa+test-instance) admin-name test-name
        ```
     2. Set the test instance type to UDP jitter.
        ```
        [test-type](cmdqueryname=test-type) jitter
        ```
     3. (Optional) Configure a description for the test instance.
        ```
        [description](cmdqueryname=description) description
        ```
  4. Configure the destination IP address and destination port number for the test instance.
     
     
     1. Set the destination IP address for test packets, that is, the IP address of the NQA server.
        ```
        [destination-address](cmdqueryname=destination-address) { ipv4 destAddress | ipv6 destAddress6 }
        ```
     2. Set the destination port number for test packets.
        
        ```
        [destination-port](cmdqueryname=destination-port) port-number
        ```
  5. (Optional) Configure the codec and advantage factor for a simulated voice test.
     
     
     1. Set the codec for the simulated voice test.
        
        ```
        [jitter-codec](cmdqueryname=jitter-codec) { g711a | g711u | g729a }
        ```
        
        If no codec is specified, a UDP jitter test instance is used to measure the jitter of common services by default, not voice services.
     2. Set the advantage factor for the simulated voice test.
        
        ```
        [adv-factor](cmdqueryname=adv-factor) factor-value
        ```
        
        By default, the advantage factor configured for a simulated voice test is 0.
  6. (Optional) Set optional parameters for the test instance to simulate packet transmission.
     
     
     1. Set the packet payload size for the NQA test instance.
        
        ```
        [datasize](cmdqueryname=datasize) datasizeValue
        ```
        
        By default, if **g711a** or **g711u** is configured using the **jitter-codec** command, the default value of *datasizeValue* is **172**; if **g729a** is configured using the **jitter-codec** command, the default value of *datasizeValue* is **32**.
     2. Set the number of packets sent in a probe.
        
        ```
        [jitter-packetnum](cmdqueryname=jitter-packetnum) packetNum
        ```
        
        By default, 20 packets are sent in a probe.
     3. Set the number of probes in a test.
        
        ```
        [probe-count](cmdqueryname=probe-count) number
        ```
     4. Set the interval at which test packets are sent.
        
        ```
        [interval](cmdqueryname=interval) { milliseconds interval | seconds interval }
        ```
     5. Configure the NQA client to send packets without searching the routing table.
        
        ```
        [sendpacket passroute](cmdqueryname=sendpacket+passroute)
        ```
     6. Configure the source IP address for test packets.
        ```
        [source-address](cmdqueryname=source-address) { ipv4 srcAddress | ipv6 srcAddress6 }
        ```
     7. Set the source port number for the NQA test instance.
        ```
        [source-port](cmdqueryname=source-port) portValue
        ```
     8. Set the source interface for test packets.
        ```
        [source-interface](cmdqueryname=source-interface) { ifName | ifType ifNum }
        ```
     9. Set the ToS value of test packets.
        
        ```
        [tos](cmdqueryname=tos) tos-value
        ```
     10. Set the TTL value of test packets.
         
         ```
         [ttl](cmdqueryname=ttl) ttlValue
         ```
  7. (Optional) Configure test failure conditions.
     
     
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
  8. (Optional) Set the maximum number of historical test records and the maximum number of test results that can be saved for the NQA test instance.
     
     
     ```
     [records](cmdqueryname=records) { history history-number | result result-number }
     ```
  9. (Optional) Configure the device to send traps.
     
     
     1. Configure the NQA client to send a trap to the NMS when the number of consecutive test failures reaches a specified value.
        ```
        [test-failtimes](cmdqueryname=test-failtimes) failTimes
        ```
     2. Set the thresholds for the RTD and OWD.
        ```
        [threshold](cmdqueryname=threshold) { owd-ds thresholdOwdDS | owd-sd thresholdOwdSD | rtd thresholdRtd }
        ```
     3. Configure the condition for sending a trap.
        ```
        [send-trap](cmdqueryname=send-trap) { all | { owd-ds | owd-sd | rtd | testfailure | testresult-change } * }
        ```
  10. (Optional) Configure the VPN instance name for the NQA test instance.
      
      
      ```
      [vpn-instance](cmdqueryname=vpn-instance) vpn-instance-name
      ```
  11. Schedule the NQA test instance.
      
      
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
  12. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```