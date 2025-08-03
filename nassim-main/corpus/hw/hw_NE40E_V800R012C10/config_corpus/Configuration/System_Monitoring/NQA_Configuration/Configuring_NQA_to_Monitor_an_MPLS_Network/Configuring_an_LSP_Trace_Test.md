Configuring an LSP Trace Test
=============================

An LSP trace test can be used to check the connectivity and measure the packet loss rate, delay, and other indicators of an MPLS network hop by hop. It can also monitor the forwarding path of MPLS packets.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Create an NQA test instance and set its type to LSP trace.
   1. Run the [**nqa**](cmdqueryname=nqa) **test-instance** *admin-name test-name* command to create an NQA test instance and enter its view.
   2. Run the [**test-type**](cmdqueryname=test-type) **lsptrace** command to set the test instance type to LSP trace.
   3. (Optional) Run the [**description**](cmdqueryname=description) *description* command to configure a description for the test instance.
3. (Optional) Run [**fragment enable**](cmdqueryname=fragment+enable)
   
   
   
   MPLS packet fragmentation is enabled for the NQA test instance.
4. Run [**lsp-type**](cmdqueryname=lsp-type) { **ipv4** | **te** | **bgp** | **srte** | **srbe** | **srte-policy** }
   
   
   
   An LSP test type is specified for the NQA test instance.
   
   
   
   If the LSP test type of the NQA test instance is set to **srbe**, run the following commands as required:
   
   * To configure an IP address for a remote FEC, run the [**remote-fec**](cmdqueryname=remote-fec) **ldp***remoteIpAddr**remoteMaskLen* command.
   * To configure the device to send Echo Request packets through the bypass LSP, run the [**path-type bypass**](cmdqueryname=path-type+bypass) command.
   * To specify a Flex-Algo ID for an SR-MPLS BE tunnel that is a Flex-Algo tunnel, run the [**flex-algo**](cmdqueryname=flex-algo) *flex-algo-id* command.
5. Configure related parameters according to the type of the LSP to be tested.
   
   
   * Test an LDP LSP:
     
     Run the [**destination-address**](cmdqueryname=destination-address) **ipv4** *destAddress* [ { **lsp-masklen** *maskLen* } | { **lsp-loopback** *loopbackAddress* } ] \* command to configure a destination address (i.e., IP address of the NQA server) for the NQA test instance.
   * Test a TE tunnel:
     
     Run the [**lsp-tetunnel**](cmdqueryname=lsp-tetunnel) { *tunnelName* | *ifType* *ifNum* } [ **hot-standby** | **primary** ] command to configure a TE tunnel interface.
   * Test a BGP tunnel:
     
     Run the [**destination-address**](cmdqueryname=destination-address) **ipv4** *destAddress* [ { **lsp-masklen** *maskLen* } | { **lsp-loopback** *loopbackAddress* } ] \* command to configure a destination address (i.e., IP address of the NQA server) for the NQA test instance.
   * Test an SR-MPLS TE tunnel:
     
     Run the [**lsp-tetunnel**](cmdqueryname=lsp-tetunnel) { *tunnelName* | *ifType* *ifNum* } [ **hot-standby** | **primary** ] command to configure a TE tunnel interface.
   * Test an SR-MPLS BE tunnel:
     
     Run the [**destination-address**](cmdqueryname=destination-address) **ipv4** *destAddress* **lsp-masklen** *maskLen* command to configure a destination address (i.e., IP address of the NQA server) for the NQA test instance.
   * Test an SR-MPLS TE Policy:
     
     Run the [**policy**](cmdqueryname=policy) { **policy-name** *policyname* | **binding-sid** *bsid* | **endpoint-ip** *endpointip* **color** *colorid* } command to configure the name, binding segment ID, endpoint IP address, and color ID of an SR-MPLS TE policy.
6. (Optional) Set optional parameters for the test instance and simulate real service flows.
   1. Run the [**lsp-exp**](cmdqueryname=lsp-exp) *exp* command to configure an LSP EXP value for the NQA test instance.
   2. Run the [**lsp-replymode**](cmdqueryname=lsp-replymode) { **level-control-channel** | **no-reply** | **udp** } command to configure a reply mode for the NQA test instance.
   3. Run the [**probe-count**](cmdqueryname=probe-count) *number* command to set the number of probes in a test for the NQA test instance.
   4. Run the [**source-address**](cmdqueryname=source-address) **ipv4** *srcAddress* command to specify a source IP address for NQA test packets.
   5. Run the [**tracert-livetime**](cmdqueryname=tracert-livetime) **first-ttl** *first-ttl* **max-ttl** *max-ttl* command to set a TTL value for test packets.
7. (Optional) Configure test failure conditions.
   1. Run the [**timeout**](cmdqueryname=timeout) *time* command to configure a timeout period for response packets.
      
      
      
      If no response packets are received within the timeout period, the probe fails.
   2. Run the [**tracert-hopfailtimes**](cmdqueryname=tracert-hopfailtimes) *hopfailtimesValue* command to set the maximum number of hop failures in a probe for the test instance.
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
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.