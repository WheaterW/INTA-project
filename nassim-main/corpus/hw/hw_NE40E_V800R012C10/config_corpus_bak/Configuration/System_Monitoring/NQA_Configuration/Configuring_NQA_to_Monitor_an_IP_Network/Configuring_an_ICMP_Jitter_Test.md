Configuring an ICMP Jitter Test
===============================

An Internet Control Message Protocol (ICMP) Jitter test can be used to measure the end-to-end jitter of various services.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Create an NQA test instance and set its type to ICMP Jitter.
   1. Run the [**nqa**](cmdqueryname=nqa) **test-instance** *admin-name test-name* command to create an NQA test instance and enter its view.
   2. Run the [**test-type**](cmdqueryname=test-type) **icmpjitter** command to set the test instance type to ICMP jitter.
   3. (Optional) Run the [**description**](cmdqueryname=description) *description* command to configure a description for the test instance.
3. Run [**destination-address**](cmdqueryname=destination-address) { **ipv4** *destAddress* | **ipv6** *destAddress6* }
   
   
   
   A destination address (i.e., IP address of the NQA server) is configured for the test instance.
4. (Optional) Run [**hardware-based enable**](cmdqueryname=hardware-based+enable)
   
   
   
   Hardware-based packet sending is enabled on an interface board.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Hardware-based packet sending on an interface board is not supported for IPv6 ICMP Jitter tests.
   * You are advised to configure hardware-based packet sending on an interface board to implement more accurate delay and jitter calculation, facilitating high-precision network monitoring.
   * After hardware-based packet sending is enabled on the involved interface board on the client, you need to run the [**nqa-server icmp-server**](cmdqueryname=nqa-server+icmp-server) [ **vpn-instance** *vpn-instance-name* ] *ip-address* command on the NQA server to specify the IP address used to monitor ICMP services.
5. (Optional) Set timestamp units for the NQA test instance.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The timestamp units need to be configured only after the [**hardware-based enable**](cmdqueryname=hardware-based+enable) command is run.
   
   
   
   1. Run the [**timestamp-unit**](cmdqueryname=timestamp-unit) { **millisecond** | **microsecond** } command to configure a timestamp unit for the source in the NQA test instance.
   2. Run the [**receive-timestamp-unit**](cmdqueryname=receive-timestamp-unit) { **millisecond** | **microsecond** } command to configure a timestamp unit for the destination in the NQA test instance.
      
      
      
      In a scenario where a Huawei device interworks with a non-Huawei device, if an ICMP jitter test in which the Huawei device functions as the source (client) is configured to measure the delay, jitter, packet loss, and other indicators on the network, you need to run this command to configure a timestamp unit for the ICMP timestamp packets returned by the destination.
      
      The source's timestamp unit configured using the [**timestamp-unit**](cmdqueryname=timestamp-unit) { **millisecond** | **microsecond** } command must be the same as the destination's timestamp unit configured using the [**receive-timestamp-unit**](cmdqueryname=receive-timestamp-unit) command. If the timestamp unit is set to microseconds and the interface board's precision supported by the device is milliseconds, the device uses milliseconds as the timestamp unit.
6. Set optional parameters for the test instance and simulate real service flows.
   1. Run the [**agetime**](cmdqueryname=agetime) *ageTimeValue* command to set the aging time of the NQA test instance.
   2. Run the [**icmp-jitter-mode**](cmdqueryname=icmp-jitter-mode) { **icmp-echo** | **icmp-timestamp** } command to specify an ICMP jitter test mode for the NQA test instance.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      This function is not supported on IPv6 networks.
   3. Run the [**datafill**](cmdqueryname=datafill) *fill-string* command to configure the padding characters to be filled into test packets.
      
      
      
      This parameter can be configured only when the ICMP jitter test mode is set to icmp-echo.
   4. Run the [**datasize**](cmdqueryname=datasize) *datasizeValue* command to set the size of the Data field in an NQA test packet.
      
      
      
      This parameter can be configured only when the ICMP jitter test mode is set to icmp-echo.
   5. Run the [**jitter-packetnum**](cmdqueryname=jitter-packetnum) *packetNum* command to configure the number of packets sent in a probe.
   6. Run the [**probe-count**](cmdqueryname=probe-count) *number* command to set the number of probes in a test for the NQA test instance.
   7. Run the [**interval**](cmdqueryname=interval) { **milliseconds** *interval* | **seconds** *interval* } command to set the interval at which NQA test packets are sent.
   8. Run the [**source-address**](cmdqueryname=source-address) { **ipv4** *srcAddress* | **ipv6** *srcAddr6* } command to configure a source IP address for NQA test packets.
   9. Run the [**ttl**](cmdqueryname=ttl) *ttlValue* command to configure a TTL value for NQA test packets.
   10. Run the [**tos**](cmdqueryname=tos) *tos-value* command to configure a ToS value for NQA test packets.
7. (Optional) Configure test failure conditions.
   1. Run the [**timeout**](cmdqueryname=timeout) *time* command to configure a timeout period for response packets.
      
      
      
      If no response packets are received within the timeout period, the probe fails.
   2. Run the [**fail-percent**](cmdqueryname=fail-percent) *percent* command to configure a failure percentage for the NQA test instance.
      
      
      
      If the percentage of failed probes to total probes is greater than or equal to the configured failure percentage, the test is considered as a failure.
8. (Optional) Run [**records**](cmdqueryname=records) { **history** *number* | **result** *number* }
   
   
   
   The maximum numbers of historical records and test results that can be saved for the NQA test instance are configured.
9. (Optional) Configure the device to send trap messages.
   1. Run the [**test-failtimes**](cmdqueryname=test-failtimes) *failTimes* command to configure the device to send trap messages to the NMS after the number of consecutive NQA test failures reaches the specified threshold.
   2. Run the [**threshold**](cmdqueryname=threshold) { **owd-ds** *thresholdOwdDS* | **owd-sd** *thresholdOwdSD* | **rtd** *thresholdRtd* | **jitter-ds***thresholdJitDS* | **jitter-sd***thresholdJitSD* } command to configure the thresholds for round-trip delay (RTD), one-way delay (OWD), and one-way jitter.
   3. Run the [**send-trap**](cmdqueryname=send-trap) { **all** | { **rtd** | **testfailure** | **testcomplete** | **owd-sd** | **owd-ds** | **jitter-sd** | **jitter-ds** | **testresult-change** }\* } command to configure conditions for sending trap messages.
10. (Optional) Run [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name*
    
    
    
    A VPN instance name is configured for the NQA test instance.
11. Schedule the NQA test instance.
    1. (Optional) Run the [**frequency**](cmdqueryname=frequency) *frequencyValue* command to configure the interval at which the NQA test instance is automatically executed.
    2. Run the [**start**](cmdqueryname=start) command to start the NQA test instance.
       
       
       
       The [**start**](cmdqueryname=start) command has multiple formats. Choose one of the following formats as needed:
       
       * To start an NQA test instance immediately, run the [**start now**](cmdqueryname=start+now) [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
       * To start an NQA test instance at a specified time, run the [**start**](cmdqueryname=start) **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
       * To start an NQA test instance after a specified delay, run the [**start delay**](cmdqueryname=start+delay) { **seconds** *second* | *hh*:*mm*:*ss* } [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
       * To start an NQA test instance at a specified time every day, run the [**start**](cmdqueryname=start) **daily** *hh*:*mm*:*ss* **to** *hh*:*mm*:*ss* [ **begin** *yyyy*/*mm*/*dd* ] [ **end** *yyyy*/*mm*/*dd* ] command.
12. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.