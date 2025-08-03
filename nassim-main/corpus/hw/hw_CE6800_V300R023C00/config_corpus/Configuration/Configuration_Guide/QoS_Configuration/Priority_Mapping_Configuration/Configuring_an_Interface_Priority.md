Configuring an Interface Priority
=================================

Configuring an Interface Priority

#### Context

The device provides differentiated services based on the interface priority in the following scenarios:

* The [**trust upstream none**](cmdqueryname=trust+upstream+none) command is configured on an interface.
* An interface receives untagged packets.![](public_sys-resources/note_3.0-en-us.png) 
  + The interface priority cannot be specified for Eth-Trunk member interfaces.
  + If no DiffServ domain is applied to an inbound interface and the interface priority is configured, the device adds a VLAN tag to received packets, uses the interface priority as the external priority, and sends packets to queues based on the interface priority.
  + When an Ethernet interface works in Layer 3 mode, the interface priority is 0 and cannot be configured.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Configure an interface priority.
   
   
   ```
   [port priority](cmdqueryname=port+priority) priority-value
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```