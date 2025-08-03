Configuring an LSP Ping Test
============================

A label switched path (LSP) ping test can be used to check the connectivity and measure the packet loss rate, delay, and other indicators of an MPLS network from end to end.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Create an NQA test instance and set its type to LSP ping.
   1. Run the [**nqa**](cmdqueryname=nqa) **test-instance** *admin-name test-name* command to create an NQA test instance and enter its view.
   2. Run the [**test-type**](cmdqueryname=test-type) **lspping** command to set the test instance type to LSP ping.
   3. (Optional) Run the [**description**](cmdqueryname=description) *description* command to configure a description for the test instance.
3. (Optional) Run [**fragment enable**](cmdqueryname=fragment+enable)
   
   
   
   MPLS packet fragmentation is enabled for the NQA test instance.
4. Run [**lsp-type**](cmdqueryname=lsp-type) { **ipv4** | **te** | **bgp** | **srte** | **srbe** | **srte-policy** }
   
   
   
   An LSP test type is specified for the NQA test instance.
   
   
   
   If the LSP test type of the NQA test instance is set to **srbe**, run the following commands as required:
   
   * Run the [**remote-fec**](cmdqueryname=remote-fec) **ldp***remoteIpAddr**remoteMaskLen* command to configure an IP address for a remote FEC.
   * Run the [**path-type bypass**](cmdqueryname=path-type+bypass) command to configure the device to send Echo Request packets through the bypass LSP.
   * Run the [**flex-algo**](cmdqueryname=flex-algo) *flex-algo-id* command to specify a Flex-Algo ID for an SR-MPLS BE tunnel that is a Flex-Algo tunnel.
5. Configure related parameters according to the type of the LSP to be tested.
   
   
   * Test an LDP LSP:
     
     Run the [**destination-address**](cmdqueryname=destination-address) **ipv4** *destAddress* [ { **lsp-masklen** *maskLen* } | { **lsp-loopback** *loopbackAddress* } ] \* command to configure a destination address (i.e., IP address of the NQA server) for the NQA test instance.
   * Test a TE tunnel:
     
     Run the [**lsp-tetunnel**](cmdqueryname=lsp-tetunnel) { *tunnelName* | *ifType* *ifNum* } [ **hot-standby** | **primary** ] command to configure a TE LSP interface.
   * Test a BGP tunnel:
     
     Run the [**destination-address**](cmdqueryname=destination-address) **ipv4** *destAddress* [ { **lsp-masklen** *maskLen* } | { **lsp-loopback** *loopbackAddress* } ] \* command to configure a destination address (i.e., IP address of the NQA server) for the NQA test instance.
   * Test an SR-MPLS TE tunnel:
     
     Run the [**lsp-tetunnel**](cmdqueryname=lsp-tetunnel) { *tunnelName* | *ifType* *ifNum* } [ **hot-standby** | **primary** ] command to configure a TE tunnel interface.
   * Test an SR-MPLS BE tunnel:
     
     Run the [**destination-address**](cmdqueryname=destination-address) **ipv4** *destAddress* **lsp-masklen** *maskLen* command to configure a destination address (i.e., IP address of the NQA server) for the NQA test instance.
   * Test an SR-MPLS TE Policy:
     
     Run the [**policy**](cmdqueryname=policy) { **policy-name** *policyname* | **binding-sid** *bsid* | **endpoint-ip** *endpointip* **color** *colorid* } command to configure the name, binding segment ID, endpoint IP address, and color ID of an SR-MPLS TE Policy.
6. (Optional) Run [**lsp-nexthop**](cmdqueryname=lsp-nexthop) *nexthop-ip-address*
   
   
   
   A next-hop address is specified in the scenario where load balancing is enabled on the ingress of the LSP ping test.
   
   
   
   If load balancing is enabled on the ingress, you can run this command to specify a next-hop address so that packets are transmitted in the specified direction.
7. Set optional parameters for the test instance and simulate real service flows.
   1. Run the [**lsp-exp**](cmdqueryname=lsp-exp) *exp* command to configure an LSP EXP value for the NQA test instance.
   2. Run the [**lsp-replymode**](cmdqueryname=lsp-replymode) { **level-control-channel** | **no-reply** | **udp** } command to configure a reply mode for the NQA test instance.
   3. Run the [**datafill**](cmdqueryname=datafill) *fill-string* command to configure the padding characters to be filled into test packets.
   4. Run the [**datasize**](cmdqueryname=datasize) *datasizeValue* command to set the size of the Data field in an NQA test packet.
   5. Run the [**probe-count**](cmdqueryname=probe-count) *number* command to set the number of probes in a test for the NQA test instance.
   6. Run the [**interval**](cmdqueryname=interval) **seconds** *interval* command to set the interval at which NQA test packets are sent.
   7. Run the [**source-address**](cmdqueryname=source-address) **ipv4** *srcAddress* command to specify a source IP address for NQA test packets.
   8. Run the [**ttl**](cmdqueryname=ttl) *ttlValue* command to configure a TTL value for NQA test packets.
8. (Optional) Configure test failure conditions.
   1. Run the [**timeout**](cmdqueryname=timeout) *time* command to configure a timeout period for response packets.
      
      
      
      If no response packets are received within the timeout period, the probe fails.
   2. Run the [**fail-percent**](cmdqueryname=fail-percent) *percent* command to configure a failure percentage for the NQA test instance.
      
      
      
      If the percentage of failed probes to total probes is greater than or equal to the configured failure percentage, the test is considered as a failure.
9. (Optional) Run [**records**](cmdqueryname=records) { **history** *number* | **result** *number* }
   
   
   
   The maximum numbers of historical records and test results that can be saved for the NQA test instance are configured.
10. Schedule the NQA test instance.
    1. (Optional) Run the [**frequency**](cmdqueryname=frequency) *frequencyValue* command to configure the interval at which the NQA test instance is automatically executed.
    2. Run the [**start**](cmdqueryname=start) command to start the NQA test instance.
       
       
       
       The [**start**](cmdqueryname=start) command has multiple formats. Choose one of the following formats as needed:
       
       * To start an NQA test instance immediately, run the [**start now**](cmdqueryname=start+now) [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
       * To start an NQA test instance at a specified time, run the [**start**](cmdqueryname=start) **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
       * To start an NQA test instance after a specified delay, run the [**start delay**](cmdqueryname=start+delay) { **seconds** *second* | *hh*:*mm*:*ss* } [ **end** { **at** [ *yyyy*/*mm*/*dd* ] *hh*:*mm*:*ss* | **delay** { **seconds** *second* | *hh*:*mm*:*ss* } | **lifetime** { **seconds** *second* | *hh*:*mm*:*ss* } } ] command.
       * To start an NQA test instance at a specified time every day, run the [**start**](cmdqueryname=start) **daily** *hh*:*mm*:*ss* **to** *hh*:*mm*:*ss* [ **begin** *yyyy*/*mm*/*dd* ] [ **end** *yyyy*/*mm*/*dd* ] command.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.