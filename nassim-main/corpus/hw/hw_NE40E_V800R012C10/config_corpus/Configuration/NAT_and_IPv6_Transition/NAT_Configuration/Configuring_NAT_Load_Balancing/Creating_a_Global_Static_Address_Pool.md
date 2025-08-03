Creating a Global Static Address Pool
=====================================

A global static address pool is a prerequisite for CGN load balancing.

#### Context

During load balancing, one NAT instance can be bound to the CPUs of multiple service boards. These CPUs share the same global static address pool, ensuring flexible extension for a single NAT user and the same public network address for multi-core CPUs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat ip-pool**](cmdqueryname=nat+ip-pool) *pool-name* [ **vpn-instance** *vpn-instance-name* ] [ **no-pat** ] [ **slave** ]
   
   
   
   A global static address pool is created, and its view is displayed.
3. Run [**section**](cmdqueryname=section) *section-id* *start-ip* **mask** *mask-length*
   
   
   
   An address segment is configured for the global static address pool.
4. (Optional) Run [**nat-instance subnet length initial**](cmdqueryname=nat-instance+subnet+length+initial) { *mask-length* | *mask* } [ **extend** { *mask-length* | *mask* } ]
   
   
   
   The mask lengths/masks are configured for the initial and extended address segments of the global static address pool.
5. (Optional) Run [**nat-instance ip used-threshold upper-limit**](cmdqueryname=nat-instance+ip+used-threshold+upper-limit) *upper-value* **lower-limit** *lower-value*
   
   
   
   The upper and lower thresholds for address segments that the instance can apply for are configured.
   
   
   
   It is recommended that the default upper and lower thresholds for the number of address segments in a global address pool be used, and the difference between *upper-value* and *lower-value* be greater than 60 (for example, use the **nat-instance ip used-threshold upper-limit 90 lower-limit 20** configuration).
6. (Optional) Run [**nat ip-pool load-balance enable**](cmdqueryname=nat+ip-pool+load-balance+enable)
   
   
   
   The load balancing function is enabled for IP addresses in the global static address pool.
7. (Optional) Run [**section**](cmdqueryname=section) *section-id* **exclude-ip-address** *start-address* [ *end-address* ]
   
   
   
   An IP address or an address segment is excluded from a specified section of the global static address pool.
8. (Optional) Run [**section**](cmdqueryname=section) *section-id* **lock**
   
   
   
   An address segment of the global static address pool is locked.
9. (Optional) Run [**lock**](cmdqueryname=lock)
   
   
   
   The global static address pool is locked.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.