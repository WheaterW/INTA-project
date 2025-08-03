Binding a Remote IPv6 Address Pool to a Domain
==============================================

Users in a domain can obtain addresses from an IPv6 address pool only after the address pool is bound to the domain.

#### Prerequisites

The address pool to be bound has been created and bound to a prefix pool.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   A domain is created, and the domain view is displayed.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
5. Run [**ipv6-pool**](cmdqueryname=ipv6-pool) *pool-name*
   
   
   
   The remote IPv6 address pool is bound to the domain.
6. (Optional) Run [**ipv6-warning-threshold**](cmdqueryname=ipv6-warning-threshold) { *upper-limit-value* | [**lower-limit**](cmdqueryname=lower-limit) *lower-limit-value* }
   
   
   
   A threshold for the usage of IPv6 addresses and prefixes is configured.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.