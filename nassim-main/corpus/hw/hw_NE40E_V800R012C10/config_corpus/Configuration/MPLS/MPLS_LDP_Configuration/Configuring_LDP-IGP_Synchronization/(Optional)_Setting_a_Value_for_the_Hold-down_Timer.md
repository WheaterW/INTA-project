(Optional) Setting a Value for the Hold-down Timer
==================================================

This section describes how to set a value for the Hold-down timer. Before the timer expires, an interface waits for the establishment of an LDP session and an LDP adjacency without setting up an IGP neighbor relationship.

#### Context

On a device that has LDP-IGP synchronization enabled, if the active physical link recovers, the IGP enters the Hold-down state, and a Hold-down timer starts. Before the Hold-down timer expires, the IGP delays establishing an IGP neighbor relationship until the reestablishment of an LDP session and an LDP adjacency over the active link so that the LDP session over and IGP route for the active link can become available simultaneously.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

A Hold-down timer can be set on either an OSPF or IS-IS interface and can only be set in an IS-IS process, not in an OSPF process.

If different Hold-down values on an interface and in an IS-IS process are set, the setting on the interface takes effect.



#### Procedure

* Set a value for the Hold-down timer on a specified OSPF interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**ospf timer ldp-sync hold-down**](cmdqueryname=ospf+timer+ldp-sync+hold-down) *value*
     
     
     
     A value is set for the Hold-down timer, which enables an OSPF interface to delay establishing an OSPF neighbor relationship until the reestablishment of an LDP session and an LDP adjacency.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To configure a value for the Hold-down timer on an OSPF multi-area adjacency interface, run the [**ospf timer ldp-sync hold-down**](cmdqueryname=ospf+timer+ldp-sync+hold-down+multi-area) *value* **multi-area** *area-id* command.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set a value for the Hold-down timer on a specified IS-IS interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**isis timer ldp-sync hold-down**](cmdqueryname=isis+timer+ldp-sync+hold-down) *value*
     
     
     
     A value is set for the Hold-down timer, which enables an IS-IS interface to delay establishing an IS-IS neighbor relationship until the reestablishment of an LDP session and an LDP adjacency.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set a value for the Hold-down timer on all IS-IS interfaces in a specified IS-IS process.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS process view is displayed.
  3. Run [**timer ldp-sync hold-down**](cmdqueryname=timer+ldp-sync+hold-down) *value*
     
     
     
     A value is set for the Hold-down timer, which enables all IS-IS interfaces in an IS-IS process to delay establishing IS-IS neighbor relationships before the establishment of LDP sessions and LDP adjacencies.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.