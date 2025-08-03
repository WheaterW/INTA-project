Configuring an IPv6 Prefix Pool
===============================

Before configuring the NDRA address assignment mode, you need to configure an IPv6 prefix pool and bind it to an address pool.

#### Context

Only one prefix and its mask can be configured in a prefix pool. After a prefix pool is locked, the leases of addresses that have been assigned cannot be renewed and new addresses cannot be assigned. The address reservation type can be configured only in a prefix pool.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ipv6 prefix**](cmdqueryname=ipv6+prefix) *prefix-name* [ **local** | **delegation** | **remote** ] command to create an IPv6 prefix pool and enter the IPv6 prefix pool view.
   
   
   * After the local prefix pool is bound to the local IPv6 address pool, the local device functions as a server to assign prefixes or IPv6 addresses to users.
   * After a delegation prefix pool is bound to an IPv6 delegation address pool, the local device functions as a delegating router to assign IPv6 prefixes to requesting routers. Requesting routers exclusively use these IPv6 prefixes. The delegation prefix pool with the [**slaac-unshare-only**](cmdqueryname=slaac-unshare-only) command configured has a higher priority.
   * After a remote prefix pool is bound to a remote IPv6 address pool, the remote DHCPv6 server assigns IPv6 prefixes or addresses to users.
3. (Optional) Run the [**slaac-unshare-only**](cmdqueryname=slaac-unshare-only) command to configure the delegation prefix pool to be used only in stateless address assignment mode.
   
   
   
   The delegation prefix pool configured with this command can only be used for unshared prefix assignment through ND, instead of DHCPv6 IA\_PD prefix assignment, and is preferred in IPv6 prefix assignment through ND.
4. Run the [**prefix**](cmdqueryname=prefix) *prefix-address/prefix-length* [ **delegating-prefix-length** *delegating-prefix-length* ] command to configure an IPv6 address prefix.
   
   
   
   The assignable prefix length is the length of the IPv6 prefix that a delegating router assigns to a requesting router. The assignable prefix length configured in a prefix pool must be greater than the prefix length configured in the prefix pool. Otherwise, prefixes in the prefix pool cannot be assigned to users.
5. (Optional) Run the [**excluded-ipv6-address**](cmdqueryname=excluded-ipv6-address) *start-ipv6-address* [ *end-ipv6-address* ] command to exclude a specified IPv6 address or address segment.
   
   
   
   The excluded IPv6 addresses must be in the assignable range of the prefix pool. If the end IPv6 address is not specified, only the start IPv6 address is excluded.
6. (Optional) Run the [**excluded-ipv6-prefix**](cmdqueryname=excluded-ipv6-prefix) *start-ipv6-prefix/prefix-length* [ *end-ipv6-prefix/prefix-length* ] command to exclude one or more IPv6 prefixes.
   
   
   
   The excluded IPv6 prefix must be in the assignable range of the prefix pool. When the end IPv6 prefix is not specified, only the start IPv6 prefix is excluded.
7. (Optional) Run the [**lock**](cmdqueryname=lock) command to lock an IPv6 prefix pool.
   
   
   
   After this command is run, no prefix in the locked prefix pool can be assigned, preventing new users from going online using prefixes in the prefix pool.
   
   This method is typically used when a prefix pool cannot be deleted because its prefixes are in use by online users. You can lock the prefix pool first to stop it from assigning prefixes. After all users go offline, the prefixes in the prefix pool are all released, and the prefix pool can then be deleted.
8. (Optional) Run the [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name* command to bind a VPN instance to the prefix pool.
9. (Optional) Run the [**lifetime preferred-lifetime**](cmdqueryname=lifetime+preferred-lifetime) { **days** *days-value* [ **hours** *hours-value* [ **minutes** *minutes-value* ] ] | **infinite** } **valid-lifetime** { **days** *days-value* [ **hours** *hours-value* [ **minutes** *minutes-value* ] ] | **infinite** } command to configure the lifetime of IPv6 prefixes.
   
   
   
   The **preferred-lifetime** parameter is used to calculate the lease renewal time and rebinding time of the IPv6 prefix pool. The time value must be no less than 1 minute. The default value is two days.
   
   The **valid-lifetime** parameter specifies the validity period of a specified IPv6 prefix. The user using the prefix will be logged out after the validity period expires. The time value must be no less than 1 minute and the **preferred-lifetime** value. The default value is three days.
10. (Optional) Run the [**conflict auto-recycle**](cmdqueryname=conflict+auto-recycle) **interval** *interval-time* command to configure the interval for automatically reclaiming conflicting prefixes.
    
    
    
    This command takes effect only in the local prefix pool.
11. (Optional) Run the [**reserved prefix**](cmdqueryname=reserved+prefix) { **duid** | **mac** } [ **lease** ] command to configure the reservation type of user prefixes in the prefix pool.
    
    
    
    This command can be run only in the local and delegation prefix pools.
12. (Optional) Run the [**recycle prefix**](cmdqueryname=recycle+prefix) *start-prefix* [ *end-prefix* ] command to configure the prefix status as idle.
13. (Optional) Run the [**reserved ipv6-address**](cmdqueryname=reserved+ipv6-address) { **duid** | **mac** } [ **lease** ] command to configure the reservation type of user addresses in the prefix pool.
    
    
    
    This command can be configured only in the remote prefix pool.
14. (Optional) Run the [**recycle ipv6-address**](cmdqueryname=recycle+ipv6-address) *start-prefix* [ *end-prefix* ] command to configure the address status as idle.
    
    
    
    The command can only be run in the local prefix pool.
15. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.