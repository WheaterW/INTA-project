Binding a DMR to a MAP-T Instance
=================================

This section describes how to bind a DMR to a MAP-T instance. The DMR is used by a MAP-CE to select a MAP-T instance to convert IPv6 packets.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view of the PE is displayed.
2. Run [**map-t instance**](cmdqueryname=map-t+instance) *map-t-instance-name* [ **id** *id* ]
   
   
   
   The MAP-T instance view is displayed.
3. Run [**dmr-prefix**](cmdqueryname=dmr-prefix) *dmr-name*
   
   
   
   A DMR is bound to the MAP-T instance.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.