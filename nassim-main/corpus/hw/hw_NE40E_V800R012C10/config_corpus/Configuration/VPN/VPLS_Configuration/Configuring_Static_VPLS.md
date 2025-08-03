Configuring Static VPLS
=======================

Static VPLS is implemented using manually configured Layer 2 VC information.

#### Usage Scenario

If devices are unable to support large numbers of LDP sessions or you want to manually manage and allocate VC labels, configure static VPLS. VPLS PWs created using manually configured VC labels do not require the transmission of Layer 2 VC or link information using LDP.


#### Pre-configuration Tasks

Before configuring static VPLS, complete the following tasks:

* Configure IP addresses and IGP routes on PEs and Ps.
* Configure LSR IDs and enable MPLS and MPLS LDP on PEs and Ps.
* Enable MPLS L2VPN on PEs.
* Establish tunnels between PEs to transmit service data.


[Creating a VSI and Configuring PWs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6002.html)

Static VPLS allows you to manually manage and allocate VC labels.

[Binding a VSI to an AC Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5005-01.html)

The view in which an AC interface is bound to a VSI depends on the type of link between the PE and CE.

[(Optional) Configuring a VSI to Ignore the AC Status](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5006-02.html)

If the services running on a legacy network need to switch to a new network, you can configure VSIs to ignore AC status.

[(Optional) Configuring VSI PW-based Traffic Suppression](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5007.html)

You can configure VSI PW-based suppression of broadcast packets, multicast packets, and unknown unicast packets.

[(Optional) Disabling the PW Source Interface Check Function](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_vpls_cfg_5011.html)

On a VPLS/VPWS network, the PW source interface check function is enabled by default, affecting system performance.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6003.html)

After configuring static VPLS, check its VSI, AC interface, and label stack information.