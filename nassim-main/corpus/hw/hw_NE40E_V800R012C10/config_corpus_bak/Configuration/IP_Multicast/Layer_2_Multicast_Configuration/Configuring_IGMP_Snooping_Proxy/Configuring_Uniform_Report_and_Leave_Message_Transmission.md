Configuring Uniform Report/Leave Message Transmission
=====================================================

Configuring a uniform Report/Leave message transmission on a Layer 2 device reduces network bandwidth consumption.

#### Context

If uniform Report/Leave message transmission is not enabled on a network with a large number of user hosts, redundant IGMP packets consume lots of network bandwidth resources. After receiving an IGMP Query message for a multicast group from an upstream device, a Layer 2 device enabled with uniform Report/Leave message transmission replies with only one IGMP Report message, regardless of how many hosts want to join the multicast group. This configuration effectively reduces network bandwidth consumption.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Perform either of the following operations based on the VLAN or VPLS networking:
   
   
   * To enter the VLAN view, run the [**vlan**](cmdqueryname=vlan) *vlan-id* command.
   * To enter the VSI view, run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command.
3. Run [**igmp-snooping proxy**](cmdqueryname=igmp-snooping+proxy)
   
   
   
   IGMP snooping proxy is enabled.
   
   IGMP snooping proxy includes the querier and uniform Report/Leave message transmission functions. The querier function enables the device to send IGMP Query messages on behalf of its upstream device, and the uniform Report/Leave message transmission function enables the device to send IGMP Report/Leave messages of downstream devices on behalf of the upstream device.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.