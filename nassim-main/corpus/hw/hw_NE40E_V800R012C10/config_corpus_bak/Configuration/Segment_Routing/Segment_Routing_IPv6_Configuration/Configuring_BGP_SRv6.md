Configuring BGP SRv6
====================

A controller orchestrates IGP SIDs and BGP SR-allocated BGP peer SIDs to implement inter-AS forwarding over the optimal path.

#### Context

BGP is a dynamic routing protocol used between ASs. BGP SRv6 is a BGP extension for SR and is used for inter-AS source routing.


[Configuring BGP EPE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_all_cfg_0033-1.html)

BGP egress peer engineering (EPE) is used to allocate Peer-Node and Peer-Adj SIDs to peers. These SIDs can be reported to a controller through BGP-LS for orchestrating E2E SRv6 TE Policies.

[Configuring the BGP Peer Relationship-based Virtual Link Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_all_cfg_0033-2.html)

A virtual link across the Layer 3 network can be created for a controller to compute paths.

[Configuring BGP-LS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_all_cfg_0033-3.html)

BGP-LS is used to collect network topology information in a more efficient and easier manner.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_all_cfg_0033-4.html)

After configuring BGP SRv6, you can verify the configuration.