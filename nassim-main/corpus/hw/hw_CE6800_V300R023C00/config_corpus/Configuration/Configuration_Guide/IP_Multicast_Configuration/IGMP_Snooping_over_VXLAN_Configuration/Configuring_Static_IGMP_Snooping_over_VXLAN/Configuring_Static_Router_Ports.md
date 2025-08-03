Configuring Static Router Ports
===============================

Configuring Static Router Ports

#### Context

A router port is located on a Layer 2 device and connects to an upstream Layer 3 device (a multicast router or Layer 3 switch). After IGMP snooping is enabled in a BD, Layer 2 sub-interfaces in the BD can learn multicast entries from multicast protocol messages. A Layer 2 device sets a Layer 2 sub-interface as a dynamic router port when the sub-interface receives an IGMP Query message or PIM Hello message. A router port provides the following functions:

* It receives multicast data from the upstream device.
* It guides IGMP Report/Leave message forwarding. The IGMP Report/Leave messages received in a BD are forwarded only to the router ports within the BD.

A dynamic router port has an aging period. If this port does not receive any IGMP Query or PIM Hello message within the aging period, it is deleted from a device's router port list. As such, if an interface must forward IGMP Report/Leave messages to the upstream IGMP querier for an extended period of time, configure the interface as a static router port.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Disable dynamic learning of router ports.
   1. Enter the BD view.
      
      
      ```
      [bridge-domain](cmdqueryname=bridge-domain) bd-id
      ```
   2. Disable dynamic learning of router ports.
      
      
      ```
      [igmp snooping router-learning disable](cmdqueryname=igmp+snooping+router-learning+disable)
      ```
      
      
      
      By default, dynamic learning of router ports is enabled in a BD.
   3. Exit the BD view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
3. Enter the Layer 2 sub-interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number.subnum mode l2
   ```
4. Configure a Layer 2 sub-interface as a static router port.
   
   
   ```
   [igmp snooping static-router-port](cmdqueryname=igmp+snooping+static-router-port) [ dot1q vid vidValue | qinq pe-vid pe-vidValue ce-vid ce-vidValue ]
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```