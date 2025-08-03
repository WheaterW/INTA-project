Configuring IGMP Snooping
=========================

IGMP snooping enables a Layer 2 device to analyze IGMP messages exchanged between a connected Layer 3 device and downstream user hosts and use these IGMP messages to set up mappings between interfaces and multicast MAC addresses. Based on the mappings, the Layer 2 device can then implement on-demand multicast data forwarding at the data link layer.

#### Usage Scenario

If IGMP snooping is not configured on any Layer 2 device, multicast data will be broadcast, wasting bandwidth resources. After IGMP snooping is configured on relevant Layer 2 devices, multicast data will be forwarded only to these Layer 2 devices.

**Figure 1** Multicast packet transmission before and after IGMP snooping is configured on a Layer 2 device  
![](images/fig_dc_vrp_l2mc_cfg_000101.png)  

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The CEs in this figure need to be deployed with IGMP Snooping.

On the network shown in [Figure 1](#EN-US_CONCEPT_0172367835__fig_dc_vrp_l2mc_cfg_000101), after IGMP snooping is configured on the CE, multicast data will be sent only to user hosts that request it, instead of being broadcast.


#### Pre-configuration Tasks

* Configure basic VLAN/VPLS functions.

#### Data Preparation

To configure IGMP snooping, you need the following data.

| No. | Data |
| --- | --- |
| 1 | VLAN ID or VSI name (required by IGMP snooping) |
| 2 | (Optional) Aging time of a router port |
| 3 | (Optional) Dynamic aging time of member entries, addresses of the multicast group and multicast source for prompt Join, and the range of multicast groups that member ports can promptly leave |
| 4 | (Optional) Aging time of entries triggered by multicast traffic |
| 5 | (Optional) Range and number of multicast groups to be limited |
| 6 | (Optional) Configuring Rapid Multicast Data Forwarding on a Backup Device |



[Configuring Basic IGMP Snooping Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0003.html)

Configuring basic IGMP snooping functions is the prerequisite for implementing Layer 2 multicast. Configuring basic IGMP snooping functions involves enabling IGMP snooping, setting the version for IGMP messages that can be processed by IGMP snooping, and setting the IGMP snooping forwarding mode.

[(Optional) Setting the Aging Time for Router Ports](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0004.html)

The aging time of router ports can be set based on the network stability to balance the update of multicast entries and network changes.

[(Optional) Configuring Rapid Group Member Information Update](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0005.html)

Rapid group member information update can be configured to enable devices to quickly update Layer 2 multicast entries generated based on Report/Leave messages received from group members, improving the multicast data forwarding efficiency.

[(Optional) Configuring Prompt Response to Layer 2 Network Topology Changes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0006.html)

Prompt response to Layer 2 network topology changes enables a device to correctly forward multicast data based on the new network topology, ensuring uninterrupted service forwarding.

[(Optional) Setting the Aging Time for Entries Triggered by Multicast Traffic](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0007.html)

Setting the aging time for Layer 2 multicast forwarding entries triggered by multicast traffic can balance the forwarding efficiency and system performance.

[(Optional) Configuring a Multicast Group Security Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0008.html)

A multicast group policy can be configured to limit the range and number of multicast groups that some hosts can join or to add security messages to multicast data packets.

[(Optional) Configuring Rapid Multicast Data Forwarding on a Backup Device](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0064.html)

In a VPLS network, you can configure a backup device to quickly switch and forward multicast data traffic in the event of a master link or device failure.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0009.html)

After configuring IGMP snooping, verify the router port and member port lists, forwarding table, and querier parameters.