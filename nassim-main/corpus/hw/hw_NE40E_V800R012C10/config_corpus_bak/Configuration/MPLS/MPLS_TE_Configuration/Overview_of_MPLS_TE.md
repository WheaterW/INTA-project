Overview of MPLS TE
===================

The Multiprotocol Label Switching Traffic Engineering (MPLS TE) technology integrates the MPLS technology with TE. It reserves resources by establishing label switched paths (LSPs) over a specified path in an attempt to prevent network congestion and balance network traffic.

#### TE

Network congestion is a major cause for backbone network performance deterioration. The network congestion is resulted from insufficient resources or locally induced by incorrect resource allocation. For the former, network device expansion can prevent the problem. For the later, TE is used to allocate some traffic to idle link so that traffic allocation is improved. TE dynamically monitors network traffic and loads on network elements and adjusts the parameters for traffic management, routing, and resource constraints in real time, which prevents network congestion induced by load imbalance.


#### MPLS TE

MPLS TE establishes constraint-based routed label switched paths (LSPs) and transparently transmits traffic over the LSPs. Based on certain constraints, the LSP path is controllable, and links along the LSP reserve sufficient bandwidth for service traffic. In the case of resource insufficiency, the LSP with a higher priority can preempt the bandwidth of the LSP with a lower priority to meet the requirements of the service with a higher priority. In addition, when an LSP fails or a node on the network is congested, MPLS TE can provide protection through Fast Reroute (FRR) and a backup path. MPLS TE allows network administrators to deploy LSPs to properly allocate network resources and prevent network congestion. As the number of LSPs increases, you can use a dedicated offline tool to analyze traffic.