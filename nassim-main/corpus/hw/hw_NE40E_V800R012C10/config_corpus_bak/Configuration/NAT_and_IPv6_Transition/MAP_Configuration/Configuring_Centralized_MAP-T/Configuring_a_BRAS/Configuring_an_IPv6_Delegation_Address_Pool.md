Configuring an IPv6 Delegation Address Pool
===========================================

In a MAP-T scenario, a prefix pool, a DMR prefix, and an FMR flag bit need to be configured in an IPv6 delegation address pool.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 pool**](cmdqueryname=ipv6+pool) *pool-name* **bas delegation**
   
   
   
   An IPv6 delegation address pool is created, and the IPv6 delegation address pool view is displayed.
3. Run [**prefix**](cmdqueryname=prefix) *prefix-name*
   
   
   
   An IPv6 prefix pool is bound to the IPv6 address pool.
4. Run [**option-s46 dmr-prefix**](cmdqueryname=option-s46+dmr-prefix) *dmr-prefix-name*
   
   
   
   A DMR prefix name is bound to the IPv6 address pool. The NE40E encapsulates the IPv6 prefix as Option 91 information (OPTION\_S46\_DMR) into the DHCPv6 Response message sent to MAP-T users.
5. (Optional) Run [**option-s46 fmr-flag disable**](cmdqueryname=option-s46+fmr-flag+disable)
   
   
   
   The F-flag bit is set to 0 in DHCPv6 OPTION\_S46\_RULE (option 89).
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.