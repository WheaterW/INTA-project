Configuring the Network Type for an Interface
=============================================

OSPFv3 classifies networks into broadcast, P2P, P2MP, and NBMA networks based on link layer protocols. By setting the network type of an interface, you can forcibly change the network type of the interface.

#### Context

By default, the network type of an interface is determined by the physical interface. The network type of Ethernet interfaces is **broadcast**, the network type of serial interfaces is **p2p**, the network type of Frame-relay interfaces is **nbma**.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ospfv3 network-type**](cmdqueryname=ospfv3+network-type) { **broadcast** | **nbma** | **p2mp** [ **non-broadcast** ] | **p2p** } [ **instance** *instance-id* ]
   
   
   
   The network type is configured for the OSPFv3 interface.
   
   After a new network type is configured for an interface, the network type of the original interface is replaced.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The network types of two OSPFv3 interfaces at both ends of a link must be identical. Otherwise, the OSPFv3 neighbor relationship cannot be established.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.