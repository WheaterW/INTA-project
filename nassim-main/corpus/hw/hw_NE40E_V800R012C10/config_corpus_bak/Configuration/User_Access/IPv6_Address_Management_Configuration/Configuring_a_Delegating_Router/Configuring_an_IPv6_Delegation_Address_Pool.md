Configuring an IPv6 Delegation Address Pool
===========================================

Configuring an IPv6 delegation address pool includes binding a prefix pool to the address pool and configuring a preference and other services (such as a DNS or DNS suffix) for the address pool.

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

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 pool**](cmdqueryname=ipv6+pool) *pool-name* **bas** **delegation**
   
   
   
   An IPv6 delegation address pool is created, and the corresponding address pool view is displayed.
3. Run the [**prefix**](cmdqueryname=prefix) *prefix-name* command to bind an IPv6 prefix pool to the IPv6 address pool.
4. (Optional) Run the [**preference**](cmdqueryname=preference) *preference-value* command to configure a preference value for the IPv6 address pool.
5. (Optional) Run the [**dns-search-list**](cmdqueryname=dns-search-list) *dns-search-list-name* command to configure a DNS suffix for domain name resolution.
6. (Optional) Run the [**dns-server**](cmdqueryname=dns-server) *ipv6-address* *&<1-2>* command to specify a DNS server for the IPv6 address pool. The DNS server is specified using an IPv6 address.
7. (Optional) Run the [**renew-time-percent**](cmdqueryname=renew-time-percent) *renew-time-value* **rebind-time-percent** *rebind-time-value* command to configure a lease renewal time and rebinding time for the IPv6 address pool.
8. (Optional) Run the [**option**](cmdqueryname=option) *code* { **ipv6-address** *ipv6-address* & <1-2> | **string** *string* | **hex** *hex-string* }&<1-160> command or the [**option**](cmdqueryname=option) *code* { **suboption** *subcode* { **ipv6-address** *ipv6-address* | **string** *string-value* } } & <1-16> command to configure a DHCPv6 user-defined option.
9. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
10. (Optional) Run [**ipv6-pool algorithm round-robin local**](cmdqueryname=ipv6-pool+algorithm+round-robin+local)
    
    
    
    The device is configured to assign addresses from IPv6 delegation address pools in round-robin mode.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.