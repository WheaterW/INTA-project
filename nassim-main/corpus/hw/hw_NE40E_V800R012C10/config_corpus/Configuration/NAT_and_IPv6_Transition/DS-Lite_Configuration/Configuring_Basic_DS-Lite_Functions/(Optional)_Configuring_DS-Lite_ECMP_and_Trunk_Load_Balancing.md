(Optional) Configuring DS-Lite ECMP and Trunk Load Balancing
============================================================

If multiple next hops are used to forward user packets destined for the same destination, configure a proper hash algorithm and its harsh factor to implement equal cost multi-path (ECMP) and trunk load balancing on a DS-Lite network.

#### Context

In a DS-Lite ECMP and trunk load balancing scenario, multiple traffic models are used. If the default hash algorithm does not meet your expectation, configure another hash algorithm or change the hash factor, which implements best load balancing performance.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the NE40E-M2K and NE40E-M2K-B support this configuration.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* [ **id** *id* ]
   
   
   
   The view of a DS-Lite instance is displayed.
3. Run [**ds-lite load-balance hash-arithmetic**](cmdqueryname=ds-lite+load-balance+hash-arithmetic) { **hash-arithmetic1** | **hash-arithmetic2** | **hash-arithmetic3** }
   
   
   
   A hash algorithm for ECMP and trunk load balancing is configured.
4. Run [**ds-lite load-balance hash-fields**](cmdqueryname=ds-lite+load-balance+hash-fields) **ip** { **l3** | **l4** }
   
   
   
   A hash element for ECMP and trunk load balancing is configured.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.