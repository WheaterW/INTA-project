Configuring Inter-AS VPLS
=========================

Inter-AS VPLS allows a VPLS network to span multiple ASs on an MPLS backbone network.

#### Usage Scenario

If multiple ASs exist on an MPLS backbone network, the VPLS network carried over the MPLS backbone network must be an inter-AS VPLS network. Currently, the following inter-AS VPLS solutions are available:

* Inter-AS VPLS Option A: This solution is recommended for scenarios where few inter-AS VCs are required. In Option A, ASBRs must support VSIs and must be capable of managing VPLS label blocks. In addition, ASBRs need to reserve dedicated interfaces for each inter-AS VPLS connection. This solution poses high performance requirements for ASBRs, but does not require inter-AS configurations to be performed on ASBRs.
* Inter-AS VPLS Option C: This solution is recommended for scenarios where each AS requires a large number of inter-AS LDP L2VPN connections. In this solution, ASBRs do not need to create or maintain VCs and therefore will not be a bottleneck that hinders network expansion.


#### Pre-configuration Tasks

Before configuring inter-AS VPLS, complete the following tasks:

* Configure an IGP for each AS on the MPLS backbone network to ensure IP connectivity of the backbone network in each AS.
* Configure basic MPLS capabilities on the MPLS backbone network in each AS.
* Configure MPLS LDP and establish LDP LSPs for the MPLS backbone network in each AS.
* Establish an IBGP peer relationship between the PE and ASBR in the same AS and an EBGP peer relationship between ASBRs in different ASs. This task is specific to Option C.
* Configure VSIs on PEs connected to CEs and bind the corresponding AC interfaces to these VSIs.


[Configuring Inter-AS LDP VPLS Option A](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6024.html)

Inter-AS LDP VPLS Option A is recommended for scenarios where few inter-AS PWs are required. In inter-AS LDP VPLS Option A, an ASBR must reserve an interface as an AC interface for each inter-AS PW. Compared with L3VPN, inter-AS LDP VPLS Option A consumes more resources and requires more configuration workload. 

[Configuring Inter-AS LDP VPLS Option C](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6025.html)

In inter-AS LDP VPLS Option C, ASBRs do not need to maintain inter-AS LDP VPLS information or reserve interfaces for inter-AS LDP VPLS PWs. As LDP VPLS information is exchanged only between PEs, this solution requires few resources and is easy to deploy.

[Configuring Inter-AS BGP VPLS Option A](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6016.html)

In Option A, an ASBR must reserve an interface as an AC interface for each inter-AS VC. Option A can be used when the number of inter-AS VCs is small. Compared with L3VPN, inter-AS L2VPN Option A consumes more resources and requires more configuration workload. Therefore, inter-AS L2VPN Option A is not recommended.

[Configuring Inter-AS BGP VPLS Option B](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6016_1.html)

The advantage of the inter-AS Option B mode is that ASBRs exchange information through routes rather than dedicated links. The disadvantage of the inter-AS Option B mode is that label mappings need to be configured on ASBRs, and consequently, a great number of labels are consumed. In addition, an ASBR needs to set up an LSP with each PE, which results in the shortage of label resources on the ASBR and easily leads to a bottleneck.

[Configuring Inter-AS BGP VPLS Option C](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6017.html)

In inter-AS Option C, a network device only needs to establish a public tunnel with a PE in a different AS. ASBRs do not need to maintain inter-AS L2VPN information or reserve AC interfaces for inter-AS L2VPN connections. As L2VPN information is exchanged only between PEs, this solution requires fewer resources and less configuration workload.

[Configuring Inter-AS BGP VPLS Option C (with RRs Deployed)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6017_1.html)

In inter-AS Option C, a network device only needs to establish a public tunnel with a PE in a different AS. ASBRs do not need to maintain inter-AS L2VPN information or reserve AC interfaces for inter-AS L2VPN connections. As L2VPN information is exchanged only between PEs, this solution requires fewer resources and less configuration workload.

[Configuring Inter-AS BGP AD VPLS Option A](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6050.html)

In inter-AS BGP AD VPLS Option A, an ASBR must reserve an interface as an AC interface for each inter-AS PW. Inter-AS BGP AD VPLS Option A applies to scenarios where few inter-AS PWs are required. Compared with L3VPN, inter-AS BGP AD VPLS Option A requires more resources and configuration workload.

[Configuring Inter-AS BGP AD VPLS Option C](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6051.html)

In inter-AS Option C, a network device only needs to establish a public tunnel with a PE in a different AS. ASBRs do not need to maintain inter-AS L2VPN information or reserve AC interfaces for inter-AS L2VPN connections. As L2VPN information is exchanged only between PEs, this solution requires fewer resources and less configuration workload.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6026.html)

After configuring inter-AS VPLS, check VPLS VSI and connection information.