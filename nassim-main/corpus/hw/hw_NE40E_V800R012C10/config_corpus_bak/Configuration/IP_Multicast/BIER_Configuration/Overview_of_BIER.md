Overview of BIER
================

Overview_of_BIER

#### Purpose

In traditional multicast technologies, a multicast distribution tree (MDT) is established for each multicast flow, so that the multicast flow is replicated along this specific MDT. In this way, the flow is transmitted and network bandwidth is saved. Traditional multicast technology has the following characteristics:

* An MDT needs to be established for each multicast flow, and each node in the MDT needs to maintain the multicast state. For example, PIM on the public network requires that a PIM MDT be established for each multicast flow. NG MVPN requires that a P2MP tunnel be established for each multicast flow. The P2MP tunnel is equivalent to a P2MP MDT.
* When a new multicast user joins a multicast group, the user needs to be added to the MDT hop by hop.

Traditional multicast technologies, however, cannot meet the requirements for rapid development of multicast services in the following aspects:

* With the increase of multicast services, the number of MDTs that need to be maintained by traditional multicast technologies increases sharply. Each node on the network is required to maintain the states of a large number of multicast flows. When the network changes, the convergence of multicast entries is slow.
* Multicast users are added to MDTs hop by hop, which increases the delay for users to be added to MDTs, and multicast services cannot be quickly deployed. In addition, large-scale multicast service requirements cannot be met. For example, to implement fast multicast service deployment on SDN networks, it may be expected that a controller delivers destination information to edge nodes for multicast replication.

To solve this problem, Bit Index Explicit Replication (BIER) uses the BitString format to encapsulate the set of destinations to which multicast packets are to be sent in the packet header and then sends the packets.


#### Definition

BIER is a new multicast technology. It encapsulates the set of destinations of multicast packets in the BitString format in the packet header before sending the packets. Intermediate network nodes do not need to establish an MDT for each multicast flow or maintain the states of multicast flows. Instead, the intermediate network nodes perform packet replication and forwarding according to the destination set in the packet header.

In BIER, each destination node is a network edge node. For example, on a network with less than 256 edge nodes, each node needs to be configured with a unique value from 1 to 256. In this case, the set of destinations is represented by a 256-bit (32-byte) BitString, and the position or index of each bit in the BitString indicates an edge node.


#### Benefits

BIER offers the following benefits:

* Reduces resource consumption in large-scale multicast service scenarios, as BIER does not need to establish an MDT for each multicast flow or maintain the states of multicast flows.
* Improves multicast group joining efficiency of the multicast users in SDN network scenarios because multicast users do not need to be added to MDTs hop by hop and instead their requests are directly sent by leaf nodes to the ingress node. This is more suitable for the controller on an SDN network to directly deliver the set of destinations to which multicast packets are to be sent after collecting the set.