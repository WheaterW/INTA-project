Definition and Classification of Load Balancing
===============================================

Load balancing allows a network node to distribute traffic among multiple links for forwarding. It is classified as route, tunnel, or trunk load balancing.

#### Route Load Balancing

Route load balancing enables traffic to be balanced among multiple forwarding paths to the same destination. If there are multiple routes with the same destination address and mask but different next hops, outbound interfaces, or tunnel IDs, route load balancing can be implemented, as shown in [Figure 1](#EN-US_CONCEPT_0000001512681954__fig_load-balance_feature_00401).

**Figure 1** Route load balancing  
![](figure/en-us_image_0000001513161146.png)

#### Tunnel Load Balancing

On a VPN, tunnel load balancing enables traffic to be balanced among the ingress PE's multiple tunnels that are destined for the same destination PE, as shown in [Figure 2](#EN-US_CONCEPT_0000001512681954__fig_load-balance_feature_00402).

**Figure 2** Tunnel load balancing  
![](figure/en-us_image_0000001564121261.png)

#### Trunk Load Balancing

Trunk load balancing enables traffic to be balanced among multiple member links of a trunk after multiple physical interfaces with the same link layer protocol are bundled into the trunk, as shown in [Figure 3](#EN-US_CONCEPT_0000001512681954__fig_load-balance_feature_00403).

**Figure 3** Trunk load balancing  
![](figure/en-us_image_0000001512841618.png)