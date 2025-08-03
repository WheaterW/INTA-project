Configuring a Control VLAN
==========================

Configuring a Control VLAN

#### Context

Control and data VLANs have different functions. On an ERPS ring, a control VLAN is used to transmit only R-APS PDUs but not user service packets, which improves ERPS security. All the devices on an ERPS ring must be configured with the same control VLAN. Different ERPS rings cannot use the same control VLAN.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of a created ERPS ring.
   
   
   ```
   [erps ring](cmdqueryname=erps+ring) ring-id
   ```
3. Configure a control VLAN for the ERPS ring.
   
   
   ```
   [control-vlan](cmdqueryname=control-vlan) vlan-id   
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * If you run the [**control-vlan**](cmdqueryname=control-vlan) command multiple times, only the latest configuration takes effect.
   * The control VLAN specified by the *vlan-id* parameter must be a VLAN that has not been created or used.
   * If ports have been added to the ERPS ring, the control VLAN cannot be changed. To delete a configured control VLAN, you must run the [**undo erps ring**](cmdqueryname=undo+erps+ring) command in the interface view or the [**undo port**](cmdqueryname=undo+port) command in the ERPS ring view to remove the ports from the ERPS ring, and then run the [**undo control-vlan**](cmdqueryname=undo+control-vlan) command to delete the control VLAN.
   * After a control VLAN is created, the [**vlan batch**](cmdqueryname=vlan+batch) *vlan-id1* [ **to** *vlan-id2* ] &<1-10> command is automatically displayed in the configuration file.
   * After a port is added to an ERPS ring configured with a control VLAN, the port is automatically added to the control VLAN. If the port is a trunk port, the [**port trunk allow-pass vlan**](cmdqueryname=port+trunk+allow-pass+vlan) *vlan-id* command is automatically displayed in the view of the port in the configuration file. If the port is a hybrid port, the [**port hybrid tagged vlan**](cmdqueryname=port+hybrid+tagged+vlan) *vlan-id* command is automatically displayed in the view of the port in the configuration file.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```