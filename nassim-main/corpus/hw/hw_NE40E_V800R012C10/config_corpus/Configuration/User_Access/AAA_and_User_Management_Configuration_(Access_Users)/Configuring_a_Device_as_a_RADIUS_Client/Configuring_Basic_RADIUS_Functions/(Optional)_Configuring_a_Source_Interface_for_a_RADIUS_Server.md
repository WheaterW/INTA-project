(Optional) Configuring a Source Interface for a RADIUS Server
=============================================================

(Optional) Configuring a Source Interface for a RADIUS Server

#### Context

To determine the route between a device and each RADIUS server to which it connects, you can configure a source interface (which connects the device to a RADIUS server) for each RADIUS server in the system view, RADIUS server group view, or both. In the scenario where the device exchanges packets with a RADIUS server, if a source interface is configured in the RADIUS server group view, this source interface is used for communication with the RADIUS server. Otherwise, the global source interface configured for RADIUS servers is used.

When the device sends packets to a RADIUS server deployed in a VPN, the device preferentially uses the IP address of the source interface configured using the [**radius-server source interface**](cmdqueryname=radius-server+source+interface) command as the source address. In scenarios where no source interface is configured, the device searches for a reachable route based on the VPN and destination IP address. If a route is found, the device uses the IP address of the route's outbound interface as the source address; otherwise, the device selects the IP address of any interface in the VPN as the source address.


#### Procedure

* Configure a global source interface for RADIUS servers.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**radius-server source interface**](cmdqueryname=radius-server+source+interface) *interface-type interface-number*
     
     
     
     A global source interface is configured for RADIUS servers.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a source interface for a specified RADIUS server group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**radius-server group**](cmdqueryname=radius-server+group) *group-name*
     
     
     
     The RADIUS server group view is displayed.
  3. Run [**radius-server source interface**](cmdqueryname=radius-server+source+interface) *interface-type* *interface-number*
     
     
     
     A source interface is configured for the RADIUS server group.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.