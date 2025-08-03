Configuring a TCP Test
======================

A TCP test can be used to check the connectivity and measure the packet loss rate, delay, and other indicators of an IP network through a TCP connection.

#### Procedure

* Configure an NQA server for the TCP test.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**nqa-server tcpconnect**](cmdqueryname=nqa-server+tcpconnect) [ **vpn-instance** *vpn-instance-name* ] *ip-address* *port-number*
     
     The IP address and port number used to monitor TCP services are specified on the NQA server.
  3. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure an NQA client for the TCP test.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Create an NQA test instance and set its type to TCP.
     
     
     1. Run the [**nqa**](cmdqueryname=nqa) **test-instance** *admin-name test-name* command to create an NQA test instance and enter its view.
     2. Run the [**test-type**](cmdqueryname=test-type) **trace** command to set the test instance type to TCP.
     3. (Optional) Run the [**description**](cmdqueryname=description) *description* command to configure a description for the test instance.
  3. Specify a destination address and a destination port number for the TCP test instance.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The destination address and destination port number specified in this step must be the same as *ip-address* and *port-number* specified on the NQA server in Step 2.
     
     1. Run the [**destination-address**](cmdqueryname=destination-address) **ipv4** *destAddress* command to configure a destination address (i.e., IP address of the NQA server) for the test instance.
     2. (Optional) Run the [**destination-port**](cmdqueryname=destination-port) *port-number* command to specify a destination port number for the NQA test instance.
  4. (Optional) Set optional parameters for the test instance and simulate real service flows.
     
     
     1. Run the [**probe-count**](cmdqueryname=probe-count) *number* command to set the number of probes in a test.
     2. Run the [**interval**](cmdqueryname=interval) { **milliseconds** *interval* | **seconds** *interval* } command to configure an interval at which test packets are sent for the NQA test instance.
     3. Run the [**sendpacket passroute**](cmdqueryname=sendpacket+passroute) command to configure the device to send NQA test packets without performing routing table lookup.
     4. Run the [**source-address**](cmdqueryname=source-address) **ipv4** *srcAddress* command to specify a source IP address for NQA test packets.
     5. Run the [**source-port**](cmdqueryname=source-port) *portValue* command to configure a source port number for the test.
     6. Run the [**tos**](cmdqueryname=tos) *tos-value* command to set a ToS value for NQA test packets.
     7. Run the [**ttl**](cmdqueryname=ttl) *ttlValue* command to set a TTL value for NQA test packets.
  5. (Optional) Configure test failure conditions.
     
     
     + Run the [**timeout**](cmdqueryname=timeout) *time* command to configure a timeout period for response packets.
       
       If no response packets are received within the timeout period, the probe fails.
     + Run the [**fail-percent**](cmdqueryname=fail-percent) *percent* command to configure a failure percentage for the NQA test instance.
       
       If the percentage of failed probes to total probes is greater than or equal to the configured failure percentage, the test is considered as a failure.
  6. (Optional) Configure NQA statistics collection.
     
     
     
     Run [**records**](cmdqueryname=records) { **history** *number* | **result** *number* }
     
     The maximum number of historical records and the maximum number of result records that can be saved for the NQA test instance are set.
  7. (Optional) Configure the device to send trap messages.
     
     
     1. Run the [**probe-failtimes**](cmdqueryname=probe-failtimes) *failTimes* command to configure the device to send trap messages to the NMS after the number of consecutive probe failures in an NQA test reaches the specified threshold.
     2. Run the [**test-failtimes**](cmdqueryname=test-failtimes) *failTimes* command to configure the device to send trap messages to the NMS after the number of consecutive NQA test failures reaches the specified threshold.
     3. Run the [**threshold**](cmdqueryname=threshold) **rtd** *thresholdRtd* command to configure a round-trip delay (RTD) threshold.
     4. Run the [**send-trap**](cmdqueryname=send-trap) { **all** | { **rtd** | **testfailure** | **probefailure** | **testcomplete** | **testresult-change** }\* } command to configure conditions for sending trap messages.
  8. (Optional) Run [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name*
     
     
     
     A VPN instance name is configured for the NQA test instance.
  9. Schedule the NQA test instance.
     
     
     1. (Optional) Run the [**frequency**](cmdqueryname=frequency) *frequencyValue* command to configure the interval at which the NQA test instance is automatically executed.
     2. Run the [**start**](cmdqueryname=start) command to start the NQA test instance.
        
        The [**start**](cmdqueryname=start) command has multiple formats. Choose one of the following formats as needed.
        
        + To start an NQA test instance immediately, run the [**start now**](cmdqueryname=start+now) [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
        + To start an NQA test instance at a specified time, run the [**start**](cmdqueryname=start) **at** [ *yyyy/mm/dd* ] *hh:mm:ss* [ **end** { **at** [ *yyyy/mm/dd* ] *hh:mm:ss* | **delay** { **seconds** *second* | *hh:mm:ss* } | **lifetime** { **seconds** *second* | *hh:mm:ss* } } ] command.
        + To start an NQA test instance after a specified delay, run the [**start delay**](cmdqueryname=start+delay) { **seconds** *second* | *hh*:*mm*:*ss* } [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
        + To start an NQA test instance at a specified time every day, run the [**start daily**](cmdqueryname=start+daily) *hh*:*mm*:*ss* **to** *hh*:*mm*:*ss* [ **begin** *yyyy*/*mm*/*dd* ] [ **end** *yyyy*/*mm*/*dd* ] command.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.