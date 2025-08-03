(Optional) Configuring an Interface to Transparently Transmit HVRP Packets
==========================================================================

(Optional) Configuring an Interface to Transparently Transmit HVRP Packets

#### Context

The Hierarchy VLAN Register Protocol (HVRP) is introduced to resolve MAC addresses insufficiency. It tries to allow each VLAN broadcast domain to have at most two ports. In this way, MAC entries do not need to be searched for before packets are broadcast.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **gigabitethernet** *interface-number*
   
   
   
   The GE interface view is displayed.
3. Run [**portswitch**](cmdqueryname=portswitch)
   
   
   
   The interface is switched to the Layer 2 mode.
4. Run [**stp enable**](cmdqueryname=stp+enable)
   
   
   
   STP/RSTP/MSTP is enabled on the interface.
5. Run [**hvrp-transport**](cmdqueryname=hvrp-transport)
   
   
   
   The interface is configured to transparently transmit HVRP packets.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The command is supported only in the multi-instance scenario rather than the multi-process scenario.