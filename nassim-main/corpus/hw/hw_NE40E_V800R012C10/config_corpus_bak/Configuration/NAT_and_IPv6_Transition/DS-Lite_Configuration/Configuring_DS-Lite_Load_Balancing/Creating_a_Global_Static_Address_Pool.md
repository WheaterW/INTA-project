Creating a Global Static Address Pool
=====================================

Creating a global static address pool is mandatory for DS-Lite load balancing. To allow for DS-Lite load balancing, a DS-Lite instance needs to be created and be bound to a global static address pool.

#### Context

During load balancing, one DS-Lite instance can be bound to the CPUs of multiple service boards. These CPUs share the same global static address pool, ensuring flexible extension for a single DS-Lite user and the same public network address for multi-core CPUs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat ip-pool**](cmdqueryname=nat+ip-pool) *pool-name* [ **vpn-instance** *vpn-instance-name* ] [ **no-pat** ] [ **slave** ]
   
   
   
   A global static address pool is created, and the global static address pool view is displayed.
3. Run [**section**](cmdqueryname=section) *section-id* *start-ip* **mask** *mask-length*
   
   
   
   An address segment is configured for the global static address pool.
4. Run [**nat-instance subnet length initial**](cmdqueryname=nat-instance+subnet+length+initial) { *mask-length* | *mask* } [ **extend** { *mask-length* | *mask* } ]
   
   
   
   The mask lengths/masks are configured for the initial and extended address segments of the global static address pool.
5. (Optional) Run [**nat-instance ip used-threshold upper-limit**](cmdqueryname=nat-instance+ip+used-threshold+upper-limit) *upper-value* **lower-limit** *lower-value*
   
   
   
   The upper limit and lower limit for the address segments in the global static address pool are configured.
   
   
   
   Using the default upper limit
   and lower limit of an address segment in a global address pool is
   recommended, and the difference between *upper-value* and *lower-value* must be over 60. For example, **nat-instance ip used-threshold upper-limit 90 lower-limit 20**.
6. (Optional) Run [**section**](cmdqueryname=section) *section-id* **exclude-ip-address** *start-address* [ *end-address* ]
   
   
   
   An IP address or an address segment is excluded from a specified section of the global static address pool.
7. (Optional) Run [**section**](cmdqueryname=section) *section-id* **lock**
   
   
   
   The address segment of the global static address pool is locked.
8. (Optional) Run [**lock**](cmdqueryname=lock)
   
   
   
   The global static address pool is locked.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.