Configuring an IPv6 Delegation Address Pool
===========================================

In a MAP-E scenario, a prefix pool, a BR device name, and an FMR flag bit need to be configured in an IPv6 delegation address pool.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 pool**](cmdqueryname=ipv6+pool) *pool-name* **bas delegation**
   
   
   
   An IPv6 delegation address pool is created, and the IPv6 delegation address pool view is displayed.
3. Run [**prefix**](cmdqueryname=prefix) *prefix-name*
   
   
   
   An IPv6 prefix pool is bound to the IPv6 address pool.
4. Run [**option-s46 br-ipv6-address**](cmdqueryname=option-s46+br-ipv6-address) *br-address-name*
   
   
   
   A BR device name is bound to an IPv6 address pool. The NE40E adds OPTION\_S46\_BR (option 90) to an IPv6 prefix in a DHCPv6 Response message to be sent to MAP-E users.
5. (Optional) Run [**option-s46 fmr-flag disable**](cmdqueryname=option-s46+fmr-flag+disable)
   
   
   
   The F-flag bit is set to 0 in DHCPv6 OPTION\_S46\_RULE (option 89).
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.