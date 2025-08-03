Configuring an Interface to Discard Incoming VLAN-Tagged Packets
================================================================

Configuring an Interface to Discard Incoming VLAN-Tagged Packets

#### Context

On a network, all hosts send untagged packets. When an interface on a device is configured for host access, the interface only needs to process untagged packets. To prevent devices other than the hosts from connecting to the interface, you can configure the interface to discard incoming VLAN-tagged packets.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the Ethernet interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   
   
   Determine whether to perform this step based on the current interface working mode.
4. Configure the interface to discard incoming VLAN-tagged packets.
   
   
   ```
   [port discard tagged-packet](cmdqueryname=port+discard+tagged-packet)
   ```
   
   
   
   By default, an interface does not discard incoming VLAN-tagged packets.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display this**](cmdqueryname=display+this) command in the interface view to check whether the interface is configured to discard incoming VLAN-tagged packets.