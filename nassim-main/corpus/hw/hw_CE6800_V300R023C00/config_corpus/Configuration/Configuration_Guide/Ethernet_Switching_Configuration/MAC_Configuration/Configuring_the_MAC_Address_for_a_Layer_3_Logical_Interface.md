Configuring the MAC Address for a Layer 3 Logical Interface
===========================================================

Configuring the MAC Address for a Layer 3 Logical Interface

#### Context

By default, the MAC address of a Layer 3 interface is dynamically allocated from the system MAC address range. MAC addresses of Layer 3 physical interfaces cannot be configured; however, MAC addresses of Layer 3 logical interfaces can be configured.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the Layer 3 logical interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
   
   If the Eth-Trunk interface is a Layer 2 interface, run the [**undo portswitch**](cmdqueryname=undo+portswitch) command to switch the interface working mode to Layer 3.
3. Configure the MAC address of the interface.
   
   
   ```
   [mac-address](cmdqueryname=mac-address) mac-address
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```