Enabling a QinQ/dot1q VLAN Tag Termination Sub-Interface to Process PIM Messages and Generate Multicast Forwarding Entries
==========================================================================================================================

If a QinQ/dot1q VLAN tag termination sub-interface of a local device is connected to a remote device, you can enable the sub-interface to process PIM messages and generate multicast forwarding entries so that the single-tagged PIM messages received from the remote device can be processed and multicast forwarding entries are generated.

#### Context

If the local Router's sub-interface with QinQ/dot1q VLAN tag termination configured receives PIM messages from its directly connected remote Router, the sub-interface can generate only multicast routing entries but not multicast forwarding entries after processing the PIM messages.

To address this problem, enable the QinQ/dot1q VLAN tag termination sub-interface to process PIM messages and generate multicast forwarding entries. After the configuration is complete, the sub-interface of the Router can process the single-tagged PIM messages received from the directly connected device and generate multicast forwarding entries.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
   
   
   
   Multicast routing is enabled.
   
   
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   Running the [**undo multicast routing-enable**](cmdqueryname=undo+multicast+routing-enable) command deletes all multicast configurations and interrupts multicast services. To restore the multicast services, you must revert the deleted multicast configurations.
3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number**.subinterface-number*
   
   
   
   The interface view is displayed.
4. Run [**pim single-tag forward enable**](cmdqueryname=pim+single-tag+forward+enable)
   
   
   
   The QinQ/dot1q VLAN tag termination sub-interface is enabled to process PIM messages and generate multicast forwarding entries.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.