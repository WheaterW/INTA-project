VLAN Overview
=============

The VLAN technology is important for Layer 2 network forwarding. This section describes the background, functions, and advantages of the VLAN technology.

#### Introduction

The traditional LAN technology based on the bus structure has the following defects:

* Conflicts are inevitable if multiple nodes send messages simultaneously.
* Messages are broadcast to all nodes.
* Networks have security risks as all the hosts in a LAN share the same transmission channel.

The network constructs a collision domain. More computers on the network cause more conflicts and lower network efficiency. The network is also a broadcast domain. When many computers on the network send data, broadcast traffic consumes much bandwidth.

Traditional networks face collision domain and broadcast domain issues, and cannot ensure information security.

To reduce the broadcast traffic, you need to enable the broadcast only among hosts that need to communicate with each other, and isolate the hosts that do not need the broadcast. A Router can select routes based on IP addresses and effectively suppress broadcast
traffic between two connected network segments. The Router solution, however, is costly. Therefore, multiple logical LANs, namely, VLANs are developed on the physical LAN.

In this manner, a physical LAN is divided into multiple broadcast domains, that is, multiple VLANs. The intra-VLAN communication is not restricted, while the inter-VLAN communication
is restricted. As a result, network security is enhanced.


#### Definition

The virtual local area network (VLAN) technology logically divides a physical LAN into multiple VLANs that are broadcast domains. Each VLAN contains a group of PCs that have the same requirements. A VLAN has the same attributes as a LAN. PCs of a VLAN can be placed on different LAN segments. Hosts
can communicate within the same VLAN, while cannot communicate in different VLANs. If two PCs are located on one LAN segment but belong to different VLANs, they do not broadcast packets to each other. In this manner, network security is enhanced.

