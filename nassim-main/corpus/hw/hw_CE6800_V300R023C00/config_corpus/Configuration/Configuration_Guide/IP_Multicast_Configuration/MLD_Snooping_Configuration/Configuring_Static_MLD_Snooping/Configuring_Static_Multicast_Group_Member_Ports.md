Configuring Static Multicast Group Member Ports
===============================================

Configuring Static Multicast Group Member Ports

#### Context

A multicast group member port (member port for short) generally connects to multicast user hosts and is used to forward multicast data to the hosts. It can be dynamically learned through multicast protocols or be statically configured. After MLD snooping is enabled in a VLAN, interfaces in the VLAN can learn multicast entries from multicast protocol messages. The device flags an interface as dynamic member port when the interface receives an MLD Report message. A dynamic member port ages periodically.

If the user hosts connected to an interface need to receive data of a specified multicast group for an extended period of time, you can manually add the interface to the group as a static member port. A static member port never ages.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode from Layer 3 to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   
   
   Determine whether to perform this step based on the current interface working mode.
4. (Optional) Disable dynamic learning of multicast member ports.
   
   
   ```
   [mld snooping learning disable](cmdqueryname=mld+snooping+learning+disable) vlan { { vlan-id1 [ to vlan-id2 ] } &<1-10> | all }
   ```
   
   By default, dynamic learning of member ports is enabled. If an interface is disabled from dynamically learning multicast member ports, the interface can only be statically added to a multicast group when they are required to forward multicast data.
5. Configure static multicast group member ports.
   
   
   ```
   [mld snooping static-group](cmdqueryname=mld+snooping+static-group) [ source-address source-address ] group-address group-address vlan { vlan-id1 [ to vlan-id2 ] } &<1-10>
   ```
   
   You can also run the [**mld snooping static-group**](cmdqueryname=mld+snooping+static-group) [ **source-address** *source-address* ] **group-address** *group-address1* **to** *group-address2* **vlan** *vlan-id* command to add the interface to multiple multicast groups in a batch.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```