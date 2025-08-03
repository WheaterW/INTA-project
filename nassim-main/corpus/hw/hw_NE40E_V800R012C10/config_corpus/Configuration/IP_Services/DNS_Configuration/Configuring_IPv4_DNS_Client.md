Configuring IPv4 DNS Client
===========================

This section describes how to configure DNS and establish mappings between domain names and IP addresses, so that a device can communicate with other devices using domain names.

#### Usage Scenario

If you want to use meaningful and easy-to-memorize domain names to access other devices, configure DNS. DNS entries record the mappings between domain names and IP addresses. In [Figure 1](#EN-US_TASK_0172364805__fig_dc_vrp_dns_cfg_000301), the DNS client and client program are on the same device.

* If you seldom use domain names to visit other devices or no DNS server is available, configure static DNS on the DNS client. To configure static DNS, you must know the mappings between domain names and IP addresses. If a mapping changes, you must manually modify the DNS entry on the DNS client.
* If you want to use domain names to visit many devices and DNS servers are available, configure dynamic DNS on the DNS client. Dynamic DNS requires DNS servers.

**Figure 1** Networking diagram for typical domain name resolution  
![](images/fig_dc_vrp_dns_cfg_000301.png)  


#### Pre-configuration Tasks

Before configuring DNS, complete the following tasks:

* Configuring a route between the DNS client and server, so that the DNS client and server can communicate
* Configuring DNS servers


#### Procedure

* Configure static DNS.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**ip host**](cmdqueryname=ip+host+vpn-instance) *host-name* *ip-address* [ **vpn-instance** *vpn-name* ]
     
     The mapping between the domain name and IPv4 address of the host is configured.
  3. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure dynamic DNS.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**dns resolve**](cmdqueryname=dns+resolve)
     
     Dynamic DNS is enabled.
  3. Run [**dns server**](cmdqueryname=dns+server+vpn-instance) *ip-address* [ **vpn-instance** *vpn-name* ] [ **tcp ssl-policy** *ssl-policy-name* ]
     
     A DNS server is configured.
  4. (Optional) Run [**dns server source-ip**](cmdqueryname=dns+server+source-ip+vpn-instance) [ **vpn-instance** *vpn-name* ] *ipv4Addr*
     
     The IP address of the local Router is specified.
     
     An IP address is specified for the DNS client to communicate with the DNS server. Using a specified source address ensures the security of communication between the DNS client and DNS server.
  5. Run [**dns domain**](cmdqueryname=dns+domain+vpn-instance) *domain-name* [ **vpn-instance** *vpn-name* ]
     
     A domain name suffix is added.
  6. (Optional) Run [**dns timeout**](cmdqueryname=dns+timeout) *interval-time*
     
     A DNS query response timeout period is configured.
  7. (Optional) Run [**dns try**](cmdqueryname=dns+try) *times*
     
     The number of retransmission times for DNS query packets is configured.
  8. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  To configure multiple DNS servers, repeatedly perform Step 3. To configure multiple domain name suffixes, repeatedly perform Step 5.

#### Verifying the Configuration of a DNS Client

After configuring a DNS client, verify the configuration.

* Run the [**display ip host**](cmdqueryname=display+ip+host) command to view static DNS entries, including mappings between domain names and IP addresses.
* Run the [**display dns server**](cmdqueryname=display+dns+server) command to view the IP addresses of all configured DNS servers.
* Run the [**display dns domain**](cmdqueryname=display+dns+domain) command to view the domain name suffix list.
* Run the [**display dns dynamic-host**](cmdqueryname=display+dns+dynamic-host) command to view dynamic DNS entries stored in the cache.