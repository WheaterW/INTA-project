Configuring OSPFv3 IP FRR
=========================

If a link fails, OSPFv3 IP FRR rapidly switches traffic to a backup link, which prevents traffic interruption and improves OSPFv3 network reliability.

#### Usage Scenario

As networks develop, services such as Voice over IP (VoIP) and on-line video services require high-quality real-time transmission. However, OSPFv3 takes more than 50 ms to rectify a fault, which cannot meet the requirement for real-time transmission of these services.

Nevertheless, if an OSPFv3 fault occurs, traffic can be switched to a new link only after the fault detection that lasts several milliseconds, fault notification to the routing control plane that lasts several milliseconds, new topology information generation and flooding that last tens of milliseconds, Shortest Path First (SPF) calculation that lasts tens of milliseconds, and new route notification and adding that last hundreds of milliseconds.

OSPFv3 IP FRR calculates a backup link in advance. If the primary link fails, OSPFv3 IP FRR rapidly switches traffic to the backup link without interrupting traffic. This protects traffic and greatly improves OSPFv3 network reliability.

OSPFv3 IP FRR is applicable to services that are sensitive to the packet delay and packet loss.

OSPFv3 LFA FRR uses the SPF algorithm to calculate the shortest path from each neighbor (root node) that provides a backup link to the destination node and store the node-based backup next hop, which applies to single-node routing scenarios. As networks are increasingly diversified, two ABRs or ASBRs are deployed to improve network reliability. In this case, OSPFv3 FRR in a scenario where multiple nodes advertise the same route is needed. In [Figure 1](#EN-US_TASK_0172365755__fig_dc_vrp_ospfv3_cfg_203102), Device B and Device C function as ABRs to forward area 0 and area 1 routes. Device E advertises an intra-area route. Upon receipt of the route, Device B and Device C translate it into a Type 3 LSA and flood the LSA to area 0. After OSPFv3 FRR is enabled on Device A, Device A considers Device B and Device C as its neighbors. Without a fixed neighbor as the root node, Device A fails to calculate FRR backup next hop. To address this problem, a virtual node is simulated between Device B and Device C and used as the root node of Device A, and Device A uses the LFA algorithm to calculate the backup next hop. This solution converts multi-node routing into single-node routing.**Figure 1** OSPFv3 FRR in the scenario where multiple nodes advertise the same route  
![](images/fig_dc_vrp_ospfv3_cfg_203102.png)

After OSPFv3 IP FRR is configured, the lower layer needs to fast respond to a link change so that traffic can be fast switched to the backup link. After FRR and BFD are bound, link failures can be detected rapidly so that traffic is rapidly switched to the backup link if the primary link fails.


#### Pre-configuration Tasks

Before configuring OSPFv3 IP FRR, complete the following tasks:

* Configure a link layer protocol.
* Configure IP addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configure basic OSPFv3 functions](dc_vrp_ospfv3_cfg_2003.html).


[Enabling OSPFv3 IP FRR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2032.html)

With OSPF IP FRR and loop-free backup links, a device can switch traffic to a backup link immediately if the primary link fails.

[(Optional) Binding IP FRR and BFD](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2033.html)

Binding IP FRR and BFD enables the lower layer to fast respond to a link change so that traffic can be rapidly switched to the backup link if the primary link fails.

[(Optional) Blocking FRR on an OSPFv3 Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2034.html)

If FRR is not required on certain OSPFv3 interfaces, FRR needs to be blocked on these interfaces.

[Verifying the Configuration of OSPFv3 IP FRR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2035.html)

After configuring OSPFv3 IP FRR, you can view information about the primary and backup links.