(Optional) Configuring Fixed IPv6 Addresses for Specified Clients in an Address Pool
====================================================================================

(Optional)_Configuring_Fixed_IPv6_Addresses_for_Specified_Clients_in_an_Address_Pool

#### Context

IPv6 addresses dynamically assigned by DHCPv6 servers can be used only within the address lease period. After the lease of the IPv6 address assigned to a client expires, a different IPv6 address may be assigned to the client during address application. To ensure the stability of some important devices, you need to statically assign fixed IPv6 addresses to specified DHCPv6 clients. You can bind the DUIDs of these clients to the IPv6 addresses. When receiving an IPv6 address application request from a specified client, a DHCPv6 server assigns the fixed IPv6 address bound to the client DUID to this client. Compared with manual IPv6 address configuration, DHCPv6 static address assignment prevents manual configuration errors and helps you perform unified maintenance and management.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Before performing this task, ensure that the IPv6 address to be statically assigned is available. (Run the [**display dhcpv6 pool**](cmdqueryname=display+dhcpv6+pool) command to check whether the address is assignable.) If the IPv6 address has been assigned to a client, use a different IPv6 address or reclaim the assigned IPv6 address (using the [**reset dhcpv6 pool**](cmdqueryname=reset+dhcpv6+pool) command) before performing this task.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcpv6 pool**](cmdqueryname=dhcpv6+pool) *ip-pool-name*
   
   
   
   An IPv6 address pool is created, and its view is displayed.
3. Run [**static-bind address**](cmdqueryname=static-bind+address) *ipv6-address* **duid** *client-duid* [ **iaid** *iaid* ] [ **life-time** { *preferred-lifetime* | **infinite** } { *valid-lifetime* | **infinite** } ]
   
   
   
   An IPv6 address is statically bound to a client DUID.
   
   
   
   An IPv6 address can be assigned only to the client whose DUID is bound to the IPv6 address.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.