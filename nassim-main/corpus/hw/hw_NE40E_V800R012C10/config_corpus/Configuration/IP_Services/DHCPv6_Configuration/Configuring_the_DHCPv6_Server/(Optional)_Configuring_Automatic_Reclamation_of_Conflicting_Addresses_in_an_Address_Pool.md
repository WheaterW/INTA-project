(Optional) Configuring Automatic Reclamation of Conflicting Addresses in an Address Pool
========================================================================================

(Optional) Configuring Automatic Reclamation of Conflicting Addresses in an Address Pool

#### Context

When a DHCPv6 server assigns IPv6 addresses to clients, address conflict may occur because IPv6 addresses of some clients have been manually configured. In this case, the DHCPv6 server sets these addresses to conflicting ones. To reclaim conflicting addresses promptly, you can set the interval for automatically reclaiming conflicting addresses on the device.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcpv6 pool**](cmdqueryname=dhcpv6+pool) *ip-pool-name*
   
   
   
   An IPv6 address pool is created, and its view is displayed.
3. Run [**conflict-address expire-time**](cmdqueryname=conflict-address+expire-time) *expire-time*
   
   
   
   The aging time for conflicting addresses in the IPv6 address pool is set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.