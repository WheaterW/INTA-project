Configuring Inter-AS VPWS
=========================

Inter-AS VPWS allows a VPWS network to span multiple ASs on the MPLS backbone network.

#### Usage Scenario

If multiple ASs exist on an MPLS backbone network, the VPWS network carried over the MPLS backbone network must be an inter-AS VPWS network.

Currently, the following inter-AS VPWS solutions are available:

* Inter-AS VPWS Option A: This solution can be easily deployed and is recommended for scenarios where few inter-AS VPWS PWs are required.
* Inter-AS VPWS Option C: ASBRs do not need to create or maintain PWs and, as a result, are not a significant factor in network expansion. This solution is recommended for scenarios where large numbers of inter-AS VPWS PWs are required.

#### Pre-configuration tasks

Before configuring inter-AS VPWS, complete the following tasks:

* Configure an IGP for each AS on the MPLS backbone network to ensure IP connectivity within the same AS.
* Configure basic MPLS functions for each AS on the MPLS backbone network.
* Configure MPLS LDP and establish LDP LSPs for each AS.
* Establish an IBGP peer relationship between the PE and ASBR in the same AS and an EBGP peer relationship between ASBRs in different ASs. This task is specific to inter-AS LDP VPWS Option C.


[Configuring Inter-AS LDP VPWS Option A](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6043.html)

Inter-AS LDP VPWS Option A applies to scenarios where few inter-AS PWs are required. Compared with L3VPN, inter-AS LDP VPWS Option A consumes more resources and requires more configuration workload.

[Configuring Inter-AS LDP VPWS Option C](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6044.html)

ASBRs do not need to maintain inter-AS L2VPN information or reserve AC interfaces for inter-AS L2VPN connections. As L2VPN information is exchanged only between PEs, this solution requires fewer resources and less configuration workload.

[Configuring Inter-AS BGP VPWS Option A](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6058.html)

Inter-AS BGP VPWS Option A applies to scenarios where few inter-AS PWs are required. Compared with L3VPN, inter-AS BGP VPWS Option A requires more resources and configuration workload.

[Configuring Inter-AS BGP VPWS Option C](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6059.html)

ASBRs do not need to maintain inter-AS L2VPN information or reserve AC interfaces for inter-AS L2VPN PWs. As L2VPN information is exchanged only between PEs, this solution requires fewer resources and less configuration workload.

[Verifying the Inter-AS VPWS Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6045.html)

After configuring inter-AS VPWS, check local and remote PW information.