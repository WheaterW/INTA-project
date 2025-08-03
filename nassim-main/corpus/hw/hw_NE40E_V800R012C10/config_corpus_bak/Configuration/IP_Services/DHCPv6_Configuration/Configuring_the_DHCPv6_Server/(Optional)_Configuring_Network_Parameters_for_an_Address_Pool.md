(Optional) Configuring Network Parameters for an Address Pool
=============================================================

(Optional)_Configuring_Network_Parameters_for_an_Address_Pool

#### Context

To ensure that DHCPv6 clients can communicate normally, the DHCPv6 server needs to specify the DNS server, the SIP server, and other configuration parameters when assigning IPv6 addresses to clients. The DHCPv6 server can automatically assign configuration parameters such as the IPv6 addresses of the DNS and SIP servers to clients.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcpv6 pool**](cmdqueryname=dhcpv6+pool) *ip-pool-name*
   
   
   
   An IPv6 address pool is created, and its view is displayed.
3. Perform the following steps to specify configuration parameters for the IPv6 address pool. You can perform one or more steps as needed:
   
   
   * Run the [**dns-server**](cmdqueryname=dns-server) *ipv6-address* command to configure the DNS server address for the IPv6 address pool.
   * Run the [**dns-domain-name**](cmdqueryname=dns-domain-name) *dns-domain-name* command to configure the DNS domain name suffix assigned by the DHCPv6 server to DHCPv6 clients.
   * Run the [**sip-server**](cmdqueryname=sip-server) *ipv6-address* command to configure the SIP server address for the IPv6 address pool.
   * Run the [**sip-domain-name**](cmdqueryname=sip-domain-name) *sip-domain-name* command to configure the SIP domain name suffix assigned by the DHCPv6 server to DHCPv6 clients.
   * Run the [**nis-server**](cmdqueryname=nis-server) *ipv6-address* command to configure the NIS server address for the IPv6 address pool.
   * Run the [**nis-domain-name**](cmdqueryname=nis-domain-name) *nis-domain-name* command to configure the NIS domain name suffix assigned by the DHCPv6 server to DHCPv6 clients.
   * Run the [**nisp-server**](cmdqueryname=nisp-server) *ipv6-address* command to configure the NISP server address for the IPv6 address pool.
   * Run the [**nisp-domain-name**](cmdqueryname=nisp-domain-name) *nisp-domain-name* command to configure the NISP domain name suffix assigned by the DHCPv6 server to DHCPv6 clients.
   * Run the [**sntp-server**](cmdqueryname=sntp-server) *ipv6-address* command to configure the SNTP server address for the IPv6 address pool.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.