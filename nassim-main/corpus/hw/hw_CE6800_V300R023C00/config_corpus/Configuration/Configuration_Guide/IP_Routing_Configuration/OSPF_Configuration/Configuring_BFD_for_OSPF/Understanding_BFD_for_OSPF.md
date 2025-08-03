Understanding BFD for OSPF
==========================

Understanding BFD for OSPF

#### Definition

Bidirectional Forwarding Detection (BFD) is a mechanism for detecting communication faults between systems.

Specifically, BFD detects the connectivity of a data protocol along a path between two systems. Such a path can be a physical link, a logical link, or a tunnel.

In BFD for OSPF, a BFD session is associated with OSPF. The session quickly detects link faults and notifies OSPF, maximizing the efficiency of OSPF's response to network topology changes.


#### Purpose

A link fault or a topology change causes devices to recalculate routes. Fast and efficient routing protocol convergence is necessary to improve network availability.

As link faults are inevitable, rapidly detecting these faults and notifying routing protocols is an effective way to quickly resolve such issues. When BFD is associated with OSPF, it can speed up OSPF convergence if a fault occurs on the link between neighbors.

**Table 1** OSPF convergence speeds before and after BFD for OSPF is configured
| With or Without BFD | Link Fault Detection Mechanism | Convergence Speed |
| --- | --- | --- |
| Without BFD | The OSPF Dead timer expires. | Within seconds |
| With BFD | The associated BFD session goes down. | Within milliseconds |



#### Fundamentals

[Figure 1](#EN-US_CONCEPT_0000001176662983__fig_dc_vrp_ospf_feature_000701) shows a typical network topology with BFD for OSPF configured.

**Figure 1** BFD for OSPF  
![](figure/en-us_image_0000001176663053.png)

1. OSPF neighbor relationships are established between the three devices.
2. After a neighbor relationship becomes Exstart, a BFD session is established.
3. The outbound interface of the route from DeviceA to DeviceB is interface 1. If the link between DeviceA and DeviceB fails, BFD detects the fault and then notifies DeviceA.
4. DeviceA processes the neighbor relationship down event and recalculates routes. The new route passes through DeviceC and reaches DeviceB, with interface 2 as the outbound interface.