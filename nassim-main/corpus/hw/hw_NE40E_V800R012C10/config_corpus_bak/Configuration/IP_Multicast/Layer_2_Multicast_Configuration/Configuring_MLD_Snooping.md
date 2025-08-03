Configuring MLD Snooping
========================

Multicast Listener Discovery (MLD) snooping enables a Layer 2 device to listen to and analyze MLD messages exchanged between a connected Layer 3 device and downstream user hosts. The Layer 2 device then uses the message information to set up multicast forwarding entries to implement on-demand multicast data forwarding at the data link layer.

#### Usage Scenario

On an IPv6 multicast network, after an upstream device sends the service flow of a multicast program, a Layer 2 device (switch) at the edge of the access layer forwards the flow to multicast users. The users can then enjoy the multicast program service. As shown in [Figure 1](#EN-US_TASK_0172367917__fig_dc_vrp_l2mc_cfg_007101), multicast data messages are broadcast at the data link layer by default, causing bandwidth waste.

To resolve this issue, configure MLD snooping on the Layer 2 device (switch), allowing this device to listen to the MLD messages exchanged between the upstream device and downstream hosts. The Layer 2 device can then analyze the messages and generate Layer 2 multicast forwarding entries based on the message information to implement on-demand multicast data forwarding at the link layer.

**Figure 1** Multicast message transmission before and after MLD snooping is configured on a Layer 2 device  
![](images/fig_dc_vrp_l2mc_cfg_007101.png)  

On the network shown in [Figure 1](#EN-US_TASK_0172367917__fig_dc_vrp_l2mc_cfg_007101), Receiver A and Receiver B request the service of a multicast group, but Receiver C does not. Before MLD snooping is configured, the Layer 2 device broadcasts the multicast data at the data link layer, and all the receivers can receive the data. After MLD snooping is configured, the Layer 2 device sends the multicast data only to Receiver A and Receiver B who request the data. Therefore, Receiver C does not receive the data of the multicast group.


#### Pre-configuration Tasks

* Configure basic VLAN and VPLS functions.

#### Data Preparation

To configure MLD snooping, you need the following data.

| No. | Data |
| --- | --- |
| 1 | VLAN ID or VSI name (required by MLD snooping) |
| 2 | (Optional) Router interface aging time |
| 3 | (Optional) Dynamic aging time of member entries, addresses of the multicast group and multicast source for prompt Join, and the range of multicast groups that member ports can promptly leave |
| 4 | (Optional) Range and number of multicast groups to be limited |
| 5 | (Optional) Aging time of entries triggered by multicast traffic |



[Configuring Basic MLD Snooping Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0072.html)

Configuring basic MLD snooping functions involves enabling MLD snooping and setting the MLD version. Those basic functions need to be configured before you configure other MLD snooping functions.

[(Optional) Setting the Aging Time for Router Ports](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0073.html)

The aging time of router ports can be set based on the network stability to balance the update of multicast entries and network changes.

[(Optional) Configuring Static Ports](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0074.html)

On a network with a stable topology, you can configure static ports, including static router ports and static multicast group member ports.

[(Optional) Configuring Rapid Group Member Information Update](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0075.html)

Rapid group member information update can be configured to enable devices to quickly update Layer 2 multicast entries generated based on Report/Done messages received from group members, improving the multicast data forwarding efficiency.

[(Optional) Setting the Aging Time for Entries Triggered by Multicast Traffic](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0076.html)

Setting the aging time for Layer 2 multicast forwarding entries triggered by multicast traffic can balance the forwarding efficiency and system performance.

[(Optional) Configuring MLD Snooping Policies](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0077.html)

To improve service security, configure MLD snooping policies on a Layer 2 multicast device to filter multicast messages or restrict the multicast group range that hosts can join.

[(Optional) Configuring Prompt Response to Layer 2 Network Topology Changes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0078.html)

Prompt response to Layer 2 network topology changes enables a device to correctly forward multicast data based on the new network topology, ensuring uninterrupted service forwarding.

[(Optional) Configuring the System to Retain the Tag Carried in an MLD Report Message](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_protocol-packet_encapsulation.html)

When an L2VPN accesses an L3VPN, you can configure the system to retain the tag carried in an MLD Report message so that the message can be normally processed when being forwarded from an L2VE sub-interface to an L3VE QinQ VLAN tag termination sub-interface.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0079.html)

After MLD snooping is configured, you can view the router port and member port lists, forwarding table, and querier parameters.