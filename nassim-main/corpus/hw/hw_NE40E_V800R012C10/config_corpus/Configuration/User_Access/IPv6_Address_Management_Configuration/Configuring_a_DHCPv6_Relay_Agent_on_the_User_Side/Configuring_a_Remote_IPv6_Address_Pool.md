Configuring a Remote IPv6 Address Pool
======================================

Configuring a remote IPv6 address pool includes binding a prefix pool to the address pool and configuring a preference and route advertisement for the address pool.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 pool**](cmdqueryname=ipv6+pool) *pool-name* **bas** **remote**
   
   
   
   A remote IPv6 address pool is created, and the corresponding address pool view is displayed.
3. Run [**prefix**](cmdqueryname=prefix) *prefix-name*
   
   
   
   An IPv6 prefix pool is bound to the remote IPv6 address pool.
4. (Optional) Run [**preference**](cmdqueryname=preference) *preference-value*
   
   
   
   A preference is configured for the remote IPv6 address pool.
5. Run [**export host-route**](cmdqueryname=export+host-route)
   
   
   
   The device is enabled to advertise host routes in the remote IPv6 address pool.
6. (Optional) Configure an address assignment mode for remote IPv6 address pools.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   By default, the device assigns addresses from address pools in sequence. You can also configure the device to assign addresses from address pools based on the weights of the address pools or in round-robin mode.
   
   * If the device is configured to assign addresses from address pools in sequence, it selects remote IPv6 address pools for address assignment based on their configuration sequence. For example, three remote IPv6 address pools are configured in a domain. When all users go online, the device selects the first address pool for address assignment. If the first address pool is exhausted, the device selects the second address pool. This process repeats until all users are assigned addresses.
   * If the device is configured to assign addresses from address pools based on their weights, it assigns addresses based on the weight configured for each address pool.
   * If the device is configured to assign addresses from remote IPv6 address pools in round-robin mode, it selects the address pools in turn. For example, three remote IPv6 address pools are configured in a domain. When the first user goes online, the device selects the first address pool; when the second user goes online, the device selects the second address pool; when the third user goes online, the device selects the third address pool; when the fourth user goes online, the device selects the first address pool; when the fifth user goes online, the device selects the second address pool. This process repeats until all users are assigned addresses.
   
   * Configure the device to assign addresses from remote IPv6 address pools based on the weights of the address pools.
     1. Run [**weight**](cmdqueryname=weight) *weight-value*
        
        A weight is configured for the remote IPv6 address pool.
     2. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
     3. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     4. Run [**ipv6-pool algorithm loading-share remote**](cmdqueryname=ipv6-pool+algorithm+loading-share+remote)
        
        The device is configured to assign addresses from remote IPv6 address pools based on the weights of the address pools.
   * Configure the device to assign addresses from remote IPv6 address pools in round-robin mode.
     
     Run [**ipv6-pool algorithm round-robin remote**](cmdqueryname=ipv6-pool+algorithm+round-robin+remote)
     
     The device is configured to assign addresses from remote IPv6 address pools in round-robin mode.
7. (Optional) Set an alarm threshold for the address usage of the IPv6 address pool bound to a VPN instance.
   1. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
      
      
      
      The VPN instance view is displayed.
   3. Run [**ipv6-family**](cmdqueryname=ipv6-family)
      
      
      
      The VPN instance IPv6 address family view is displayed.
   4. Run [**ipv6-pool warning-threshold**](cmdqueryname=ipv6-pool+warning-threshold) *threshold*
      
      
      
      An alarm threshold is set for the address usage of the IPv6 address pool bound to the VPN instance, so that the NE40E generates an alarm when the address usage reaches the threshold.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.