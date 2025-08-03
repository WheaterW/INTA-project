Configuring the Querier Function
================================

The querier function enables a device to send Query messages for its upstream device and respond to Join/Leave messages sent from downstream devices.

#### Context

A Layer 3 multicast device on a multicast network running IGMP acts as an IGMP querier, sending IGMP Query messages to create and maintain multicast forwarding entries for normal multicast data forwarding.

However, if the following situations exist:

* IGMP messages sent by the upstream device cannot reach the device.
* Multicast forwarding entries on the upstream device are statically configured, not dynamically learned.

In this case, the IGMP querier function of the upstream device cannot be implemented on the network.

To solve these issues, configure the querier function on the Layer 2 device so that it can create and maintain multicast forwarding entries at the data link layer, ensuring normal multicast data forwarding. The querier parameters can be set as required.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Perform either of the following operations based on the VLAN or VPLS networking:
   
   
   * To enter the VLAN view, run the [**vlan**](cmdqueryname=vlan) *vlan-id* command.
   * To enter the VSI view, run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command.
3. Run [**igmp-snooping enable**](cmdqueryname=igmp-snooping+enable)
   
   
   
   IGMP snooping is enabled for the VLAN or VSI.
4. Run [**igmp-snooping querier enable**](cmdqueryname=igmp-snooping+querier+enable)
   
   
   
   The querier function is enabled.
   
   By default, the querier function is disabled.
5. Run [**igmp-snooping querier-election**](cmdqueryname=igmp-snooping+querier-election)
   
   
   
   Query election is enabled so that a device is elected as the querier to send Query messages to user hosts on behalf of the upstream device.
   
   By default, query election is not enabled on all devices.
   
   If the querier function is enabled on multiple devices in the VLAN or VSI, this step needs to be performed.
6. (Optional) Set querier parameters.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   An IGMPv1 host does not send a Leave message when leaving a multicast group. Therefore, this configuration is valid only when IGMPv2 messages can be processed in the VLAN or VSI.
   
   * Run [**igmp-snooping query-interval**](cmdqueryname=igmp-snooping+query-interval) *query-interval*
     
     The interval at which a querier sends General Query messages is set.
     
     By default, a querier sends General Query messages at an interval of 60s.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The default interval at which a querier sends General Query messages is 60 seconds, but the default interval defined in the corresponding protocol is 125 seconds. Currently, some vendor devices use the protocol-defined default interval of 125 seconds. To enable the querier to interwork with such devices, you must change the corresponding configuration to ensure that both ends send General Query messages at the same interval.
   * Run [**igmp-snooping robust-count**](cmdqueryname=igmp-snooping+robust-count) *robust-count*
     
     The number of times a Group-specific Query message is sent is set.
     
     By default, a Group-specific Query message is sent twice.
   * Run [**igmp-snooping max-response-time**](cmdqueryname=igmp-snooping+max-response-time) *max-response-time*
     
     The maximum time for a downstream host to respond to a querier is set.
     
     By default, the maximum time for a downstream host to respond to a querier is 10s.
     
     The maximum response time must be shorter than the interval at which General Query messages are sent.
   * Run [**igmp-snooping lastmember-queryinterval**](cmdqueryname=igmp-snooping+lastmember-queryinterval) *lastmember-queryinterval*
     
     The interval at which a querier sends Group-specific Query messages or Group-and-Source-specific Query messages is set.
     
     By default, a querier sends Group-specific Query messages at an interval of 1s.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
8. (Optional) Configure a source IP address for IGMP General Query messages.
   
   
   * Configuration in the system view: Run the [**igmp-snooping send-query source-address**](cmdqueryname=igmp-snooping+send-query+source-address) *ip-source-address* command.
   * Configuration in the VLAN view:
     1. Run the [**vlan**](cmdqueryname=vlan) *vlan-id* command to enter the VLAN view.
     2. Run the [**igmp-snooping send-query source-address**](cmdqueryname=igmp-snooping+send-query+source-address) *ip-source-address* command to configure the source IP address of IGMP Query messages in the VLAN view.
     3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If both the system view and VLAN view have their own configurations, the configuration in the VLAN view is preferentially used.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.