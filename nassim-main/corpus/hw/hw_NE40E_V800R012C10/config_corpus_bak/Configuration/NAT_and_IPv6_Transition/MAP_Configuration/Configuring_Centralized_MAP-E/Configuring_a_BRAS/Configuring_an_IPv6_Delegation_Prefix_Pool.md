Configuring an IPv6 Delegation Prefix Pool
==========================================

In a MAP-E or MAP-T scenario, a MAP rule needs to be bound to an IPv6 delegation prefix pool. The NE40E uses the BMR configured using the **map-rule** command to assign prefixes to MAP users.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 prefix**](cmdqueryname=ipv6+prefix) *prefix-name* **delegation**
   
   
   
   An IPv6 delegation prefix pool is created, and the IPv6 delegation prefix pool view is displayed.
3. Run [**map-rule**](cmdqueryname=map-rule) *rule-name*
   
   
   
   A MAP rule is bound to the IPv6 prefix pool.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.