Enabling User Traffic Statistics Collection Based on Inner or Outer VLAN IDs on a Device
========================================================================================

This section describes how to enable user traffic statistics
collection based on inner or outer VLAN IDs on a device.

#### Context

If PPPoE users go online through user VLAN sub-interfaces
that permit packets carrying undefined VLAN tags, the VLAN users can
go online through any interface, making it difficult to collect user
traffic statistics. After user traffic statistics collection based
on inner or outer VLAN IDs is enabled on the Router, the Router collects user traffic statistics based on inner or outer VLAN IDs.
Perform the following steps on the Router.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**access user-flow-statistics enable**](cmdqueryname=access+user-flow-statistics+enable)
   
   
   
   User traffic statistics collection is enabled based on inner
   or outer VLAN IDs on the device.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Result

* After PPPoE users go online through QinQ VLAN tag termination
  sub-interfaces and any is specified for inner VLAN tags, which means
  that packets carrying any inner VLAN tags are forwarded, you can run
  the [**display access user-flow-statistics configuration**](cmdqueryname=display+access+user-flow-statistics+configuration) or [**display
  vlan-statistics pevlan**](cmdqueryname=display+vlan-statistics+pevlan) command to check user traffic
  collection configuration or user traffic statistics on the Router.
* To collect user traffic statistics in a coming period, run the [**reset vlan-statistics
  pevlan**](cmdqueryname=reset+vlan-statistics+pevlan) command to clear the existing statistics based
  on a specified inner or outer VLAN ID, and then run the [**display vlan-statistics
  pevlan**](cmdqueryname=display+vlan-statistics+pevlan) command.