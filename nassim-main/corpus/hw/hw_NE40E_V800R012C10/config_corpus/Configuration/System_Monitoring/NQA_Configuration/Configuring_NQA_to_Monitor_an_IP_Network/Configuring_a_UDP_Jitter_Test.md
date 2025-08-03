Configuring a UDP Jitter Test
=============================

A UDP jitter test can be used to measure the end-to-end jitter of various services. It can also simulate a voice test. A UDP jitter test can be used when an ICMP jitter test cannot be used due to the ICMP reply function being disabled on network devices for security purposes.

#### Procedure

* Configure an NQA server for the UDP jitter test.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run either of the following commands according to the IP address type:
     + To specify the IPv4 address and port number used to monitor UDP jitter services on the NQA server, run the [**nqa-server udpecho**](cmdqueryname=nqa-server+udpecho) [ **vpn-instance** *vpn-instance-name* ] *ip-address* *port-number* command.
     + To specify the IPv6 address and port number used to monitor UDP jitter services on the NQA server, run the [**nqa-server udpecho**](cmdqueryname=nqa-server+udpecho) [ **vpn-instance** *vpn-instance-name* ] **ipv6** *ipv6-address* *port-number* command.
  3. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure an NQA client for the UDP jitter test.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. (Optional) Run [**nqa-jitter tag-version**](cmdqueryname=nqa-jitter+tag-version) *version-number*
     
     
     
     The packet version is set for the UDP jitter test instance.
     
     
     
     Packet statistics collected in version 2 is more accurate than those in version 1. Packet version 2 is therefore recommended.
  3. Create an NQA test instance and set its type to UDP jitter.
     
     
     1. Run the [**nqa**](cmdqueryname=nqa) **test-instance** *admin-name test-name* command to create an NQA test instance and enter its view.
     2. Run the [**test-type**](cmdqueryname=test-type) **jitter** command to set the test instance type to UDP jitter.
     3. (Optional) Run the [**description**](cmdqueryname=description) *description* command to configure a description for the test instance.
  4. The destination address and destination port number are set for the UDP jitter test instance.
     
     
     1. Run the [**destination-address**](cmdqueryname=destination-address) { **ipv4** *destAddress* | **ipv6** *destAddress6* } command to configure a destination address (i.e., IP address of the NQA server) for the test instance.
     2. Run the [**destination-port**](cmdqueryname=destination-port) *port-number* command to configure a destination port number for the NQA test instance.
  5. (Optional) Run [**hardware-based enable**](cmdqueryname=hardware-based+enable)
     
     
     
     Hardware-based packet sending is enabled on an interface board.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + Hardware-based packet sending on interface boards is not supported for IPv6 UDP Jitter tests.
     + You are advised to configure hardware-based packet sending on an interface board to implement more accurate delay and jitter calculation, facilitating high-precision network monitoring.
  6. (Optional) Run [**timestamp-unit**](cmdqueryname=timestamp-unit) { **millisecond** | **microsecond** }
     
     
     
     A timestamp unit is configured for the NQA test instance.
     
     
     
     The timestamp unit needs to be configured only after the [**hardware-based enable**](cmdqueryname=hardware-based+enable) command is run.
  7. (Optional) Configure a code type and advantage factor for a simulated voice test.
     
     
     1. Run the [**jitter-codec**](cmdqueryname=jitter-codec) { **g711a** | **g711u** | **g729a** } command to configure a code type for the simulated voice test.
     2. Run the [**adv-factor**](cmdqueryname=adv-factor) *factor-value* command to configure an advantage factor for simulated voice test calculation.
  8. (Optional) Set optional parameters for the test instance and simulate real service flows.
     
     
     1. Run the [**datasize**](cmdqueryname=datasize) *datasizeValue* command to set the size of the Data field in an NQA test packet.
     2. Run the [**jitter-packetnum**](cmdqueryname=jitter-packetnum) *number* command to configure the number of packets sent in a probe.
     3. Run the [**probe-count**](cmdqueryname=probe-count) *number* command to configure the number of probes in a test.
     4. Run the [**interval**](cmdqueryname=interval) { **milliseconds** *interval* | **seconds** *interval* } command to set the interval at which NQA test packets are sent.
     5. Run the [**sendpacket passroute**](cmdqueryname=sendpacket+passroute) command to configure the device to send NQA test packets without performing routing table lookup.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        This function is not supported on IPv6 networks.
     6. Run the [**source-address**](cmdqueryname=source-address) { **ipv4** *srcAddress* | **ipv6** *srcAddr6* } command to configure a source IP address for NQA test packets.
     7. Run the [**source-port**](cmdqueryname=source-port) *portValue* command to configure a source port number for the test.
     8. Run the [**tos**](cmdqueryname=tos) *tos-value* command to configure a ToS value for NQA test packets.
     9. Run the [**ttl**](cmdqueryname=ttl) *ttlValue* command to configure a TTL value for NQA test packets.
  9. (Optional) Configure test failure conditions.
     
     
     + Run the [**timeout**](cmdqueryname=timeout) *time* command to configure a timeout period for response packets.
       
       If no response packets are received within the timeout period, the probe fails.
     + Run the [**fail-percent**](cmdqueryname=fail-percent) *percent* command to configure a failure percentage for the NQA test instance.
       
       If the percentage of failed probes to total probes is greater than or equal to the configured failure percentage, the test is considered as a failure.
  10. (Optional) Configure NQA statistics collection.
      
      
      
      Run [**records**](cmdqueryname=records) { **history** *number* | **result** *number* }
      
      The maximum numbers of historical records and test results that can be saved for the NQA test instance are configured.
  11. (Optional) Configure the device to send trap messages.
      
      
      1. Run the [**test-failtimes**](cmdqueryname=test-failtimes) *failTimes* command to configure the device to send trap messages to the NMS after the number of consecutive NQA test failures reaches the specified threshold.
      2. Run the [**threshold**](cmdqueryname=threshold) { **owd-ds** *thresholdOwdDS* | **owd-sd** *thresholdOwdSD* | **rtd** *thresholdRtd* } command to configure thresholds for round-trip delay (RTD) and one-way delay (OWD).
      3. Run the [**send-trap**](cmdqueryname=send-trap) { **all** | { **owd-ds** | **owd-sd** | **rtd** | **testfailure** | **testresult-change** }\* } command to configure conditions for sending trap messages.
  12. (Optional) Run [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name*
      
      
      
      A VPN instance name is configured for the NQA test instance.
  13. Schedule the NQA test instance.
      
      
      1. (Optional) Run the [**frequency**](cmdqueryname=frequency) *frequencyValue* command to configure the interval at which the NQA test instance is automatically executed.
      2. Run the [**start**](cmdqueryname=start) command to start the NQA test instance.
         
         The [**start**](cmdqueryname=start) command has multiple formats. Choose one of the following formats as needed.
         
         + To start an NQA test instance immediately, run the [**start now**](cmdqueryname=start+now) [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
         + To start an NQA test instance at a specified time, run the [**start**](cmdqueryname=start) **at** [ *yyyy/mm/dd* ] *hh:mm:ss* [ **end** { **at** [ *yyyy/mm/dd* ] *hh:mm:ss* | **delay** { **seconds** *second* | *hh:mm:ss* } | **lifetime** { **seconds** *second* | *hh:mm:ss* } } ] command.
         + To start an NQA test instance after a specified delay, run the [**start delay**](cmdqueryname=start+delay) { **seconds** *second* | *hh*:*mm*:*ss* } [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
         + To start an NQA test instance at a specified time every day, run the [**start daily**](cmdqueryname=start+daily) *hh*:*mm*:*ss* **to** *hh*:*mm*:*ss* [ **begin** *yyyy*/*mm*/*dd* ] [ **end** *yyyy*/*mm*/*dd* ] command.
  14. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.