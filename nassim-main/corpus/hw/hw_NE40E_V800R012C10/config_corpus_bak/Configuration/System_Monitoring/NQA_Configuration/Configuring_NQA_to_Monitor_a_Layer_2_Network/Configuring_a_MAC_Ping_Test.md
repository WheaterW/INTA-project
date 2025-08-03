Configuring a MAC Ping Test
===========================

A MAC ping test can be used to check the connectivity and measure the packet loss, delay, and other indicators of the link between any two devices on a Layer 2 network, facilitating fault locating.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**cfm**](cmdqueryname=cfm) { **lbm** | **ltm** | **gmac-ltm** } [**receive disable**](cmdqueryname=receive+disable)
   
   
   
   The device is disabled from receiving loopback messages (LBMs) or linktrace messages (LTMs).
3. Create an NQA test instance and set its type to MAC ping.
   1. Run the [**nqa**](cmdqueryname=nqa) **test-instance** *admin-name test-name* command to create an NQA test instance and enter its view.
   2. Run the [**test-type**](cmdqueryname=test-type) **macping** command to set the test instance type to MAC ping.
   3. (Optional) Run the [**description**](cmdqueryname=description) *description* command to configure a description for the test instance.
4. Configure the MEP ID, MD name, and MA name based on the MAC ping type.
   1. Run the [**mep**](cmdqueryname=mep) **mep-id** *mep-id* command to configure a local MEP ID.
   2. Run the [**md**](cmdqueryname=md) *md-name* **ma** *ma-name* command to specify the names of the MD and MA for sending NQA test packets.
5. Perform either of the following steps to configure a destination address for the MAC ping test:
   
   
   * Run the [**destination-address**](cmdqueryname=destination-address) **mac** *macAddress* command to configure a destination MAC address.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     You can run the [**display cfm remote-mep**](cmdqueryname=display+cfm+remote-mep) command to query the destination MAC address.
   * Run the [**destination-address**](cmdqueryname=destination-address) **remote-mep** **mep-id** *remoteMepID* command to configure an RMEP ID.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the destination address type is **remote-mep**, you must configure the mapping between the remote MEP and MAC address first.
6. (Optional) Set optional parameters for the test instance and simulate real service flows.
   1. Run the [**datasize**](cmdqueryname=datasize) *datasizeValue* command to configure the size of the Data field in an NQA test packet.
   2. Run the [**probe-count**](cmdqueryname=probe-count) *number* command to set the number of probes in a test for the NQA test instance.
   3. Run the [**interval**](cmdqueryname=interval) **seconds** *interval* command to set the interval at which NQA test packets are sent.
7. (Optional) Configure test failure conditions and enable the function to send traps to the NMS upon test failures.
   1. Run the [**timeout**](cmdqueryname=timeout) *time* command to configure a timeout period for response packets.
   2. Run the [**fail-percent**](cmdqueryname=fail-percent) *percent* command to configure a failure percentage for the NQA test instance.
   3. Run the [**probe-failtimes**](cmdqueryname=probe-failtimes) *failTimes* command to configure the device to send trap messages to the NMS after the number of consecutive probe failures in an NQA test reaches the specified threshold.
   4. Run the [**test-failtimes**](cmdqueryname=test-failtimes) *failTimes* command to configure the device to send trap messages to the NMS after the number of consecutive NQA test failures reaches the specified threshold.
   5. Run the [**threshold**](cmdqueryname=threshold) **rtd** *thresholdRtd* command to configure a round-trip delay (RTD) threshold.
   6. Run the [**send-trap**](cmdqueryname=send-trap) { **all** | { **rtd** | **testfailure** | **probefailure** | **testcomplete** | **testresult-change** }\* } command to configure conditions for sending trap messages.
   7. Run the [**jitter-packetnum**](cmdqueryname=jitter-packetnum) *packetNum* command to configure the number of test packets to be sent in each test.
8. (Optional) Configure NQA statistics collection.
   
   
   
   Run [**records**](cmdqueryname=records) { **history** *number* | **result** *number* }
   
   The maximum numbers of historical records and test results that can be saved for the NQA test instance are configured.
9. (Optional) Run [**agetime**](cmdqueryname=agetime) *ageTimeValue*
   
   
   
   The aging time of the NQA test instance is set.
10. Schedule the NQA test instance.
    1. (Optional) Run the [**frequency**](cmdqueryname=frequency) *frequencyValue* command to configure the interval at which the NQA test instance is automatically executed.
    2. Run the [**start**](cmdqueryname=start) command to start an NQA test.
       
       
       
       The [**start**](cmdqueryname=start) command has multiple formats. Choose one of the following as needed.
       
       * To start an NQA test instance immediately, run the [**start now**](cmdqueryname=start+now) [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
       * To start an NQA test instance at a specified time, run the [**start**](cmdqueryname=start) **at** [ *yyyy/mm/dd* ] *hh:mm:ss* [ **end** { **at** [ *yyyy/mm/dd* ] *hh:mm:ss* | **delay** { **seconds** *second* | *hh:mm:ss* } | **lifetime** { **seconds** *second* | *hh:mm:ss* } } ] command.
       * To start an NQA test instance after a specified delay, run the [**start delay**](cmdqueryname=start+delay) { **seconds** *second* | *hh*:*mm*:*ss* } [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
       * To start an NQA test instance at a specified time every day, run the [**start**](cmdqueryname=start) **daily** *hh:mm:ss* **to** *hh:mm:ss* [ **begin** *yyyy/mm/dd* ] [ **end** *yyyy/mm/dd* ] command.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.