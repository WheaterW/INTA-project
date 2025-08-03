Configuring Static Layer 2 Multicast
====================================

If a user host needs to receive multicast data for a specific multicast group from a router port over a long period of time, static Layer 2 multicast can be used to ensure a stable multicast data transmission. Before configuring static Layer 2 multicast, familiarize yourself with the usage scenario and complete the pre-configuration tasks.

#### Usage Scenario

Layer 2 multicast can be implemented in either dynamic or static mode. In dynamic mode, multicast forwarding tables are dynamically generated based on multicast protocols, whereas in static mode, multicast forwarding tables are manually configured and multicast entries are statically bound to interfaces. After static Layer 2 multicast is deployed on a device, multicast entries on the device do not age and users attached to the device can regularly receive multicast data for specific multicast groups, while avoiding network attacks.

On the network shown in [Figure 1](#EN-US_CONCEPT_0172367850__fig_dc_vrp_l2mc_cfg_001001), static router ports and static member ports are components of the static Layer 2 multicast configuration.

* Static router ports (blue circles) receive multicast traffic.
* Static member ports (yellow squares) send data for specific multicast groups.

**Figure 1** Static Layer 2 multicast  
![](images/fig_dc_vrp_l2mc_cfg_001001.png)  


#### Pre-configuration Tasks

Before configuring static Layer 2 multicast, complete the following tasks:

* Configure a link layer protocol to ensure link connectivity between devices.
* Enable global IGMP snooping.


[Configuring Static Router Ports](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0012.html)

Static router ports can be configured to enable users to regularly receive multicast data packets because static router ports do not age.

[Configuring Static Member Ports](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0013.html)

Static member ports send data for specific multicast groups.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0015.html)

After configuring static Layer 2 multicast, verify the port information table and Layer 2 multicast forwarding table to verify that the static Layer 2 multicast configurations are complete.