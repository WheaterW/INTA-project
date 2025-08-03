(Optional) Configuring a Whitelist for Web Users Who Access the Network Using HTTPS
===================================================================================

This section describes how to configure a whitelist for web users who access the network using HTTPS.

#### Context

When web users access the network using HTTPS and a list of accessible domain names or IP addresses in the pre-authentication domain needs to be configured, you can configure whitelists so that the system sends DNS packets that match the whitelists to the CPU while redirecting the DNS packets that do not match the whitelists to a specified web server address.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dns-url permit**](cmdqueryname=dns-url+permit) *url-name*
   
   
   
   A whitelist is configured for web users who access the network using HTTPS.
3. Run [**dns-redirect response ttl**](cmdqueryname=dns-redirect+response+ttl) *ttl-value*
   
   
   
   A TTL value is configured for the DNS packets that do not match the whitelist.
4. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
5. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The domain view is displayed.
6. Run [**dns-redirect web-server**](cmdqueryname=dns-redirect+web-server) *ip-address*
   
   
   
   The IP address of the web server to which DNS packets are redirected is configured.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.