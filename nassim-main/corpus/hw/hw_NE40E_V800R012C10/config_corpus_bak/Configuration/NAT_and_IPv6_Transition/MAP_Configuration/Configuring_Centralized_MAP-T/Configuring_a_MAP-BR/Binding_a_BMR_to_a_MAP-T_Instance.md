Binding a BMR to a MAP-T Instance
=================================

This section describes how to bind a BMR to a MAP-T instance. The BMR is used to encapsulate and verify packets in the MAP-T instance.

#### Prerequisites

A BMR has been configured.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view of the PE is displayed.
2. Run [**map-t instance**](cmdqueryname=map-t+instance) *map-t-instance-name* [ **id** *id* ]
   
   
   
   The MAP-T instance view is displayed.
3. Run [**map-rule**](cmdqueryname=map-rule) *rule-name*
   
   
   
   A BMR is bound to the MAP-T instance.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.