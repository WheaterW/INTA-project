Configuring an LDP LSP
======================

LDP is a label distribution protocol used to establish LSPs in an MPLS domain.

#### Usage Scenario

LDP can dynamically establish an LSP. An LDP LSP provided that LDP nodes do not need to be specified and traffic engineering (TE) does not need to be deployed on the MPLS network.

The maximum number of LSPs varies with the capacity and performance of a device. If too many LSPs are configured on a device, the device may operate unstably.

An LSP can be established only when eligible routes exist on LSRs and match the LSP setup policy. LDP can only use routes that match a specified policy to set up LSPs, which helps control the number of LSPs.

The NE40E provides the following policies for controlling the number of LSPs:

* Policies for establishing ingress or egress LSPs are as follows:
  
  + LDP uses all IGP routes to establish LSPs
  + LDP uses host routes to establish LSPs.
  + LDP uses an IP prefix list to establish LSPs.
  + LDP does not establish LSPs.
* To control the number of transit LSPs on a transit LSR, an IP prefix list can be used to filter routes, and only the routes matching the filtering policy can be used to establish transit LSPs.

To correctly select a path maximum transmission unit (MTU), an LSR must obtain the MTU of each link connected to it using LDP MTU signaling.


#### Pre-configuration Tasks

Before configuring an LDP LSP, [configure a local LDP session](dc_vrp_ldp-p2p_cfg_0003.html).


#### Configuration Procedures

**Figure 1** LDP LSP configuration
  
![](images/fig_dc_vrp_ldp-p2p_cfg_001503.png "Click to enlarge")


[Establishing an LDP LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0016.html)

An LDP LSP can be automatically established only after an LDP session is established.

[(Optional) Configuring PHP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0017.html)

The penultimate hop popping (PHP) function can be enabled after you configure the label to be assigned by the egress to the penultimate hop.

[(Optional) Configuring an LDP Label Advertisement Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0072.html)

An LDP label advertisement mode can be configured to control LSP establishment.

[(Optional) Configuring a Global LDP Label Distribution Control Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0081.html)

An LDP label distribution control mode can be globally configured to enable a local node to control the sequence of distributing labels to upstream nodes.

[(Optional) Configuring LDP to Automatically Trigger Requests in DoD Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0200.html)

A remote LDP session must be configured before LDP is configured to automatically send requests in downstream-on-demand (DoD) mode

[(Optional) Configuring an MPLS MTU for an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0018.html)

If an MPLS MTU needs to be configured for an interface, the related configuration needs to be performed on all nodes.

[(Optional) Configuring LDP MTU Signaling](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0019.html)

LDP MTU signaling can be configured to allow sent Label Mapping messages to carry MTU TLVs.

[(Optional) Configuring an LDP Split Horizon Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0036.html)

An LDP split horizon policy can be configured to prevent an LSR from distributing labels to a specified downstream LDP peer.

[(Optional) Configuring an LDP Inbound Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_2049.html)

An LDP inbound policy can be configured to prevent the establishment of unwanted LSPs, reducing memory consumption.

[(Optional) Configuring an LDP Outbound Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0047.html)

Configuring an LDP outbound policy helps prevent an LSR from establishing unwanted LSPs, saving memory resources.

[(Optional) Configuring a Policy of Triggering LSP Establishment Using IGP Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0020.html)

A policy can be configured to allow LDP to use eligible static and IGP routes to trigger LSP establishment.

[(Optional) Configuring a Policy of Triggering LSP Establishment Using Labeled BGP Routes of the Public Network](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_00210.html)

A policy can be configured to allow LDP to use eligible labeled BGP routes of the public network to trigger LSP establishment.

[(Optional) Configuring a Policy for Triggering Transit LSP Establishment](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0021.html)

A policy for triggering the establishment of transit LSPs can be configured to enable LDP to use routes that meet the specified policy to establish transit LSPs.

[(Optional) Disabling LDP LSP Flapping Suppression](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0190.html)

LDP LSP flapping suppression helps effectively prevent label flapping. This function can be disabled.

[(Optional) Disabling a Device from Forwarding Unknown TLVs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0191.html)

A local device can be disabled from forwarding unknown TLVs to peers.

[(Optional) Configuring the Policy for Triggering Interworking Between LDP LSPs and SR LSPs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0088.html)

Configure the policy for triggering interworking between LDP LSPs and SR LSPs, allowing SR LSPs to interwork with proxy egress LSPs and transit LSPs that are established over non-local host routes with a 32-bit mask.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0022.html)

After configuring LDP LSPs, you can view information about LDP configurations, LDP LSPs, and LSPs.