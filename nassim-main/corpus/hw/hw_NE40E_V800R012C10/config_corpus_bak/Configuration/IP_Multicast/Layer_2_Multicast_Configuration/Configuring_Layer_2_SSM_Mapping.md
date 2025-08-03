Configuring Layer 2 SSM Mapping
===============================

After Source-Specific Multicast (SSM) mapping is configured on a device directly connected to hosts running IGMPv1 or IGMPv2 on a Layer 2 network, these hosts can use IGMPv3 services. Before configuring Layer 2 SSM mapping, familiarize yourself with the usage scenario, complete the pre-configuration tasks, and obtain the data required for the configuration.

#### Usage Scenario

Compared with ASM, SSM conserves multicast addresses and is more secure. Only IGMPv3 supports SSM. Currently, most devices support IGMPv3. Most old multicast terminals support only IGMPv1 or IGMPv2 but require IGMPv3 multicast services. The SSM mapping mechanism enables devices running IGMPv3 to provide SSM services for hosts running IGMPv1 or IGMPv2.

SSM mapping can be used to convert IGMPv1 or IGMPv2 (\*, G) messages, within an SSM group address range, to IGMPv3 (S, G) messages. This allows hosts running IGMPv1 or IGMPv2 to obtain SSM services.


#### Pre-configuration Tasks

Before configuring Layer 2 SSM mapping, complete the following task:

* Enable global IGMP snooping.

#### Data Preparation

To configure Layer 2 SSM mapping, you need the following data.

| No. | Data |
| --- | --- |
| 1 | (Optional) ACL rule used to define an SSM group address range, and VSI name or VLAN ID |
| 2 | Multicast group and source addresses between which a mapping is set up and IGMP snooping version |



[(Optional) Configuring an SSM Group Address Range](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0018.html)

After a multicast group is configured within a Source-Specific Multicast (SSM) group address range, user hosts that join the group can use SSM services.

[Configuring SSM Mapping](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0019.html)

To provide SSM services for old-fashioned multicast terminals that support only IGMPv1 or IGMPv2, configure SSM mapping on the terminals. The SSM mapping mechanism is used to convert IGMPv1 and IGMPv2 Report messages into messages with (S, G) information. It allows hosts that do not support IGMPv3 to enjoy SSM services. SSM mapping allows the mapping to be established between a multicast group and a multicast source.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2mc_cfg_0020.html)

After configuring Layer 2 SSM mapping, verify mappings between multicast group addresses and multicast source addresses to verify that the Layer 2 SSM mapping configurations are complete.