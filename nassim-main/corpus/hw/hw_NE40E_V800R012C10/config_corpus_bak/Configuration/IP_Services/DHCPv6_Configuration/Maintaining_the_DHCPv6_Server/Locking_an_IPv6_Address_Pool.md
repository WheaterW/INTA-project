Locking an IPv6 Address Pool
============================

Locking_an_IPv6_Address_Pool

#### Context

DHCPv6 server migration involves migrating address pools on one server to another server. To retain the addresses that have been assigned to clients from an address pool prior to migration, you can lock this address pool. When new users go online, they apply for IPv6 addresses from the DHCPv6 server to which address pools have been migrated.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**dhcpv6 pool**](cmdqueryname=dhcpv6+pool) *ip-pool-name* command to create an IPv6 address pool and enter its view.
3. Run the [**lock**](cmdqueryname=lock) command to lock the IPv6 address pool.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Follow-up Procedure

After IPv6 address pools are migrated to another DHCPv6 server, run the [**undo lock**](cmdqueryname=undo+lock) command to unlock them.