[Figure 1](feature_0003994398.html#EN-US_CONCEPT_0172352265__fig_dc_vrp_vlan_feature_000101) is a networking diagram of a typical VLAN application. Device A, Device B, and Device C are placed at different locations, such as different floors in an office building. Each switch connects to three computers which belong to three different VLANs. In [Figure 1](feature_0003994398.html#EN-US_CONCEPT_0172352265__fig_dc_vrp_vlan_feature_000101), each dashed line frame identifies a VLAN. Packets of enterprise customers in the same VLAN are broadcast within the VLAN but not among VLANs. In this way, enterprise customers in the same VLAN can share resources as well as protect their information security.

**Figure 1** Typical VLAN application
  
![](images/fig_feature_image_0003992673.png)  


This application shows the following VLAN advantages:

* Broadcast domains are confined. A broadcast domain is confined to a VLAN. This saves bandwidth and improves network processing capabilities.
* Network security is enhanced. Packets from different VLANs are separately transmitted. PCs in one VLAN cannot directly communicate with PCs in another VLAN.
* Network robustness is improved. A fault in a VLAN does not affect PCs in other VLANs.
* Virtual groups are set up flexibly. With the VLAN technology, PCs in different geographical areas can be grouped together. This facilitates network construction and maintenance.


#### Basic VLAN Concepts and Principles

* 802.1q and VLAN frame format
  
  A conventional Ethernet frame is encapsulated with the Length/Type field for an upper-layer protocol following the Destination address and Source address fields, as shown in [Figure 2](#EN-US_CONCEPT_0172363048__fig_dc_vrp_vlan_cfg_000203).
  
  **Figure 2** Conventional Ethernet frame format  
  ![](figure/en-us_image_0000001367344785.png)
  
  IEEE 802.1Q modifies the Ethernet frame format by adding a 4-byte 802.1Q tag between the source MAC address field and the Length/Type field, as shown in [Figure 1](feature_0003992551.html#EN-US_CONCEPT_0172352271__fig_dc_vrp_vlan_feature_000401).
  
  **Figure 3** VLAN frame format defined in IEEE 802.1Q  
  ![](figure/en-us_image_0000001488752781.png)
  
  An 802.1Q tag contains four fields:
  
  + EType
    
    The 2-byte EType field indicates a frame type. If the value of the field is 0x8100, it indicates an 802.1Q frame. If a device that does not support 802.1Q frames receives an 802.1Q frame, it discards the frame.
  + PRI
    
    The 3-bit Priority field indicates the frame priority. A greater PRI value indicates a higher frame priority. Frames with a higher priority are preferentially sent in the case of congestion.
  + CFI
    
    The 1-bit Canonical Format Indicator (CFI) field indicates whether a MAC address is in the canonical format. If the CFI field value is 0, the MAC address is in canonical format. If the CFI field value is 1, the MAC address is not in canonical format. This field is mainly used to differentiate among Ethernet frames, Fiber Distributed Digital Interface (FDDI) frames, and token ring frames. The CFI field value in an Ethernet frame is 0.
  + VID
    
    The 12-bit VLAN ID (VID) field indicates to which VLAN a frame belongs. A VID is an integer ranging from 0 to 4095. The values 0 and 4095 are reserved, and therefore available VIDs are in the range from 1 to 4094.
    
    Each frame sent by an 802.1Q-capable switch carries a VID. On a VLAN, Ethernet frames are classified into the following types:
    - Tagged frames: frames with 4-byte 802.1Q tags.
    - Untagged frames: frames without 4-byte 802.1Q tags.
* Port-based VLAN classification
  
  VLANs are classified based on port numbers. In this mode, VLANs are classified based on the numbers of ports on a switching device. The network administrator configures a unique PVID for each port on the switch. When a data frame reaches a port which is configured with a PVID, the frame is marked with the PVID if the data frame carries no VLAN tag. If the data frame carries a VLAN tag, the switch will not add a VLAN tag to the data frame even if the port is configured with a PVID. Different types of ports process VLAN frames in different manners.
* Type of VLAN links
  
  **Figure 4** VLAN links  
  ![](figure/en-us_image_0000001316258062.png)
  
  As shown in [Figure 4](#EN-US_CONCEPT_0172363048__fig_dc_vrp_vlan_cfg_000205), there are the following types of VLAN links:
  
  + Access link: a link connecting a user host and a switch. Generally, a host does not know which VLAN it belongs to, and host hardware cannot identify frames with VLAN tags. Therefore, hosts send and receive only untagged frames.
  + Trunk link: a link connecting switches. Data of different VLANs is transmitted along a trunk link. The two ends of a trunk link must be able to identify the VLANs to which the data frames belong. Therefore, only tagged frames are transmitted along trunk links.
* Port types
  
  [Table 1](#EN-US_CONCEPT_0172363048__tab_dc_vrp_vlan_cfg_000202) lists VLAN port types.
  
  **Table 1** Port types
  | Port Type | Method for Processing a Received Untagged Frame | Method for Processing a Received Tagged Frame | Method for Sending a Frame | Application |
  | --- | --- | --- | --- | --- |
  | Access port | Accepts the frame and adds a tag with the default VLAN ID to the frame. | + Accepts the frame if the VLAN ID carried in the frame is the same as the default VLAN ID. + Discards the frame if the VLAN ID carried in the frame is different from the default VLAN ID. | Removes the tag from the frame and sends the frame. | An access port connects a switch to a PC and can be added to only one VLAN. |
  | Trunk port | Discards the frame. | + Accepts the frame if the port permits the VLAN ID carried in the frame. + Discards the frame if the port denies the VLAN ID carried in the frame. | + Directly sends the frame if the port permits the VLAN ID carried in the frame. + Discards the frame if the port denies the VLAN ID carried in the frame. | A trunk port can be added to multiple VLANs to send and receive frames for these VLANs. A trunk port connects a switch to another switch or to a router. |
  | Hybrid port | + If only the **port default vlan** command is run on a hybrid port, the hybrid port receives the frame and adds the default VLAN tag to the frame. + If only the **port trunk allow-pass** command is run on a hybrid port, the hybrid port discards the frame. + If both the **port default vlan** and **port trunk allow-pass** commands are run on a hybrid port, the hybrid port receives the frame and adds the VLAN tag with the default VLAN ID specified in the **port default vlan** command to the frame. | + If only the **port default vlan** command is run on a hybrid port:   - The hybrid port accepts the frame if the frame's VLAN ID is the same as the default VLAN ID of the port.   - The hybrid port discards the frame if the frame's VLAN ID is different from the default VLAN ID of the port. + If only the **port trunk allow-pass** command is run on a hybrid port:   - The hybrid port accepts the frame if the frame's VLAN ID is in the permitted range of VLAN IDs.   - The hybrid port discards the frame if the frame's VLAN ID is not in the permitted range of VLAN IDs. + If both the **port default vlan** and **port trunk allow-pass** commands are run on a hybrid port:   - The hybrid port accepts the frame if the frame's VLAN ID is in the permitted range of VLAN IDs specified in the **port trunk allow-pass** command or is the same as the default VLAN ID specified in the **port default vlan** command.   - The hybrid port discards the frame if the frame's VLAN ID is not in the permitted range of VLAN IDs specified in the **port trunk allow-pass** command or is different from the default VLAN ID specified in the **port default vlan** command. | + If only the **port default vlan** command is run on the hybrid port and the frame's VLAN ID is the same as the default VLAN ID, the hybrid port removes the VLAN tag and forwards the frame. Otherwise, the hybrid port discards the frame. + If only the **port trunk allow-pass** command is run on a hybrid port:   - The hybrid port forwards the frame if the frame's VLAN ID is in the permitted range of VLAN IDs.   - The hybrid port discards the frame if the frame's VLAN ID is not in the permitted range of VLAN IDs. + If both the **port default vlan** and **port trunk allow-pass** commands are run on a hybrid port:   - The hybrid port removes the VLAN tag and forwards the frame if the frame's VLAN ID is the same as the default VLAN ID of the port.   - The hybrid port forwards the frame if the frame's VLAN ID is different from the default VLAN ID of the port but in the permitted range of VLAN IDs specified in the **port trunk allow-pass** command. Otherwise, the hybrid port discards the frame.    NOTE:  The hybrid port removes the VLAN tag and forwards the frame if the frame's VLAN ID is the same as the default VLAN ID configured using the **port default vlan** command and the default VLAN ID is in the permitted range of VLAN IDs specified in the **port trunk allow-pass** command. | A hybrid port can be added to multiple VLANs to send and receive frames of these VLANs. A hybrid port can be used to connect network devices or connect user devices. |
  | QinQ port | QinQ ports are enabled with the IEEE 802.1QinQ protocol. A QinQ port adds a tag to a single-tagged frame, and thus supports a maximum of 4094 x 4094 VLANs, which meets the requirement of a Metropolitan Area Network (MAN) for the number of VLANs. | | | |
* Principle for data switching in a VLAN
  
  Use the network shown in [Figure 4](#EN-US_CONCEPT_0172363048__fig_dc_vrp_vlan_cfg_000205) as an example. If PC1 in VLAN 2 intends to send data to PC2, the data is forwarded as follows:
  
  1. An access port on CE1 receives an untagged frame from PC1 and adds a PVID (VLAN 2) to the frame. CE1 searches the MAC address table for an outbound port. Then the frame is transmitted from the outbound port.
  2. After the trunk port on PE receives the frame, the port checks whether the VLAN ID carried in the frame is the same as that configured on the port. If the VLAN ID has been configured on the port, the port transparently transmits the frame to CE2. If the VLAN ID is not configured on the port, the port discards the frame.
  3. After a trunk port on CE2 receives the frame, the system searches the MAC address table for an outbound port, which is the access port connecting CE2 to PC2.
  4. After the frame is sent to the access port connecting CE2 to PC2, the port checks that the VLAN ID carried in the frame is the same as that configured on the port. The port then removes the tag from the frame and sends the untagged frame to PC2.
* VLANIF interface
  
  A VLANIF interface is a Layer 3 logical interface, which can be configured on either a Layer 3 switch or a router.
  
  Layer 3 switching combines both routing and switching techniques to implement routing on a switch, improving the overall performance of the network. After sending the first data flow based on a routing table, a Layer 3 switch generates a mapping table, in which the mapping between the MAC address and the IP address about this data flow is recorded. If the switch needs to send the same data flow again, it directly sends the data flow at Layer 2 but not Layer 3 based on the mapping table. In this manner, delays on the network caused by route selection are eliminated, and data forwarding efficiency is improved.
  
  To allow the first data flow to be correctly forwarded based on the routing table, the routing table must contain correct routing entries. Therefore, configuring a Layer 3 interface and a routing protocol on the Layer 3 switch is required. VLANIF interfaces are therefore introduced.

![](../../../../public_sys-resources/note_3.0-en-us.png) Key points are summarized as follows:

* A PC does not need to know the VLAN to which it belongs. It sends only untagged frames.
* After receiving an untagged frame from a PC, a switching device determines the VLAN to which the frame belongs. The determination is based on the configured VLAN classification method such as port information, and then the switching device processes the frame accordingly.
* If the frame needs to be forwarded to another switching device, the frame must be transparently transmitted along a trunk link. Frames transmitted along trunk links must carry VLAN tags to allow other switching devices to properly forward the frame based on the VLAN information.
* Before sending the frame to the destination PC, the switching device connected to the destination PC removes the VLAN tag from the frame to ensure that the PC receives an untagged frame.

Generally, only tagged frames are transmitted on trunk links; only untagged frames are transmitted on access links. In this manner, switching devices on the network can properly process VLAN information, and PCs do not need to learn VLAN information.