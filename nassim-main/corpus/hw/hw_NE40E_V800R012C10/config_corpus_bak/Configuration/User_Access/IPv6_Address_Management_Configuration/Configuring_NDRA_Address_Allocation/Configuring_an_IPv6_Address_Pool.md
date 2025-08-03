Configuring an IPv6 Address Pool
================================

In NDRA address allocation mode, after an IPv6 prefix pool is configured, you need to configure an IPv6 address pool.

#### Context

* Prefix pool binding
  
  A prefix pool can be bound only to one address pool. Similarly, an address pool can be bound only to one prefix pool.
  
  **Table 1** Binding between address pools and prefix pools
  | Address Pool Type | IPv6 Prefix Pool That Can be Bound |
  | --- | --- |
  | User-side local address pool | Local prefix pool |
  | User-side delegation address pool | Delegation prefix pool |
  | User-side relay address pool | Local prefix pool |
  | User-side remote address pool | Remote prefix pool |
* Priority configuration
  
  Among address pools of the same type, a larger value indicates a higher priority.
  
  In NDRA address allocation mode, BAS local address pools are used to allocate shared prefixes, and BAS delegation address pools are used to allocate unshared prefixes. A BAS delegation address pool with the [**slaac-unshare-only**](cmdqueryname=slaac-unshare-only) command configured takes precedence over other BAS delegation address pools.
* Address pool locking
  
  This method is usually used when an address pool cannot be deleted because an IP address in the pool is already used by an online user. In this case, lock the address pool so that no IP address can be assigned from this address pool. After all users go offline and all IP addresses in the address pool are released, delete the address pool.
* DNS suffix configuration
  
  Only one DNS suffix can be set for each IPv6 address pool.
* DNS server configuration
  
  A maximum of two DNS servers can be bound to an IPv6 address pool.
* Address lease configuration
  
  If an IPv6 address pool has been bound to a domain, the address lease cannot be changed.

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. (Optional) Run the [**access wait-request-time dhcpv6**](cmdqueryname=access+wait-request-time+dhcpv6) *time-value* command to configure a timeout period for the router to wait for a Request message from a client in response to an Advertise message sent to the client.
3. Run the [**ipv6 pool**](cmdqueryname=ipv6+pool) *pool-name* { **bas** { **local** | **delegation** | **remote** } } command to create an IPv6 address pool and enter its view.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
5. Run the [**prefix**](cmdqueryname=prefix) *prefix-name* command to bind an IPv6 prefix pool to the IPv6 address pool.
6. (Optional) Run the [**preference**](cmdqueryname=preference) *preference-value* command to configure a preference value for the IPv6 address pool.
7. (Optional) Run the [**dns-server**](cmdqueryname=dns-server) *ipv6-address* *&<1-2>* command to specify a DNS server for the IPv6 address pool. The DNS server is specified using an IPv6 address.
8. (Optional) Run the [**dns-search-list**](cmdqueryname=dns-search-list) *dns-search-list-name* command to configure a DNS suffix for domain name resolution.
9. (Optional) Run the [**renew-time-percent**](cmdqueryname=renew-time-percent) *renew-time-value* **rebind-time-percent** *rebind-time-value* command to configure a lease renewal time and rebinding time for the IPv6 address pool.
10. (Optional) Run the [**wait-request-time**](cmdqueryname=wait-request-time) *time-value* command to configure a timeout period for the router to wait for a Request message from a client in response to an Advertise message sent to the client.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The [**wait-request-time**](cmdqueryname=wait-request-time) *time-value* command is run in the address pool view, and the [**access wait-request-time dhcpv6**](cmdqueryname=access+wait-request-time+dhcpv6) *time-value* command is run in the system view. If both commands are run, the command run in the address pool view takes effect.
11. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
12. (Optional) Run the [**ipv6-pool statistic include shared-user**](cmdqueryname=ipv6-pool+statistic+include+shared-user) command to configure IPv6 address pool statistics to include statistics about users sharing the prefix pool.
13. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.