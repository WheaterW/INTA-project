Understanding VLAN Mapping
==========================

Understanding VLAN Mapping

#### Definition and Application

The VLAN mapping function enables a device to change VLAN tags in packets to map different VLANs.

This function applies to the following scenarios:

* Two Layer 2 user networks in the same VLAN are connected through a backbone network. To allow user communication at Layer 2 and uniformly deploy Layer 2 protocols, the two user networks need to interwork seamlessly. In this case, the backbone network needs to transmit the VLAN-tagged Layer 2 packets of the user networks; however, the backbone network cannot directly transmit such packets between the user networks, because the VLAN plans on the backbone and user networks are different.
  
  To solve this problem, VLAN mapping is used. When VLAN-tagged packets from a user network arrive at the backbone network, an edge device on the backbone network changes the customer VLAN (C-VLAN) ID to the service provider VLAN (S-VLAN) ID. After the packets arrive at the edge device connected to the destination user network, the edge device retrieves the C-VLAN IDs to ensure seamless interworking between the two user networks.
* If VLAN IDs on two directly connected Layer 2 networks are different due to different VLAN plans, you can configure VLAN mapping on the devices connecting the two networks to map VLAN IDs on the two networks. This means the two networks can be managed as a single Layer 2 network, while it helps implement Layer 2 user communication and unified deployment of Layer 2 protocols.

![](public_sys-resources/note_3.0-en-us.png) 

VLAN-based VLAN mapping can be configured only on the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S.



#### Category

VLAN mapping is classified into VLAN-based VLAN mapping and MQC-based VLAN mapping. VLAN-based VLAN mapping includes the following mapping modes:

* 1 to 1 mapping mode
  
  When an interface on a device configured with VLAN mapping receives a single-tagged packet, the interface replaces the VLAN tag in the packet with a new VLAN tag.
* 2 to 1 mapping mode
  + When an interface on a device configured with VLAN mapping receives a double-tagged packet, the interface maps both the inner and outer VLAN tags to one VLAN tag.
* 2 to 2 mapping mode
  + When an interface on a device configured with VLAN mapping receives a double-tagged packet, the interface replaces both the inner and outer VLAN tags with a new VLAN tag.
  + When an interface on a device configured with VLAN mapping receives a double-tagged packet, the interface replaces the outer VLAN tag with a new VLAN tag and transparently transmits the inner VLAN tag as data.

MQC-based VLAN mapping uses MQC to implement VLAN mapping for classified packets. Packets can be classified based on matching rules in a traffic classifier. To re-mark the VLAN IDs in classified packets, configure a traffic policy to associate a traffic classifier with a traffic behavior defining VLAN mapping. MQC-based VLAN mapping provides differentiated services based on service types.


#### Fundamentals

Once a device receives a VLAN-tagged packet, it determines whether to replace a single tag, double tags, or the outer tag based on the configured VLAN mapping mode. The device then learns the MAC addresses carried in the packet, and updates the corresponding MAC address entry based on the source MAC address and translated VLAN ID. The device searches for a matching MAC address entry based on the destination MAC address and translated VLAN ID. If such an entry is found, the device forwards the packet through the corresponding outbound interface; however, if not, the device broadcasts the packet in the VLAN with the translated VLAN ID.

[Figure 1](#EN-US_CONCEPT_0000001176742321__fig1323764016438) shows how VLAN mapping works. The mapping between VLAN 2 and VLAN 3 is configured on interface 1 on DeviceA. When sending a frame from VLAN 2 to VLAN 3, interface 1 replaces the VLAN ID 2 with VLAN ID 3. When receiving a frame from VLAN 3 to VLAN 2, interface 1 replaces the VLAN ID 3 with VLAN ID 2. This implements communication between devices in VLAN 2 and VLAN 3.

![](public_sys-resources/note_3.0-en-us.png) 

If devices in two VLANs need to communicate using VLAN mapping, the IP addresses of these devices must be on the same network segment. Otherwise, communication between these devices must be implemented using Layer 3 routes, making VLAN mapping invalid.


**Figure 1** VLAN mapping  
![](figure/en-us_image_0000001176742351.png)