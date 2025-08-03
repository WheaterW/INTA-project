DNS
===

DNS

#### Security Policy

* DNS TLS authentication
  
  Dynamic domain name resolution supports encrypted transmission of TCP-based TLS packets. You can configure SSL policies and load digital certificates on the DNS client and server in advance. During domain name resolution, the DNS server encrypts and decrypts packets based on the specified SSL policy to improve DNS packet transmission security.

#### Attack Methods

When a bogus DNS server exists on the network, it replies to the DNS client with spoofing information, such as an incorrect IP address. As a result, the DNS client cannot access the network or accesses an incorrect network.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**dns resolve**](cmdqueryname=dns+resolve)
   
   Dynamic domain name resolution is enabled.
3. Run [**dns server**](cmdqueryname=dns+server) *ip-address* [ **vpn-instance** *vpn-name* ] **tcp ssl-policy** *ssl-policy-name*
   
   A DNS server is added and an SSL policy is bound to the DNS server.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   DNS domain name resolution uses TCP-based SSL encryption to prevent packets from being intercepted or forged.
4. (Optional) Run [**dns server source-ip**](cmdqueryname=dns+server+source-ip) [ **vpn-instance** *vpn-name* ] *ipv4Addr*
   
   The local Router IP address is specified.
   
   Specify the local Router's IP address which is used to communicate with the DNS server. This ensures communication security.
5. Run [**dns domain**](cmdqueryname=dns+domain) *domain-name* [ **vpn-instance** *vpn-name* ]
   
   A domain name suffix is added.
6. (Optional) Run [**dns timeout**](cmdqueryname=dns+timeout) *interval-time*
   
   The timeout period for the DNS client to wait for a query response is configured.
7. (Optional) Run [**dns try**](cmdqueryname=dns+try) *times*
   
   The number of retransmission times for DNS query packets is configured on the DNS client.
8. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.

#### Verifying the Security Hardening Result

Run the [**display dns server**](cmdqueryname=display+dns+server) [ **vpn-instance** *vpn-instance-name* ] command to check the configured TLS policy name.