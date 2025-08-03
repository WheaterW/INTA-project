(Optional) Specifying a Resource Pool of Queues
===============================================

This section describes how to specify a resource pool of queues for an interface, making full use of QoS resources.

#### Context

On each physical interface, the unidirectional SQ resources used for user login are limited. If the number of unidirectional SQ resources on a physical interface exceeds the upper limit, unidirectional QoS resources cannot meet requirements. In this case, you can run the [**qos scheduling-mode**](cmdqueryname=qos+scheduling-mode) command to configure different resource scheduling modes on different sub-interfaces. In this manner, QoS resources are fully utilized.

In VS mode, this configuration is supported only by the admin VS.


#### Procedure

* Specifying a resource pool of queues in mode2.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**qos scheduling-mode**](cmdqueryname=qos+scheduling-mode) **mode2** **slot** *slot-id*
     
     
     
     The scheduling mode is set to mode2 on a board.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The queue resource pool configuration takes effect only when the scheduling mode is set to mode2.
  3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  4. Run [**qos queue-resource pool**](cmdqueryname=qos+queue-resource+pool) *id* { **inbound** | **outbound** }
     
     
     
     A resource pool of queues is specified on the interface.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Specifying a resource pool of queues in mode3.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**qos scheduling-mode**](cmdqueryname=qos+scheduling-mode) **mode3** **slot** *slot-id*
     
     
     
     The scheduling mode is set to mode3 on a board.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.