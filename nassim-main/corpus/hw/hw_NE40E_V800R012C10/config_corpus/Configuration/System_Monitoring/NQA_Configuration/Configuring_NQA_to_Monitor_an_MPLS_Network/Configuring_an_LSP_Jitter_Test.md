Configuring an LSP Jitter Test
==============================

An LSP jitter test can be used to measure the end-to-end jitter of services carried on an MPLS network.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Create an NQA test instance and set its type to LSP jitter.
   1. Run the [**nqa**](cmdqueryname=nqa) **test-instance** *admin-name test-name* command to create an NQA test instance and enter its view.
   2. Run the [**test-type**](cmdqueryname=test-type) **lspjitter** command to set the test instance type to LSP jitter.
   3. (Optional) Run the [**description**](cmdqueryname=description) *description* command to configure a description for the test instance.
3. (Optional) Run [**fragment enable**](cmdqueryname=fragment+enable)
   
   
   
   MPLS packet fragmentation is enabled for the NQA test instance.
4. Run [**lsp-type**](cmdqueryname=lsp-type) { **ipv4** | **te** }
   
   
   
   An LSP test type is specified for the NQA test instance.
5. Configure the destination address or tunnel interface based on the type of the LSP to be tested.
   
   
   * Test an LDP LSP:
     
     Run the [**destination-address**](cmdqueryname=destination-address) **ipv4** *destAddress* [ { **lsp-masklen** *maskLen* } | { **lsp-loopback** *loopbackAddress* } ] \* command to configure a destination address (i.e., IP address of the NQA server) for the NQA test instance.
   * Test a TE tunnel:
     
     Run the [**lsp-tetunnel**](cmdqueryname=lsp-tetunnel) { *tunnelName* | *ifType* *ifNum* } [ **hot-standby** | **primary** ] command to configure a TE tunnel interface.
6. (Optional) Set optional parameters for the test instance and simulate real service flows.
   1. Run the [**lsp-exp**](cmdqueryname=lsp-exp) *exp* command to configure an LSP EXP value for the NQA test instance.
   2. Run the [**lsp-replymode**](cmdqueryname=lsp-replymode) { **level-control-channel** | **no-reply** | **udp** } command to configure a reply mode for the NQA test instance.
   3. Run the [**datafill**](cmdqueryname=datafill) *fill-string* command to configure the padding characters to be filled into test packets.
   4. Run the [**datasize**](cmdqueryname=datasize) *datasizeValue* command to set the size of the Data field in an NQA test packet.
   5. Run the [**jitter-packetnum**](cmdqueryname=jitter-packetnum) *packetNum* command to configure the number of packets to be sent in each probe.
   6. Run the [**probe-count**](cmdqueryname=probe-count) *number* command to set the number of probes in a test for the NQA test instance.
   7. Run the [**interval**](cmdqueryname=interval) **seconds** *interval* command to configure the interval at which NQA test packets are sent.
   8. Run the [**source-address**](cmdqueryname=source-address) **ipv4** *srcAddress* command to specify a source IP address for NQA test packets.
   9. Run the [**ttl**](cmdqueryname=ttl) *ttlValue* command to configure a TTL value for NQA test packets.
7. (Optional) Configure test failure conditions.
   1. Run the [**timeout**](cmdqueryname=timeout) *time* command to configure a timeout period for response packets.
      
      
      
      If no response packets are received within the timeout period, the probe fails.
   2. Run the [**fail-percent**](cmdqueryname=fail-percent) *percent* command to configure a failure percentage for the NQA test instance.
      
      
      
      If the percentage of failed probes to total probes is greater than or equal to the configured failure percentage, the test is considered as a failure.
8. (Optional) Run [**records**](cmdqueryname=records) { **history** *number* | **result** *number* }
   
   
   
   The maximum numbers of historical records and test results that can be saved for the NQA test instance are configured.
9. Schedule the NQA test instance.
   1. (Optional) Run the [**frequency**](cmdqueryname=frequency) *frequencyValue* command to configure the interval at which the NQA test instance is automatically executed.
   2. Run the [**start**](cmdqueryname=start) command to start the NQA test instance.
      
      
      
      The [**start**](cmdqueryname=start) command has multiple formats. Choose one of the following formats as needed:
      
      * To start an NQA test instance immediately, run the [**start now**](cmdqueryname=start+now) [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
      * To start an NQA test instance at a specified time, run the [**start**](cmdqueryname=start) **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
      * To start an NQA test instance after a specified delay, run the [**start delay**](cmdqueryname=start+delay) { **seconds** *second* | *hh*:*mm*:*ss* } [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
      * To start an NQA test instance at a specified time every day, run the [**start**](cmdqueryname=start) **daily** *hh*:*mm*:*ss* **to** *hh*:*mm*:*ss* [ **begin** *yyyy*/*mm*/*dd* ] [ **end** *yyyy*/*mm*/*dd* ] command.
10. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.