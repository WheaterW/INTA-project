Configuring Layer 2 Multicast Instances
=======================================

If users in different VLANs or VSIs request for the same multicast group's data from the same source, configure a Layer 2 multicast instance on the Layer 2 device.

#### Context

In conventional multicast on-demand mode, if users of a Layer 2 multicast device in different VLANs or VSIs request for the same multicast group's data from the same source, the connected upstream Layer 3 device has to send a copy of each multicast flow of this group for each VLAN or VSI. Such implementation wastes bandwidth resources and burdens the upstream device.

To resolve these issues, configure a Layer 2 multicast instance on the Layer 2 multicast device. Then, the Layer 2 device requests for only one copy of the group's flow for all such users from the connected Layer 3 device.

With a Layer 2 multicast instance configured:

* Multicast data can be replicated on a VPLS network and be replicated from a VPLS network to a VLAN.
* Channels that consist of multiple multicast groups can be specified for the Layer 2 multicast instance, facilitating the management of replicated multicast data flows.

For example, on the network shown in [Figure 1](#EN-US_TASK_0172367912__fig_dc_vrp_l2mc_cfg_006601), users in VLAN 11 and VLAN 22 request for data of the same multicast group from the same source. In this scenario, create a VLAN (for example, VLAN 3) and configure the VLAN as a multicast VLAN on the CE. Associate VLAN 3 with VLAN 11 and VLAN 22. Then, the CE requests for only a single copy of the data flow from the PE, and replicates separate copies for VLAN 11 and VLAN 22.

**Figure 1** Multicast replication before and after a Layer 2 multicast instance is configured  
![](images/fig_dc_vrp_l2mc_cfg_006601.png)  

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The CE in the figure represents a Layer 2 device on which Layer 2 multicast replication needs to be deployed.




[Configuring Layer 2 Multicast Instances for VLAN or VSI Users](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0067.html)

If users in different VLANs or VSIs request for the same group's data from the same source, configure a Layer 2 multicast instance on a device, allowing the device to request for only one copy of each multicast data flow for such users from the upstream device.

[Verifying the Layer 2 Multicast Instance Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0068.html)

After configuring a Layer 2 multicast instance, verify the configuration.