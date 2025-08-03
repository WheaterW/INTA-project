Configuring a Reflector
=======================

This section describes how to configure a reflector, which loops traffic back to an initiator. Parameters configured on the reflector vary according to scenarios.

#### Context

Devices performing an Ethernet service activation test play two roles: initiator and reflector. An initiator sends simulated service traffic to a reflector, and the reflector reflects the service traffic.

The reflector must be specified before a test is started.

A reflector can reflect test traffic in either of the following modes:

* Interface-based mode: A reflector reflects all traffic that its interface receives.
* Flow-based mode: A reflector reflects only traffic meeting specified conditions. In flow-based mode, a test flow must have been configured.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nqa test-flow**](cmdqueryname=nqa+test-flow) *flow-id*
   
   
   
   A test flow is configured, and the NQA test flow view is displayed.
3. Configure service flow characteristics.
   
   
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
      * Run the [**udp destination-port**](cmdqueryname=udp+destination-port) *destination-port* [ *end-destination-port* ] command to specify a destination UDP port number or range.
      * Run the [**udp source-port**](cmdqueryname=udp+source-port) *source-port* [ *end-source-port* ] command to specify a source UDP port number or range.![](../../../../public_sys-resources/note_3.0-en-us.png) 
        + For the same test flow, a value range can be specified for only one of the following items: MAC or IP address (configured using the [**traffic-type**](cmdqueryname=traffic-type) command), VLAN (configured using the [**vlan**](cmdqueryname=vlan) or [**pe-vid**](cmdqueryname=pe-vid) command), and UDP port number (configured using the [**udp destination-port**](cmdqueryname=udp+destination-port) or [**udp source-port**](cmdqueryname=udp+source-port)command). In addition, the difference between the start and end values cannot be more than 127, and the end value must be greater than the start value.
        + In the [**traffic-type**](cmdqueryname=traffic-type) command, the start MAC or IP address can have only one different octet from the end MAC or IP address. For example, if the start IP address is set to 1.1.1.1, the end IP address can only be set to an IP address on the network segment 1.1.1.0. In addition, the difference between the start and end values cannot be more than 127, and the end value must be greater than the start value.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**nqa reflector**](cmdqueryname=nqa+reflector)*reflector-id***interface** { *interface-name* | *interface-type**interface-number* } [ [ [ **test-flow** { *testFlowId* } &<1-16> ] | [ [ **ipv4***ip-address* | **simulate-ipipv4***ip-address2* | **mac***mac-address* ] [ **pe-vid***pe-vid***ce-vid***ce-vid* | **vlan***vlan-id* ] [ **source-port***source-port* ] [ **destination-port***destination-port* ] ] ] | **exclusive** ] [ **exchange-port** ] [ **agetime***agetime* | **endtime** { *endtime* | *enddateendtime* } ]
   
   
   
   A reflector is specified.
   
   
   
   If the **test-flow** *flow-id* & <1-16> parameter is configured, the reflector reflects traffic based on a specified flow. Otherwise, the reflector reflects all traffic that its interface receives. The **agetime** *age-time* parameter is optional, and the default value is 14400s.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.