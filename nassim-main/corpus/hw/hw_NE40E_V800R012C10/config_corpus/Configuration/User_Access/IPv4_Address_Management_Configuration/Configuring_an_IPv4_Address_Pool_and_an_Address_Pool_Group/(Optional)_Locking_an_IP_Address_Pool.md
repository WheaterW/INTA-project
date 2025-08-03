(Optional) Locking an IP Address Pool
=====================================

This section describes how to lock an IP address pool so
that the address pool cannot be used to assign IP addresses to new
users.

#### Context

An IP address pool with an in-use IP address cannot be
deleted. Therefore, configure the drain function to lock the address
pool before you delete the address pool. After an IP address pool
is locked using the [**lock drain**](cmdqueryname=lock+drain) command, DHCP Request
messages for lease renewal from online users will be discarded. The
address pool can be deleted after all online users using the address
pool go offline upon lease expiry. If you only need to disable an
IP address pool so that the address pool will not be used to assign
IP addresses to new users but online users can still use assigned
IP addresses, configure the lock function to lock the address pool
using the **lock** command.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip pool**](cmdqueryname=ip+pool) *pool-name* [ **bas** { **local** | **remote** } ]
   
   
   
   The IP address pool view is displayed.
3. Perform either of the following configurations as needed:
   
   
   * Configure the drain function to lock the address pool.
     
     1. Run [**lock
        drain**](cmdqueryname=lock+drain)
        
        The IP address pool is locked so
        that the address pool cannot be used to assign IP addresses to new
        users and Request messages for lease renewal from online users using
        the address pool are discarded.
     2. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Configure the lock function to lock the address pool.
     
     1. Run [**lock**](cmdqueryname=lock)
        
        The IP address pool is locked so
        that the address pool cannot be used to assign IP addresses to new
        users but Request messages for lease renewal from online users can
        still be processed.
     2. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.