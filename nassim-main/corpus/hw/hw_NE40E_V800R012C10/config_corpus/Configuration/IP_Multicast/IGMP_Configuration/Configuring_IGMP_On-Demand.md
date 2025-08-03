Configuring IGMP On-Demand
==========================

Internet Group Management Protocol (IGMP) on-demand helps to maintain IGMP group memberships and frees a multicast device and its connected access device from exchanging a large number of packets.

#### Usage Scenario

When a multicast device is directly connected to user hosts, the multicast device sends IGMP Query messages to and receives IGMP Report and Leave messages from the user hosts to identify the multicast groups that have attached receivers on the shared network segment. The device directly connected to a multicast device, however, may not be a host but an IGMP proxy-capable access device, as shown in [Figure 1](#EN-US_TASK_0172366733__fig_dc_vrp_multicast_cfg_220301).**Figure 1** IGMP on-demand  
![](images/fig_dc_vrp_multicast_cfg_220301.png)

The provider edge (PE) is a multicast device, and the customer edge (CE) is an access device.

* On the network segment a shown in [Figure 1](#EN-US_TASK_0172366733__fig_dc_vrp_multicast_cfg_220301), if IGMP on-demand is not enabled on the PE, the PE sends a large number of IGMP Query messages to the CE, and the CE sends a large number of Report and Leave messages to the PE. As a result, lots of PE and CE resources are consumed.
* On the network segment b shown in [Figure 1](#EN-US_TASK_0172366733__fig_dc_vrp_multicast_cfg_220301), after IGMP on-demand is enabled on the PE, the PE sends only one general query message to the CE. After receiving the general query message from the PE, the CE sends the collected Join and Leave status of IGMP groups to the PE. The CE sends a Report or Leave message for a group to the PE only when the Join or Leave status of the group changes. To be specific, the CE sends an IGMP Report message for a multicast group to the PE only when the first user joins the multicast group and sends a Leave message only when the last user leaves the multicast group.

![](../../../../public_sys-resources/note_3.0-en-us.png) IGMP on-demand applies only to IGMPv2 and IGMPv3. After you enable IGMP on-demand on a multicast device connected to an IGMP proxy-capable access device, the multicast device implements IGMP in a different way as it implements standard IGMP in the following aspects:

* The multicast device interface connected to the access device sends only one IGMP general query message to the access device.
* The records about dynamically joined IGMP groups on the multicast device interface connected to the access device do not time out.
* The multicast device interface connected to the access device directly deletes the entry for a group only after the multicast device interface receives an IGMP Leave message for the group.



#### Pre-configuration Tasks

Before configuring IGMP on-demand, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* [Configure basic IGMP functions](dc_vrp_multicast_cfg_2044.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**igmp on-demand**](cmdqueryname=igmp+on-demand)
   
   
   
   The IGMP group that an interface dynamically joins is configured not to time out.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

Run the [**display igmp interface**](cmdqueryname=display+igmp+interface) command to check IGMP on-demand configurations on an interface.