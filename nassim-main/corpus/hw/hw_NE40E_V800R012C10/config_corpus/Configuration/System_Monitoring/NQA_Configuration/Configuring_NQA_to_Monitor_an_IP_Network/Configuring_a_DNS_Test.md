Configuring a DNS Test
======================

This section describes how to configure a DNS test to detect the speed at which a DNS name is resolved to an IP address.

#### Context

A DNS test is based on UDP packets. Only one probe packet is sent in one DNS test to detect the speed at which a DNS name is resolved to an IP address. The test result clearly reflects the performance of the DNS protocol on the network.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dns resolve**](cmdqueryname=dns+resolve)
   
   
   
   Dynamic DNS is enabled.
3. Run [**dns server**](cmdqueryname=dns+server)*ip-address* [ [**vpn-instance**](cmdqueryname=vpn-instance)*vpn-name* ]
   
   
   
   An IP address is configured for the DNS server.
4. Run [**dns server source-ip**](cmdqueryname=dns+server+source-ip) *ipv4Addr*
   
   
   
   The IP address of the local DNS client is configured as the source address for DNS communication.
5. Create an NQA test instance and set its type to DNS.
   1. Run the [**nqa**](cmdqueryname=nqa) **test-instance** *admin-name test-name* command to create an NQA test instance and enter its view.
   2. Run the [**test-type**](cmdqueryname=test-type) **dns** command to set the test instance type to DNS.
   3. (Optional) Run the [**description**](cmdqueryname=description) *description* command to configure a description for the test instance.
6. Run [**dns-server**](cmdqueryname=dns-server) **ipv4** *ip-address*
   
   
   
   An IP address is configured for the DNS server in the DNS test instance.
7. Run [**destination-address**](cmdqueryname=destination-address) **url** *urlValue*
   
   
   
   A destination URL is specified for the NQA test instance.
8. (Optional) Set optional parameters for the test instance and simulate real service flows.
   1. Run the [**agetime**](cmdqueryname=agetime) *ageTimeValue* command to set the aging time of the NQA test instance.
9. (Optional) Configure a test failure condition.
   
   
   
   Run [**timeout**](cmdqueryname=timeout) *time*
   
   
   
   A timeout period is configured for a response packet.
10. (Optional) Run [**records**](cmdqueryname=records) { **history** *number* | **result** *number* }
    
    
    
    The maximum numbers of historical records and test results that can be saved for the NQA test instance are configured.
11. (Optional) Configure the device to send trap messages.
    1. Run the [**test-failtimes**](cmdqueryname=test-failtimes) *failTimes* command to configure the device to send trap messages to the NMS after the number of consecutive NQA test failures reaches the specified threshold.
    2. Run the [**threshold**](cmdqueryname=threshold) **rtd** *thresholdRtd* command to configure a round-trip delay (RTD) threshold.
    3. Run the [**send-trap**](cmdqueryname=send-trap) { **all** | { **rtd** | **testfailure** | **probefailure** | **testcomplete** | **testresult-change** }\* } command to configure conditions for sending trap messages.
12. (Optional) Run [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name*
    
    
    
    A VPN instance name is configured for the NQA test instance.
13. Schedule the NQA test instance.
    1. (Optional) Run the [**frequency**](cmdqueryname=frequency) *frequencyValue* command to configure the interval at which the NQA test instance is automatically executed.
    2. Run the [**start**](cmdqueryname=start) command to start the NQA test instance.
       
       
       
       The [**start**](cmdqueryname=start) command has multiple formats. Choose one of the following formats as needed:
       
       * To start an NQA test instance immediately, run the [**start now**](cmdqueryname=start+now) [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
       * To start an NQA test instance at a specified time, run the [**start**](cmdqueryname=start) **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
       * To start an NQA test instance after a specified delay, run the [**start delay**](cmdqueryname=start+delay) { **seconds** *second* | *hh*:*mm*:*ss* } [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
       * To start an NQA test instance at a specified time every day, run the [**start**](cmdqueryname=start) **daily** *hh*:*mm*:*ss* **to** *hh*:*mm*:*ss* [ **begin** *yyyy*/*mm*/*dd* ] [ **end** *yyyy*/*mm*/*dd* ] command.
14. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.