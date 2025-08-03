Configuring a DSCP Value for RADIUS Packets
===========================================

Configuring a DSCP Value for RADIUS Packets

#### Context

To prevent RADIUS packets sent by a device from being discarded due to network congestion, you can configure a DSCP value for the RADIUS packets sent by the device to the RADIUS server in either the system or RADIUS server group view. The DSCP value configured in the RADIUS server group view takes precedence over that configured in the system view.


#### Procedure

* In the system view, configure a DSCP value for RADIUS packets:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**radius-server packet**](cmdqueryname=radius-server+packet) **dscp** *dscp-value*
     
     
     
     A DSCP value is configured for RADIUS packets sent by the device.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* In the RADIUS server group view, configure a DSCP value for RADIUS packets:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**radius-server group**](cmdqueryname=radius-server+group) *group-name*
     
     
     
     The RADIUS server group view is displayed.
  3. Run [**radius-server packet**](cmdqueryname=radius-server+packet) **dscp** *dscp-value*
     
     
     
     A DSCP value is configured for RADIUS packets sent by the device.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.