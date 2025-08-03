Understanding BFD for OSPFv3
============================

Understanding BFD for OSPFv3

#### Definition

Bidirectional Forwarding Detection (BFD) is a mechanism for detecting communication faults between systems.

Specifically, BFD detects the connectivity of a data protocol along a path between two systems. Such a path can be a physical link, a logical link, or a tunnel.

In BFD for OSPFv3, a BFD session is associated with OSPFv3. The session quickly detects link faults and notifies OSPFv3, speeding up OSPFv3 response to network topology changes.


#### Purpose

A link fault or a topology change causes devices to recalculate routes. Fast and efficient routing protocol convergence is necessary to improve network availability.

As link faults are inevitable, rapidly detecting these faults and notifying routing protocols is an effective way to quickly resolve such issues. If BFD is associated with the routing protocol, once a link fault occurs, BFD can speed up the convergence of the routing protocol.

**Table 1** Benefits of BFD for OSPFv3
| With or Without BFD | Link Fault Detection Mechanism | Convergence Speed |
| --- | --- | --- |
| Without BFD | The OSPFv3 Dead timer expires. | Within seconds |
| With BFD | The associated BFD session goes down. | Within milliseconds |



#### Fundamentals

[Figure 1](#EN-US_CONCEPT_0000001176662763__en-us_concept_0275858004_fig_dc_vrp_ospfv3_feature_200601) shows a typical network topology with BFD for OSPFv3 configured.

**Figure 1** BFD for OSPFv3 implementation  
![](figure/en-us_image_0000001229801095.png)

1. OSPFv3 neighbor relationships are established between the three devices.
2. After a neighbor relationship becomes Exstart, a BFD session is established.
3. The outbound interface of the route from DeviceA to DeviceB is interface 1. If the link between DeviceA and DeviceB fails, BFD detects the fault and then notifies DeviceA.
4. DeviceA processes the neighbor relationship down event and recalculates routes. The new route passes through DeviceC to reach DeviceB, with interface 2 as the outbound interface.