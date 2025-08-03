(Optional) Configuring DNS Services for the DHCPv4 Client
=========================================================

You can configure DNS server parameters for the DHCPv4 client. This allows the DHCPv4 client to automatically obtain DNS services automatically. Then, users can use easy-to-memorize domain names rather than complicated IP addresses.

#### Context

Perform the following operations on the device if the device that functions as a DHCPv4 server needs to provide DNS services for DHCPv4 clients.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip pool**](cmdqueryname=ip+pool) *pool-name*  [ **bas** { **local** | **remote** } | **server** ]
   
   
   
   An IP address pool is created, and the IP address pool view is displayed.
3. Run [**dns-suffix**](cmdqueryname=dns-suffix) *suffix-name*
   
   
   
   The DNS suffix of the IP address pool is configured.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command is valid for only the local address pool and server address pool.
4. Run [**dns-server**](cmdqueryname=dns-server) *ip-address* &<1-8>
   
   
   
   The IP address of the DNS server for the address pool is configured.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If IP addresses are automatically allocated from the BAS address pool, the DNS server can be configured in both the domain view and the address pool view, but the configuration in the domain view takes precedence.
   
   If the RADIUS server is used to deliver IP addresses and gateway addresses, the following situations are available:
   * If the RADIUS server also delivers the DNS server address, the DNS server address delivered by the RADIUS server takes precedence.
   * If the RADIUS server does not deliver the DNS server address, the DNS server must be configured in the domain view, and this configuration does not take effect for the address pool.
5. Run [**domain-search-list**](cmdqueryname=domain-search-list) *domain-name*
   
   
   
   The search domain is configured.
   
   If a client sends a packet carrying Option 119 to request search domain information from the DHCP server, the [**domain-search-list**](cmdqueryname=domain-search-list) *domain-name* command can be used to configure a search domain so that the DHCP server can send required search domain information to the user. After the [**domain-search-list**](cmdqueryname=domain-search-list) *domain-name* command is run and the first domain name resolution fails, the configured search domain is used for resolution.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

On the DHCPv4 server, designate a DNS suffix for each address pool used to assign IP addresses to clients.

When a host accesses the Internet by using the DNS suffix, the DNS server resolves the DNS suffix into an IP address. Therefore, to ensure that the client successfully accesses the Internet, the DHCPv4 server also needs to specify the DNS server address for the client when it assigns IP addresses.

To improve network reliability, you can configure several DNS servers.