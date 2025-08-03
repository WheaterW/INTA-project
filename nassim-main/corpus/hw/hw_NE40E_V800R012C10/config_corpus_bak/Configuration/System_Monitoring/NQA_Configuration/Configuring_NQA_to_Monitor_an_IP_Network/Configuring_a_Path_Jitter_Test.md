Configuring a Path Jitter Test
==============================

An NQA path jitter test instance, however, can identify the Router whose jitter value is great.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nqa**](cmdqueryname=nqa) **test-instance** *admin-name* *test-name*
   
   
   
   An NQA test instance is created and the test instance view is displayed.
3. Run [**test-type**](cmdqueryname=test-type) **pathjitter**
   
   
   
   The type of the test instance is configured as path jitter.
4. Run [**destination-address**](cmdqueryname=destination-address) **ipv4** *destAddress*
   
   
   
   The destination IP address is configured.
5. (Optional) Run the following commands to configure other parameters for the path jitter test:
   
   
   * Run [**icmp-jitter-mode**](cmdqueryname=icmp-jitter-mode) { **icmp-echo** | **icmp-timestamp** }
     
     The mode of the path jitter test is configured.
   * Run [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name*
     
     The VPN instance to be tested is configured.
   * Run [**source-address**](cmdqueryname=source-address) **ipv4** *srcAddress*
     
     The source IP address is configured.
   * Run [**probe-count**](cmdqueryname=probe-count) *number*
     
     The number of test probes to be sent each time is set.
   * Run [**jitter-packetnum**](cmdqueryname=jitter-packetnum) *packetNum*
     
     The number of test packets to be sent during each test is set.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The [**probe-count**](cmdqueryname=probe-count) command is used to configure the number of times for the jitter test and the [**jitter-packetnum**](cmdqueryname=jitter-packetnum) command is used to configure the number of test packets sent during each test. In actual configuration, the product of the number of times for the jitter test and the number of test packets must be less than 3000.
   * Run [**interval**](cmdqueryname=interval) **seconds** *interval*
     
     The interval for sending jitter test packets is set.
     
     The shorter the interval is, the sooner the test is complete. However, delays arise when the processor sends and receives test packets. Therefore, if the interval for sending test packets is set to a small value, a relatively greater error may occur in the statistics of the jitter test.
   * Run [**fail-percent**](cmdqueryname=fail-percent) *percent*
     
     The percentage of the failed NQA tests is set.
6. Run [**start**](cmdqueryname=start)
   
   
   
   The NQA test is started.
   
   Select the start mode as required because the [**start**](cmdqueryname=start) command has several forms.
   
   * To perform the NQA test immediately, run the [**start**](cmdqueryname=start)**now** [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
     
     The test instance is started immediately.
   * To perform the NQA test at the specified time, run the [**start**](cmdqueryname=start)**at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
     
     The test instance is started at a specified time.
   * To perform the NQA test after a certain delay period, run the [**start**](cmdqueryname=start)**delay** { **seconds** *second* | *hh*:*mm*:*ss* } [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
     
     The test instance is started after a certain delay.