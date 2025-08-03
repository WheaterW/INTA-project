Understanding OSPF IP FRR
=========================

OSPF IP fast reroute (FRR) refers to the process in which the device precomputes a backup path based on the network-wide LSDBs, and stores this backup path in the forwarding table. If the primary path fails, traffic can be quickly switched to the backup path, reducing the fault recovery time.

#### Context

As networks develop, services such as Voice over IP (VoIP) and online video services require high-quality and real-time transmission. However, if a link fails, OSPF must complete the following procedure before switching traffic to a new link: detect the fault, update LSAs, flood LSAs, calculate routes, and deliver route entries to the FIB. This is a lengthy process, and the associated traffic interruption is often longer than users can tolerate. As a result, real-time transmission requirements cannot be met. OSPF IP FRR can effectively solve this problem. OSPF IP FRR conforms to dynamic IP FRR defined by a standard protocol, and allows traffic to be quickly switched to a backup link, protecting traffic against link or node failures and minimizing the length of interruptions.

Major FRR techniques include loop-free alternate (LFA), U-turn, Not-Via, remote LFA, and maximally redundant tree (MRT). Of these, only LFA is supported by OSPF.


#### Related Concepts

**OSPF IP FRR**

OSPF IP FRR refers to a mechanism in which a device uses the LFA algorithm to precompute the next hop of a backup route, and stores the primary and backup routes to the same destination address but with different next hops in the forwarding table. If the primary link fails, OSPF IP FRR switches traffic to the backup link before route convergence is complete on the control plane. This mechanism minimizes the length of traffic interruptions and protects services.

**OSPF IP FRR policy**

An OSPF IP FRR policy can be used to filter backup routes. Only the backup routes that match the filtering rules in the policy can be added to the IP routing table, facilitating flexible control of the OSPF backup routes to be added to the table.

**LFA algorithm**

The LFA algorithm calculates a backup link as follows: With the neighbor that can provide a backup link as the root node, the SPF algorithm is used to calculate the shortest path to the destination node, and then a loop-free backup link with the smallest cost is calculated according to the inequality defined in the standard protocol.


#### OSPF LFA FRR

OSPF LFA FRR protects traffic against either a link failure or a node-and-link failure. The node-and-link protection takes precedence over the link protection.

**Link protection**

Link protection takes effect when the traffic to be protected flows along a specified link.

