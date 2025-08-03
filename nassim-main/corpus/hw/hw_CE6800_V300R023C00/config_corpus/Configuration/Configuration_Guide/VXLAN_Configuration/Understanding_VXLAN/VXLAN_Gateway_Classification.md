VXLAN Gateway Classification
============================

Similar to VLAN isolation, VXLANs identified by different VNIs or VXLANs and non-VXLANs cannot communicate with each other. To enable communication between VXLANs and between VXLANs and non-VXLANs, VXLAN gateways are deployed.

VXLAN gateways are categorized into the following types:

* Layer 2 gateway: allows tenant access to VXLANs and intra-subnet VXLAN communication.
* Layer 3 gateway: allows access to external networks and inter-subnet VXLAN communication.

Layer 3 VXLAN gateways are further categorized as centralized and distributed gateways.

#### Centralized Gateway Deployment

In this gateway deployment mode, Layer 3 gateways are deployed on a single device. For example, on the network shown in [Figure 1](#EN-US_CONCEPT_0000001176664039__fig_dc_fd_vxlan_000501), inter-subnet traffic is forwarded through Layer 3 gateways to implement centralized traffic management.

**Figure 1** Centralized VXLAN gateway networking  
![](figure/en-us_image_0000001130624526.png)
Centralized VXLAN gateway deployment has the following advantages and disadvantages:

* Advantages: Inter-subnet traffic can be centrally managed, and gateway deployment and management are simplified.
* Disadvantages:
  + Forwarding paths are not optimal. Inter-subnet Layer 3 traffic of DCs connected to the same Layer 2 gateway must be transmitted to the centralized Layer 3 gateway for forwarding.
  + The ARP entry specification is a bottleneck. ARP entries must be generated for tenants on the Layer 3 gateway, which allows only a limited number of such entries. As such, this impedes DCN expansion.


#### Distributed Gateway Deployment

* **Background**
  
  Distributed VXLAN gateway deployment addresses the problems that occur in centralized VXLAN gateway deployment. Distributed VXLAN gateway deployment typically utilizes the spine-leaf networking architecture, in which leaf nodes are used as VTEPs to establish VXLAN tunnels, and each leaf node can function as a Layer 3 VXLAN gateway. Spine nodes are unaware of VXLAN tunnels and only forward VXLAN packets between leaf nodes. On the network shown in [Figure 2](#EN-US_CONCEPT_0000001176664039__fig_dc_fd_vxlan_000502), Server1 and Server2 are on different network segments but connect to same leaf node (Leaf1). When Server1 and Server2 communicate, traffic is forwarded only through Leaf1, and not through any spine node.
  
  **Figure 2** Distributed VXLAN gateway networking  
  ![](figure/en-us_image_0000001130624528.png)
  
  A spine node is used to implement high-speed IP forwarding, whereas a
  
  leaf node can:
  + Function as a Layer 2 VXLAN gateway and connect to physical servers or VMs, allowing tenants to access VXLAN segments.
  + Function as a Layer 3 VXLAN gateway to perform VXLAN encapsulation and decapsulation, allowing inter-subnet communication and access to external networks.
* **Characteristics**
  + Flexible deployment: A leaf node can function as both a Layer 2 and Layer 3 VXLAN gateway.
  + Improved network expansion capabilities: Unlike a centralized Layer 3 gateway, which must learn the ARP entries of all servers on a network, a distributed gateway (leaf node) only needs to learn the ARP entries of servers attached to it in distributed gateway deployment mode. As a result, the ARP entry specification is no longer a bottleneck on a distributed gateway.