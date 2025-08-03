Configuring High-Priority Scheduling on a Board
===============================================

Low-priority queues on a board can be configured as high-priority queues.

#### Context

Perform the following steps on the Router.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
3. Run [**qos convergent-precedence cos**](cmdqueryname=qos+convergent-precedence+cos) *start-cos-value* [ **to** *end-cos-value* ] **high**
   
   
   
   The specified low-priority queues on the board are configured as high-priority queues.
   
   By default, the BE, AF1, AF2, AF3, and AF4 queues are low-priority queues and can be configured as high-priority queues. The EF, CS6, and CS7 queues are high-priority queues and cannot be changed.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.