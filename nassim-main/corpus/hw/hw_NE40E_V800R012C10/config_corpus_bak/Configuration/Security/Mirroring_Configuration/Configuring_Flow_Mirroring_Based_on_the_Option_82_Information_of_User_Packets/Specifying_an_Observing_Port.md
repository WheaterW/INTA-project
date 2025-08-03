Specifying an Observing Port
============================

This section describes how to specify an observing port for mirroring. You can then associate this port with the corresponding mirrored port.

#### Context

You can use either of the following methods to specify an observing port for mirroring:

* Specify an observing port for board-based mirroring.
  
  With this method, the mirrored traffic of the entire interface board on the NE40E is sent to only the same observing port.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The observing port specified for board-based mirroring can be configured on either the local or non-local interface board.
* Specify an observing port for interface-based mirroring.
  
  With this method, the mirrored traffic of an interface on the NE40E is sent to the specified observing port.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Packets on an interface can be mirrored to an observing port on any interface board. This means that the observing port can reside on the local or any other interface board. If observing ports are specified for both interface-based mirroring and board-based mirroring, the observing port specified for interface-based mirroring takes effect.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Specify an observing port for board-based flow mirroring or interface-based flow mirroring as required.
   
   
   
   Specify an observing port for board-based flow mirroring.
   
   
   
   1. Run the [**slot**](cmdqueryname=slot) *slot-id* command to enter the slot view.
   2. (Optional) Run the [**observe-filter**](cmdqueryname=observe-filter) *filter-index* **local** { **dst-ip** *dst-ip-address dst-mask* | **dst-mac** *dst-mac-address* | **dst-port***dst-port* | **ether-type***type-value* | { **ip-protocol***ip-protocol-number* | **ppp-protocol***ppp-protocol-number* } | **pppoe-session** *session-id*| **src-ip***src-ip-addresssrc-mask* | **src-mac** **src-mac-address** | **src-port***src-port* | **vlan***vlan-id*} \* command to configure a filter rule for mirrored packets.
   3. Run the [**mirror to observe-index**](cmdqueryname=mirror+to+observe-index) *observe-index* command to specify an observing port for board-based mirroring.
   4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   
   
   
   Specify an observing port for interface-based flow mirroring.
   
   
   
   1. Run the [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name* command to define a traffic behavior and enter the traffic behavior view.
   2. Run the [**port-mirroring to**](cmdqueryname=port-mirroring+to) { **observe-index** *observe-index* &<1-8> } command to specify an observing port for interface-based flow mirroring.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.