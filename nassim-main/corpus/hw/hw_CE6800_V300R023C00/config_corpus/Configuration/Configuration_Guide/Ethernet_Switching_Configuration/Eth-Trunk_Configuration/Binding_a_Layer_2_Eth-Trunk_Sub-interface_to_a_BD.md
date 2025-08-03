Binding a Layer 2 Eth-Trunk Sub-interface to a BD
=================================================

Binding a Layer 2 Eth-Trunk Sub-interface to a BD

#### Prerequisites

Before creating a Layer 2 Eth-Trunk sub-interface, ensure that the corresponding Eth-Trunk interface has been created. You can add member interfaces to the Eth-Trunk interface in any sequence. For example, you can add member interfaces to the Eth-Trunk interface after creating a Layer 2 sub-interface.


#### Context

When the device is connected to a Layer 2 network through a Layer 2 Eth-Trunk interface, you can configure the same bridge domain (BD) for different Layer 2 sub-interfaces of the Eth-Trunk interface to implement Layer 2 packet forwarding between the Layer 2 Eth-Trunk sub-interfaces.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of an Eth-Trunk interface.
   
   
   ```
   [interface eth-trunk](cmdqueryname=interface+eth-trunk) trunk-id
   ```
3. Configure the Eth-Trunk interface to work in Layer 2 mode and return to the system view.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   [quit](cmdqueryname=quit)
   ```
4. Create a BD.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
6. Create a Layer 2 Eth-Trunk sub-interface and enter the Layer 2 Eth-Trunk sub-interface view.
   
   
   ```
   [interface eth-trunk](cmdqueryname=interface+eth-trunk) trunk-id.subnumber mode [l2](cmdqueryname=interface+l2)
   ```
   
   *subnumber* specifies the number of a Layer 2 Eth-Trunk sub-interface.
7. Bind the Layer 2 Eth-Trunk sub-interface to the BD.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id
   ```
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Follow-up Procedure

After a Layer 2 Eth-Trunk sub-interface is created, you can configure services such as traffic encapsulation and traffic behaviors on the sub-interface. You can also run the [**display interface eth-trunk**](cmdqueryname=display+interface+eth-trunk) *trunk-id.subnumber* command to view the status of the Eth-Trunk sub-interface.