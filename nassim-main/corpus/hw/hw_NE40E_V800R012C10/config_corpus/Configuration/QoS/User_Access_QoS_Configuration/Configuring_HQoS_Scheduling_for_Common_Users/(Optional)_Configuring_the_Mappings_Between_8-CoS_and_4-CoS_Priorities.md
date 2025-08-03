(Optional) Configuring the Mappings Between 8-CoS and 4-CoS Priorities
======================================================================

You can define the mappings between 8-CoS and 4-CoS priorities to provide more flexible 4-CoS priority configurations.

#### Context

The system has the default mappings between 8-CoS and 4-CoS priorities. The default mappings are as follows.

| Flow Queue | Mappings | Scheduling Mode | Weight | Traffic Shaping Percentage | Drop Mode |
| --- | --- | --- | --- | --- | --- |
| cos0 | BE and AF1 | WFQ | 10 | - | Tail drop |
| cos1 | AF2, AF3, and AF4 | WFQ | 15 | - | Tail drop |
| cos2 | EF | PQ | - | - | Tail drop |
| cos3 | CS6 and CS7 | PQ | - | - | Tail drop |

You can define the mappings between 8-CoS and 4-CoS priorities.

In VS mode, this configuration is supported only by the admin VS.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**queue-4cos-mapping**](cmdqueryname=queue-4cos-mapping) *mapping-name*
   
   
   
   A 4-CoS mapping profile is created and its view is displayed.
3. Run [**queue**](cmdqueryname=queue) *serviceclass* **mapping** { **cos0** | **cos1** | **cos2** | **cos3** }
   
   
   
   The mappings between 8-CoS and 4-CoS priorities are configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.