(Optional) Configuring IPv4 Address Pool Isolation
==================================================

By default, the association between IPv4 address pool isolation and master/slave main control board switchover is enabled. You can enable or disable this function as required.

#### Context

By default, automatic isolation is enabled for an IPv4 address pool. If a user fails to apply for an IPv4 address from an IPv4 address pool for 50 consecutive times, the address pool is considered faulty and automatically isolated. The device preferentially selects another available address pool for address allocation. If no other address pool is available, the device selects the current address pool. If the address pool isolation function is disabled, the address pool will not be automatically isolated even if a user fails to apply for an IP address from the address pool for 50 consecutive times. The device still assigns an IP address to the user from this address pool.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip-pool auto-block enable**](cmdqueryname=ip-pool+auto-block+enable)
   
   
   
   The automatic isolation of IPv4 address pools is enabled.
3. (Optional) Run [**ip-pool auto-block slave-switch enable**](cmdqueryname=ip-pool+auto-block+slave-switch+enable)
   
   
   
   The association between the IPv4 address pool isolation function and the master/slave main control board switchover function is enabled.
   
   
   
   If the address pool on the master slave is isolated and the address pool on the slave main control board is not isolated, you can enable the IPv4 address pool isolation function to trigger a master/slave main control board switchover.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.