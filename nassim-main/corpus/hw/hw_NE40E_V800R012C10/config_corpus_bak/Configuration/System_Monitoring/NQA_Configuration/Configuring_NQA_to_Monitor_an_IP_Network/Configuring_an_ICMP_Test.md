Configuring an ICMP Test
========================

An Internet Control Message Protocol (ICMP) test can be used to check the connectivity and measure the packet loss rate, delay, and other indicators of an IP network from end to end.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Create an NQA test instance and set its type to ICMP.
   1. Run the [**nqa**](cmdqueryname=nqa) **test-instance** *admin-name test-name* command to create an NQA test instance and enter its view.
   2. Run the [**test-type**](cmdqueryname=test-type) **icmp** command to set the test instance type to ICMP.
   3. (Optional) Run the [**description**](cmdqueryname=description) *description* command to configure a description for the test instance.
3. Run [**destination-address**](cmdqueryname=destination-address) { **ipv4** *destAddress* | **ipv6** *destAddress6* }
   
   
   
   A destination address (i.e., IP address of the NQA server) is configured for the test instance.
4. (Optional) Set optional parameters for the test instance and simulate real service flows.
   1. Run the [**agetime**](cmdqueryname=agetime) *ageTimeValue* command to set the aging time of the NQA test instance.
   2. Run the [**datafill**](cmdqueryname=datafill) *fill-string* command to configure the padding characters to be filled into test packets.
   3. Run the [**datasize**](cmdqueryname=datasize) *datasizeValue* command to set the size of the Data field in an NQA test packet.
   4. Run the [**probe-count**](cmdqueryname=probe-count) *number* command to set the number of probes in a test for the NQA test instance.
   5. Run the [**interval**](cmdqueryname=interval) **seconds** *interval* command to set the interval at which NQA test packets are sent.
   6. Run the [**sendpacket passroute**](cmdqueryname=sendpacket+passroute) command to configure the device to send NQA test packets without performing routing table lookup.
   7. Run the [**source-address**](cmdqueryname=source-address) { **ipv4** *srcAddress* | **ipv6** *srcAddr6* } command to configure a source IP address for NQA test packets.
   8. Run the [**source-interface**](cmdqueryname=source-interface) *ifType* *ifNum* command to specify a source interface for NQA test packets.
   9. Run the [**tos**](cmdqueryname=tos) *tos-value* [ **dscp** ] command to configure a ToS value for NQA test packets.
   10. Run the [**ttl**](cmdqueryname=ttl) *ttlValue* command to configure a TTL value for NQA test packets.
   11. Run the [**nexthop**](cmdqueryname=nexthop) { **ipv4** *ipv4Address* | **ipv6** *ipv6Address* } command to configure a next-hop address for the test instance.
5. (Optional) Run [**forwarding-simulation inbound-interface**](cmdqueryname=forwarding-simulation+inbound-interface) { *ifName* | *ifType* *ifNum* }
   
   
   
   The inbound interface for simulated packets is configured.
6. (Optional) Run [**path-type bypass**](cmdqueryname=path-type+bypass)
   
   
   
   The device is configured to send Echo Request packets through an IP fast reroute (FRR) bypass LSP.
7. (Optional) Configure test failure conditions.
   1. Run the [**timeout**](cmdqueryname=timeout) *time* command to configure a timeout period for response packets.
      
      
      
      If no response packets are received within the timeout period, the probe fails.
   2. Run the [**fail-percent**](cmdqueryname=fail-percent) *percent* command to configure a failure percentage for the NQA test instance.
      
      
      
      If the percentage of failed probes to total probes is greater than or equal to the configured failure percentage, the test is considered as a failure.
8. (Optional) Run [**records**](cmdqueryname=records) { **history** *number* | **result** *number* }
   
   
   
   The maximum numbers of historical records and test results that can be saved for the NQA test instance are configured.
9. (Optional) Configure the device to send trap messages.
   1. Run the [**test-failtimes**](cmdqueryname=test-failtimes) *failTimes* command to configure the device to send trap messages to the NMS after the number of consecutive NQA test failures reaches the specified threshold.
   2. Run the [**threshold**](cmdqueryname=threshold) **rtd** *thresholdRtd* command to configure a round-trip delay (RTD) threshold.
   3. Run the [**send-trap**](cmdqueryname=send-trap) { **all** | { **rtd** | **testfailure** | **probefailure** | **testcomplete** | **testresult-change** }\* } command to configure conditions for sending trap messages.
10. (Optional) Run [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name*
    
    
    
    A VPN instance name is configured for the NQA test instance.
11. Schedule the NQA test instance.
    1. (Optional) Run the [**frequency**](cmdqueryname=frequency) *frequencyValue* command to configure the interval at which the NQA test instance is automatically executed.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       If the following conditions are met, the **Completion** field in the test results may be displayed as **no result**:
       
       * [**frequency**](cmdqueryname=frequency) < ([**probe-count**](cmdqueryname=probe-count) â 1) x [**interval**](cmdqueryname=interval) + [**timeout**](cmdqueryname=timeout) +1
    2. Run the [**start**](cmdqueryname=start) command to start the NQA test instance.
       
       
       
       The [**start**](cmdqueryname=start) command has multiple formats. Choose one of the following formats as needed:
       
       * To start an NQA test instance immediately, run the [**start now**](cmdqueryname=start+now) [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
       * To start an NQA test instance at a specified time, run the [**start**](cmdqueryname=start) **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
       * To start an NQA test instance after a specified delay, run the [**start delay**](cmdqueryname=start+delay) { **seconds** *second* | *hh*:*mm*:*ss* } [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
       * To start an NQA test instance at a specified time every day, run the [**start**](cmdqueryname=start) **daily** *hh*:*mm*:*ss* **to** *hh*:*mm*:*ss* [ **begin** *yyyy*/*mm*/*dd* ] [ **end** *yyyy*/*mm*/*dd* ] command.
12. (Optional) In the system view, run [**whitelist session-car**](cmdqueryname=whitelist+session-car) { [**nqa-icmp**](cmdqueryname=nqa-icmp) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** **pir-value** | **pbs** *pbs-value* } \* | [**nqa-icmpv6**](cmdqueryname=nqa-icmpv6) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** **pir-value** | **pbs** *pbs-value* } \* }
    
    
    
    The session-CAR value of the ICMP test instance is adjusted.
    
    
    
    The session CAR function is enabled by default. If the session CAR function is abnormal, you can run the [**whitelist session-car**](cmdqueryname=whitelist+session-car) { [**nqa-icmp**](cmdqueryname=nqa-icmp) | [**nqa-icmpv6**](cmdqueryname=nqa-icmpv6) } [**disable**](cmdqueryname=disable) command to disable it.
13. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.