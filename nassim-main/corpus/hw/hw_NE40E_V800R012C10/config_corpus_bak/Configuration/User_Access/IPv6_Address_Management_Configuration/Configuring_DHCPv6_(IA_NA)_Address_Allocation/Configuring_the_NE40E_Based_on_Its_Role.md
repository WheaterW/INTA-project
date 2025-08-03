Configuring the NE40E Based on Its Role
=======================================

This section describes how to configure the NE40E based on its role.

#### Context

When a device acts as a DHCPv6 relay agent, see [Configuring a DHCPv6 Relay Agent on the User Side](dc_ne_ipv6_address_cfg_0012.html).

When a device acts as a DHCPv6 server, perform the following operations
to allow Layer 3 DHCPv6 users to request for IPv6 addresses from an
IPv6 relay address pool.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 prefix**](cmdqueryname=ipv6+prefix) *prefix-name* **local**
   
   
   
   An IPv6 prefix pool is created, and the IPv6 prefix pool
   view is displayed.
   
   The address pool is of the relay type, and
   the prefix pool must be configured to work in local mode.
3. Run [**prefix**](cmdqueryname=prefix) *prefix-address*/*prefix-length*
   
   
   
   An IPv6 address prefix is configured.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**ipv6 pool**](cmdqueryname=ipv6+pool) *pool-name* **bas** **relay**
   
   
   
   An IPv6 address pool is created, and the IPv6 address pool
   view is displayed.
6. Run [**prefix**](cmdqueryname=prefix) *prefix-name*
   
   
   
   The IPv6 address pool is bound to the IPv6 prefix pool.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.