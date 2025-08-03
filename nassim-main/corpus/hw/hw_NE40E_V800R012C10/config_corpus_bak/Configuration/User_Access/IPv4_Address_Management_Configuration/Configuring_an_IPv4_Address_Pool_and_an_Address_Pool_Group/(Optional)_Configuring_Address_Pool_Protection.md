(Optional) Configuring Address Pool Protection
==============================================

Configuring address pool protection includes locking an address pool, disabling IP addresses, and reclaiming IP addresses in special scenarios.

#### Context

Address pool protection can be performed using the following methods:

* Locking an address pool
  
  An address pool can be locked using a command. IP addresses in a locked address pool cannot be assigned any more.
  
  This method is usually used when an address pool cannot be deleted because an address in the pool is already used by an online user. In this case, lock the address pool so that no address can be assigned from this address pool. After all users go offline and all IP addresses in the address pool are released, delete the address pool.
* Disabling IP addresses
  
  In complex network planning, some IP addresses may need to be disabled.
* IP Address Reclaiming
  
  When an IP address in an address pool is abnormal, that is, the IP address is in use but actually no user is using it, this IP address cannot be used any more. In this case, you can run a command to forcibly reclaim the IP address.

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ip pool**](cmdqueryname=ip+pool) *pool-name* [ **bas** { **local** | **remote** } | **server** ] command to create an address pool and enter the address pool view.
3. Run the [**lock**](cmdqueryname=lock) command to lock the address pool.
   
   
   
   Alternatively, run the [**excluded-ip-address**](cmdqueryname=excluded-ip-address) *start-ip-address* [ *end-ip-address* ] command to exclude an IP address or an address segment.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command is required when you configure static IP addresses.
   
   Alternatively, run the [**recycle**](cmdqueryname=recycle) *start-ip-address* [ *end-ip-address* ] command to reclaim an IP address or an address segment.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.