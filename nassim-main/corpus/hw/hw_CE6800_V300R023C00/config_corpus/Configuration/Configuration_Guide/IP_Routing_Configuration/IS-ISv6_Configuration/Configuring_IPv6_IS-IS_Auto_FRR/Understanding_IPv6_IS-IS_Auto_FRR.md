Understanding IPv6 IS-IS Auto FRR
=================================

Understanding IPv6 IS-IS Auto FRR

#### Context

As networks develop, services such as Voice over IP (VoIP) and online video services pose higher requirements for real-time transmission. However, if an IS-IS fault occurs, multiple processes must be performed before traffic is switched to a new link. Such processes include fault detection, LSP update, LSP flooding, route calculation, and FIB entry generation. As a result, the fault recovery time is too long and cannot meet the requirement for real-time transmission.

IS-IS Auto Fast Reroute (FRR) is dynamic IP FRR in which a backup link is pre-computed by an IGP based on the LSDBs on the entire network. The backup link is stored in the forwarding table and is used to protect traffic if a link failure occurs. Because IP FRR helps implement fast route convergence, it becomes increasingly popular with carriers.

Major FRR techniques include loop-free alternate (LFA), U-turn, Not-Via, remote LFA, and maximally redundant tree (MRT). Of these, only LFA is supported by IS-IS.


#### Related Concepts

**LFA**

LFA uses the SPF algorithm to compute the shortest path from the neighbor that can provide a backup link to the destination node and then computes a loop-free backup link with the smallest cost based on the following inequality:

LFA inequality: Distance\_opt (N, D) < Distance\_opt (N, S) + Distance\_opt (S, D). In this inequality, Distance\_opt indicates the shortest path between two nodes. N, D, and S indicate the node that provides a backup link, destination node, and source node, respectively.


#### IS-IS LFA Auto FRR

IS-IS LFA Auto FRR protects against both link and node-and-link failures.

Link protection: takes effect when the traffic to be protected flows along a specified link.

In [Figure 1](#EN-US_CONCEPT_0000001176742051__fig_dc_vrp_isis_feature_001501), traffic flows from DeviceS to DeviceD, and link costs meet the link protection inequality: Distance\_opt (N, D) < Distance\_opt (N, S) + Distance\_opt (S, D). If the primary link fails, DeviceS switches the traffic to the backup link (DeviceS -> DeviceN -> DeviceD), minimizing traffic loss.

**Figure 1** Networking for IS-IS LFA Auto FRR link protection  
![](figure/en-us_image_0000001130782446.png)

Node-and-link protection: takes effect when the traffic to be protected flows along a specified node and link, and takes precedence over link protection. [Figure 2](#EN-US_CONCEPT_0000001176742051__fig_dc_vrp_isis_feature_001502) illustrates a network where node-and-link protection is used.

Node-and-link protection takes effect only if the following conditions are met:

1. Link costs meet the inequality: Distance (N, D) < Distance (N, S) + Distance (S, D).
2. Interface costs meet the inequality: Distance (N, D) < Distance (N, E) + Distance (E, D).
   
   DeviceS stands for the source node, DeviceE for the faulty node, DeviceN for a node along the backup link, and DeviceD for the destination node.

**Figure 2** Networking for IS-IS LFA auto FRR node-and-link protection  
![](figure/en-us_image_0000001176662199.png)

#### IS-IS FRR in the Scenario Where Multiple Nodes Advertise the Same Route

IS-IS LFA FRR uses the SPF algorithm to calculate the shortest path to the destination node, with each neighbor that provides a backup link as the root node. The calculated backup next hop is node-based, which applies to the scenario where each route is received from a single node. As networks diversify, multiple nodes may advertise the same route. In this case, LFA conditions in the scenario where each route is received from a single node cannot be met. As a result, the backup next hop cannot be calculated. IS-IS FRR for the scenario where multiple nodes advertise the same route can address this problem by using one of the route sources to protect the primary route source, improving network reliability.

**Figure 3** IS-IS FRR in the scenario where multiple nodes advertise the same route  
![](figure/en-us_image_0000001176662207.png)

As shown in [Figure 3](#EN-US_CONCEPT_0000001176742051__fig_dc_vrp_isis_feature_001504)(a), the cost of the DeviceA-to-DeviceB link is 5, and that of the DeviceA-to-DeviceC link is 10. DeviceB and DeviceC advertise the route 10.1.1.0/24 simultaneously. IS-IS FRR is enabled on DeviceA. However, DeviceA cannot calculate the backup next hop of the route 10.1.1.0/24 because the LFA conditions in the scenario where each route is received from a single node cannot be met. To address this issue, IS-IS FRR for the scenario where multiple nodes advertise the same route can be used.

The implementation is as follows:

In [Figure 3](#EN-US_CONCEPT_0000001176742051__fig_dc_vrp_isis_feature_001504)(b), a virtual node is simulated between DeviceB and DeviceC and is connected to DeviceB and DeviceC. The cost of the link from DeviceB or DeviceC to the virtual node is 0, whereas the cost of the link from the virtual node to DeviceB or DeviceC is the maximum value. After the virtual node advertises the route 10.1.1.0/24, DeviceA can use the LFA algorithm to calculate the backup next hop of the virtual node because the scenario where multiple nodes advertise the same route has been converted to the scenario where the route is received from only one node. DeviceA computes two links to the virtual node. The primary link is from DeviceA to DeviceB, and the backup link is from DeviceA to DeviceC.


#### IS-IS SRLG FRR

A shared risk link group (SRLG) is a set of links that share a common physical resource (such as a fiber). These links share the same risk level. If one of the links fails, all the other links in the SRLG may also fail. On the network shown in [Figure 4](#EN-US_CONCEPT_0000001176742051__fig_dc_vrp_isis_feature_002506), traffic from DeviceA to DeviceB is balanced between link 1 and link 2.

If IS-IS LFA Auto FRR is enabled, it implements protection for the two links. That is, link 1 and link 2 back up each other.

* If link 1 fails but the backup link (link 2) is normal, traffic can be forwarded normally after being switched to the backup link.
* If both link 1 and link 2 fail, traffic is interrupted after being switched to the backup link.

IS-IS SRLG FRR prevents service interruptions in the scenario where links have the same risk of failure. To prevent traffic interruption in this case, add link 1 and link 2 to an SRLG so that a link outside the SRLG is preferentially selected as a backup link.

**Figure 4** Networking for IS-IS SRLG FRR  
![](figure/en-us_image_0000001130622664.png)