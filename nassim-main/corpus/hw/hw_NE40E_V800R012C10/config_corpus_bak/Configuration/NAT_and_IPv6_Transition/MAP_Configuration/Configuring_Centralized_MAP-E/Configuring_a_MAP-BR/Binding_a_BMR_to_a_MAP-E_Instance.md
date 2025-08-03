Binding a BMR to a MAP-E Instance
=================================

This section describes how to bind a BMR to a MAP-E instance. The BMR is used to encapsulate and verify packets in the MAP-E instance.

#### Prerequisites

A BMR has been configured.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view of the PE is displayed.
2. Run [**map-e instance**](cmdqueryname=map-e+instance) *map-e-instance-name* [ **id** *id* ]
   
   
   
   The MAP-E instance view is displayed.
3. Run [**map-rule**](cmdqueryname=map-rule) *rule-name*
   
   
   
   A BMR is bound to the MAP-E instance.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.