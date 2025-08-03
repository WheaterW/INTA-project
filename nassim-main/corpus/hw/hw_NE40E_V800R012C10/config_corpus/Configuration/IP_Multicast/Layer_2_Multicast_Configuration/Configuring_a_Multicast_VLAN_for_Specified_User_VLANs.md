Configuring a Multicast VLAN for Specified User VLANs
=====================================================

To enable a Device to request only one copy of multicast data from an upstream device and replicate a separate copy for each user VLAN that is interested in the data, create and associate a multicast VLAN with the user VLANs.

#### Usage Scenario

In traditional multicast on demand mode, if users in different VLANs are interested in data from the same multicast source, a device connected to these user VLANs requests a separate copy of data from an upstream Layer 3 device for each user VLAN, which consumes bandwidth resources and increases the upstream device's workload.

To resolve this issue, create and associate a multicast VLAN with the user VLANs. After these configurations are complete, the downstream device uses the multicast VLAN to request only one copy of data from the upstream device and then replicates a separate copy for each user VLAN.

For example, on the network shown in [Figure 1](#EN-US_TASK_0172367870__fig_dc_vrp_l2mc_cfg_003901), users in VLAN 11 and VLAN 22 request data from the same multicast source. In this scenario, create VLAN 3 and configure it as a multicast VLAN on the CE. Associate VLAN 3 with VLAN 11 and VLAN 22. Then, the CE requests only one copy of data from the PE and replicates a separate copy for VLAN 11 and VLAN 22.

**Figure 1** Associating a multicast VLAN with specified user VLANs  
![](images/fig_dc_vrp_l2mc_cfg_003901.png)  



#### Pre-configuration Tasks

Before associating a multicast VLAN with specified user VLANs, complete the following tasks:

* Check that all link layer protocols are Up.
* Enable Internet Group Management Protocol (IGMP) snooping globally.


[Associating a Multicast VLAN with Specified User VLANs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0040.html)

If users in different VLANs need to receive the same multicast data flow, you can configure a multicast VLAN to manage the multicast source and multicast group members and save bandwidth.

[Adding Interfaces to VLANs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0041.html)

After associating a multicast VLAN with specified user VLANs, add a network-side interface to the multicast VLAN and add user-side interfaces to the user VLANs.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0042.html)

After associating a multicast VLAN with specified user VLANs, verify the configuration.