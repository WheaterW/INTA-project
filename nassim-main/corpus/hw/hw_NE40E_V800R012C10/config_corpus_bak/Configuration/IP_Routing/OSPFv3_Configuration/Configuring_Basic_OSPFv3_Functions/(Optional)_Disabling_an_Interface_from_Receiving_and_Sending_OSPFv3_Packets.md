(Optional) Disabling an Interface from Receiving and Sending OSPFv3 Packets
===========================================================================

Disabling an interface from receiving and sending OSPFv3 packets prevents other network devices from obtaining OSPFv3 routing information and prevents the local device from receiving routing updates advertised by other network devices.

#### Context

To prevent a device interface from sending its OSPFv3 routing information to other devices on the network and disable the device interface from receiving routing updates from other devices, you can suppress the interface from sending and receiving OSPFv3 packets. After an interface is disabled from receiving and sending OSPFv3 packets, the interface can still advertise its routes but cannot exchange Hello packets with others. Therefore, no neighbor relationship can be established between the interface and others. This can enhance the networking adaptability of OSPFv3 and reduce system resource consumption.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
   
   
   
   The OSPFv3 process view is displayed.
3. Run [**silent-interface**](cmdqueryname=silent-interface) *interface-type* *interface-number*
   
   
   
   The interface is disabled from receiving and sending OSPFv3 packets.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In different processes, you can suppress the same interface from sending and receiving OSPFv3 packets. However, the [**silent-interface**](cmdqueryname=silent-interface) configuration takes effect only in the specified process of an interface, not all processes associated with the interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.