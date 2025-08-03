Configuring an SNMP Test
========================

An NQA SNMP test can be used to measure the communication speed between a host and an SNMP agent using UDP packets.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Create an NQA test instance and set its type to SNMP.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before configuring an NQA SNMP test instance, configure SNMP. The NQA SNMP test instance supports SNMPv1, SNMPv2c, and SNMPv3.
   
   
   
   1. Run the [**nqa**](cmdqueryname=nqa) **test-instance** *admin-name test-name* command to create an NQA test instance and enter its view.
   2. Run the [**test-type**](cmdqueryname=test-type) **snmp** command to set the test instance type to SNMP.
   3. (Optional) Run the [**description**](cmdqueryname=description) *description* command to configure a description for the test instance.
3. Run [**destination-address**](cmdqueryname=destination-address) **ipv4** *destAddress*
   
   
   
   A destination address (i.e., IP address of the NQA server) is configured for the test instance.
4. (Optional) Run [**community read cipher**](cmdqueryname=community+read+cipher) *community-name*
   
   
   
   A community name is specified for the SNMP test instance.
   
   
   
   If a target SNMP agent runs SNMPv1 or SNMPv2c, the read community name specified using the **community read cipher** command must be the same as the read community name configured on the SNMP agent. Otherwise, the SNMP test will fail.
5. (Optional) Set optional parameters for the test instance and simulate real service flows.
   1. Run the [**probe-count**](cmdqueryname=probe-count) *number* command to set the number of probes in a test for the NQA test instance.
   2. Run the [**interval**](cmdqueryname=interval) **seconds** *interval* command to set the interval at which NQA test packets are sent.
   3. Run the [**sendpacket passroute**](cmdqueryname=sendpacket+passroute) command to configure the device to send NQA test packets without performing routing table lookup.
   4. Run the [**source-address**](cmdqueryname=source-address) **ipv4** *srcAddress* command to specify a source IP address for NQA test packets.
   5. Run the [**source-port**](cmdqueryname=source-port) *portValue* command to configure a source port number for the test.
   6. Run the [**tos**](cmdqueryname=tos) *tos-value* command to configure a ToS value for NQA test packets.
   7. Run the [**ttl**](cmdqueryname=ttl) *ttlValue* command to configure a TTL value for NQA test packets.
6. (Optional) Configure test failure conditions.
   1. Run the [**timeout**](cmdqueryname=timeout) *time* command to configure a timeout period for response packets.
      
      
      
      If no response packets are received within the timeout period, the probe fails.
   2. Run the [**fail-percent**](cmdqueryname=fail-percent) *percent* command to configure a failure percentage for the NQA test instance.
      
      
      
      If the percentage of failed probes to total probes is greater than or equal to the configured failure percentage, the test is considered as a failure.
7. (Optional) Run [**records**](cmdqueryname=records) { **history** *number* | **result** *number* }
   
   
   
   The maximum numbers of historical records and test results that can be saved for the NQA test instance are configured.
8. (Optional) Configure the device to send trap messages.
   1. Run the [**probe-failtimes**](cmdqueryname=probe-failtimes) *failTimes* command to enable the device to send traps to the NMS after the number of consecutive probe failures in an NQA test reaches the specified threshold.
   2. Run the [**test-failtimes**](cmdqueryname=test-failtimes) *failTimes* command to configure the device to send trap messages to the NMS after the number of consecutive NQA test failures reaches the specified threshold.
   3. Run the [**threshold**](cmdqueryname=threshold) **rtd** *thresholdRtd* command to configure a round-trip delay (RTD) threshold.
   4. Run the [**send-trap**](cmdqueryname=send-trap) { **all** | { **rtd** | **testfailure** | **probefailure** | **testcomplete** | **testresult-change** }\* } command to configure conditions for sending trap messages.
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
11. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.