Creating an Eth-Trunk Interface and Configuring It to Work in Manual Load Balancing Mode
========================================================================================

You can add physical interfaces to an Eth-Trunk interface working in manual load balancing mode. All the member interfaces are in the forwarding state and load-balance traffic.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id*
   
   
   
   An Eth-Trunk interface is created, and its view is displayed.
3. (Optional) Run [**portswitch**](cmdqueryname=portswitch)
   
   
   
   The Eth-Trunk interface is switched to the Layer 2 mode.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Physical interfaces can be added to an Eth-Trunk interface regardless of which mode the Eth-Trunk interface works in. If the Eth-Trunk interface needs to work in Layer 3 mode, skip this step and go to the next step.
4. Run [**mode manual load-balance**](cmdqueryname=mode+manual+load-balance)
   
   
   
   The Eth-Trunk interface is configured to work in manual load balancing mode.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.