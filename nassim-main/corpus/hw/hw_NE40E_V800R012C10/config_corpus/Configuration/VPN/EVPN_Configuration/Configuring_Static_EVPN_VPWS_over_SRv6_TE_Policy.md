Configuring Static EVPN VPWS over SRv6 TE Policy
================================================

This section describes how to configure static EVPN VPWS over SRv6 TE Policy, so that static EVPN VPWS services can be carried over more flexible SRv6 TE Policies.

#### Usage Scenario

Static EVPN VPWS over SRv6 TE Policy uses public network SRv6 TE Policies to carry EVPN VPWS services. As shown in [Figure 1](dc_vrp_cfg_evpn-vpws_over_srv6-te_policy.html#EN-US_TASK_0179342422__fig1138145962319), PE1 and PE2 communicate through an IPv6 public network. Deploy an SRv6 TE Policy on the network and then perform this task, so that EVPN VPWS services can be carried over the SRv6 TE Policy.

**Figure 1** Configuring static EVPN VPWS over SRv6 TE Policy  
![](figure/en-us_image_0000001321505433.png)
#### Pre-configuration Tasks

Before configuring static EVPN VPWS over SRv6 TE Policy, complete the following task:

* [Configure an SRv6 TE Policy manually](dc_vrp_srv6_cfg_all_0110.html) or [use a controller to dynamically deliver an SRv6 TE Policy](dc_vrp_srv6_cfg_all_0116.html).
  
  + Apply a tunnel policy to the EVPN instance that works in EVPN VPWS mode when configuring traffic steering in the preceding task.
  + Run the **opcode** command to configure a static SID when configuring an SRv6 SID in the preceding task.


[Configuring EVPN Source Addresses](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0261.html)

An EVPN source address uniquely identifies a PE in EVPN networking.

[Configuring EVPN Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0241.html)

EVPN VPWS is deployed based on the EVPN service architecture. Before configuring EVPN VPWS over SRv6 TE Policy, you need to configure EVPN functions.

[Configuring a Static EVPL Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0243.html)

This section describes how to configure a static EVPL instance.

[Configuring AC Interfaces](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0244.html)

In an EVPN VPWS scenario, you can configure Layer 2 sub-interfaces to function as AC interfaces and configure traffic encapsulation on these Layer 2 sub-interfaces, so that they can transmit different types of data packets.

[Configuring Route Recursion to SRv6 TE Policies](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0264.html)

EVPN VPWS is deployed based on the EVPN service architecture. Before configuring EVPN VPWS over SRv6 BE, you need to configure EVPN functions.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0259.html)

After configuring static EVPN VPWS over SRv6 TE Policy, verify EVPL instance information.