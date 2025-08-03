Overview of Ethernet Interfaces
===============================

Ethernet interfaces include the following: traditional Ethernet interfaces, fast Ethernet (FE) interfaces, gigabit Ethernet (GE) interfaces, 10GE interfaces, , 25GE interfaces, 40GE interfaces, 50GE interfaces, 100GE interfaces, 200GE interfaces.

#### Overview of Ethernet Interfaces

Both Ethernet and token ring networks are typical types of LANs. The Ethernet technology has become the most important LAN networking technology because it is flexible, simple, and easy to implement.

The HUAWEI NE40E-M2 series-M2 supports the following types of LAN interfaces:

* GE interfaces: comply with 1000Base-TX physical layer specifications and are compatible with the 10Base-T and 100Base-TX physical layer specifications.
* 10GE interfaces: comply with IEEE 802.3ae and are compatible with 10Base-T, 100Base-TX, and 1000Base-TX physical layer specifications.
* 25GE interfaces: comply with IEEE802.3by.
* 40GE interfaces: comply with IEEE802.3ba.
* 50GE interfaces: comply with IEEE802.3cd.
* 100GE interfaces: comply with IEEE 802.3ba and are compatible with 100GBase-LR4 physical layer specifications.
* 200GE interfaces: comply with IEEE802.3bs.

Ethernet electrical interfaces can work in either full-duplex or half-duplex mode. They support auto-sensing. In auto-sensing mode, they negotiate with other network devices for the most suitable duplex mode and rate. This simplifies system configuration and management.


#### Basic Concepts of Ethernet Interfaces

* Ethernet interface types
  
  [Table 1](#EN-US_CONCEPT_0172362764__tab_dc_vrp_ethernet_cfg_000101) shows the types of Ethernet interfaces defined on the device. Ethernet interfaces are classified into different types to meet various network requirements.
  
  **Table 1** Ethernet interface types
  | Interface Type | Description |
  | --- | --- |
  | Layer 3 Ethernet interface | A physical interface that operates at the network layer. The interface can be configured with an IP address, supporting Layer 3 protocols and providing routing functions. |
  | Layer 3 Ethernet sub-interface | A logical interface that is configured on a main interface. The main interface can be a physical interface (such as a Layer 3 Ethernet interface) or a logical interface. The Layer 3 Ethernet sub-interface shares physical layer parameters of the main interface and can be configured with specific link layer and network layer parameters. You can activate or deactivate the sub-interface, without affecting the performance of the main interface. The change of the main interface status, however, affects the sub-interface. The sub-interface functions properly only if the main interface is in the Up state. |
* Ethernet interface rate and duplex mode
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Only Ethernet electrical interfaces instead of Ethernet optical interfaces support rate and duplex mode configuration. Ethernet optical interfaces support only the auto-negotiation mode.
  
  By default, the Ethernet interface rate and duplex mode are automatically negotiated. In auto-negotiation mode, a local interface automatically adjusts its rate and duplex mode based on the peer interface rate and duplex mode so that both ends can work in the same duplex mode at the highest possible rate.
  
  If interface hardware complies with auto-negotiation standards, it is recommended that Ethernet interfaces work in auto-negotiation mode, unless the two ends of a link have different Ethernet rates or duplex modes. In this case, you can disable auto-negotiation and manually set the interface rate and duplex mode.
  
  However, manually setting the interface rate and duplex mode usually complicates network planning and maintenance, and incorrect settings may affect or even interrupt the network communication.
  
  + If the rates of Ethernet interfaces at two ends of a link are set to 10 Mbit/s and 100 Mbit/s respectively, the link goes down.
  + If the Ethernet interface at one end of a link works in duplex mode at a fixed rate (such as 10 Mbit/s or 100 Mbit/s) and the Ethernet interface at the other end works in auto-negotiation mode, the interface working in auto-negotiation mode can detect the peer interface's fixed rate, not the duplex mode. In this case, even if negotiation between the two ends succeeds, the interface working in auto-negotiation mode adopts the default working mode, 10M half duplex.
    
    That is, if one end works in auto-negotiation mode while the other end works in a fixed mode, the auto-negotiation mechanism does not take effect. To implement the auto-negotiation mechanism, both the communicating parties must work in auto-negotiation mode.
  + If one end of a link works in full-duplex mode while the other end works in half-duplex mode, communication performance of the interfaces is affected.
  
  Manually setting the interface rate and duplex mode is recommended only when auto-negotiation of an Ethernet link fails. When there is an auto-negotiation problem, you are advised to upgrade device software or hardware for the device to support the auto-negotiation mechanism defined in IEEE 802.3u/z.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The poor quality of network cables may also cause auto-negotiation failures.
* Maximum transmission unit (MTU)
  
  MTU is the largest packet of data that can be transmitted on a network, expressed in bytes. MTU is determined by data link layer protocols, and MTU values vary with networks.
  
  The size of packets is limited at the network layer. Whenever receiving an IP packet, the IP layer determines the next-hop interface for the packet and obtains the MTU configured on the interface. Then, the IP layer compares the MTU with the packet length. If the packet length is longer than the MTU, the IP layer fragments the packet into smaller packets, which are shorter than or equal to the MTU. If unfragmentation is configured, some packets may be discarded during data transmission at the IP layer.
  
  If the size of packets is much greater than the configured MTU value, the packets are broken into a great number of fragments. The packets may be discarded by quality of service (QoS) queues.
* LAN mode of 10GE interfaces
  
  A 10GE interface can operate in either of the following modes according to its physical features:
  + LAN mode: In this mode, the 10GE interface transmits Ethernet packets and connects to an Ethernet network.
* Overhead bytes
  
  SDH frames contain various overhead bytes that are used to implement operation and maintenance functions, such as layered management of SDH transport networks. J0 and J1 are used for interoperability between devices of different countries, areas, or manufacturers.
* Loopback test for Ethernet interfaces
  
  Loopback tests can be performed on Ethernet interfaces to check whether the interfaces operate properly.
  
  The loopback tests are classified as follows:
  
  + Internal loopback test: establishes a loop within the switching module of an Ethernet interface to check whether certain hardware of the interface is faulty.
  + External loopback test: sends the packet received from a remote interface back to the remote interface, instead of forwarding the packet to the destination address. This kind of test is used to check whether the link between the local and peer ends is faulty.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  + An Ethernet interface cannot properly forward packets during a loopback test.
  + If an Ethernet interface is down, only internal loopback tests can be performed.
    
    If an Ethernet interface is administratively down after the [**shutdown**](cmdqueryname=shutdown) command is run, neither internal nor external loopback tests can be performed.
  + The [**shutdown**](cmdqueryname=shutdown) command cannot be run on an Ethernet interface during the loopback test.
  + After the loopback test function is enabled on an Ethernet interface, the interface operates in full-duplex mode. After the loopback test function is disabled, the Ethernet interface restores the original settings.