Configuring Static Router Ports
===============================

Configuring Static Router Ports

#### Context

A router port is located on a Layer 2 device and connects to an upstream Layer 3 device (a multicast router or Layer 3 switch). After IGMP snooping is enabled in a VLAN, interfaces in the VLAN can learn multicast entries from multicast protocol packets. A Layer 2 device flags an interface as a dynamic router port when the interface receives an IGMP Query message or PIM Hello message. A router port provides the following functions:

* It receives multicast data from the upstream device.
* It guides IGMP Report/Leave message forwarding. Such messages received in a VLAN are forwarded only to the router ports within the VLAN.

A dynamic router port has an aging time. This port is deleted from a device's router port list if it does not receive an IGMP Query or a PIM Hello message before the aging time expires. If an interface must forward IGMP Report/Leave messages to the upstream IGMP querier for an extended period of time, configure the interface as a static router port.


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
      [igmp snooping router-learning disable](cmdqueryname=igmp+snooping+router-learning+disable)
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
4. Configure a static router port.
   
   
   ```
   [igmp snooping static-router-port](cmdqueryname=igmp+snooping+static-router-port) vlan { vlan-id1 [ to vlan-id2 ] } &<1-10>
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```