Configuring Layer 2 Multicast CAC
=================================

Layer 2 multicast Call Admission Control (CAC) is a feature used on a VPLS networking to limit the multicast group number and bandwidth that subscribers can utilize and manage the channels of each service provider. This feature prevents bandwidth resources from exceeding the total bandwidth of the aggregation network and ensures service quality for most subscribers.

#### Usage Scenario

As IPTV service applications become increasingly popular among consumers, multicast services are widely deployed. The following problems may arise when IPTV services are deployed on a Layer 2 network:

* Sparsely distributed multicast groups (programs) may increase network deployment burdens.
* If network bandwidth is insufficient, the aggregation network cannot bear all multicast traffic, which degrades subscribers' image experience.
* Static multicast group management policies cannot meet the requirements of users to access different multicast services. Service providers expect more refined channel management, for example, they expect to limit the bandwidth of multicast groups in channels.

To solve the preceding problems, Layer 2 multicast CAC can be used to control IPTV services on the aggregation network based on different criteria, including global multicast group number and bandwidth limits, and multicast group number and bandwidth limits for a channel. Layer 2 multicast CAC enables service providers to offer more flexible and refined contents and subscriber-specific policies to ensure service quality for most subscribers.

On the network shown in [Figure 1](#EN-US_TASK_0172367900__fig_dc_vrp_l2mc_cfg_05901), a UPE is downlinked to CEs through a VLAN or VPLS network. Layer 2 multicast CAC can be deployed on the UPE to limit the multicast bandwidth for IPTV channels delivered by the UPE to CEs.

**Figure 1** Layer 2 multicast CAC networking  
![](images/fig_dc_vrp_l2mc_cfg_05901.png)

#### Pre-configuration Tasks

Before configuring Layer 2 multicast CAC, complete the following tasks:

* Connect and configure interfaces correctly to ensure that the link layer protocol status of the interfaces is Up.
* Complete basic VSI configurations.
* Enable IGMP snooping on the device where multicast CAC is to be enabled and for the VSI where the device resides.


[Configuring Global Layer 2 Multicast CAC](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_060.html)

Global Layer 2 multicast CAC configurations are performed to limit the global multicast bandwidth.

[Configuring Layer 2 Multicast CAC in a VSI Scenario](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_061.html)

Layer 2 multicast CAC configurations are performed in a VSI scenario to limit the multicast group number and bandwidth.

[Verifying the Layer 2 Multicast CAC Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_062.html)

After configuring Layer 2 multicast CAC, verify the configuration, including Layer 2 multicast entry and bandwidth limits of global and VSI channels.