Configuring Static EVPN VPWS over SRv6 BE
=========================================

This section describes how to configure static EVPN VPWS over SRv6 BE.

#### Usage Scenario

Static EVPN VPWS over SRv6 BE uses SRv6 BE on a public network to carry EVPN services. As shown in [Figure 1](#EN-US_TASK_0000001268938572__fig_dc_vrp_evpn_cfg_110001), PE1 and PE2 communicate through an IPv6 public network. SRv6 BE is deployed on the IPv6 public network to carry Layer 2 EVPN services.

**Figure 1** Static EVPN VPWS over SRv6 BE networking  
![](figure/en-us_image_0000001270705636.png)
#### Pre-configuration Tasks

Before configuring static EVPN VPWS over SRv6 BE, complete the following tasks:

* Configure a link layer protocol.
* Configure IP addresses for interfaces to ensure IP reachability between neighboring devices.
* Configure IPv6 IS-IS on the PEs and P. For detailed configurations, see [Configuring Basic IS-IS Functions (IPv6)](dc_vrp_isis_cfg_1023.html).


[Configuring SRv6 BE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0265.html)

A PE's global redundancy mode determines whether the PE can work with other PEs in load-balancing mode.

[Configuring EVPN Source Addresses](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0260.html)

An EVPN source address uniquely identifies a PE in EVPN networking.

[Configuring EVPN Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0231.html)

EVPN VPWS is deployed based on the EVPN service architecture. Before configuring EVPN VPWS over SRv6 BE, you need to configure EVPN functions.

[Configuring a Static EVPL Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0233.html)

This section describes how to configure a static EVPL instance.

[Configuring AC Interfaces](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0234.html)

In an EVPN VPWS scenario, you can configure Layer 2 sub-interfaces to function as AC interfaces and configure traffic encapsulation on these Layer 2 sub-interfaces, so that they can transmit different types of data packets.

[Configuring Route Recursion to SRv6 BE Paths](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0262.html)

This section describes how to configure EVPN routes on PEs to carry SIDs and recurse to SRv6 BE paths based on SIDs.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0239.html)

After configuring static EVPN VPWS over SRv6 BE, verify EVPL instance information.