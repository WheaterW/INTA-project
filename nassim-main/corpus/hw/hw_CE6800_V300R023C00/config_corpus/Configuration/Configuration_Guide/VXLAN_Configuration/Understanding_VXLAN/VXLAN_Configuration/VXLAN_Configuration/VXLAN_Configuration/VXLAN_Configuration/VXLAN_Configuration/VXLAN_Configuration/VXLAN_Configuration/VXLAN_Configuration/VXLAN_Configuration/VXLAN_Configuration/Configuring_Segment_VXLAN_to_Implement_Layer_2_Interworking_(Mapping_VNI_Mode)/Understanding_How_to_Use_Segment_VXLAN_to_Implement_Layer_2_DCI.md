Understanding How to Use Segment VXLAN to Implement Layer 2 DCI
===============================================================

Understanding How to Use Segment VXLAN to Implement Layer 2 DCI

#### Background

[Figure 1](#EN-US_CONCEPT_0000001259907887__fig_dc_fd_vxlan_004001) shows a typical scenario where segment VXLAN is used to implement Layer 2 DCI. One VXLAN tunnel needs to be configured within DC A, one within DC B, and one between the transit leaf nodes in the two DCs. To enable communication between VM1 and VM2, Layer 2 connectivity must be established between DC A and DC B. In practice, however, different DCs have their own VNI spaces. Therefore, the VXLAN tunnels within DC A and DC B tend to use different VNIs. In this case, to establish a VXLAN tunnel between Transit Leaf1 and Transit Leaf2, VNI conversion is required.

**Figure 1** Configuring segment VXLAN to for Layer 2 interworking  
![](figure/en-us_image_0000001215470728.png)

#### Benefits

Segment VXLAN offers the following benefits to users:

* Enables Layer 2 communication between hosts in different DCs.
* Decouples the VNI space of the intra-DC network from that of the inter-DC network, simplifying network maintenance.
* Isolates network faults within a DC from those that span multiple DCs, facilitating fault location.

#### Fundamentals

Segment VXLAN is similar to VLAN mapping. In segment VXLAN, packets exchanged between transit leaf nodes use the same mapping VNI for VXLAN encapsulation.

**Control Plane**

![](../public_sys-resources/note_3.0-en-us.png) 

The establishment of VXLAN tunnels between leaf nodes is the same as that for intra-subnet interworking in common VXLAN scenarios. Therefore, the detailed process is omitted here. Regarding the control plane, MAC address learning by a host is described here.

[Figure 2](#EN-US_CONCEPT_0000001259907887__fig20791182212577) shows how the control plane works in mapping VNI mode.

**Figure 2** Control plane in mapping VNI mode  
![](figure/en-us_image_0000001219685398.png)

1. Server Leaf1 learns VM1's MAC address, generates a BGP EVPN route, and sends it to Transit Leaf1. The BGP EVPN route contains the following information:
   
   * Type 2 route: EVPN instance's RD value, VM1's MAC address, and Server Leaf1's local VNI
   * Next hop: Server Leaf1's VTEP IP address
   * Extended community attribute: encapsulated tunnel type (VXLAN)
   * ERT: EVPN instance's export RT value
2. Upon receipt, Transit Leaf1 adds the BGP EVPN route to its local EVPN instance and generates a MAC address entry for VM1 in the EVPN instance-bound BD. Based on the next hop and encapsulated tunnel type, the MAC address entry's outbound interface recurses to the VXLAN tunnel destined for Server Leaf1. The VNI in the VXLAN tunnel encapsulation information is Server Leaf1's local VNI.
3. Transit Leaf1 re-originates the BGP EVPN route. When modifying VNI information, Transit Leaf1 searches the BD ID-local VNI mapping table for the desired mapping VNI and then changes the re-originated route's VNI to the mapping VNI. The re-originated BGP EVPN route contains the following information:
   
   * Type 2 route: EVPN instance's RD value, VM1's MAC address, and mapping VNI for the local VNI
   * Next hop: Transit Leaf1's VTEP IP address
   * Extended community attribute: encapsulated tunnel type (VXLAN)
   * ERT: EVPN instance's export RT value
4. Upon receipt, Transit Leaf2 adds the re-originated BGP EVPN route to its local EVPN instance and generates a MAC address entry for VM1 in the EVPN instance-bound BD. Based on the next hop and encapsulated tunnel type, the MAC address entry's outbound interface recurses to the VXLAN tunnel destined for Transit Leaf1. The VNI in the VXLAN tunnel encapsulation information is the mapping VNI.
5. Transit Leaf2 re-originates the BGP EVPN route. When modifying VNI information, Transit Leaf2 searches the BD ID-mapping VNI mapping table for the desired local VNI and then changes the re-originated route's VNI to the local VNI. The re-originated BGP EVPN route contains the following information:
   
   * Type 2 route: EVPN instance's RD value, VM1's MAC address, and local VNI for the mapping VNI
   * Next hop: Transit Leaf2's VTEP IP address
   * Extended community attribute: encapsulated tunnel type (VXLAN)
   * ERT: EVPN instance's export RT value
6. Upon receipt, Server Leaf2 adds the re-originated BGP EVPN route to its local EVPN instance and generates a MAC address entry for VM1 in the EVPN instance-bound BD. Based on the next hop and encapsulated tunnel type, the MAC address entry's outbound interface recurses to the VXLAN tunnel destined for Transit Leaf2. The VNI in the VXLAN tunnel encapsulation information is Server Leaf2's local VNI.

![](../public_sys-resources/note_3.0-en-us.png) 

* The preceding process uses MAC address learning by VM1 as an example. MAC address learning by VM2 is the same, and is omitted here.
* VXLAN tunnels both within DCs and between DCs are established in BGP EVPN mode in the preceding process. If the VXLAN tunnels are established in static mode, MAC addresses are learned during data forwarding. The next-hop VTEP IP address and VNIs (outbound VNI and mapping VNI) in the VXLAN tunnel encapsulation information must be manually configured.

**Forwarding Plane****Figure 3** Known unicast packet forwarding in mapping VNI mode  
![](figure/en-us_image_0000001259910599.png)

1. After receiving a Layer 2 packet from VM2 through a BD Layer 2 sub-interface, Server Leaf2 uses the destination MAC address to search the BD's MAC address table for the VXLAN tunnel's outbound interface and obtains the VXLAN tunnel encapsulation information (local VNI, destination VTEP IP address, and source VTEP IP address). Based on the obtained information, Server Leaf2 encapsulates the packet into a VXLAN packet and sends the packet to Transit Leaf2.
2. Upon receipt, Transit Leaf2 decapsulates the VXLAN packet, finds the target BD based on the VNI, uses the destination MAC address to search the BD's MAC address table for the VXLAN tunnel's outbound interface, and obtains the VXLAN tunnel encapsulation information (mapping VNI, destination VTEP IP address, and source VTEP IP address). Based on the obtained information, Transit Leaf2 encapsulates the packet into a new VXLAN packet and sends the packet to Transit Leaf1.
3. Upon receipt, Transit Leaf1 decapsulates the VXLAN packet, finds the target BD based on the VNI, uses the destination MAC address to search the BD's MAC address table for the VXLAN tunnel's outbound interface, and obtains the VXLAN tunnel encapsulation information (outbound VNI, destination VTEP IP address, and source VTEP IP address). Based on the obtained information, Transit Leaf1 encapsulates the packet into a new VXLAN packet and sends the packet to Server Leaf1.
4. Upon receipt, Server Leaf1 decapsulates the VXLAN packet and forwards it at Layer 2 to VM1.

![](../public_sys-resources/note_3.0-en-us.png) 

In the scenario with segment VXLAN for Layer 2 interworking, BUM packet forwarding is the same as that in the common VXLAN scenario except that a split horizon group is used to prevent loops:

* After receiving BUM packets from a server leaf node in a DC, a transit leaf node in the same DC obtains the split horizon group to which the source VTEP belongs. Because all nodes in the same DC belong to the same default split horizon group, BUM packets will not be replicated to other server leaf nodes within the DC. However, as the peer transit leaf node belongs to a different split horizon group, BUM packets will be replicated to the peer transit leaf node.
* Upon receipt, the peer transit leaf node obtains the split horizon group to which the source VTEP belongs. Because this transit leaf node belongs to the same split horizon group as its peer transit leaf node, it will not replicate the BUM packets to its peer transit leaf node. However, as this transit leaf node belongs to a different split horizon group from the server leaf nodes within a DC, it will replicate the BUM packets to them.