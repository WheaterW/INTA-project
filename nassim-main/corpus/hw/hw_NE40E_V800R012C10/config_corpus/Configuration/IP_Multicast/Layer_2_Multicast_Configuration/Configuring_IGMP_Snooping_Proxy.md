Configuring IGMP Snooping Proxy
===============================

IGMP snooping proxy enables a device to represent its upstream device and downstream hosts to send IGMP messages to maintain group memberships and use the group memberships to forward multicast traffic, which greatly reduces bandwidth consumption. Before configuring the IGMP Snooping Proxy, familiarize yourself with the usage scenario, complete the pre-configuration tasks, and obtain the data required for the configuration.

#### Usage Scenario

Forwarding entries are set up according to IGMP messages exchanged between a Layer 3 device and user hosts. If there are many user hosts, redundant IGMP messages increase the workload of the PE.

IGMP Snooping Proxy can be deployed on a Layer 2 device between the Layer 3 device and user hosts to address this problem.

On the network shown in [Figure 1](#EN-US_CONCEPT_0172367862__fig_dc_vrp_l2mc_cfg_002101), IGMP Snooping Proxy is configured on the CE. The IGMP Snooping Proxy-capable CE has the following functions:

* Acting as an attached host of the Layer 3 device, the CE collects and processes Report/Leave messages received from hosts before sending them to the Layer 3 device. If a large number of users frequently join or leave multicast groups, the CE suppresses Report and Leave messages, reducing message processing workload for the upstream device.
* Acting as a Layer 3 device directly connected to hosts, the CE sends Query messages and establishes the mapping between group members and interfaces.

Uniform Report/Leave message transmission is typically configured on a Layer 2 device, and the querier function is typically configured on the upstream device of the Layer 2 device.

**Figure 1** IGMP Snooping Proxy  
![](images/fig_dc_vrp_l2mc_cfg_002101.png)  

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The CE in the figure needs to be deployed with IGMP Snooping Proxy.



#### Pre-configuration Tasks

Before configuring IGMP Snooping Proxy, complete the following tasks:

* Configure a link layer protocol to ensure link connectivity between devices.
* Enable global IGMP snooping.

#### Data Preparation

To configure an IGMP Snooping Proxy, you need the following data.

| No. | Data |
| --- | --- |
| 1 | (Optional) Querier parameters, including the interval at which general Query messages are sent, the number of times a group-specific query message is set, the maximum response time, and the interval at which group-specific query messages are sent |



[Configuring the Querier Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0023.html)

The querier function enables a device to send Query messages for its upstream device and respond to Join/Leave messages sent from downstream devices.

[Configuring Uniform Report/Leave Message Transmission](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0024.html)

Configuring a uniform Report/Leave message transmission on a Layer 2 device reduces network bandwidth consumption.

[(Optional) Configuring Transparent Transmission of Protocol Messages](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0025.html)

To prevent IGMP snooping proxy-enabled upstream and downstream devices from learning multicast forwarding entries from each other, configure them to transparently transmit protocol messages.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0026.html)

After configuring IGMP snooping proxy, you can verify its configurations.