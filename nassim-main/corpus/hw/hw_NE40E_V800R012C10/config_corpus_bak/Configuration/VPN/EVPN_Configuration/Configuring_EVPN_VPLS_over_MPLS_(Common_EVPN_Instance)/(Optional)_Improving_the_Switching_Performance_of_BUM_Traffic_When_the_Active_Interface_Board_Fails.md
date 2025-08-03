(Optional) Improving the Switching Performance of BUM Traffic When the Active Interface Board Fails
===================================================================================================

Enabling a device to deliver standby leaf node information to the standby interface board helps improve the switching performance of BUM traffic when the active interface board of the device fails.

#### Context

In a scenario where BUM traffic heads for the public network, the active and standby leaf node information can be delivered to the active and standby interface boards respectively for protection. If the active interface board fails, traffic can be quickly switched to the standby leaf nodes, improving link switching performance.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**evpn reserve-interface enhancement**](cmdqueryname=evpn+reserve-interface+enhancement)
   
   
   
   The device is enabled to deliver information about standby leaf nodes to the standby interface board.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.