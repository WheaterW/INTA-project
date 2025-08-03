Configuring Static Multicast Group Member Ports
===============================================

Configuring Static Multicast Group Member Ports

#### Context

Group member ports are connected to user hosts (multicast group members) and can be learned dynamically through multicast protocols or configured manually. After IGMP snooping is enabled in a BD, Layer 2 sub-interfaces in the BD can learn multicast entries from multicast protocol messages. The device sets a Layer 2 sub-interface as a dynamic member port when the sub-interface receives an IGMP Report message. A dynamic member port ages periodically.

If the user hosts connected to a Layer 2 sub-interface need to steadily receive group-specific or group-and-source-specific multicast data, add the sub-interface to the multicast group or (S, G) manually so that the sub-interface becomes a static member port. A static member port never ages out.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the Layer 2 sub-interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number.subnum mode l2
   ```
3. (Optional) Disable dynamic learning of multicast member ports.
   
   
   ```
   [igmp snooping learning disable](cmdqueryname=igmp+snooping+learning+disable)
   ```
   
   
   
   By default, an interface is enabled to dynamically learn forwarding entries. If this function is disabled, interfaces must be manually added to a multicast group when they are required to forward multicast data.
4. Manually add the Layer 2 sub-interface to a multicast group as a static member port.
   
   
   ```
   [igmp snooping static-group](cmdqueryname=igmp+snooping+static-group) [ source-address source-addr ] group-address group-addr [ dot1q vid vid | qinq pe-vid pe-vidValue ce-vid ce-vidValue]
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```