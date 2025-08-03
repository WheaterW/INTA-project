Configuring a Mapping Policy for a Static Source Tracing Algorithm
==================================================================

With a mapping policy for a static source tracing algorithm, the mapping between the IP addresses in a private address pool, the IP addresses in a public address pool, and the port range can be manually specified.

#### Context

Before configuring a static source tracing algorithm, plan the mapping between private addresses, public addresses, and port numbers. After a private IP address is bound to a public IP address, the public IP address in the public IP address pool cannot be mapped to another private IP address.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat static-mapping**](cmdqueryname=nat+static-mapping)
   
   
   
   The static mapping algorithm view is displayed.
3. Run [**inside-pool**](cmdqueryname=inside-pool) *inside-pool-id* 
   
   
   
   A private address pool is configured.
4. Run [**section**](cmdqueryname=section) *section-id* *start-address* *end-address*
   
   
   
   The private IP address range is configured.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the private address pool view.
7. Run [**global-pool**](cmdqueryname=global-pool) *global-pool-id*
   
   
   
   The public address pool ID is configured.
8. Run [**section**](cmdqueryname=section) *section-id* *start-address* *end-address*
   
   
   
   The public IP address range is configured.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
10. Run [**quit**](cmdqueryname=quit)
    
    
    
    Exit the public address pool view.
11. Run [**static-mapping**](cmdqueryname=static-mapping+inside-pool+global-pool+port-range+port-size) *static-mapping-id* **inside-pool** *inside-pool-id* **global-pool** *global-pool-id* **port-range** *start-port* *end-port* [ **port-size** *port-size* ]
    
    
    
    The mapping between the IP address range of the private address pool, the IP address range of the public address pool, and the port numbers is configured.
    
    
    
    A public or private address pool can exist only in one static source tracing algorithm mapping.
12. (Optional) Run [**exclude**](cmdqueryname=exclude+static-mapping) *start-port* *end-port* **static-mapping** *static-mapping-id*
    
    
    
    The range of ports that are not allocated based on the static source tracing algorithm is configured.
13. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.