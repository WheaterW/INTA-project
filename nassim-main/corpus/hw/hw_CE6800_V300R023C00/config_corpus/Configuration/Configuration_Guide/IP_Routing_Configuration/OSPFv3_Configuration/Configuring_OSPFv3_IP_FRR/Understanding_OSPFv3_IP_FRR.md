Understanding OSPFv3 IP FRR
===========================

OSPFv3 IP fast reroute (FRR) is dynamic IP FRR, in which the IGP (OSPFv3) precomputes a backup path based on the network-wide LSDBs, and stores this backup path in the forwarding table. If the primary path fails, traffic can be quickly switched to the backup path, reducing the fault recovery time. OSPFv3 IP FRR complies with standard protocols and provides link and node protection for traffic.

#### Context

As networks develop, services such as Voice over IP (VoIP) and online video services require high-quality and real-time transmission. However, if a link fails, OSPFv3 must complete the following procedure before switching traffic to a new link: detect the fault, update LSAs, flood LSAs, calculate routes, and deliver route entries to the FIB. This is a lengthy process, and the associated traffic interruption is often longer than users can tolerate. As a result, real-time transmission requirements cannot be met.


#### Fundamentals

OSPFv3 IP FRR refers to a mechanism in which a device uses the loop-free alternate (LFA) algorithm to precompute a backup route, and stores the primary and backup routes in the forwarding table. If a fault occurs on the network, OSPFv3 IP FRR can fast switch traffic to the backup link before routes on the control plane converge. This ensures uninterrupted traffic transmission and improves OSPFv3 network reliability.

A device uses the SPF algorithm to calculate shortest paths to destinations, with each neighbor that provides a backup link as a root node. The device then uses an inequality defined in the standard protocol to calculate the loop-free backup link with the lowest cost among available shortest paths.

An OSPFv3 IP FRR policy can be used to filter backup routes. Only the backup routes that match the filtering rules in the policy can be added to the IP routing table, facilitating flexible control of the OSPFv3 backup routes to be added to the table.

A BFD session can be associated with OSPFv3 IP FRR. With this configuration, the BFD session goes down if BFD detects a link fault. In this case, OSPFv3 IP FRR is triggered to switch traffic from the faulty link to the backup link, thereby protecting traffic.


#### Application Scenario

OSPFv3 IP FRR protects traffic against either a link failure or a node-and-link failure. Distance\_opt (*X*, *Y*) indicates the shortest path from node *X* to node *Y*.

* **Link protection**: takes effect when the traffic to be protected flows along a specified link.
  
  The link costs must meet the inequality: Distance\_opt (N, D) < Distance\_opt (N, S) + Distance\_opt (S, D).
  + S: source node that forwards traffic
  + N: node along the backup link
  + D: destination node for traffic forwarding
  
  In [Figure 1](#EN-US_CONCEPT_0000001130783000__en-us_concept_0275857994_fig_dc_vrp_ospfv3_feature_200701), traffic flows from DeviceS to DeviceD, and the link costs meet the preceding inequality. If the primary link fails, DeviceS switches traffic to the backup link DeviceS -> DeviceN, minimizing the traffic interruption duration.
  
  **Figure 1** OSPFv3 IP FRR â link protection  
  ![](figure/en-us_image_0000001229682723.png)
* **Node-and-link protection**: [Figure 2](#EN-US_CONCEPT_0000001130783000__en-us_concept_0275857994_fig_dc_vrp_ospfv3_feature_200702) shows a network diagram for node-and-link protection. Node-and-link protection takes precedence over link protection.
  
  Node-and-link protection takes effect only if the following conditions are met:
  
  + The link costs meet the inequality: Distance\_opt (N, D) < Distance\_opt (N, S) + Distance\_opt (S, D).
  + The interface costs meet the inequality: Distance\_opt (N, D) < Distance\_opt (N, E) + Distance\_opt (E, D).
  
  S stands for the source node, E for the faulty node, N for a node along the backup link, and D for the destination node.
  
  **Figure 2** OSPFv3 IP FRR â node-and-link protection  
  ![](figure/en-us_image_0000001184761504.png)


#### OSPFv3 FRR for a Scenario Where the Same Route Is Received from Multiple Nodes

With OSPFv3 LFA FRR, a device uses the SPF algorithm to calculate the shortest path to the destination with a neighbor that provides a backup link as the root node, and then stores the node-based backup next hop. This applies to a scenario where a route is received from only one node. As networks are increasingly diversified, two ABRs or ASBRs are deployed to improve network reliability. In this case, OSPFv3 FRR is developed for scenarios where the same route is received from multiple nodes.

![](../public_sys-resources/note_3.0-en-us.png) 

In scenarios where the same route is received from multiple nodes, OSPFv3 FRR is implemented by calculating the Type 3 LSAs advertised by the ABRs of an area for intra-area, inter-area, or ASE routing. Inter-area routing is used as an example to describe how FRR works in a scenario where the same route is received from multiple nodes.


**Figure 3** OSPFv3 FRR in a scenario where the same route is received from multiple nodes  
![](figure/en-us_image_0000001229602675.png)

In [Figure 3](#EN-US_CONCEPT_0000001130783000__en-us_concept_0275857994_fig_dc_vrp_ospfv3_feature_200703), DeviceB and DeviceC function as ABRs to forward routes between area 0 and area 1. DeviceE advertises an intra-area route. Upon receipt of the route, DeviceB and DeviceC each translate it into a Type 3 LSA and flood the LSA to area 0. After OSPFv3 FRR is enabled on DeviceA, DeviceA considers both DeviceB and DeviceC as its neighbors. Without a fixed neighbor as the root node, DeviceA fails to calculate the FRR backup next hop. To address this problem, a virtual node is simulated between DeviceB and DeviceC, which converts the scenario where the same route is received from multiple nodes to a scenario where a route is received from a single node. The LFA algorithm is then used to calculate the backup next hop for the virtual node. The multi-source route inherits the backup next hop from the virtual node.

For example, DeviceB and DeviceC each advertise a route with the prefix 2001:DB8:1::1/64, and OSPFv3 FRR is enabled on DeviceA. After DeviceA receives the route, it fails to calculate a backup next hop due to a lack of a fixed root node. To address this problem, a virtual node is simulated between DeviceB and DeviceC. The cost of the link from DeviceB to the virtual node is 0, and the cost of the link from DeviceC to the virtual node is 5. The costs of the links from the virtual node to DeviceB and to DeviceC are both the maximum value (65535). If the virtual node advertises the 2001:DB8:1::1/64 route, it will use the lower cost of the routes advertised by DeviceB and DeviceC as the cost of the 2001:DB8:1::1/64 route. DeviceA considers DeviceB and DeviceC as invalid sources of the 2001:DB8:1::1/64 route and uses the LFA algorithm to calculate a backup next hop for the route, with the virtual node as the root node.