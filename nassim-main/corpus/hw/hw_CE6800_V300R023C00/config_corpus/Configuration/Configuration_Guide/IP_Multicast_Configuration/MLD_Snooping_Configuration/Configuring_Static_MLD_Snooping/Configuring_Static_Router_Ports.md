Configuring Static Router Ports
===============================

Configuring Static Router Ports

#### Context

A router port is located on a Layer 2 device and connects to an upstream Layer 3 device (a multicast router or Layer 3 switch). After MLD snooping is enabled in a VLAN, interfaces in the VLAN can learn multicast entries from multicast protocol messages. A Layer 2 device flags an interface as a dynamic router port when the interface receives an MLD Query message or PIM Hello message. A router port provides the following two functions:

* It receives multicast data from the upstream device.
* Forwards MLD Report/Done messages. MLD Report/Done messages received in a VLAN are forwarded only to router ports in the VLAN.

A dynamic router port has an aging time. This port is deleted from a device's router port list if it does not receive an MLD Query or a PIM Hello message throughout the aging time. To enable an interface to forward MLD Report/Done messages to the upstream MLD querier for a long time, configure the interface as a static router port.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Disable dynamic learning of router ports.
   1. Enter the VLAN view.
      
      
      ```
      [vlan](cmdqueryname=vlan) vlan-id
      ```
   2. Disable dynamic learning of router ports.
      
      
      ```
      [mld snooping router-learning disable](cmdqueryname=mld+snooping+router-learning+disable)
      ```
      
      By default, dynamic learning of router ports is enabled in a VLAN.
   3. Exit the VLAN view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
3. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Switch the interface working mode from Layer 3 to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   
   
   Determine whether to perform this step based on the current interface working mode.
5. Configure a static router port.
   
   
   ```
   [mld snooping static-router-port](cmdqueryname=mld+snooping+static-router-port) vlan { vlan-id1 [ to vlan-id2 ] } &<1-10>
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```