Applying a Static Source Tracing Algorithm to a NAT Instance
============================================================

This section describes how to apply a static source tracing algorithm to a NAT instance so that the mapping between the IP addresses in the private and public address pools is applied to the NAT instance.

#### Context

A static source tracing algorithm and a dynamic NAT algorithm are mutually exclusive in the NAT instance view. After a static source tracing algorithm is bound to a NAT instance, the mapping relationship of the static source tracing algorithm is applied to the NAT instance.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat instance**](cmdqueryname=nat+instance+id) *instance-name* [ **id** *id* ]
   
   
   
   The NAT instance view is displayed.
3. Run [**nat bind static-mapping**](cmdqueryname=nat+bind+static-mapping) *static-mapping-id*
   
   
   
   The static source tracing algorithm is bound to the NAT instance.
   
   
   
   A static source tracing algorithm can be applied to one NAT instance.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.