Configuring a VPLS MAC Ping Test
================================

A VPLS MAC ping test can be used to check the connectivity of Layer 2 forwarding links on a VPLS network.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Create an NQA test instance and set its type to VPLS MAC ping.
   1. Run the [**nqa**](cmdqueryname=nqa) **test-instance** *admin-name test-name* command to create an NQA test instance and enter its view.
   2. Run the [**test-type**](cmdqueryname=test-type) **vplsping** command to set the test instance type to VPLS MAC ping.
   3. (Optional) Run the [**description**](cmdqueryname=description) *description* command to configure a description for the test instance.
3. (Optional) Run [**fragment enable**](cmdqueryname=fragment+enable)
   
   
   
   MPLS packet fragmentation is enabled for the NQA test instance.
4. Set the VPLS network parameters to be tested. Specifically:
   1. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* command to configure the name of a VSI to be tested.
   2. Run the [**destination-address**](cmdqueryname=destination-address) **mac** *macAddress* command to configure the MAC address associated with the VSI.
   3. (Optional) Run the [**vlan**](cmdqueryname=vlan) *vlan-id* command to configure a VLAN ID for the NQA test instance.
5. (Optional) Set optional parameters for the test instance and simulate real service flows.
   1. Run the [**lsp-exp**](cmdqueryname=lsp-exp) *exp* command to configure an LSP EXP value for the NQA test instance.
   2. Run the [**lsp-replymode**](cmdqueryname=lsp-replymode) { **no-reply** | **udp** | **udp-via-vpls**} command to configure a reply mode for the NQA test instance.
   3. Run the [**datafill**](cmdqueryname=datafill) *fill-string* command to configure the padding characters to be filled into test packets.
   4. Run the [**datasize**](cmdqueryname=datasize) *datasizeValue* command to set the size of the Data field in an NQA test packet.
   5. Run the [**probe-count**](cmdqueryname=probe-count) *number* command to set the number of probes in a test for the NQA test instance.
   6. Run the [**interval**](cmdqueryname=interval) **seconds** *interval* command to set the interval at which NQA test packets are sent.
   7. Run the [**ttl**](cmdqueryname=ttl) *ttlValue* command to configure a TTL value for NQA test packets.
6. (Optional) Configure test failure conditions and enable the function to send traps to the NMS upon test failures.
   1. Run the [**timeout**](cmdqueryname=timeout) *time* command to configure a timeout period for response packets.
   2. Run the [**fail-percent**](cmdqueryname=fail-percent) *percent* command to configure a failure percentage for the NQA test instance.
   3. Run the [**probe-failtimes**](cmdqueryname=probe-failtimes) *failTimes* command to configure the device to send trap messages to the NMS after the number of consecutive probe failures in an NQA test reaches the specified threshold.
   4. Run the [**test-failtimes**](cmdqueryname=test-failtimes) *failTimes* command to configure the device to send trap messages to the NMS after the number of consecutive NQA test failures reaches the specified threshold.
   5. Run the [**threshold**](cmdqueryname=threshold) **rtd** *thresholdRtd* command to configure a round-trip delay (RTD) threshold.
   6. Run the [**send-trap**](cmdqueryname=send-trap) { **all** | { **rtd** | **testfailure** | **probefailure** | **testcomplete** | **testresult-change** }\* } command to configure conditions for sending trap messages.
7. (Optional) Configure the NQA statistics function.
   
   
   
   Run [**records**](cmdqueryname=records) { **history** *number* | **result** *number* }
   
   The maximum numbers of historical records and test results that can be saved for the NQA test instance are configured.
8. (Optional) Run [**agetime**](cmdqueryname=agetime) *ageTimeValue*
   
   
   
   The aging time of the NQA test instance is set.
9. Schedule the NQA test instance.
   1. (Optional) Run the [**frequency**](cmdqueryname=frequency) *frequencyValue* command to configure the interval at which the NQA test instance is automatically executed.
   2. Run the [**start**](cmdqueryname=start) command to start the NQA test instance.
      
      
      
      The [**start**](cmdqueryname=start) command has multiple formats. Choose one of the following as needed.
      
      * To start an NQA test instance immediately, run the [**start now**](cmdqueryname=start+now) [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
      * To start an NQA test instance at a specified time, run the [**start**](cmdqueryname=start) **at** [ *yyyy/mm/dd* ] *hh:mm:ss* [ **end** { **at** [ *yyyy/mm/dd* ] *hh:mm:ss* | **delay** { **seconds** *second* | *hh:mm:ss* } | **lifetime** { **seconds** *second* | *hh:mm:ss* } } ] command.
      * To start an NQA test instance after a specified delay, run the [**start delay**](cmdqueryname=start+delay) { **seconds** *second* | *hh*:*mm*:*ss* } [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
      * To start an NQA test instance at a specified time every day, run the [**start**](cmdqueryname=start) **daily** *hh:mm:ss* **to** *hh:mm:ss* [ **begin** *yyyy/mm/dd* ] [ **end** *yyyy/mm/dd* ] command.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.