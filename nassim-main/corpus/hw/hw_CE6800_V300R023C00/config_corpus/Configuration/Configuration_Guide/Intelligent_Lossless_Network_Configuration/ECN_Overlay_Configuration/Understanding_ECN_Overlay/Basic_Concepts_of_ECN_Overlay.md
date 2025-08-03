Basic Concepts of ECN Overlay
=============================

Basic Concepts of ECN Overlay

#### ECN Field in an IP Packet

**Figure 1** ECN field in an IP packet  
![](figure/en-us_image_0000001513170050.png)

The ECN field in an IP packet can transmit the congestion status. As shown in [Figure 1](#EN-US_CONCEPT_0000001512690878__fig336717331830), the type of service (ToS) field in an IP header consists of eight bits. Bits 0 to 2 constitute the precedence field, which specifies the precedence of packet transmission. The eight precedence values are represented by digits 0 through 7, with a larger digit indicating a higher precedence. Bits 0 to 5 specify the differentiated services code point (DSCP) value, and bits 6 and 7 constitute the ECN field.

* If the value of the ECN field is 00, the packet does not support ECN and is marked as Non-ECN Capable Transport (ECT).
* If the value of the ECN field is 01 or 10, the packet supports ECN and is marked as ECT, indicating the forwarding path of the packet is not congested.
* If the value of the ECN field is 11, the packet supports ECN and is marked as Congestion Experienced (CE), indicating the forwarding path of the packet is congested.

Therefore, a forwarding device can notify the traffic receiver of congestion on the forwarding device by setting the ECN field of packets to CE.


#### Overlay Deployment Modes

Based on the deployment mode of VXLAN tunnel endpoints (VTEPs), that is, the deployment location of network virtualization edges (NVEs), there are three overlay deployment modes:

* **Network overlay**
  
  In network overlay, all VTEPs are deployed on physical devices that perform VXLAN encapsulation and decapsulation.
  
  **Figure 2** Network overlay  
  ![](figure/en-us_image_0000001512850486.png)
* **Host overlay**
  
  In host overlay, all VTEPs are deployed on vSwitches installed on servers, and the vSwitches perform VXLAN encapsulation and decapsulation.
  
  **Figure 3** Host overlay  
  ![](figure/en-us_image_0000001564130133.png)
* **Hybrid overlay**
  
  In hybrid overlay, VTEPs are deployed on physical devices and vSwitches, both of which may perform VXLAN encapsulation and decapsulation.
  
  **Figure 4** Hybrid overlay  
  ![](figure/en-us_image_0000001563890029.png)