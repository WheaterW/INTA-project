(Optional) Configuring a Mapping from an FQ to a PQ
===================================================

If you want to define a mapping from an FQ to a PQ instead of using the default mapping, you need to set the priority of a type of service in a user queue entering a PQ.

#### Context

Perform the following configurations on the Router.

You can configure eight mappings from FQs to PQs in one FQ mapping profile.

If no FQ-to-PQ mapping is set, the system defaults the one-to-one mapping.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**flow-mapping**](cmdqueryname=flow-mapping) *mapping-name*
   
   
   
   The flow mapping view is displayed.
3. Run [**map flow-queue**](cmdqueryname=map+flow-queue) *cos-value* **to** **port-queue** *cos-value*
   
   
   
   The CoS of the FQ is mapped to the CoS of the PQ.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.