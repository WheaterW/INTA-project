Binding a BR to a MAP-E Instance
================================

This section describes how to bind a BR to a MAP-E instance so that a MAP-CE selects a MAP-E instance to convert IPv6 packets after MAP processing.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view of the PE is displayed.
2. Run [**map-e instance**](cmdqueryname=map-e+instance) *map-e-instance-name* [ **id** *id* ]
   
   
   
   The MAP-E instance view is displayed.
3. Run [**br-ipv6-address**](cmdqueryname=br-ipv6-address) *br-name*
   
   
   
   A BR is bound to the MAP-E instance.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.