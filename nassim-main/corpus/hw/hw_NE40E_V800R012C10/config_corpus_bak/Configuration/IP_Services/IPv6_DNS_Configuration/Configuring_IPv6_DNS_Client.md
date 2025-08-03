Configuring IPv6 DNS Client
===========================

IPv6 DNS establishes mapping between domain names and IPv6 addresses, which allows devices to use domain names to communicate.

#### Usage Scenario

If you want to use meaningful and easy-to-memorize domain names to access other devices, configure IPv6 DNS. IPv6 DNS entries record the mapping between domain names and IPv6 addresses. On the network in [Figure 1](#EN-US_TASK_0172364820__fig_dc_vrp_ipv6_dns_cfg_000301), the client program and IPv6 DNS client are configured on the same device.

* If you seldom use domain names to access other devices or no IPv6 DNS server is available, configure static IPv6 DNS on the IPv6 DNS client. To configure static IPv6 DNS, you must know the mapping between domain names and IPv6 addresses. If a mapping changes, you must manually modify the IPv6 DNS entry on the IPv6 DNS client.
* If you want to use domain names to access many devices and IPv6 DNS servers are available, configure dynamic IPv6 DNS on the IPv6 DNS client.

**Figure 1** IPv6 DNS networking  
![](images/fig_dc_vrp_ipv6_dns_cfg_000301.png)  


#### Pre-configuration Tasks

Before configuring IPv6 DNS, complete the following tasks:

* Configure a route from an IPv6 DNS client to an IPv6 DNS server to allow the client and server to communicate at Layer 3.
* Configure an IPv6 DNS server.


#### Procedure

* Configure static IPv6 DNS.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**ipv6 host**](cmdqueryname=ipv6+host+vpn-instance) *host-name* *ipv6-address* [ **vpn-instance** *vpn-name* ]
     
     A mapping between domain names and IPv6 addresses is configured.
  3. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure dynamic IPv6 DNS.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**dns resolve**](cmdqueryname=dns+resolve)
     
     Dynamic DNS is enabled.
  3. Run [**dns server ipv6**](cmdqueryname=dns+server+ipv6+vpn-instance) *ipv6-address* [ *interface-type interface-number* ] [ **vpn-instance** *vpn-name* ] [ **tcp ssl-policy** *ssl-policy-name* ]
     
     A DNS server is configured.
  4. (Optional) Run [**dns server ipv6 source-ip**](cmdqueryname=dns+server+ipv6+source-ip+vpn-instance) [ **vpn-instance** *vpn-name* ] *ipv6Addr*
     
     A source IPv6 address is specified for the IPv6 DNS client for domain name resolution.
     
     Specifying a source IPv6 address to be used by an IPv6 DNS client to communicate with an IPv6 DNS server ensures communication security.
  5. Run [**dns domain**](cmdqueryname=dns+domain+vpn-instance) *domain-name* [ **vpn-instance** *vpn-name* ]
     
     A domain name suffix is added.
  6. (Optional) Run [**dns timeout**](cmdqueryname=dns+timeout) *interval-time*
     
     A DNS query response timeout period is configured.
  7. (Optional) Run [**dns try**](cmdqueryname=dns+try) *times*
     
     The number of retransmission times for DNS query packets is configured.
  8. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  To specify multiple DNS server IPv6 addresses, repeat Step 3. To specify multiple domain name suffixes, repeat Step 5.

#### Verifying the Configuration of IPv6 DNS

After configuring IPv6 DNS, verify the configuration.

* Run the [**display ipv6 host**](cmdqueryname=display+ipv6+host) command to check static IPv6 DNS entries that record mapping between host names and IPv6 addresses.
* Run the [**display dns server**](cmdqueryname=display+dns+server) command to check all DNS server IPv6 addresses.
* Run the [**display dns domain**](cmdqueryname=display+dns+domain) command to check domain name suffixes.
* Run the [**display dns ipv6 dynamic-host**](cmdqueryname=display+dns+ipv6+dynamic-host) command to check dynamic IPv6 DNS entries in the domain name cache.