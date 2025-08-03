Setting the Delay for Transmitting LSAs on an Interface
=======================================================

This configuration is important for low-speed networks.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The OSPF interface view is displayed.
3. Run the [**ospf trans-delay**](cmdqueryname=ospf+trans-delay) *delayvalue* command to set the delay for the interface to transmit LSAs.
   
   
   
   The LSAs in the LSDB of the local device age with time (increase by 1 each second), but not during transmission. Therefore, an LSA transmission delay needs to be set before LSAs are sent.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.