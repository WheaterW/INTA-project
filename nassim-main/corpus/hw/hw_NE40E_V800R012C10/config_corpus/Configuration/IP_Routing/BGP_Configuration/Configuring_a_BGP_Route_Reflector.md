Configuring a BGP Route Reflector
=================================

By configuring a BGP route reflector (RR), you can avoid fully meshed connections between multiple IBGP peers.

#### Usage Scenario

Fully meshed connections need to be established between IBGP peers to ensure the connectivity between the IBGP peers. When there are a large number of IBGP peers, the cost of establishing a fully meshed network is high. This problem can be solved by using RRs.

RRs can reduce the total number of IBGP connections. On a large network, to reduce the number of clients of each RR, you need to configure multiple RRs. Because fully meshed connections need to be established between the RRs, there are still a large number of IBGP connections on the network. In this situation, configure hierarchical RRs to further reduce the number of IBGP connections.

[Figure 1](#EN-US_TASK_0172366197__fig_dc_vrp_bgp_cfg_303401) shows typical networking with hierarchical RRs. In this networking, R1, R2, R3, and R4 function as Level-1 RRs; R5, R6, R7, and R8 function as level-2 RRs and the clients of the Level-1 RRs. The Level-1 RRs are not the clients of any RR and must be fully meshed. The Level-2 RRs function as the clients of the Level-1 RRs and do not need to be fully meshed.

**Figure 1** Typical networking with hierarchical RRs
  
![](images/fig_dc_vrp_bgp_cfg_303401.png)

#### Pre-configuration Tasks

Before configuring a BGP route reflector, [configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).


[Configuring a Route Reflector and Specifying Clients](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3035.html)

RRs reflect routes between clients, and therefore IBGP connections do not need to be established between the clients.

[(Optional) Disabling Route Reflection Between Clients Through the RR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3036.html)

If the clients of a route reflector are fully connected, you need to disable route reflection among them through the RR to reduce bandwidth consumption.

[(Optional) Setting the Cluster ID of a Route Reflector](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3037.html)

When there are multiple route reflectors in a cluster, you need to configure the same cluster ID for all the route reflectors in this cluster to avoid routing loops.

[(Optional) Preventing a Device from Adding BGP Routes to the IP Routing Table](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3038.html)

After you prevent an RR from adding BGP routes to the IP routing table, the RR no longer forwards traffic, which improves route advertisement efficiency.

[(Optional) Enabling an RR to Modify Route Attributes Using an Export Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3090.html)

You can enable an RR to modify route attributes using an export policy to control BGP route selection.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3039.html)

After configuring a BGP route reflector, verify information about BGP routes and BGP peer groups.