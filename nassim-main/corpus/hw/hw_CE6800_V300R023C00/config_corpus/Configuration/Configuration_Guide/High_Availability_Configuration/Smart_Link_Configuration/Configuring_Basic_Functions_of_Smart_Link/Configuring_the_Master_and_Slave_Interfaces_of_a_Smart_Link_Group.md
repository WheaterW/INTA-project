Configuring the Master and Slave Interfaces of a Smart Link Group
=================================================================

Configuring the Master and Slave Interfaces of a Smart Link Group

#### Context

The slave interface is blocked when the Smart Link group is enabled. If the primary link fails, Smart Link unblocks the slave interface and switches traffic to the secondary link.

An interface cannot be added to a Smart Link group in the following situations:

* STP has been enabled on the interface.
* The interface has been added to a Monitor Link group.
* The interface has been added to another Smart Link group.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a Smart Link group.
   
   
   ```
   [smart-link group](cmdqueryname=smart-link+group) group-id
   ```
3. Configure a protection instance for the Smart Link group.
   
   
   ```
   [protected-vlan reference-instance](cmdqueryname=protected-vlan+reference-instance) { instance-id1 [ to instance-id2 ] }&<1-10>
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After a protection instance is bound to the Smart Link group, Smart Link takes effect only on packets from VLANs mapped to the protection instance. If no protection instance is bound to the Smart Link group, Smart Link takes effect on all VLAN packets.
4. Add an interface to the Smart Link group and configure the interface as the master interface.
   
   
   ```
   [port](cmdqueryname=port) interface-type interface-number [master](cmdqueryname=master)
   ```
5. Add an interface to the Smart Link group and configure the interface as the slave interface.
   
   
   ```
   [port](cmdqueryname=port) interface-type interface-number [slave](cmdqueryname=slave)
   ```
   
   By default, a Smart Link group has no interface.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```