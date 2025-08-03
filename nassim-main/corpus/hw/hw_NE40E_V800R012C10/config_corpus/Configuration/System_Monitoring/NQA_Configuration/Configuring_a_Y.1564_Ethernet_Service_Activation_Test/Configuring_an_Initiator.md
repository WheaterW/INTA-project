Configuring an Initiator
========================

This section describes how to configure an initiator that sends simulated service traffic. You can set initiator parameters based on usage scenarios and test indicator types.

#### Context

Devices performing an Ethernet service activation test play two roles: initiator and reflector. An initiator sends simulated service traffic to a reflector, and the reflector reflects the service traffic.

The process of configuring an initiator is as follows:

1. Configure a test flow.
2. Configure a test instance.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nqa test-flow**](cmdqueryname=nqa+test-flow) *flow-id*
   
   
   
   A test flow is configured, and the NQA test flow view is displayed.
3. Specify service flow characteristics.
   
   
   1. Run either of the following commands to configure a traffic type and specify a MAC/IP address (or range) for test packets:
      * [**traffic-type**](cmdqueryname=traffic-type) **mac** { **destination** *destination-mac* [ *end-destination-mac* ] | **source** *source-mac* [ *end-source-mac* ] }
      * [**traffic-type**](cmdqueryname=traffic-type) **ipv4** { **destination** *destination-ip* [ *end-destination-ip* ] | **source** *source-ip* [ *end-source-ip* ] }
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Services may be forwarded based on the MAC or IP address or using MPLS based on the service type, such as Ethernet, IP, L2VPN, L2VPN accessing L3VPN, and L3VPN. When testing a service network, you must determine the specific service forwarding mode before configuring a traffic type for the service flow to be tested.
      
      * For Ethernet Layer 2 switching and L2VPN services, a MAC address must be specified, and an IP address is optional.
      * For IP routing and L3VPN services, an IP address and a MAC address must be specified. If no IP address or MAC address is specified, the reflector will reflect all the traffic, affecting other service functions.
      * For L2VPN accessing L3VPN, both MAC and IP addresses must be specified.
   2. Configure the following parameters as needed:
      * In the NQA test flow view, run the [**vlan**](cmdqueryname=vlan) *vlan-id* [ *end-vlan-vid* ] command to specify a single VLAN ID for Ethernet packets.
      * In the NQA test flow view, run the [**pe-vid**](cmdqueryname=pe-vid) *pe-vid* **ce-vid** *ce-vid* [ *ce-vid-end* ] command to specify double VLAN IDs for Ethernet packets.
      * Run the [**udp destination-port**](cmdqueryname=udp+destination-port) *destination-port* [ *end-destination-port* ] command to configure a destination UDP port number or range.
      * Run the [**udp source-port**](cmdqueryname=udp+source-port) *source-port* [ *end-source-port* ] command to configure a source UDP port number or range.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      * For the same test flow, a value range can be specified for only one of the following items: MAC or IP address (configured using the [**traffic-type**](cmdqueryname=traffic-type) command), VLAN (configured using the [**vlan**](cmdqueryname=vlan) or [**pe-vid**](cmdqueryname=pe-vid) command), and UDP port number (configured using the [**udp destination-port**](cmdqueryname=udp+destination-port) or [**udp source-port**](cmdqueryname=udp+source-port)command). In addition, the difference between the start and end values cannot be more than 127, and the end value must be greater than the start value.
      * In the [**traffic-type**](cmdqueryname=traffic-type) command, the start MAC or IP address can have only one different octet from the end MAC or IP address. For example, if the start IP address is set to 1.1.1.1, the end IP address can only be set to an IP address on the network segment 1.1.1.0. In addition, the difference between the start and end values cannot be more than 127, and the end value must be greater than the start value.
4. Run [**bandwidth cir**](cmdqueryname=bandwidth+cir) *cir-value* [ **eir** *eir-value* ]
   
   
   
   A bandwidth profile is configured for the NQA test flow, including service parameters such as the CIR.
   
   
   
   The default excess information rate (EIR) is 0 kbit/s. If the **eir** *eir-value* parameter is not configured, the EIR is not tested
5. Run [**sac**](cmdqueryname=sac) **flr** *flr-value* **ftd** *ftd-value* **fdv** *fdv-value*
   
   
   
   The frame loss ratio (FLR) is specified, expressed in 1/100000, the frame transfer delay (FTD) is specified, expressed in µs, and the frame delay variation (FDV) is specified, expressed in µs.
6. Enable the simple CIR test, enable traffic policing test, configure the color mode, and configure a test flow description as needed:
   
   
   1. Run the [**cir simple-test enable**](cmdqueryname=cir+simple-test+enable) command to enable the simple CIR test.
   2. Run the [**traffic-policing test enable**](cmdqueryname=traffic-policing+test+enable) command to enable the traffic policing test.
   3. Run the [**color-mode**](cmdqueryname=color-mode) { **8021p** **green** *begin-8021p-value* [ *end-8021p-value* ] **yellow** *begin-8021p-value* [ *end-8021p-value* ] | **dscp** **green** *begin-dscp-value* [ *end-dscp-value* ] **yellow** *begin-dscp-value* [ *end-dscp-value* ]}\* command to enable the color mode and configure the mapping between packet priorities and colors.
   4. Run the [**description**](cmdqueryname=description) *description* command to configure a description for the test flow.
7. Configure an Ethernet service activation test.
   1. Run the [**nqa**](cmdqueryname=nqa) **test-instance** *admin-name test-name* command to create an NQA test instance and enter its view.
   2. Run the [**test-type**](cmdqueryname=test-type) **ethernet-service** command to set the test instance type to Ethernet service activation.
   3. Run the [**test-flow**](cmdqueryname=test-flow) *flow-id* <1-16> command to configure a referenced test flow. Multiple test flows can be configured.
   4. Run the [**forwarding-simulation inbound-interface**](cmdqueryname=forwarding-simulation+inbound-interface) { **ifName** | *i*fType** **ifNum** } command to configure a simulated inbound interface.
   5. (Optional) Run the [**packet-size**](cmdqueryname=packet-size) *packet-size* <1-10> command to configure one or multiple sizes for test packets.
   6. (Optional) Run the [**duration**](cmdqueryname=duration) { **configuration-test** *configuration-test-time* | **performance-test** *performance-test-time* } command to set the durations of configuration and performance tests.
   7. Run the [**start**](cmdqueryname=start) **now** command to start the test.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.