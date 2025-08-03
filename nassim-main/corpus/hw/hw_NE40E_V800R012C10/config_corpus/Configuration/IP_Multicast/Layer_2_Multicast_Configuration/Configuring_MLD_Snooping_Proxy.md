Configuring MLD Snooping Proxy
==============================

To conserve network bandwidth, you can configure MLD snooping proxy on the devices. Then the devices work as proxy devices between the upstream devices and downstream hosts and substitute for them to send MLD messages, maintain group memberships, and forward multicast messages based on the group member interface information. Before configuring MLD snooping proxy, familiarize yourself with the applicable environment, complete the pre-configuration tasks, and obtain the required data. This can help you complete the configuration task quickly and accurately.

#### Usage Scenario

Forwarding entries are set up based on MLD messages exchanged between a Layer 3 device and user hosts. If there are many user hosts, redundant MLD messages increase the workload of the Layer 3 device.

To address the problem, MLD snooping proxy is generally deployed on a Layer 2 device between a Layer 3 device and hosts, allowing the Layer 2 device to process multicast protocol messages.

MLD snooping proxy allows a Layer 2 device to act as a Layer 3 device to send Query messages. It also allows a Layer 2 device to act as user hosts to respond to MLD Query messages. For example, on the network shown in [Figure 1](#EN-US_TASK_0172367939__fig_dc_vrp_l2mc_cfg_008001), MLD snooping proxy is configured on a CE.

* Acting as a host, the CE collects, processes, and report Report and Done messages to the Layer 3 device. If a large number of users frequently join or leave multicast groups, the CE suppresses Report and Done messages, reducing message processing workload on the upstream Layer 3 device.
* Acting as the Layer 3 device (PE), the CE sends Query messages and establishes the mapping between group members and interfaces using the MLD snooping function.

Generally, configure querier function on upstream devices in Layer 2 network and enable collect and process Report and Done messages.

**Figure 1** Configuring MLD snooping proxy  
![](images/fig_dc_vrp_l2mc_cfg_008001.png)  

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In the preceding figure, the CE is a Layer 2 device on which MLD snooping proxy needs to be configured.



#### Pre-configuration Tasks

Before configuring the MLD snooping proxy, complete the following tasks:

* Configure a link layer protocol to ensure link connectivity between devices.
* Enable global MLD snooping.


[Configuring the Querier Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0081.html)

The querier function enables a device to send Query messages for its upstream device and respond to Multicast Listener Discovery (MLD) messages sent from downstream devices.

[Configuring Unified Transmission of Report/Done Messages](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0082.html)

Unified transmission of Report/Done messages enables a device to summarize Report/Done messages of downstream hosts and send them to an upstream device in a unified manner. This saves bandwidth resources on the network side.

[(Optional) Configuring Transparent Transmission of Protocol Messages](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0083.html)

To prevent MLD snooping proxy-enabled upstream and downstream devices from learning multicast forwarding entries from each other, configure them to transparently transmit protocol messages.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0084.html)

After configuring MLD snooping proxy, verify the configuration.