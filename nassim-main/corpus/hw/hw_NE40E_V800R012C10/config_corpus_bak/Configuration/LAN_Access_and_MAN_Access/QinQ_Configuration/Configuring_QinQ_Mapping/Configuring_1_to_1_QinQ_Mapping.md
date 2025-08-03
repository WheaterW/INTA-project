Configuring 1 to 1 QinQ Mapping
===============================

When a 1 to 1 QinQ mapping-enabled sub-interface receives a single-tagged packet, the sub-interface replaces the virtual local area network (VLAN) ID in the packet with a specified VLAN ID.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subinterface-number*
   
   
   
   The view of a CE-side sub-interface on a PE is displayed.
3. Run [**qinq mapping vid**](cmdqueryname=qinq+mapping+vid) *vid* **map-vlan vid** *map-vid* [ **vlan-group** *group-id* ]
   
   
   
   The sub-interface is configured to map the VLAN ID in a single-tagged packet to a specified VLAN ID.
   
   The original VLAN ID in the single-tagged packet cannot be the same as the outer VLAN ID of packets on any other sub-interfaces.
   
   If the [**qinq mapping**](cmdqueryname=qinq+mapping) command has been run on a sub-interface, any commands related to the QinQ stacking, QinQ termination, or dot1q termination function cannot be configured on the sub-interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.