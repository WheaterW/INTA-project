Configuring the Querier Function
================================

The querier function enables a device to send Query messages for its upstream device and respond to Multicast Listener Discovery (MLD) messages sent from downstream devices.

#### Context

There is an MLD-capable Layer 3 multicast device acting as a querier on a multicast network. The querier sends MLD Query messages to create and maintain multicast forwarding entries for normal multicast data forwarding.

The querier function, however, cannot be implemented on a Layer 3 device in either of the following conditions:

* MLD messages sent from the Layer 3 device cannot reach a downstream Layer 2 device.
* Multicast forwarding entries on the Layer 3 device are statically configured and do not need to be dynamically learned.

In this case, the MLD querier function of the upstream device cannot be implemented on the network.

To solve these issues, configure the querier function on the Layer 2 device so that it can create and maintain multicast forwarding entries at the data link layer, ensuring normal multicast data forwarding. The querier parameters can be set as required.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Perform either of the following operations based on the VLAN or VPLS networking:
   
   
   * To enter the VLAN view, run the [**vlan**](cmdqueryname=vlan) *vlan-id* command.
   * To enter the VSI view, run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command.
3. Run [**mld-snooping enable**](cmdqueryname=mld-snooping+enable)
   
   
   
   MLD snooping is enabled for the VLAN or VSI.
4. Run [**mld-snooping querier enable**](cmdqueryname=mld-snooping+querier+enable)
   
   
   
   The querier function is enabled.
5. (Optional) Run [**mld-snooping querier-election**](cmdqueryname=mld-snooping+querier-election)
   
   
   
   The querier election function is enabled, so that the device can participate in querier election and send Query messages on behalf of the upstream device.
   
   
   
   If the querier function is enabled on multiple devices in a VLAN or VSI, you need to configure this function.
6. (Optional) Set querier parameters.
   
   
   * Run the [**mld-snooping query-interval**](cmdqueryname=mld-snooping+query-interval) *query-interval* command to set an interval at which a querier sends General Query messages.
   * Run the [**mld-snooping robust-count**](cmdqueryname=mld-snooping+robust-count) *robust-count* command to set the number of times Group-specific Query messages are sent.
   * Run the [**mld-snooping max-response-time**](cmdqueryname=mld-snooping+max-response-time) *max-response-time* command to set the maximum time for a querier to wait for responses from downstream hosts.
     
     The maximum response time must be shorter than the interval at which General Query messages are sent.
   * Run the [**mld-snooping lastmember-queryinterval**](cmdqueryname=mld-snooping+lastmember-queryinterval) *lastmember-queryinterval* command to configure the interval at which a querier sends Group-specific Query messages or Group-and-Source-Specific Query messages.![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   In a VSI scenario, if MLD snooping proxy is configured on one end of a PW, IPv6 addresses on the same network segment must be configured for the physical interfaces to which the two PW interfaces recurse. Otherwise, the sending of Group-specific Query messages is affected.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.