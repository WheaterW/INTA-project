Configuring a DNS Test
======================

Configuring a DNS Test

#### Context

A DNS test is based on UDP packets. In a DNS test, only one UDP packet is sent to detect the time required for a DNS server on a network to resolve a specified domain name into an IP address. The test result clearly reflects the performance of the DNS protocol on the network. [Figure 1](#EN-US_TASK_0000001176661841__dc_vrp_network-monitor_feature_009301) shows a network on which a DNS test is performed. A DNS test process is as follows:

1. DeviceA (source) sends a DNS request packet to the DNS server (destination), requesting the DNS server to resolve the DNS name (server.com).
2. The DNS server receives the DNS request packet, parses the DNS request packet, finds the IP address corresponding to the domain name, constructs a DNS response packet, and sends the DNS response packet to DeviceA.
3. DeviceA receives the DNS response packet and calculates the time difference between receiving the DNS response packet and sending the DNS request packet, which is the time required for resolving the domain name into an IP address. The time can reflect the network DNS protocol performance.

**Figure 1** DNS test networking  
![](figure/en-us_image_0000001176741767.png)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the dynamic DNS function.
   
   
   ```
   [dns resolve](cmdqueryname=dns+resolve)
   ```
   
   By default, the dynamic DNS function is disabled.
3. Configure an IP address of the DNS server.
   
   
   ```
   [dns server](cmdqueryname=dns+server) ip-address [ vpn-instance vpn-instance-name ]
   ```
   
   By default, no IP address of the DNS server is configured.
4. Create an NQA test instance and set the test instance type to DNS.
   1. Create an NQA test instance and enter its view.
      
      
      ```
      [nqa](cmdqueryname=nqa) test-instance admin-name test-name
      ```
   2. Set the test instance type to DNS.
      
      
      ```
      [test-type](cmdqueryname=test-type) dns
      ```
   3. (Optional) Configure a description for the test instance.
      
      
      ```
      [description](cmdqueryname=description) description
      ```
5. Specify the IP address of the DNS server in the DNS test instance.
   
   
   ```
   [dns-server](cmdqueryname=dns-server) ipv4 ip-address
   ```
6. Specify a destination URL for the NQA test instance.
   
   
   ```
   [destination-address](cmdqueryname=destination-address) url urlValue
   ```
7. (Optional) Set optional parameters for the test instance to simulate packet transmission.
   1. Configure the aging time for the NQA test instance.
      
      
      ```
      [agetime](cmdqueryname=agetime) ageTimeValue
      ```
8. (Optional) Set the response timeout interval.
   
   
   ```
   [timeout](cmdqueryname=timeout) time
   ```
   
   If no response is received within the specified timeout interval, the test is considered as a failure.
9. (Optional) Set the maximum numbers of historical test records and test results that can be saved for the NQA test instance.
   
   
   ```
   [records](cmdqueryname=records) { history history-number | result result-number }
   ```
10. (Optional) Configure the device to send traps.
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
11. (Optional) Configure the VPN instance name for the NQA test instance.
    
    
    ```
    [vpn-instance](cmdqueryname=vpn-instance) vpn-instance-name
    ```
12. Schedule the NQA test instance.
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
13. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```