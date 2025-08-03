Creating a CGN Global Address Pool
==================================

Two types of CGN global address pools are available: static address pool and dynamic address pool. The difference between the two types of CGN global address pools is that the address segments in a dynamic global address pool require a CGN device to dynamically apply for address segments from a RADIUS server, whereas the address segments in a static global address pool are manually configured on a CGN device. A NAT instance dynamic address pool can apply for address segments from either a static or dynamic global address pool. A CGN global address pool supports both centralized and distributed CGN scenarios.

#### Context

A CGN global address pool saves public network addresses and simplifies configurations, facilitating public address management.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the NE40E-M2K and NE40E-M2K-B support this configuration.


![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only dedicated boards support this configuration.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a CGN global static address pool.
   
   
   1. Run [**nat ip-pool**](cmdqueryname=nat+ip-pool+vpn-instance+no-pat) *pool-name* [ **vpn-instance** *vpn-instance-name* ] [ **no-pat** ]
      
      A static CGN global address pool is created.
   2. Run [**section**](cmdqueryname=section+mask) *section-id* *start-ip* **mask** *mask-length*
      
      An address segment is created.
   3. (Optional) Run [**section**](cmdqueryname=section+lock) *section-num* **lock**
      
      An address segment in the address pool is locked. IP addresses in the locked address segment cannot be allocated to users anymore. To unlock this address segment, run the [**undo section**](cmdqueryname=undo+section+lock) *section-num* **lock** command.
   4. Run [**nat-instance subnet length**](cmdqueryname=nat-instance+subnet+length+initial) **initial** { *mask-length* | *mask* } [ **extend** { *mask-length* | *mask* } ]
      
      The lengths of the initial and extended address segments that a dynamic NAT address pool requests from the static global address pool are configured.
   5. Run [**nat-instance ip used-threshold**](cmdqueryname=nat-instance+ip+used-threshold+upper-limit+lower-limit) **upper-limit** *upper-value* **lower-limit** *lower-value*
      
      The address segment requesting and releasing thresholds for the dynamic NAT address pool are configured.
   6. (Optional) Run [**nat ip-pool load-balance enable**](cmdqueryname=nat+ip-pool+load-balance+enable)
      
      The load balancing function is enabled for the global static address pool.
   7. (Optional) Run [**lock**](cmdqueryname=lock)
      
      The static global address pool is locked.
   8. (Optional) Run [**nat alarm ip**](cmdqueryname=nat+alarm+ip+log+trap+disable) { **log** | **trap** } **disable**
      
      The log or trap function for the global address pool is disabled.
   9. (Optional) Run [**nat alarm ip threshold**](cmdqueryname=nat+alarm+ip+threshold) *value*
      
      An alarm threshold is set for the global address pool.
   10. (Optional) Run [**section**](cmdqueryname=section+exclude-ip-address) *section-id* **exclude-ip-address** *start-address* [ *end-address* ]
       
       A single IP address or a range of IP addresses is excluded from a specified NAT address pool.
   11. (Optional) Run [**export subnet-route**](cmdqueryname=export+subnet-route)
       
       The global address pool is enabled to advertise network segment routes.
       
       By default, a network segment route is advertised only after the network segment in a global address pool is assigned to an instance. If the mask length of the network segment allocated to an instance is large, a large number of routes with long masks are generated. In this case, you can perform this step to enable the CGN device to advertise the summary route to upstream and downstream devices.
   12. Run [**quit**](cmdqueryname=quit)
       
       Return to the system view.
3. Configure a dynamic CGN global address pool.
   
   
   1. Run [**nat ip-pool**](cmdqueryname=nat+ip-pool+dynamic+vpn-instance+no-pat) *pool-name* **dynamic** [ **vpn-instance** *vpn-instance-name* ] [ **no-pat** ]
      
      The dynamic CGN global address pool is created.
   2. Run [**radius-server group**](cmdqueryname=radius-server+group) *group-name*
      
      The RADIUS server group used by the dynamic CGN global address pool is configured.
   3. Run [**authentication-name**](cmdqueryname=authentication-name+password+cipher) *authentication-name* **password** **cipher** *password*
      
      The authentication username and password for the RADIUS server group used by the dynamic CGN global address pool are configured.
   4. Run [**subnet length**](cmdqueryname=subnet+length+initial) **initial** { *initial-mask-length* | *initial-mask* } [ **extend** { *extend-mask-length* | *extend-mask* } ]
      
      The lengths of the initial and extended address segments that the dynamic global address pool requests from the RADIUS server are configured.
   5. Run [**ip used-threshold**](cmdqueryname=ip+used-threshold+upper-limit+lower-limit) **upper-limit** *upper-value* **lower-limit** *lower-value*
      
      The address segment requesting and releasing thresholds for the dynamic global address pool are configured.
   6. Run [**nat-instance subnet length**](cmdqueryname=nat-instance+subnet+length+initial) **initial** { *mask-length* | *mask* } [ **extend** { *mask-length* | *mask* } ]
      
      The lengths of the initial and extended address segments that a dynamic NAT address pool requests from the dynamic global address pool are configured.
   7. Run [**nat-instance ip used-threshold**](cmdqueryname=nat-instance+ip+used-threshold+upper-limit+lower-limit) **upper-limit** *upper-value* **lower-limit** *lower-value*
      
      The address segment requesting and releasing thresholds for the dynamic NAT address pool are configured.
   8. Run [**detect retransmit**](cmdqueryname=detect+retransmit+interval) *retransmit-value* **interval** *day-value* *hour-value* *minute-value*
      
      The lease renewal retransmission times and interval for the dynamic global address pool are configured.
   9. (Optional) Run [**lock**](cmdqueryname=lock)
      
      The dynamic global address pool is locked.
   10. (Optional) Run [**nat alarm ip**](cmdqueryname=nat+alarm+ip+log+trap+disable) { **log** | **trap** } **disable**
       
       The log or trap function for the global address pool is disabled.
   11. (Optional) Run [**nat alarm ip threshold**](cmdqueryname=nat+alarm+ip+threshold) *value*
       
       An alarm threshold is set for the global address pool.
   12. (Optional) Run [**export subnet-route**](cmdqueryname=export+subnet-route)
       
       The global address pool is enabled to advertise network segment routes.
       
       By default, a network segment route is advertised only after the network segment in a global address pool is assigned to an instance. If the mask length of the network segment allocated to an instance is large, a large number of routes with long masks are generated. In this case, you can perform this step to enable the CGN device to advertise the summary route to upstream and downstream devices.
   13. Run [**quit**](cmdqueryname=quit)
       
       Return to the system view.
4. Bind the dynamic NAT address pool to a CGN global address pool.
   
   
   1. Run [**nat instance**](cmdqueryname=nat+instance+id) *instance-name* [ **id** *id* ]
      
      The NAT instance view is displayed.
   2. Run [**nat address-group**](cmdqueryname=nat+address-group+group-id+bind-ip-pool+over-load) *address-group-name* **group-id** *group-id* **bind-ip-pool** *pool-name* [ **over-load** ]
      
      The dynamic NAT address pool is bound to the CGN global address pool.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Binding a dynamic address pool in a NAT instance to a CGN global address pool is mutually exclusive with configuring a static algorithm, port-forwarding, and common address pool.
   3. Run [**nat outbound**](cmdqueryname=nat+outbound+any+address-group) { *acl-number* | **any** } **address-group** *address-group-name*
      
      A conversion policy is configured for the NAT address pool. Either the ACL matching mode or non-ACL matching mode can be selected.
   4. Run [**quit**](cmdqueryname=quit)
      
      Return to the system view.
   5. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.