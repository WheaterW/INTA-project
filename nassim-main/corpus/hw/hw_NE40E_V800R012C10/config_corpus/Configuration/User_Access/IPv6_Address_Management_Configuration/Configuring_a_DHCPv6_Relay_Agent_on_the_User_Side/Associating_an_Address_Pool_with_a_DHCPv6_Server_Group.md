Associating an Address Pool with a DHCPv6 Server Group
======================================================

Associating an address pool with a DHCPv6 server group
is required only when the remote IPv6 address pool is used.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 pool**](cmdqueryname=ipv6+pool) *pool-name* **bas** **remote**
   
   
   
   The remote address pool view is displayed.
3. Run [**dhcpv6-server group**](cmdqueryname=dhcpv6-server+group) *group-name*
   
   
   
   The address pool is associated with a DHCPv6 server group.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.