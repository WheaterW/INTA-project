(Optional) Locking an IPv6 Address Pool
=======================================

This section describes how to lock an IPv6 address pool
so that the address pool cannot be used to assign IPv6 addresses to
new users.

#### Context

An IPv6 address pool with an in-use IPv6 address cannot
be deleted. Therefore, configure the drain function to lock the IPv6
address pool before you delete the address pool. After an IPv6 address
pool is locked using the [**lock drain**](cmdqueryname=lock+drain) command, DHCP
Renew or Rebind messages from online users will be discarded. The
IPv6 address pool can be deleted after all online users using the
address pool go offline upon lease expiry. If you only need to disable
an IPv6 address pool so that the address pool will not be used to
assign IPv6 addresses to new users but online users can still use
assigned IPv6 addresses, configure the lock function to lock the address
pool using the **lock** command.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 pool**](cmdqueryname=ipv6+pool) *pool-name* [ **bas** { **local** | **remote** | **delegation** | **relay** } ]
   
   
   
   The IPv6 address pool view is displayed.
3. Perform either of the following configurations as needed:
   
   
   * Configure the drain function to lock the IPv6 address pool.
     
     1. Run [**lock drain**](cmdqueryname=lock+drain)
        
        The IPv6 address pool is locked
        so that the address pool cannot be used to assign IPv6 addresses to
        new users and Renew or Rebind messages from online users using the
        address pool are discarded.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        This command
        does not take effect for ND users in remote address pool scenarios.
     2. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Configure the lock function to lock the IPv6 address pool.
     
     1. Run [**lock**](cmdqueryname=lock)
        
        The IPv6 address pool is locked
        so that the address pool cannot be used to assign IPv6 addresses to
        new users but Renew or Rebind messages from online users can still
        be processed.
     2. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.