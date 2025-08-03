Configuring MLD On-demand
=========================

Multicast Listener Discovery (MLD) on-demand helps to maintain MLD group memberships and frees a multicast device and its connected access device from exchanging a large number of packets.

#### Usage Scenario

When a multicast device is directly connected to user hosts, the multicast device sends MLD Query messages to and receives MLD Report and Done messages from the user hosts to identify the multicast groups that have attached receivers on the shared network segment. The device directly connected to a multicast device, however, may not be a host but an MLD proxy-capable access device.

If a multicast device is directly connected to an MLD proxy-capable access device, enable MLD on-demand on the multicast device. The multicast device sends only one general query message to the access device. After receiving the general query message, the access device sends the collected Join and Leave status of multicast groups to the multicast device. The multicast device uses the Join and Leave status of the multicast groups to maintain multicast group memberships on the local network segment.

MLD on-demand reduces packet exchanges between a multicast device and its connected access device and reduces the loads of these devices.


#### Pre-configuration Tasks

Before configuring MLD on-demand, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* Enable multicast routing.
* [Configure basic MLD functions](dc_vrp_multicast_cfg_2073.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**mld on-demand**](cmdqueryname=mld+on-demand)
   
   
   
   The MLD group that an interface dynamically joins is configured not to time out.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

Run the [**display mld interface**](cmdqueryname=display+mld+interface) command to check MLD on-demand configurations on an interface.