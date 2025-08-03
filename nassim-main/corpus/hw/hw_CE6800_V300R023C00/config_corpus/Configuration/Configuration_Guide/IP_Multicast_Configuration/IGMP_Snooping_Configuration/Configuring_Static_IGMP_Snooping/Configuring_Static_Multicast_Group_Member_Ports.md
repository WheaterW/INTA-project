Configuring Static Multicast Group Member Ports
===============================================

Configuring Static Multicast Group Member Ports

#### Context

A multicast group member port (member port for short) generally connects to multicast user hosts. It can be dynamically learned through multicast protocols or be statically configured. After IGMP snooping is enabled in a VLAN, interfaces in the VLAN can learn multicast entries from multicast protocol packets. The device flags an interface as dynamic member port when the interface receives an IGMP Report message. A dynamic member port ages periodically.

If the user hosts connected to an interface need to receive specific multicast group data, you can manually add the interface to the group as a static member port. A static member port never ages out.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. (Optional) Disable dynamic learning of multicast member ports.
   
   
   ```
   [igmp snooping learning disable](cmdqueryname=igmp+snooping+learning+disable) vlan { { vlan-id1 [ to vlan-id2 ] } &<1-10> | all }
   ```
   
   By default, dynamic learning of member ports is enabled. If this function is disabled, interfaces must be statically added to a multicast group when they are required to forward multicast data.
4. Add the interface to a multicast group as a static member port.
   
   
   ```
   [igmp snooping static-group](cmdqueryname=igmp+snooping+static-group) [ source-address source-ip-address ] group-address group-ip-address vlan { vlan-id1 [ to vlan-id2 ] } &<1-10>
   ```
   
   You can also run the [**igmp snooping static-group**](cmdqueryname=igmp+snooping+static-group) [ **source-address** *source-ip-address* ] **group-address** *group-ip-address1* **to** *group-ip-address2* **vlan** *vlan-id* command to add the interface to multiple multicast groups in a batch.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```