In [Figure 1](#EN-US_CONCEPT_0000001176742933__en-us_concept_0275861918_fig_dc_vrp_ospf_feature_002701), traffic flows from DeviceS to DeviceD. The primary link is DeviceS -> DeviceE -> DeviceD, and the backup link is DeviceS -> DeviceN -> DeviceE -> DeviceD. If the link costs meet the inequality: Distance\_opt (N, D) < Distance\_opt (N, S) + Distance\_opt (S, D) (10 + 5 < 10 + 5 + 5 in this example), OSPF LFA FRR enables DeviceS to switch traffic to the backup link if the primary link fails, reducing the traffic interruption duration.

![](../public_sys-resources/note_3.0-en-us.png) 

Distance\_opt (X, Y) indicates the shortest path from X to Y. In the inequality: Distance\_opt (N, D) < Distance\_opt (N, S) + Distance\_opt (S, D), S indicates the traffic's source node (DeviceS in the figure), N indicates a node (DeviceN in the figure) on the backup link, and D indicates the destination node (DeviceD in the figure).


**Figure 1** OSPF LFA FRR â link protection  
![](figure/en-us_image_0000001229800817.png)

**Node-and-link protection**

Node-and-link protection takes effect when the traffic to be protected flows along a specified node and link.

In [Figure 2](#EN-US_CONCEPT_0000001176742933__en-us_concept_0275861918_fig_dc_vrp_ospf_feature_002702), traffic flows from DeviceS to DeviceD. The primary link is DeviceS -> DeviceE -> DeviceD, and the backup link is DeviceS -> DeviceN -> DeviceD. With OSPF LFA FRR, DeviceS switches traffic to the backup link if the primary link fails, minimizing the traffic interruption duration.

Node-and-link protection takes effect only if the following conditions are met:

* The link costs meet the inequality: Distance\_opt (N, D) < Distance\_opt (N, S) + Distance\_opt (S, D).
* The interface costs meet the inequality: Distance\_opt (N, D) < Distance\_opt (N, E) + Distance\_opt (E, D).

![](../public_sys-resources/note_3.0-en-us.png) 

Distance\_opt (X, Y) indicates the shortest path from X to Y. In the inequality: Distance\_opt (N, D) < Distance\_opt (N, S) + Distance\_opt (S, D), S indicates the source node, E indicates the faulty node, N indicates a node on the backup link, and D indicates the destination node.


**Figure 2** OSPF LFA FRR â node-and-link protection  
![](figure/en-us_image_0000001229682379.png)

#### OSPF FRR for a Multi-Node Routing Scenario

With OSPF LFA FRR, a device uses the SPF algorithm to calculate the shortest path to the destination with a neighbor that provides a backup link as the root node, and then stores the node-based backup next hop. This applies to a scenario where a route is received from only one node, single-node routing scenario for short. As networks are increasingly diversified, two ABRs or ASBRs are deployed to improve network reliability. In this case, OSPF FRR is developed for scenarios where the same route is received from multiple nodes, multi-node routing scenarios for short.

![](../public_sys-resources/note_3.0-en-us.png) 

In a multi-node routing scenario, OSPF FRR is implemented by calculating the Type 3 LSAs advertised by the ABRs of an area for intra-area, inter-area, ASE, or NSSA routing. Inter-area routing is used as an example to describe how OSPF FRR works in a multi-node routing scenario.


**Figure 3** OSPF FRR in a multi-node routing scenario  
![](figure/en-us_image_0000001184601250.png)

In [Figure 3](#EN-US_CONCEPT_0000001176742933__en-us_concept_0275861918_fig_dc_vrp_ospf_feature_002704), DeviceB and DeviceC function as ABRs to forward routes between area 0 and area 1, while DeviceE advertises an intra-area route. Upon receipt of the route, DeviceB and DeviceC each translate it into a Type 3 LSA and flood the LSA to area 0. After OSPF FRR is enabled on DeviceA, DeviceA considers both DeviceB and DeviceC as its neighbors. Without a fixed neighbor as the root node, DeviceA fails to calculate the FRR backup next hop. To address this problem, a virtual node is simulated between DeviceB and DeviceC and used as the root node of DeviceA, and DeviceA uses the LFA algorithm to calculate the backup next hop. This solution converts multi-node routing into single-node routing.

For example, DeviceB and DeviceC each advertise a route with the prefix 10.1.1.0/24. After DeviceA with OSPF FRR enabled receives the routes, it fails to calculate a backup next hop due to a lack of a fixed root node. To address this problem, a virtual node is simulated between DeviceB and DeviceC and used as the root node of DeviceA. The cost of the link from DeviceB to the virtual node is 0, and the cost of the link from DeviceC to the virtual node is 5. The costs of the links from the virtual node to DeviceB and to DeviceC are both the maximum value (65535). If the virtual node advertises the 10.1.1.0/24 route, it will use the lower cost of the routes advertised by DeviceB and DeviceC as the cost of the 10.1.1.0/24 route. DeviceA is configured to consider DeviceB and DeviceC as invalid sources of the 10.1.1.0/24 route and use the LFA algorithm to calculate a backup next hop for the route, with the virtual node as the root node.


#### Derivative Functions

A BFD session can be associated with OSPF IP FRR. With this configuration, the BFD session goes down if BFD detects a link fault. In this case, OSPF IP FRR is triggered to switch traffic from the faulty link to the backup link, thereby protecting traffic.