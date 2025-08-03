Understanding How to Use Segment VXLAN for Layer 3 Interworking
===============================================================

Understanding How to Use Segment VXLAN for Layer 3 Interworking

#### Background

Segment VXLAN is usually used to establish one VXLAN tunnel segment in each of two DCs and also to establish one VXLAN tunnel segment between the DCs. As shown in [Figure 1](#EN-US_CONCEPT_0000001560863472__fig_dc_vrp_vxlan_feature_300701), BGP EVPN is configured to create a VXLAN tunnel in distributed gateway mode within both DC A and DC B so that the VMs deployed in each DC can communicate with each other. Leaf2 and Leaf3 are the edge devices within the DCs that connect to the backbone network. BGP EVPN is configured to create a VXLAN tunnel between Leaf2 and Leaf3 so that the VXLAN packets received by one DC can be decapsulated, re-encapsulated, and sent to the peer DC. This process allows the VXLAN tunnel to transmit inter-DC packets end to end and ensures that the VMs in different DCs can communicate with each other.

**Figure 1** Configuring segment VXLAN for Layer 3 interworking  
![](figure/en-us_image_0000001581730682.png)

#### Fundamentals

**Control Plane**

The following describes how a segment VXLAN tunnel is established.

1. Leaf4 learns the IP address of VMb2 in DC B and saves it to the routing table of the L3VPN instance. Leaf4 then sends a BGP EVPN route to Leaf3.
2. Upon receipt (as shown in [Figure 2](#EN-US_CONCEPT_0000001560863472__fig_dc_vrp_vxlan_feature_300702)), Leaf3 obtains the host IP route contained in the route and establishes a VXLAN tunnel to Leaf4. Leaf3 then sets the next hop of the route to its own VTEP address, re-encapsulates the route with the L3VNI of the L3VPN instance, sets the source MAC address to its own MAC address, and sends the re-encapsulated BGP EVPN route to Leaf2.**Figure 2** Control plane process  
   ![](images/fig_dc_fd_vxlan_002802dcf.png)
3. Upon receipt, Leaf2 obtains the host IP route contained in the route and establishes a VXLAN tunnel to Leaf3. Leaf2 then sets the next hop of the route to its own VTEP address, re-encapsulates the route with the L3VNI of the L3VPN instance, sets the source MAC address to its own MAC address, and sends the re-encapsulated BGP EVPN route to Leaf1.
4. Upon receipt, Leaf1 establishes a VXLAN tunnel to Leaf2.

**Forwarding Plane**

1. Leaf1 receives a Layer 2 packet destined for VMb2 from VMa1 and determines that the destination MAC address in the packet is the gateway interface's MAC address. Leaf1 then terminates the Layer 2 packet and finds the L3VPN instance corresponding to the VBDIF interface through which VMa1 accesses the BD. Leaf1 then searches the routing table of the L3VPN instance for VMb2's host route and determines that it needs to send the packet to Leaf2 over the VXLAN tunnel. Leaf1 then encapsulates the received packet as a VXLAN packet and sends it to Leaf2 over this tunnel.
2. Upon receipt, Leaf2 parses the VXLAN packet (as shown in [Figure 3](#EN-US_CONCEPT_0000001560863472__fig_dc_vrp_vxlan_feature_300703)). It finds the L3VPN instance corresponding to the L3VNI of the packet, searches the routing table of the L3VPN instance for VMb2's host route, and determines that it needs to send the packet to Leaf3 over the VXLAN tunnel. Leaf2 then re-encapsulates the packet as a VXLAN packet and sends it to Leaf3 over this tunnel.**Figure 3** Data packet forwarding  
   ![](figure/en-us_image_0000001563646326.png)
3. Upon receipt, Leaf3 parses the VXLAN packet (as shown in [Figure 3](#EN-US_CONCEPT_0000001560863472__fig_dc_vrp_vxlan_feature_300703)). It finds the L3VPN instance corresponding to the L3VNI of the packet, searches the routing table of the L3VPN instance for VMb2's host route, and determines that it needs to send the packet to Leaf4 over the VXLAN tunnel. Leaf3 then re-encapsulates the packet as a VXLAN packet and sends it to Leaf4 over this tunnel.
4. Upon receipt, Leaf4 parses the VXLAN packet. It finds the L3VPN instance corresponding to the L3VNI of the packet, and then searches the routing table of the L3VPN instance for VMb2's host route. Using this routing information, Leaf4 forwards the packet to VMb2.