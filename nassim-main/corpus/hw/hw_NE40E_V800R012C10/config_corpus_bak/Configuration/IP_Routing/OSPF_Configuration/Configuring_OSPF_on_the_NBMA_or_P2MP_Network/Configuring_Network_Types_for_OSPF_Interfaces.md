Configuring Network Types for OSPF Interfaces
=============================================

OSPF classifies networks into four types based on the types of link layer protocols. You can configure the network type for an OSPF interface to forcibly change its original network type.

#### Context

Network types of OSPF interfaces on both ends of a link must be the same. Otherwise, the two interfaces cannot establish an OSPF neighbor relationship. By default, the network type of an interface is determined by the physical interface. The network type of Ethernet interfaces is **broadcast**, the network type of serial interfaces is **p2p**, the network type of Frame-relay interfaces is **nbma**.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ospf network-type**](cmdqueryname=ospf+network-type) { **broadcast** | **nbma** | **p2mp** | **p2p** }
   
   
   
   A network type is configured for the OSPF interface.
   
   
   
   After a new network type is configured for an interface, the original network type of the interface is replaced.
   
   Configure a network type for the interface as required. For example:
   * If the network type of the interface is broadcast but there are Routers that do not support multicast addresses on the broadcast network, change the network type of the interface to NBMA.
   * If the network type of the interface is NBMA and the network is fully meshed (any two Routers are directly reachable), you can change the network type of the interface to broadcast without the need to configure neighboring Routers.
   * If the network type of the interface is NBMA but the network is not fully meshed, change the network type of the interface to P2MP. In this manner, two Routers that are not directly reachable can exchange routing information through a Router that is directly reachable to both Routers. After the network type of the interface is changed to P2MP, there is no need to manually configure neighboring Routers.
   * If only two Routers run OSPF on the same network segment, changing the network type of the interface to P2P is recommended.
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   OSPF does not support the configuration on a null interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.