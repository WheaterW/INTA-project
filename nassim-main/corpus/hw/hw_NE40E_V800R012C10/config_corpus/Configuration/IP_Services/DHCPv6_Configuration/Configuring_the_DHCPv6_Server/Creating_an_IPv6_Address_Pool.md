Creating an IPv6 Address Pool
=============================

Creating an IPv6 Address Pool

#### Context

A DHCPv6 server selects available IPv6 addresses and prefixes from an address pool and assigns them to DHCPv6 clients. You need to create an IPv6 address pool and configure its attributes, including the network prefix, PD prefix, lifetime, and any IPv6 addresses that cannot be automatically assigned to clients.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcpv6 pool**](cmdqueryname=dhcpv6+pool) *ip-pool-name*
   
   
   
   An IPv6 address pool is created, and its view is displayed.
3. Run the following commands in the IPv6 address pool view to configure prefixes. When functioning as a DHCPv6 server, the device can assign network parameters to clients in DHCPv6 stateful or stateless mode. In DHCPv6 stateful mode, the server automatically assigns IPv6 addresses, prefixes, and other network configuration parameters (such as DNS, NIS, and SNTP server addresses). In DHCPv6 stateless mode, the server assigns configuration parameters (such as DNS, NIS, and SNTP server addresses) but does not assign IPv6 addresses. IPv6 addresses of clients are automatically generated through RA messages.
   
   
   * Run [**address prefix**](cmdqueryname=address+prefix) *ipv6-prefix/ipv6-prefix-length* [ **life-time** { *preferred-lifetime* | **infinite** } { *valid-lifetime* | **infinite** } ]
     
     A network prefix and lifetime are configured in the IPv6 address pool view.
   * Run [**prefix-delegation**](cmdqueryname=prefix-delegation) *ipv6-prefix/ipv6-prefix-length* *assign-prefix-length* [ **life-time** { *preferred-lifetime* | **infinite** } { *valid-lifetime* | **infinite** } ]
     
     A PD prefix and lifetime are configured in the IPv6 address pool view.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the DHCPv6 server automatically assigns network parameters in DHCPv6 stateless mode, you do not need to run the preceding commands.
4. Run [**excluded-address**](cmdqueryname=excluded-address) *start-ipv6-address* [ **to** *end-ipv6-address* ]
   
   
   
   The IPv6 addresses that cannot be automatically assigned to clients (including the IPv6 address of the interface connected to DHCPv6 clients) are added to the list of IPv6 addresses that cannot be assigned automatically.
5. Run **[**vpn-instance**](cmdqueryname=vpn-instance)** *vpn-instance-name*
   
   
   
   A VPN instance is configured for the address pool.
   
   
   
   To apply the DHCPv6 service to a VPN instance, you need to run this command to bind the IPv6 address pool created on the DHCPv6 server to the VPN instance.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.