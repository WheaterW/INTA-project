Configuring a Trace Test
========================

A trace test can be used to check the connectivity and measure the packet loss rate, delay, and other indicators of an IP network hop by hop. It can also monitor the packet forwarding path.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Create an NQA test instance and set its type to trace.
   1. Run the [**nqa**](cmdqueryname=nqa) **test-instance** *admin-name test-name* command to create an NQA test instance and enter its view.
   2. Run the [**test-type**](cmdqueryname=test-type) **trace** command to set the test instance type to trace.
   3. (Optional) Run the [**description**](cmdqueryname=description) *description* command to configure a description for the test instance.
3. Specify the destination address and destination port number for the test instance.
   
   
   1. Run the [**destination-address**](cmdqueryname=destination-address) { **ipv4** *destAddress* | **ipv6** *destAddress6* } command to configure a destination address (i.e., IP address of the NQA server) for the test instance.
   2. (Optional) Run the [**destination-port**](cmdqueryname=destination-port) *port-number* command to specify a destination port number for the NQA test instance.
4. (Optional) Set optional parameters for the test instance and simulate real service flows.
   1. Run the [**agetime**](cmdqueryname=agetime) *ageTimeValue* command to set the aging time of the NQA test instance.
   2. Run the [**datafill**](cmdqueryname=datafill) *fill-string* command to configure the padding characters to be filled into test packets.
   3. Run the [**datasize**](cmdqueryname=datasize) *datasizeValue* command to set the size of the Data field in an NQA test packet.
   4. Run the [**probe-count**](cmdqueryname=probe-count) *number* command to set the number of probes in a test for the NQA test instance.
   5. Run the [**sendpacket passroute**](cmdqueryname=sendpacket+passroute) command to configure the device to send NQA test packets without performing routing table lookup.
   6. Run the [**source-address**](cmdqueryname=source-address) { **ipv4** *srcAddress* | **ipv6** *srcAddr6* } command to configure a source IP address for NQA test packets.
   7. Run the [**source-interface**](cmdqueryname=source-interface) *ifType* *ifNum* command to specify a source interface for NQA test packets.
   8. Run the [**tos**](cmdqueryname=tos) *tos-value* [ **dscp** ] command to configure a ToS value for NQA test packets.
   9. Run the [**nexthop**](cmdqueryname=nexthop) { **ipv4** *ipv4Address* | **ipv6** *ipv6Address* } command to configure a next-hop address for the test instance.
   10. Run the [**tracert-livetime**](cmdqueryname=tracert-livetime) **first-ttl** *first-ttl* **max-ttl** *max-ttl* command to set a TTL value for test packets.
5. (Optional) Run [**set-df**](cmdqueryname=set-df)
   
   
   
   Packet fragmentation is disabled.
   
   
   
   Use a trace test instance to obtain the path MTU as follows:
   
   Run the [**set-df**](cmdqueryname=set-df) command to disable packet fragmentation. Then, run the [**datasize**](cmdqueryname=datasize) command to set the size of the Data field in a test packet. After that, start the test instance. If the test is successful, the size of the Data field in sent packets is smaller than the path MTU. Then, keep increasing the packet data area size using the **datasize** command until the test fails. If the test fails, the size of the sent packet's data area is greater than the path MTU. The maximum size of the packet that can be sent without being fragmented is used as the path MTU.
6. (Optional) Configure test failure conditions.
   1. Run the [**timeout**](cmdqueryname=timeout) *time* command to configure a timeout period for response packets.
      
      
      
      If no response packets are received within the timeout period, the probe fails.
   2. Run the [**tracert-hopfailtimes**](cmdqueryname=tracert-hopfailtimes) *hopfailtimesValue* command to set the maximum number of hop failures in a probe for the test instance.
7. (Optional) Run [**records**](cmdqueryname=records) { **history** *number* | **result** *number* }
   
   
   
   The maximum numbers of historical records and test results that can be saved for the NQA test instance are configured.
8. (Optional) Configure the device to send trap messages.
   1. Run the [**test-failtimes**](cmdqueryname=test-failtimes) *failTimes* command to configure the device to send trap messages to the NMS after the number of consecutive NQA test failures reaches the specified threshold.
   2. Run the [**threshold**](cmdqueryname=threshold) **rtd** *thresholdRtd* command to configure a round-trip delay (RTD) threshold.
   3. Run the [**send-trap**](cmdqueryname=send-trap) { **all** | { **rtd** | **testfailure** | **testcomplete** | **testresult-change** }\* } command to configure conditions for sending trap messages.
9. (Optional) Run [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name*
   
   
   
   A VPN instance name is configured for the NQA test instance.
10. Schedule the NQA test instance.
    1. (Optional) Run the [**frequency**](cmdqueryname=frequency) *frequencyValue* command to configure the interval at which the NQA test instance is automatically executed.
    2. Run the [**start**](cmdqueryname=start) command to start the NQA test instance.
       
       
       
       The [**start**](cmdqueryname=start) command has multiple formats. Choose one of the following formats as needed:
       
       * To start an NQA test instance immediately, run the [**start now**](cmdqueryname=start+now) [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
       * To start an NQA test instance at a specified time, run the [**start**](cmdqueryname=start) **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
       * To start an NQA test instance after a specified delay, run the [**start delay**](cmdqueryname=start+delay) { **seconds** *second* | *hh*:*mm*:*ss* } [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
       * To start an NQA test instance at a specified time every day, run the [**start**](cmdqueryname=start) **daily** *hh*:*mm*:*ss* **to** *hh*:*mm*:*ss* [ **begin** *yyyy*/*mm*/*dd* ] [ **end** *yyyy*/*mm*/*dd* ] command.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.