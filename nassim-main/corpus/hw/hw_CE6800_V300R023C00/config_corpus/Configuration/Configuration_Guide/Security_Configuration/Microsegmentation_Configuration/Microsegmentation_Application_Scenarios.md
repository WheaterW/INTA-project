Microsegmentation Application Scenarios
=======================================

Microsegmentation Application Scenarios

#### Local Forwarding of Layer 3 Packets on the VXLAN Network

On the distributed VXLAN network shown in [Figure 1](#EN-US_CONCEPT_0000001563994777__fig16392644171811), Leaf1 is VTEP1 and connected to Host1 and Host2. Access traffic between Host1 and Host2 only needs to be forwarded on Leaf1. Host1 belongs to EPG1 and Host2 belongs to EPG2.

**Figure 1** Local forwarding of Layer 3 packets on the VXLAN network  
![](figure/en-us_image_0000001563994789.png)
Host1's access to Host2 exemplifies microsegmentation when Layer 3 packets are locally forwarded on the VXLAN network.

1. After VTEP1 receives packets sent from Host1 to Host2, it obtains the source IP address of 192.168.10.1 and destination IP address of 192.168.20.2 from the packets.
2. According to the source IP address, VTEP1 searches for TCAM entries based on the longest match principle and obtains the ID of the EPG (EPG1) that Host1 belongs to.
3. According to the destination IP address, VTEP1 searches for the routing table and finds that Host2 is also connected to VTEP1. That is, packets only need to be forwarded locally. According to the destination IP address, VTEP1 searches for TCAM entries based on the longest match principle and obtains the ID of the EPG (EPG2) that Host2 belongs to.
4. VTEP1 searches for TCAM entries based on EPG1 and EPG2 that Host1 and Host2 belong to, respectively. It obtains GBPs between EPG1 and EPG2 and performs traffic control based on GBPs.


#### Inter-device Forwarding of Layer 3 Packets on the VXLAN Network

On the distributed VXLAN network shown in [Figure 2](#EN-US_CONCEPT_0000001563994777__fig5812241171916), Leaf1 and Leaf2 are VTEP1 and VTEP2 and are connected to Host1 and Host3, respectively. Access traffic between Host1 and Host3 needs to be forwarded over the VXLAN tunnel across devices. Host1 belongs to EPG1 and Host3 belongs to EPG3.

**Figure 2** Inter-device forwarding of Layer 3 packets on the VXLAN network  
![](figure/en-us_image_0000001513034550.png)
Host1's access to Host3 exemplifies microsegmentation when Layer 3 packets are forwarded across devices on the VXLAN network.

1. After VTEP1 receives packets sent from Host1 to Host3, it obtains the source IP address of 192.168.10.1 and destination IP address of 192.168.30.3 from the packets.
2. According to the source IP address, VTEP1 searches for TCAM entries based on the longest match principle and obtains the ID of the EPG (EPG1) that Host1 belongs to.
3. According to the destination IP address, VTEP1 searches for the routing table and finds that Host3 is connected to VTEP2. After packets are encapsulated with the VXLAN header, the packets are forwarded over the VXLAN tunnel across devices. During VXLAN encapsulation, VTEP1 resets the **G flag bit** in the VXLAN packet header, encapsulates EPG1 that Host1 belongs to into the **Group Policy ID** field of the VXLAN packet header, and sends the packets to VTEP2.
4. After receiving VXLAN packets sent by VTEP1, VTEP2 decapsulates the VXLAN packets. VTEP2 finds that the **G** flag bit is 1 and obtains EPG1 of Host1 from the **Group Policy ID** field.
5. According to the inner destination IP address, VTEP2 searches for TCAM entries based on the longest match principle and obtains the ID of the EPG (EPG3) that Host3 belongs to.
6. VTEP2 searches for TCAM entries based on EPG1 and EPG3 that Host1 and Host3 belong to, respectively. It obtains GBPs between EPG1 and EPG3 and performs traffic control based on GBPs.