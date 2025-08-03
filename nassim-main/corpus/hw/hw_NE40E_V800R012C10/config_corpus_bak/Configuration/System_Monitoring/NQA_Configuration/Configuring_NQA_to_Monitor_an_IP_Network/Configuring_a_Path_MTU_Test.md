Configuring a Path MTU Test
===========================

A path MTU test can obtain the maximum MTU value that does not require packet fragmentation during the packet transmission on the link.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nqa**](cmdqueryname=nqa) **test-instance** *admin-name* *test-name*
   
   
   
   An NQA test instance is created and the test instance view is displayed.
3. Run [**test-type**](cmdqueryname=test-type) **pathmtu**
   
   
   
   The type of the test instance is configured as path MTU.
4. Run [**destination-address**](cmdqueryname=destination-address) **ipv4** *destAddress*
   
   
   
   The destination IP address is configured.
5. (Optional) Run the following commands to configure other parameters for the path MTU test.
   
   
   * Run [**discovery-pmtu-max**](cmdqueryname=discovery-pmtu-max) *pmtu-max*
     
     The maximum value of the path MTU test range is set.
   * Run [**step**](cmdqueryname=step) *step*
     
     The value of the incremental step is set for the packet length in the path MTU test.
   * Run [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name*
     
     The VPN instance to be tested is configured.
   * Run [**source-address**](cmdqueryname=source-address) **ipv4** *srcAddress*
     
     The source IP address is configured.
   * Run [**probe-count**](cmdqueryname=probe-count) *number*
     
     The maximum number of probe packets that are allowed to time out consecutively is configured.
6. Run [**start**](cmdqueryname=start)
   
   
   
   The NQA test is started.
   
   Select the start mode as required because the [**start**](cmdqueryname=start) command has several forms.
   
   * To perform the NQA test immediately, run the [**start**](cmdqueryname=start)**now** [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
     
     The test instance is started immediately.
   * To perform the NQA test at the specified time, run the [**start**](cmdqueryname=start)**at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
     
     The test instance is started at a specified time.
   * To perform the NQA test after a certain delay period, run the [**start**](cmdqueryname=start)**delay** { **seconds** *second* | *hh*:*mm*:*ss* } [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
     
     The test instance is started after a certain delay.