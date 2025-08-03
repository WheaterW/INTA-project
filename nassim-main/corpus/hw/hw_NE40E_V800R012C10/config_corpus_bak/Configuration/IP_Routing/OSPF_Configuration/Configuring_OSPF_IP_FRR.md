Configuring OSPF IP FRR
=======================

If a link fails, an OSPF IP FRR-capable device can fast switch traffic to a backup link, which protects traffic and improves OSPF network reliability.

#### Usage Scenario

As networks develop, services such as Voice over IP (VoIP) and on-line video services require high-quality real-time transmission. However, OSPF takes more than 50 ms to rectify a fault, which cannot meet the requirement for real-time transmission of these services.

Nevertheless, if an OSPF fault occurs, traffic can be switched to a new link only after the fault detection that lasts several milliseconds, fault notification to the routing control plane that lasts several milliseconds, new topology information generation and flooding that last tens of milliseconds, Shortest Path First (SPF) calculation that lasts tens of milliseconds, and new route notification and adding that last hundreds of milliseconds. Therefore, traffic can be quickly switched to a new link only when the time for new route notification and adding is shortened, ensuring that the traffic interruption time is less than 50 ms.

With OSPF IP FRR that calculates a backup link in advance, devices can fast switch traffic to the backup link without interrupting traffic if the primary link fails, which protects traffic and improves OSPF network reliability.

As shown in [Figure 1](#EN-US_TASK_0172365611__fig_dc_vrp_ospf_cfg_200902), traffic flows from Device S to Device D. The preceding inequality is met. Device S switches the traffic to the backup link if the primary link fails.

**Figure 1** OSPF IP FRR link protection  
![](images/fig_dc_vrp_ospf_cfg_200902.png)  

OSPF IP FRR is applicable to services that are sensitive to packet delay and packet loss.

The NE40E supports OSPF IP FRR that uses LFA or Remote LFA as the algorithm.

FRR implemented by the LFA algorithm cannot calculate backup paths on large-scale networks, especially on ring networks. As a result, reliability requirements cannot be met. To address this problem, enable Remote LFA Auto FRR. Before configuring Remote LFA, you need to enable LFA.

In OSPF LFA FRR and Remote LFA, the SPF algorithm is used to calculate the shortest path to the destination node, with each neighbor that provides a backup link as the root node, and the backup next hop is node-based. This implementation applies to single-node routing scenarios. As networks are increasingly diversified, two ABRs or ASBRs are deployed to improve network reliability. In this case, OSPF FRR for the scenario where multiple nodes advertise the same route is introduced. In [Figure 2](#EN-US_TASK_0172365611__fig_dc_vrp_ospf_cfg_200904), Device B and Device C function as ABRs to forward area 0 and area 1 routes. Device E advertises an intra-area route. Upon receipt of the route, Device B and Device C translate it to a Type 3 LSA and flood the LSA to area 0. After OSPF FRR is enabled on Device A, Device A considers Device B and Device C as its neighbors. Without a fixed neighbor as the root node, Device A fails to calculate FRR backup next hop. To solve this problem, a virtual node is constructed between Device B and Device C. The virtual node converts the same route advertised by multiple nodes into a route with a single route source, and then calculates the backup next hop of the virtual node based on the LFA or Remote LFA algorithm. The same route advertised by multiple nodes inherits the backup next hop from the created virtual node.

**Figure 2** OSPF FRR in the scenario where multiple nodes advertise the same route  
![](images/fig_dc_vrp_ospf_cfg_200904.png)

After OSPF IP FRR is configured, the lower layer needs to fast respond to a link change so that traffic can be fast switched to the backup link. After FRR and BFD are bound, link failures can be detected rapidly so that traffic is rapidly switched to the backup link if the primary link fails.


#### Pre-configuration Tasks

Before configuring OSPF IP FRR, complete the following tasks:

* Configure a link layer protocol.
* Configure IP addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configure basic OSPF functions](dc_vrp_ospf_cfg_0003.html).
* Before you configure remote LFA FRR, configure LDP LSPs to perform recursion hop by hop between the source node and PQ node. That is, [configure a local LDP session](dc_vrp_ldp-p2p_cfg_0003.html) between each pair of directly connected nodes along the link from the source node to PQ node.


[Enabling OSPF IP FRR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2010.html)

With OSPF IP FRR and loop-free backup links, a device can switch traffic to a backup link immediately if the primary link fails.

[(Optional) Binding IP FRR and BFD](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2011.html)

Binding IP FRR and BFD enables the lower layer to fast respond to a link change so that traffic can be rapidly switched to the backup link if the primary link fails.

[(Optional) Disabling OSPF IP FRR on an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2013.html)

If an interface runs key services, ensure that the backup path does not pass through this interface so that services will not be affected after FRR calculation.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2014.html)

After configuring OSPF IP FRR, you can view the information about the backup next hop.