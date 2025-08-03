Configuring a Layer 2 Eth-Trunk Sub-interface
=============================================

Configuring a Layer 2 Eth-Trunk Sub-interface

#### Context

When a device connects to a Layer 2 network through a Layer 2 Eth-Trunk interface, you can configure Layer 2 Eth-Trunk sub-interfaces to implement Layer 2 forwarding of packets between the sub-interfaces.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the Eth-Trunk interface view.
   
   
   ```
   [interface eth-trunk](cmdqueryname=interface+eth-trunk) trunk-id
   ```
3. Configure the Eth-Trunk interface to work in Layer 2 mode and return to the system view.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   [quit](cmdqueryname=quit)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
5. Create a Layer 2 Eth-Trunk sub-interface and enter its view.
   
   
   ```
   [interface eth-trunk](cmdqueryname=interface+eth-trunk) trunk-id.subnumber mode [l2](cmdqueryname=interface+l2)
   ```
   
   *subnumber* specifies the number of a Layer 2 Eth-Trunk sub-interface.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```