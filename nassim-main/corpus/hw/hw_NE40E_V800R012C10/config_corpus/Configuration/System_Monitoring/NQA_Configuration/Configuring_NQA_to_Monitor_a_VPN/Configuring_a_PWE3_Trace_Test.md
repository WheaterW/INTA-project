Configuring a PWE3 Trace Test
=============================

A Pseudowire Emulation Edge-to-Edge (PWE3) trace test can be used to check the pseudo wire (PW) connectivity and measure the packet loss rate, delay, and other indicators of a virtual private wire service (VPWS) network. It can also be used to check the forwarding path of test packets.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Create an NQA test instance and set its type to PWE3 trace.
   1. Run the [**nqa**](cmdqueryname=nqa) **test-instance** *admin-name test-name* command to create an NQA test instance and enter its view.
   2. Run the [**test-type**](cmdqueryname=test-type) **pwe3trace** command to set the test instance type to PWE3 trace.
   3. (Optional) Run the [**description**](cmdqueryname=description) *description* command to configure a description for the test instance.
3. (Optional) Run [**fragment enable**](cmdqueryname=fragment+enable)
   
   
   
   MPLS packet fragmentation is enabled for the NQA test instance.
4. Set parameters for the Layer 2 virtual private network (L2VPN) to be tested.
   1. Run the [**vc-type ldp**](cmdqueryname=vc-type+ldp) command to set the VC protocol type to LDP.
   2. Run the [**local-pw-type**](cmdqueryname=local-pw-type) *pwTypeValue* command to configure a PW encapsulation type for the local PE.
   3. Run the [**label-type**](cmdqueryname=label-type) { **control-word** | {{ **label-alert** | **normal** } [ **no-control-word** ] } } command to configure a packet encapsulation type.
   4. Run the [**lsp-version**](cmdqueryname=lsp-version) { **rfc4379** | **ptn-mode** } command to specify a protocol for the LSP test instance.
   5. Run the [**local-pw-id**](cmdqueryname=local-pw-id) *pwIdValue* command to configure a PW ID for the local PE.
   6. (Optional) Run the [**peer-address**](cmdqueryname=peer-address) *peeraddress* command to configure the peer IP address.
   7. (Optional) Run the [**ttl-copymode**](cmdqueryname=ttl-copymode) { **pipe** | **uniform** } command to specify a TTL propagation mode.
5. (Optional) Run [**destination-address**](cmdqueryname=destination-address) **ipv4** *destAddress*
   
   
   
   An IP address is configured for the remote PE.
   
   
   
   To monitor a multi-segment PW, you need to configure remote PE information. An MS-PW can be tested only after you specify **control-word** or **normal**.
6. Set optional parameters for the test instance and simulate real service flows.
   1. Run the [**lsp-exp**](cmdqueryname=lsp-exp) *exp* command to configure an LSP EXP value for the NQA test instance.
   2. Run the [**lsp-replymode**](cmdqueryname=lsp-replymode) { **level-control-channel** | **no-reply** | **udp** } command to configure a reply mode for the NQA test instance.
   3. Run the [**probe-count**](cmdqueryname=probe-count) *number* command to set the number of probes in a test for the NQA test instance.
   4. Run the [**tracert-livetime**](cmdqueryname=tracert-livetime) **first-ttl** *first-ttl* **max-ttl** *max-ttl* command to configure the lifetime of the NQA test instance.
7. (Optional) Configure test failure conditions.
   1. Run the [**timeout**](cmdqueryname=timeout) *time* command to configure a timeout period for response packets.
      
      
      
      If no response packets are received within the timeout period, the probe fails.
   2. Run the [**tracert-hopfailtimes**](cmdqueryname=tracert-hopfailtimes) *hopfailtimesValue* command to set the maximum number of hop failures in a probe for the test instance.
8. Run [**records**](cmdqueryname=records) { **history** *number* | **result** *number* }
   
   
   
   The maximum numbers of historical records and test results that can be saved for the NQA test instance are configured.
9. (Optional) Configure the device to send trap messages.
   
   
   1. Run the [**probe-failtimes**](cmdqueryname=probe-failtimes) *failTimes* command to configure the device to send trap messages to the NMS after the number of consecutive probe failures in an NQA test reaches the specified threshold.
   2. Run the [**test-failtimes**](cmdqueryname=test-failtimes) *failTimes* command to configure the device to send trap messages to the NMS after the number of consecutive NQA test failures reaches the specified threshold.
   3. Run the [**threshold**](cmdqueryname=threshold) **rtd** *thresholdRtd* command to configure a round-trip delay (RTD) threshold.
   4. Run the [**send-trap**](cmdqueryname=send-trap) { **all** | { **rtd** | **testfailure** | **probefailure** | **testcomplete** | **testresult-change** }\* } command to configure conditions for sending trap messages.
10. Schedule the test instance.
    1. (Optional) Run the [**frequency**](cmdqueryname=frequency) *frequencyValue* command to configure the interval at which the NQA test instance is automatically executed.
    2. Run the [**start**](cmdqueryname=start) command to start an NQA test instance.
       
       
       
       The [**start**](cmdqueryname=start) command has multiple formats. Choose one of the following as needed.
       
       * To start an NQA test instance immediately, run the [**start now**](cmdqueryname=start+now) [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
       * To start an NQA test instance at a specified time, run the [**start**](cmdqueryname=start) **at** [ *yyyy/mm/dd* ] *hh:mm:ss* [ **end** { **at** [ *yyyy/mm/dd* ] *hh:mm:ss* | **delay** { **seconds** *second* | *hh:mm:ss* } | **lifetime** { **seconds** *second* | *hh:mm:ss* } } ] command.
       * To start an NQA test instance after a specified delay, run the [**start delay**](cmdqueryname=start+delay) { **seconds** *second* | *hh*:*mm*:*ss* } [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
       * To start an NQA test instance at a specified time every day, run the [**start**](cmdqueryname=start) **daily** *hh:mm:ss* **to** *hh:mm:ss* [ **begin** *yyyy/mm/dd* ] [ **end** *yyyy/mm/dd* ] command.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.