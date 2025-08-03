Understanding URPF
==================

Understanding URPF

#### Working Mode

On a complex network, the routing paths recorded on a remote device may be different from those recorded on the local device. A URPF-enabled device on such a network may discard packets received from valid paths. To solve this problem, the device provides two URPF modes:

* **Strict mode**
  
  In strict mode, the device allows a packet to pass through only when there is a route to the source IP address of the packet in its FIB table and the inbound interface of the packet is the same as the outbound interface of the route.
  
  You are advised to use the strict mode when you are sure that the routing paths recorded on the local and remote devices are the same. For example, if there is only one path between two network edge devices, strict mode can be used to ensure network security.
* **Loose mode**
  
  In loose mode, the device allows a packet to pass through as long as there is a route to the source IP address of the packet in its FIB table. In contrast to strict mode, the inbound interface of the packet does not need to be the same as the outbound interface of the route.
  
  You are advised to use the loose mode when the routing paths recorded on the local and remote devices may be different. For example, if there are multiple paths between two network edge devices, the loose mode can be used to effectively protect the device against network attacks while preventing valid packets from being discarded.

#### Implementation

[Figure 1](#EN-US_CONCEPT_0000001513030738__fig12480103514270) shows how URPF is implemented.

**Figure 1** URPF implementation  
![](figure/en-us_image_0000001512671602.png)