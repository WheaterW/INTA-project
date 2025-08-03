Configuring BGP4+ RRs
=====================

BGP4+ RRs avoid fully meshed connections between multiple IBGP peers, which reduces network costs.

#### Usage Scenario

Fully meshed connections need to be established between IBGP peers to ensure the connectivity between IBGP peers. When there are a large number of IBGP peers, it is costly to establish a full-mesh network. An RR can be used to solve the problem.

Using RRs reduces the total number of IBGP connections. On a large network, however, multiple RRs need to be configured to reduce the number of clients of each RR. Therefore, there are still a large number of IBGP connections on the network because fully meshed connections need to be established between the RRs. To further reduce the number of IBGP connections, multi-level BGP4+ RR networking is introduced.

[Figure 1](#EN-US_TASK_0172366468__fig_dc_vrp_bgp6_cfg_004002) shows a typical BGP4+ hierarchical RR networking. Device A, Device B, Device C, and Device D function as level-2 RRs; Device E, Device F, Device G, and Device H function as level-1 RRs and the clients of level-2 RRs. Level-2 RRs are not the clients of any RR and therefore must be fully meshed. Level-1 RRs function as the clients of level-2 RRs and do not need to be fully meshed.

**Figure 1** Network diagram with hierarchical BGP4+ RRs  
![](images/fig_dc_vrp_bgp6_cfg_004002.png)

#### Pre-configuration Tasks

Before configuring BGP4+ RRs, [configure basic BGP4+ functions](dc_vrp_bgp6_cfg_0003.html).


[Configuring an RR and Specifying Its Clients](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0041.html)

RRs reflect routes between clients, and therefore IBGP connections do not need to be established between the clients.

[(Optional) Disabling Route Reflection Between Clients Through the RR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0042.html)

If the clients of an RR are fully meshed, you can disable route reflection between the clients through the RR. This reduces the memory overhead.

[(Optional) Configuring a Cluster ID for RRs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0043.html)

If a cluster has multiple RRs, you can configure the same cluster ID for these RRs to prevent routing loops.

[(Optional) Preventing BGP4+ from Adding Routes to the IP Routing Table](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0083.html)

Disabling BGP4+ route delivery to the IP routing table on an RR can prevent traffic from being forwarded by the RR, improving route advertisement efficiency.

[(Optional) Enabling an RR to Modify Route Attributes Using an Export Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0084.html)

Enabling an RR to modify route attributes using an export policy can change BGP4+ route selection results.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0044.html)

After configuring BGP4+ RRs, check information about BGP4+ routes and peer groups.