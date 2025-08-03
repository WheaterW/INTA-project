Configuring MPAC
================

Management Plane Access Control (MPAC) policies can be
applied to sub-interfaces, to interfaces, or globally to filter packets
destined for the CPU.

#### Usage Scenario

MPAC can be configured to
filter packets destined for the CPU, thereby helping protect network
devices against Denial of Service (DoS) attacks.


#### Pre-configuration Tasks

Before configuring
MPAC, configure link layer protocol parameters and IP addresses for
interfaces to ensure that the link layer protocol on the interfaces
is in the Up state.


[Configuring an IPv4 MPAC Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpac_cfg_0005.html)

An IPv4 Management Plane Access Control (MPAC) policy can be configured to filter IPv4 packets destined for the CPU.

[Configuring an IPv6 MPAC Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpac_cfg_0006.html)

An IPv6 management plane access control (MPAC) policy can be configured to determine the IPv6 packets that can be sent to the CPU.

[Verifying the MPAC Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpac_cfg_0007.html)

After configuring the Management Plane Access Control (MPAC) policy, check the configurations.